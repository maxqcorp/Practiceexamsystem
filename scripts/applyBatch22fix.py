MD_FILE = './src/imports/project-management-questions-1.md'

with open(MD_FILE, 'r', encoding='utf-8') as f:
    content = f.read()

# Use curly apostrophes U+2019 for stakeholders' and teams'
replacements = [
    # Q1073 - curly apostrophe in stakeholders'
    (
        "Explanation: Need: listen to people needs. Options A and E (Update the project stakeholder analysis and methods to satisfy the stakeholders’ requirements.; Engage all stakeholders in the project including the unsupportive stakeholders.) work together.\"",
        "Explanation: Keywords: stakeholders working against project, tight budget, unsupportive stakeholders, inclusive engagement. When stakeholders actively resist a project, excluding them escalates opposition while ignoring legitimate concerns. The project manager must update the stakeholder analysis to understand what is driving resistance and then engage all stakeholders — including the unsupportive ones — to address concerns and build alignment. (PMBOK Guide) – Seventh Edition, 2021, p. 30, 'Effectively Engage with Stakeholders'\""
    ),
    # Q1074 - curly apostrophe in teams'
    (
        "Explanation: Need: guide and calm the team. Option B (Develop relationship skills as a leader and also develop the teams’ emotional intelligence skills.) fixes it.\"",
        "Explanation: Keywords: high turnover, relationship management gaps, emotional intelligence, leadership development. When exit interviews consistently cite the project manager's poor relationship management as the reason for departures, the project manager must invest in developing their own interpersonal and emotional intelligence skills. Building these capabilities in the team as well creates a more emotionally resilient environment that reduces the relational friction driving turnover. (PMBOK Guide) – Seventh Edition, 2021, p. 36, 'Demonstrate Leadership Behaviors'\""
    ),
]

updated = 0
failed = []

for old, new in replacements:
    if old in content:
        content = content.replace(old, new)
        updated += 1
    else:
        failed.append(old[:80])

with open(MD_FILE, 'w', encoding='utf-8') as f:
    f.write(content)

print(f'Done: {updated} updated, {len(failed)} failed.')
for s in failed:
    print(f'  NOT FOUND: {s!r}')
