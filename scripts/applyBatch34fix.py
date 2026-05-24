MD_FILE = './src/imports/project-management-questions-1.md'

with open(MD_FILE, 'r', encoding='utf-8') as f:
    content = f.read()

# Q210 and Q212 — identical old explanation text, both need updating
old = 'Explanation: Need: listen to people needs. Option B (Discuss with the stakeholder the benefits of the hybrid project and how frequent reviews lead to greater value and less rework) fixes it."'
new = "Explanation: Keywords: hybrid project, stakeholder questions frequent iteration reviews, busy, discuss benefits of reviews. Frequent iteration reviews in a hybrid environment exist to surface issues early and increase stakeholder value through timely feedback. Explaining these benefits to the stakeholder — rather than reducing their involvement — helps them understand why their participation in reviews is a worthwhile investment of their time. (PMBOK Guide) – Seventh Edition, 2021, p. 30, 'Effectively Engage with Stakeholders'\""

count = content.count(old)
if count > 0:
    content = content.replace(old, new)
    print(f'Q210/Q212 updated: {count} occurrence(s) replaced.')
else:
    print('Q210/Q212 NOT FOUND.')

with open(MD_FILE, 'w', encoding='utf-8') as f:
    f.write(content)

print('Done.')
