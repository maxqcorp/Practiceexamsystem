MD_FILE = './src/imports/project-management-questions-1.md'

with open(MD_FILE, 'r', encoding='utf-8') as f:
    content = f.read()

# These use escaped ASCII apostrophe \' in old text to match file content
replacements = [
    (
        'Explanation: Need: keep plans flexible. Option C (The project manager is obligated to comply with the project location\'s regulatoryrequirements.) fixes it."',
        'Explanation: Keywords: health and safety requirements, regulatory compliance, project location, legal obligation. Health and safety regulations are non-negotiable legal requirements that the project manager is obligated to address regardless of project complexity or schedule pressure. As a steward of organizational and public interests, the project manager must identify and integrate all regulatory requirements of the project location into the project plan. (PMBOK Guide) – Seventh Edition, 2021, p. 25, \'Be a Diligent, Respectful, and Caring Steward\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option D (Treat it as a change request and assess the effect on the project\'s goals.) fixes it."',
        'Explanation: Keywords: missing feature claim, change request, international client, scope impact assessment. When a stakeholder claims a feature discussed at initiation was not implemented, the project manager must treat it as a change request and assess its full impact on project goals before taking any action. Implementing unvetted claims as immediate work items bypasses change control and risks disrupting the scope, schedule, and cost baselines. (PMBOK Guide) – Seventh Edition, 2021, p. 34, \'Recognize, Evaluate, and Respond to System Interactions\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option B (Talk with project B\'s leader to discuss possible impacts to both projects.) fixes it."',
        'Explanation: Keywords: cross-project resource sharing, competing demands, impact on both projects, leader dialogue. When a team member is consistently being pulled into another project, the project manager must proactively engage with that project\'s leader to understand and address the potential impact on both initiatives. This leader-to-leader conversation demonstrates accountability, prevents silent resource conflicts from escalating, and enables a coordinated solution serving both projects\' needs. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option A (Emphasize the ground rules and then focus on today\'s activities and impediments.) fixes it."',
        'Explanation: Keywords: standup meeting, open criticism, psychological safety, ground rules. During a standup meeting, publicly criticizing a team member disrupts psychological safety and derails the meeting from its intended purpose. The agile coach should immediately reinforce ground rules to restore a respectful environment, then redirect the team to focus on impediments and activities as the meeting structure requires. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option D (Recommend to the sponsor to review the results of the team\'s supplier evaluation.) fixes it."',
        'Explanation: Keywords: sponsor preferred supplier, unreliable vendor, objective evaluation results, stewardship. A project manager who knows a sponsor-preferred supplier has a track record of non-performance has a professional obligation to present objective evaluation data rather than simply accommodating the preference. Recommending that the sponsor review the team\'s supplier evaluation ensures procurement decisions are grounded in evidence and due diligence, protecting the project\'s quality and schedule integrity. (PMBOK Guide) – Seventh Edition, 2021, p. 25, \'Be a Diligent, Respectful, and Caring Steward\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option D (Document the client\'s responsibility for the integration with the security subsystem.) fixes it."',
        'Explanation: Keywords: external dependency, client team integration, security subsystem, documented responsibility. When a client insists their own team must perform a specific integration, the project manager must formally document this as the client\'s responsibility — not simply accept it verbally or resist it. Clear documentation protects the project team from being blamed for delays caused by the client\'s integration work and ensures all parties understand where accountability lies for that deliverable. (PMBOK Guide) – Seventh Edition, 2021, p. 34, \'Recognize, Evaluate, and Respond to System Interactions\'"'
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
