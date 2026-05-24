/**
 * Updates all question explanations in the markdown file with PMBOK 7th Edition-aligned
 * explanations in the format: Keywords → short explanation → PMBOK citation.
 *
 * Usage:
 *   ANTHROPIC_API_KEY=sk-ant-... node scripts/updateExplanations.mjs
 *
 * It processes questions in batches of 10 and saves a checkpoint file so it can
 * be safely interrupted and resumed without losing progress.
 */

import fs from 'fs';
import Anthropic from '@anthropic-ai/sdk';

const MD_FILE = './src/imports/project-management-questions-1.md';
const CHECKPOINT_FILE = './scripts/explanation_progress.json';
const BATCH_SIZE = 10;

const PMBOK_SECTIONS = `
Use ONLY these PMBOK 7th Edition sections with their exact pages:
- p. 25, 'Be a Diligent, Respectful, and Caring Steward'
- p. 28, p. 29, 'Create a Collaborative Team Environment'
- p. 30, 'Effectively Engage with Stakeholders'
- p. 32, 'Focus on Value'
- p. 34, 'Recognize, Evaluate, and Respond to System Interactions'
- p. 36, 'Demonstrate Leadership Behaviors'
- p. 40, 'Tailor Based on Context'
- p. 42, 'Build Quality into Processes and Deliverables'
- p. 44, 'Navigate Complexity'
- p. 46, 'Optimize Risk Responses'
- p. 48, 'Embrace Adaptability and Resiliency'
- p. 50, 'Enable Change to Achieve the Envisioned Future State'
`.trim();

// ── Parser ────────────────────────────────────────────────────────────────────

