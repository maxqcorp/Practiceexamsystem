MD_FILE = './src/imports/project-management-questions-1.md'

with open(MD_FILE, 'r', encoding='utf-8') as f:
    content = f.read()

# All three have special characters:
# Q1295: curly apostrophe U+2019 in "team members'"
# Q1320: curly apostrophe U+2019 in "company's"
# Q1328: left double quote U+201C opening "project burnout

replacements = [
    # Q1295 - curly apostrophe in team members'
    (
        "Explanation: Need: guide and calm the team. Option A (Develop different approaches based on team members’ motivation and ability.) fixes it.\"",
        "Explanation: Keywords: team performance assessment, poor performers, tailored leadership, motivation and ability. Effective performance management recognizes that team members have different motivations, experience levels, and developmental needs. Developing different approaches based on each team member's specific motivation and ability level ensures that the feedback and support provided are targeted and likely to drive genuine improvement. (PMBOK Guide) – Seventh Edition, 2021, p. 36, 'Demonstrate Leadership Behaviors'\""
    ),
    # Q1320 - curly apostrophe in company's
    (
        "Explanation: Need: protect value and acceptance. Option D (Propose a hybrid approach, leveraging the benefits of an agile approach while respecting some aspects of the company’s industry.) fixes it.\"",
        "Explanation: Keywords: predictive approach, regulated market, competitive disadvantage, hybrid delivery. When a company in a regulated market is losing its competitive advantage because its predictive approach is too slow, a full pivot to agile is not always feasible given regulatory constraints. A hybrid approach allows the company to benefit from agile's speed and adaptability while still respecting the compliance and governance requirements that the industry demands. (PMBOK Guide) – Seventh Edition, 2021, p. 40, 'Tailor Based on Context'\""
    ),
    # Q1328 - left double quote U+201C opening "project burnout
    (
        "Explanation: Need: protect benefits for users. Option C (The engineer has “project burnout\"\" from working long hours and solving difficult problems.) fixes it.\"",
        "Explanation: Keywords: engineer refusal, project burnout, recognition, workload management. When a highly motivated and capable engineer declines a project invitation, the most likely cause — especially given their history of initiative and complex problem-solving — is burnout from sustained overwork. Project managers must be alert to signs of unsustainable workload and recognize that even highly capable team members need recovery time, or risk losing them from future engagements. (PMBOK Guide) – Seventh Edition, 2021, p. 28, 'Create a Collaborative Team Environment'\""
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
