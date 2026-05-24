MD_FILE = './src/imports/project-management-questions-1.md'

with open(MD_FILE, 'r', encoding='utf-8') as f:
    content = f.read()

# Q1445 - curly apostrophe U+2019 in "stakeholders'"
old = "Explanation: Need: listen to people needs. Option B (Include the project stakeholders’ needs while planning the project communications strategy.) fixes it.\""
new = "Explanation: Keywords: emails from stakeholders requesting status, project communications strategy, avoid in the future. When stakeholders proactively reach out for information the project has not provided, it signals a gap in the communications plan. Including stakeholder communication needs during planning — rather than after complaints arise — ensures that each stakeholder receives the right information at the right frequency, eliminating the need for ad hoc requests. (PMBOK Guide) – Seventh Edition, 2021, p. 30, ‘Effectively Engage with Stakeholders’\""

updated = 0
if old in content:
    content = content.replace(old, new)
    updated += 1
    print('Q1445 updated.')
else:
    print('Q1445 NOT FOUND.')

with open(MD_FILE, 'w', encoding='utf-8') as f:
    f.write(content)

print(f'Done: {updated} updated.')
