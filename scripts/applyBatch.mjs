/**
 * Applies a batch of new explanations to the markdown file.
 * Run with: node scripts/applyBatch.mjs
 */

import fs from 'fs';

const MD_FILE = './src/imports/project-management-questions-1.md';

// Each entry: { num: question number, old: exact current explanation text, new: replacement }
const replacements = [
  {
    num: 4,
    old: `Explanation: Need: listen to people needs. Option B (Review the historical information and lessons learned from last year's project to justify the new budget estimate) fixes it."`,
    new: `Explanation: Keywords: three-point estimate, similar project, new sponsor, budget justification. When a new sponsor questions the budget, the PM's best tool is evidence. Historical information and lessons learned from a comparable project provide objective data that validates the estimate and builds the sponsor's confidence without changing the methodology. (PMBOK Guide) – Seventh Edition, 2021, p. 25, 'Be a Diligent, Respectful, and Caring Steward'"`,
  },
  {
    num: 5,
    old: `Explanation: Need: listen to people needs. Option C (Identify the source of the disagreement) fixes it."`,
    new: `Explanation: Keywords: stakeholder disagreement, requirements approval, schedule at risk. Before resolving a conflict among stakeholders, the PM must first understand what is driving it. Identifying the source of the disagreement gives the PM the context needed to facilitate a targeted resolution rather than applying a generic approach that may not address the real issue. (PMBOK Guide) – Seventh Edition, 2021, p. 30, 'Effectively Engage with Stakeholders'"`,
  },
  {
    num: 6,
    old: `Explanation: Need: listen to people needs. Option B (Use a focus group and brainstorming sessions to gather more details about the project scope) fixes it."`,
    new: `Explanation: Keywords: project charter, requirements conflict, scope clarification. When requirements during scope management differ from what the charter states, the PM needs more information before deciding what to do. A focus group and brainstorming sessions bring the right people together to surface the real needs and reconcile the discrepancy through direct stakeholder engagement. (PMBOK Guide) – Seventh Edition, 2021, p. 30, 'Effectively Engage with Stakeholders'"`,
  },
  {
    num: 7,
    old: `Explanation: Need: guide and calm the team. Option B (Ensure that knowledge transfer activities are executed as planned) fixes it."`,
    new: `Explanation: Keywords: project closing, knowledge transfer, two-year initiative. During project closure, the most critical priority is ensuring that the knowledge created throughout the project is captured and transferred. Without this, the organization loses the value of two years of learning, which cannot be recovered after resources are released. (PMBOK Guide) – Seventh Edition, 2021, p. 32, 'Focus on Value'"`,
  },
  {
    num: 8,
    old: `Explanation: Need: keep plans flexible. Option B (One iteration) fixes it."`,
    new: `Explanation: Keywords: agile, epics to stories, story estimation, iteration planning. In an agile approach, story-level estimates are sized to fit within a single iteration. Estimating story duration at one iteration keeps the work actionable and maintains the inspect-and-adapt rhythm that makes agile planning reliable. (PMBOK Guide) – Seventh Edition, 2021, p. 40, 'Tailor Based on Context'"`,
  },
  {
    num: 9,
    old: `Explanation: Need: guide and calm the team. Option D (Use the retrospective meeting to better understand the root cause of the quality problems and put together a plan with the team to address the problems) fixes it."`,
    new: `Explanation: Keywords: agile project, recurring quality issues, production problems, retrospective. Recurring quality defects signal a process problem, not just a skills gap. The retrospective is the agile team's dedicated mechanism to inspect their process, identify the root cause of quality failures, and commit to improvements — making it the right forum to address this systematically. (PMBOK Guide) – Seventh Edition, 2021, p. 42, 'Build Quality into Processes and Deliverables'"`,
  },
  {
    num: 10,
    old: `Explanation: Need: guide and calm the team. Option C (Help the team to find a new approach to launch the product as soon as possible) fixes it."`,
    new: `Explanation: Keywords: agile project, new competitor, market pressure, accelerate delivery. When external conditions change mid-project, the PM's role is to help the team adapt their approach rather than simply demanding more output. Helping the team find a new way to launch faster leverages agile's built-in adaptability while keeping the team engaged and empowered. (PMBOK Guide) – Seventh Edition, 2021, p. 48, 'Embrace Adaptability and Resiliency'"`,
  },
  {
    num: 11,
    old: `Explanation: Need: listen to people needs. Option C (Revisiting the stakeholder engagement plan, focusing on specific overlooked stakeholders) fixes it."`,
    new: `Explanation: Keywords: stakeholder conflicts, deliverable delays, overlooked stakeholders. Approval delays caused by stakeholder conflicts often point to gaps in engagement rather than substantive disagreements. Revisiting the stakeholder engagement plan allows the PM to identify which stakeholders have been underserved and correct the engagement approach before delays compound further. (PMBOK Guide) – Seventh Edition, 2021, p. 30, 'Effectively Engage with Stakeholders'"`,
  },
  {
    num: 12,
    old: `Explanation: Need: control changes and baselines. Option C (Initiate the change request to modify the scope and adjust the timelines) fixes it."`,
    new: `Explanation: Keywords: operations project, scope changes, critical task delays, change control. When scope changes and schedule delays occur, the correct response is to route them through the formal change management process. Initiating a change request ensures that scope and timeline adjustments are reviewed, approved, and documented — preserving the integrity of the baseline. (PMBOK Guide) – Seventh Edition, 2021, p. 50, 'Enable Change to Achieve the Envisioned Future State'"`,
  },
  {
    num: 13,
    old: `Explanation: Need: guide and calm the team. Option C (Provide performance feedback as part of the retrospective ceremony.) fixes it."`,
    new: `Explanation: Keywords: new resource, iterative project, performance gap, retrospective. On an iterative project, the retrospective is the structured space for the team to surface and address performance issues constructively. Raising the new team member's delivery challenges in the retrospective keeps the conversation in a collaborative, improvement-focused context rather than making it a disciplinary matter. (PMBOK Guide) – Seventh Edition, 2021, p. 28, p. 29, 'Create a Collaborative Team Environment'"`,
  },
  {
    num: 14,
    old: `Explanation: Need: protect value and acceptance. Option C (Increased technical debt) fixes it."`,
    new: `Explanation: Keywords: skipping testing, velocity recovery, quality trade-off. Bypassing testing to recover schedule velocity does not eliminate defects — it defers them. The immediate consequence is increased technical debt: hidden defects that will cost more to fix later and undermine the long-term quality and maintainability of the product. (PMBOK Guide) – Seventh Edition, 2021, p. 42, 'Build Quality into Processes and Deliverables'"`,
  },
  {
    num: 16,
    old: `Explanation: Need: listen to people needs. Option C (Help sponsors and stakeholders craft the product vision, and bring the team and product owner together to clarify expectations) fixes it."`,
    new: `Explanation: Keywords: agile adoption, scope definition concern, product vision, stakeholder alignment. In an agile approach, scope is defined collaboratively through a shared product vision rather than a fixed requirements document. Bringing sponsors, stakeholders, and the product owner together to craft that vision ensures everyone has a common understanding of what the project will deliver and why. (PMBOK Guide) – Seventh Edition, 2021, p. 30, 'Effectively Engage with Stakeholders'"`,
  },
  {
    num: 17,
    old: `Explanation: Need: guide and calm the team. Option D (Review the risk management plan to evaluate the probability and impact of these delays) fixes it."`,
    new: `Explanation: Keywords: international team, holiday-related delays, work performance decline, risk evaluation. Delays caused by regional holidays in a multi-country project are a risk event that should have been captured in the risk register. Reviewing the risk management plan tells the PM whether this was anticipated and whether a response strategy already exists, making it the right first step before taking corrective action. (PMBOK Guide) – Seventh Edition, 2021, p. 46, 'Optimize Risk Responses'"`,
  },
  {
    num: 18,
    old: `Explanation: Need: guide and calm the team. Options A and C (Encourage all team members to use a virtual workspace; Talk to the team member about their engagement and take appropriate action.) work together."`,
    new: `Explanation: Keywords: virtual team, communication gap, daily calls, critical work imminent. With critical work starting and a team member disengaged from daily calls, two actions are needed: setting up a shared virtual workspace so all communication is transparent regardless of participation style, and addressing the engagement issue directly with the team member to understand and resolve the root cause. (PMBOK Guide) – Seventh Edition, 2021, p. 28, p. 29, 'Create a Collaborative Team Environment'"`,
  },
  {
    num: 19,
    old: `Explanation: Need: listen to people needs. Option D (Submit a change request to accelerate the project as requested) fixes it."`,
    new: `Explanation: Keywords: construction project, customer-driven acceleration, subcontractor, additional budget. When a customer requests a change that affects delivery timing and cost, that request must enter the formal change management process. Submitting a change request ensures the acceleration is properly evaluated, approved, and funded before the subcontractor is asked to act on it. (PMBOK Guide) – Seventh Edition, 2021, p. 50, 'Enable Change to Achieve the Envisioned Future State'"`,
  },
  {
    num: 20,
    old: `Explanation: Need: listen to people needs. Option D (Involved stakeholders from all levels of the company so everyone understands the change) fixes it."`,
    new: `Explanation: Keywords: new software system, staff resistance, change management, early engagement. Resistance to a new system is most effectively prevented by involving those affected at the start, not after implementation. Engaging stakeholders from all levels early ensures the change is understood, concerns are heard, and people feel ownership rather than having the change imposed on them. (PMBOK Guide) – Seventh Edition, 2021, p. 30, 'Effectively Engage with Stakeholders'"`,
  },
  {
    num: 21,
    old: `Explanation: Need: listen to people needs. Option C (Evaluate the consequences and meet with the client to explain the possible scenarios.) fixes it."`,
    new: `Explanation: Keywords: external resource rejection, client cost concern, quality risk, consequence analysis. When a client rejects a resource that the project plan identifies as necessary, the PM's responsibility is to make the consequences visible. Evaluating the impact and presenting the possible scenarios to the client gives them the information they need to make an informed decision about the trade-off between cost and quality. (PMBOK Guide) – Seventh Edition, 2021, p. 32, 'Focus on Value'"`,
  },
  {
    num: 22,
    old: `Explanation: Need: guide and calm the team. Option B (Appreciate this team member's performance throughout the project life cycle) fixes it."`,
    new: `Explanation: Keywords: high-performing team member, mentoring, role model, team recognition. A project manager who demonstrates leadership acknowledges and reinforces the behaviors that make the team stronger. Appreciating a team member's contribution continuously throughout the project — not just at year-end — reinforces those behaviors in real time and models the culture the PM wants across the team. (PMBOK Guide) – Seventh Edition, 2021, p. 36, 'Demonstrate Leadership Behaviors'"`,
  },
  {
    num: 23,
    old: `Explanation: Need: listen to people needs. Option C (Allocate time to gain buy-in from the stakeholder prior to key decision meetings.) fixes it."`,
    new: `Explanation: Keywords: opinionated client representative, non-decision maker, buy-in, meeting disruption risk. An influential but non-authoritative stakeholder who can block progress requires proactive management. Allocating time before key meetings to understand their concerns and build alignment prevents public resistance during decisions and turns a potential roadblock into a supporter before it matters. (PMBOK Guide) – Seventh Edition, 2021, p. 30, 'Effectively Engage with Stakeholders'"`,
  },
  {
    num: 24,
    old: `Explanation: Need: guide and calm the team. Option C (Ensured frequent and continuous integration of work to obtain early feedback and continuous learning) fixes it."`,
    new: `Explanation: Keywords: multi-team agile, integration failures, product release decline, continuous integration. When five teams each show progress independently but fail at the product level, the gap is integration. Frequent and continuous integration across teams surfaces compatibility issues early — when they are small and fixable — rather than at release when they become critical and costly. (PMBOK Guide) – Seventh Edition, 2021, p. 42, 'Build Quality into Processes and Deliverables'"`,
  },
  {
    num: 26,
    old: `Explanation: Need: listen to people needs. Option D (Engage the stakeholder to solicit more information before responding to the request) fixes it."`,
    new: `Explanation: Keywords: overlooked stakeholder, requirements traceability matrix, late engagement. Before evaluating whether a stakeholder's request belongs in scope or not, the PM must first understand what is actually being asked and why. Engaging the stakeholder directly to gather more information ensures the PM responds to the real need rather than making a decision based on incomplete information. (PMBOK Guide) – Seventh Edition, 2021, p. 30, 'Effectively Engage with Stakeholders'"`,
  },
  {
    num: 27,
    old: `Explanation: Need: keep plans flexible. Options B and E (Publish information on the city's website about the benefits that the new tram station will bring; Register this situation as a risk and develop a mitigation plan) work together."`,
    new: `Explanation: Keywords: community resistance, hybrid project, public communication, risk registration. Neighbor opposition that could delay or stop a public project must be managed on two fronts simultaneously: communicating the project's value to shift public perception, and formally registering the resistance as a risk so a mitigation plan is in place if opposition escalates to legal action. (PMBOK Guide) – Seventh Edition, 2021, p. 46, 'Optimize Risk Responses'; p. 32, 'Focus on Value'"`,
  },
];

let markdown = fs.readFileSync(MD_FILE, 'utf-8');
let updated = 0;
let failed = [];

for (const r of replacements) {
  if (markdown.includes(r.old)) {
    markdown = markdown.replace(r.old, r.new);
    updated++;
    console.log(`✓ Q${r.num}`);
  } else {
    failed.push(r.num);
    console.warn(`✗ Q${r.num} — old text not found`);
  }
}

fs.writeFileSync(MD_FILE, markdown);
console.log(`\nDone: ${updated} updated, ${failed.length} failed${failed.length ? ': Q' + failed.join(', Q') : ''}.`);
