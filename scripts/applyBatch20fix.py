MD_FILE = './src/imports/project-management-questions-1.md'

with open(MD_FILE, 'r', encoding='utf-8') as f:
    content = f.read()

replacements = [
    # Q974 - curly apostrophe U+2019 in stakeholders'
    (
        "Explanation: Need: listen to people needs. Option A (Acknowledge the stakeholders’ concerns with open dialogues and realign the project with stakeholder requirements and past lessons learned.) fixes it.\"",
        "Explanation: Keywords: remodeling project, missing original documentation, stakeholder skepticism, open dialogue. When stakeholders are hesitant due to an absence of original design records, the project manager must acknowledge their concerns genuinely and facilitate open dialogue about requirements and relevant lessons learned from comparable work. This transparent engagement builds the confidence needed to secure stakeholder support for a project that carries inherent uncertainty. (PMBOK Guide) – Seventh Edition, 2021, p. 30, 'Effectively Engage with Stakeholders'\""
    ),
    # Q1008 - curly apostrophe U+2019 in architects'
    (
        "Explanation: Need: guide and calm the team. Option D (Support the outcome of the architects’ agreement.) fixes it.\"",
        "Explanation: Keywords: architect disagreement resolved, module ownership agreement, team consensus, project manager support. When team members who are best positioned to make a technical decision reach their own resolution and the team supports it, the project manager should respect and support that outcome rather than reopening the discussion. Overriding a self-organized resolution undermines team autonomy and the servant leadership model. (PMBOK Guide) – Seventh Edition, 2021, p. 36, 'Demonstrate Leadership Behaviors'\""
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
