MD_FILE = './src/imports/project-management-questions-1.md'

with open(MD_FILE, 'r', encoding='utf-8') as f:
    content = f.read()

# Q1181 - curly apostrophe in managers'
replacements = [
    (
        "Explanation: Need: guide and calm the team. Option A (Set up a proper governance structure to ensure functional managers’ requests are processed correctly.) fixes it.\"",
        "Explanation: Keywords: scope creep, governance, change control, functional manager interference. When functional managers add requirements outside the formal change process and team members accommodate them directly, the project's scope baseline is at risk. Establishing a proper governance structure ensures all requests are routed through the change control process, protecting the schedule and cost baselines while maintaining transparency. (PMBOK Guide) – Seventh Edition, 2021, p. 50, 'Enable Change to Achieve the Envisioned Future State'\""
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
