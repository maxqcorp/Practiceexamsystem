MD_FILE = './src/imports/project-management-questions-1.md'

with open(MD_FILE, 'r', encoding='utf-8') as f:
    content = f.read()

# Q1580 - curly apostrophe U+2019 in "recipients'"
old = "Explanation: Need: listen to people needs. Option B (Focus on the recipients’ needs and not the information itself.) fixes it.\""
new = "Explanation: Keywords: matrix organization, specialist resources, diverse departments, effective communications setup. Effective communication in a complex, multi-department environment requires the project manager to prioritize what each recipient needs to know — not what the project manager wants to convey. Focusing on the recipients' needs shapes the format, level of detail, and timing of communications to maximize comprehension and action, reducing the misunderstandings that arise when information is broadcast uniformly regardless of audience. (PMBOK Guide) – Seventh Edition, 2021, p. 30, 'Effectively Engage with Stakeholders'\""

updated = 0
if old in content:
    content = content.replace(old, new)
    updated += 1
    print('Q1580 updated.')
else:
    print('Q1580 NOT FOUND.')
    # Try to find it
    idx = content.find('Question 1580')
    seg = content[idx:idx+600]
    exp_idx = seg.find('Explanation:')
    print(repr(seg[exp_idx:exp_idx+150]))

with open(MD_FILE, 'w', encoding='utf-8') as f:
    f.write(content)

print(f'Done: {updated} updated.')
