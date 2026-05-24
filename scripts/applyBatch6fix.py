MD_FILE = './src/imports/project-management-questions-1.md'

with open(MD_FILE, 'r', encoding='utf-8') as f:
    content = f.read()

replacements = [
    (
        'Explanation: Need: guide and calm the team. Options A and D (Issue log; Change log) work together."',
        'Explanation: Keywords: invoice errors, post-implementation issue, issue log, change log. Three invoices with errors represent an active problem requiring tracking and corrective action — both the issue itself and any resulting changes to the system must be documented. The issue log captures the problem and its resolution progress, while the change log records any system modifications made in response. (PMBOK Guide) – Seventh Edition, 2021, p. 46, \'Optimize Risk Responses\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option D (Collaborate with the compliance team member to review and prioritize the requirement’s delivery) fixes it."',
        'Explanation: Keywords: hybrid project, compliance requirement, urgent priority, collaborative prioritization. A compliance requirement that must be delivered ahead of all others cannot be simply added to the backlog and left to be deprioritized — it has a mandated delivery position. Collaborating with the compliance team member ensures the requirement is properly understood before the team determines how and when it can be delivered. (PMBOK Guide) – Seventh Edition, 2021, p. 32, \'Focus on Value\'"'
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