function parseQuestions(markdown) {
  const blocks = [];
  const splitPattern = /(?="Question \d+\n)/g;
  const parts = markdown.split(splitPattern);

  for (const part of parts) {
    const numMatch = part.match(/^"Question (\d+)\n/);
    if (!numMatch) continue;

    const number = parseInt(numMatch[1]);
    const optionAIdx = part.indexOf('\na. ');
    if (optionAIdx === -1) continue;

    const questionText = part.substring(numMatch[0].length, optionAIdx).trim();

    const optA = part.match(/\na\. (.+?)(?=\nb\. )/s);
    const optB = part.match(/\nb\. (.+?)(?=\nc\. )/s);
    const optC = part.match(/\nc\. (.+?)(?=\nd\. )/s);
    const optD = part.match(/\nd\. (.+?)(?=\n)/s);
    if (!optA || !optB || !optC || !optD) continue;

    const answerMatch = part.match(/Answer: ([A-D])/);
    if (!answerMatch) continue;

    const expMatch = part.match(/Explanation: (.+?)(?="$|"\n|$)/s);
    const explanation = expMatch ? expMatch[1].trim() : '';

    const answerLetter = answerMatch[1];
    const answerIndex = answerLetter.charCodeAt(0) - 65;
    const options = [
      optA[1].trim(),
      optB[1].trim(),
      optC[1].trim(),
      optD[1].trim(),
    ];

    blocks.push({
      number,
      raw: part,
      questionText,
      options,
      answerLetter,
      correctOptionText: options[answerIndex],
      explanation,
    });
  }

  return blocks;
}

// ── Claude API call ───────────────────────────────────────────────────────────

async function generateBatch(client, batch) {
  const questionsText = batch
    .map(
      (q, i) => `--- Q${i + 1} (Question ${q.number}) ---
Question: ${q.questionText}
a. ${q.options[0]}
b. ${q.options[1]}
c. ${q.options[2]}
d. ${q.options[3]}
Correct Answer: ${q.answerLetter} — ${q.correctOptionText}`
    )
    .join('\n\n');

  const prompt = `You are a PMP exam expert with deep knowledge of PMBOK Guide 7th Edition (2021).

For each question below generate a concise explanation in this EXACT format (no extra text):

Keywords: [3-4 key terms extracted from the question scenario]
[One short paragraph: why the correct answer aligns with the relevant PMBOK principle. Focus strictly on the keywords. Do NOT mention wrong answers.]
(PMBOK Guide) – Seventh Edition, 2021, [page citation], '[Section Name]'

${PMBOK_SECTIONS}

Return a valid JSON array only — no markdown fences, no preamble:
[
  { "questionNumber": <number>, "explanation": "<full explanation text>" },
  ...
]

Questions:
${questionsText}`;

  let lastError;
  for (let attempt = 1; attempt <= 3; attempt++) {
    try {
      const response = await client.messages.create({
        model: 'claude-haiku-4-5-20251001',
        max_tokens: 4096,
        messages: [{ role: 'user', content: prompt }],
      });

      const text = response.content[0].text.trim();
      const jsonMatch = text.match(/\[[\s\S]*\]/);
      if (!jsonMatch) throw new Error('No JSON array in response');

      const parsed = JSON.parse(jsonMatch[0]);
      return parsed;
    } catch (err) {
      lastError = err;
      console.warn(`  Attempt ${attempt} failed: ${err.message}. Retrying...`);
      await sleep(2000 * attempt);
    }
  }
  throw lastError;
}

// ── File updater ──────────────────────────────────────────────────────────────

function applyExplanation(markdown, questionNumber, newExplanation) {
  // Match the specific question block and replace its Explanation line
  const blockPattern = new RegExp(
    `("Question ${questionNumber}\\n[\\s\\S]+?Explanation: )(.+?)(?="Question \\d+|$)`,
    's'
  );

  return markdown.replace(blockPattern, (match, prefix) => {
    return `${prefix}${newExplanation}\n`;
  });
}

// ── Checkpoint helpers ────────────────────────────────────────────────────────

function loadCheckpoint() {
  if (fs.existsSync(CHECKPOINT_FILE)) {
    return JSON.parse(fs.readFileSync(CHECKPOINT_FILE, 'utf-8'));
  }
  return { done: [] };
}

function saveCheckpoint(checkpoint) {
  fs.writeFileSync(CHECKPOINT_FILE, JSON.stringify(checkpoint, null, 2));
}

// ── Utilities ─────────────────────────────────────────────────────────────────

function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

// ── Main ──────────────────────────────────────────────────────────────────────

async function main() {
  const apiKey = process.env.ANTHROPIC_API_KEY;
  if (!apiKey) {
    console.error('Error: ANTHROPIC_API_KEY environment variable is not set.');
    console.error('Run as: ANTHROPIC_API_KEY=sk-ant-... node scripts/updateExplanations.mjs');
    process.exit(1);
  }

  const client = new Anthropic({ apiKey });

  console.log(`Reading ${MD_FILE}...`);
  let markdown = fs.readFileSync(MD_FILE, 'utf-8');

  console.log('Parsing questions...');
  const questions = parseQuestions(markdown);
  console.log(`Found ${questions.length} questions.`);

  const checkpoint = loadCheckpoint();
  const doneSet = new Set(checkpoint.done);

  const todo = questions.filter(q => !doneSet.has(q.number));
  console.log(`${doneSet.size} already done. ${todo.length} remaining.\n`);

  let processed = 0;

  for (let i = 0; i < todo.length; i += BATCH_SIZE) {
    const batch = todo.slice(i, i + BATCH_SIZE);
    const nums = batch.map(q => q.number).join(', ');
    process.stdout.write(`Processing Q${nums}... `);

    try {
      const results = await generateBatch(client, batch);

      for (const result of results) {
        markdown = applyExplanation(markdown, result.questionNumber, result.explanation);
        checkpoint.done.push(result.questionNumber);
        processed++;
      }

      // Save the file and checkpoint after every batch
      fs.writeFileSync(MD_FILE, markdown);
      saveCheckpoint(checkpoint);

      console.log(`done (${processed}/${todo.length})`);
    } catch (err) {
      console.error(`\nFailed batch starting at Q${batch[0].number}: ${err.message}`);
      console.error('Progress saved. Re-run the script to continue from where it stopped.');
      process.exit(1);
    }

    // Small delay between batches to avoid rate limits
    if (i + BATCH_SIZE < todo.length) await sleep(500);
  }

  // Clean up checkpoint when fully done
  if (fs.existsSync(CHECKPOINT_FILE)) fs.unlinkSync(CHECKPOINT_FILE);

  console.log(`\nDone! All ${questions.length} explanations updated.`);
}

main();
