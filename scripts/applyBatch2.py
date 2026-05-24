import sys

MD_FILE = './src/imports/project-management-questions-1.md'

with open(MD_FILE, 'r', encoding='utf-8') as f:
    content = f.read()

replacements = [
    (
        'Explanation: Need: guide and calm the team. Options B and D (Evaluate the project manager’s own strengths and weaknesses as a virtual team leader to identify avoidable pitfalls; Establish in the beginning, how progress will be monitored and the best means for communicating progress) work together."',
        'Explanation: Keywords: virtual team launch, PM self-assessment, progress monitoring, communication norms. Launching a virtual team requires the PM to first understand their own gaps as a remote leader, then establish clear norms for how progress will be tracked and communicated. Both actions set the foundation before any work begins, preventing the coordination breakdowns that typically derail virtual teams. (PMBOK Guide) – Seventh Edition, 2021, p. 28, p. 29, ‘Create a Collaborative Team Environment’"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option A (The project is decomposed into features and based on the feature value and the velocity of the team, the team provides the estimate) fixes it."',
        'Explanation: Keywords: portfolio backlog, budget estimation, feature decomposition, team velocity. In an agile context, budget estimates are most reliably produced by decomposing the project into features and using the team’s known velocity to derive a cost-per-feature figure. This grounds the estimate in real delivery data rather than assumptions, making it suitable for portfolio prioritization. (PMBOK Guide) – Seventh Edition, 2021, p. 40, ‘Tailor Based on Context’"'
    ),
    (
        'Explanation: Need: listen to people needs. Option B (Implemented the communications management plan properly) fixes it."',
        'Explanation: Keywords: cost overrun threshold, CEO constraint, risk communication gap. The PM updated the risk register but never surfaced the 25% overrun risk to stakeholders who held the authority to define acceptable thresholds. A properly implemented communications management plan would have ensured the right information reached the CEO in time to align on tolerance limits before the risk materialized. (PMBOK Guide) – Seventh Edition, 2021, p. 30, ‘Effectively Engage with Stakeholders’"'
    ),
    (
        'Explanation: Need: control changes and baselines. Option D (Procurement audit) fixes it."',
        'Explanation: Keywords: multiple suppliers, project closure, unexpected financial balance, procurement. An unexplained financial balance at project close involving multiple suppliers points to a procurement discrepancy. A procurement audit traces each supplier contract and payment against the project records to identify where the surplus originated, which is required before the project can be properly closed. (PMBOK Guide) – Seventh Edition, 2021, p. 25, ‘Be a Diligent, Respectful, and Caring Steward’"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option C (Validated the project artifacts) fixes it."',
        'Explanation: Keywords: mid-project handover, risk register version conflict, project artifacts. When a PM takes over mid-project, conflicting document versions are a sign that artifact governance has broken down. Validating the project artifacts at onboarding ensures the PM is working from a single authoritative baseline rather than building plans on outdated information. (PMBOK Guide) – Seventh Edition, 2021, p. 25, ‘Be a Diligent, Respectful, and Caring Steward’"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option A (Submit a change request.) fixes it."',
        'Explanation: Keywords: missing deliverable, critical path impact, execution phase, scope change. Discovering a missing deliverable that affects the critical path is a scope change, not something the PM can quietly absorb. Submitting a change request ensures the addition is formally reviewed, approved, and reflected in the baseline so schedule and cost impacts are properly managed. (PMBOK Guide) – Seventh Edition, 2021, p. 50, ‘Enable Change to Achieve the Envisioned Future State’"'
    ),
    (
        'Explanation: Need: listen to people needs. Option D (Analyze the reason for the gap in understanding with both sides and negotiate a solution) fixes it."',
        'Explanation: Keywords: sprint review, stakeholder expectation gap, acceptance criteria met, feature misalignment. When a stakeholder says features are missing but the team can prove each increment was approved, the issue is a gap in shared understanding rather than a delivery failure. Analyzing the root cause of that gap with both parties and negotiating a solution addresses the relationship problem, not just the technical one. (PMBOK Guide) – Seventh Edition, 2021, p. 30, ‘Effectively Engage with Stakeholders’"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option D (Mentor the new team member on the methodology the project team is using) fixes it."',
        'Explanation: Keywords: new Scrum team member, methodology mismatch, daily standup disruption, team friction. A team member defaulting to Scrum habits on a non-Scrum project is not being disruptive intentionally — they are applying what they know. Mentoring them on the project’s specific methodology corrects the behaviour at the source while preserving team cohesion. (PMBOK Guide) – Seventh Edition, 2021, p. 28, p. 29, ‘Create a Collaborative Team Environment’"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option B (Get commitment from the team to include all of the required regulations) fixes it."',
        'Explanation: Keywords: MVP definition, mandatory regulations, compliance, agile scope decision. Mandatory regulations are not negotiable backlog items — they are constraints the product must satisfy regardless of schedule pressure. The PM must get the team’s commitment to include them because launching a non-compliant product would invalidate the entire project’s value. (PMBOK Guide) – Seventh Edition, 2021, p. 25, ‘Be a Diligent, Respectful, and Caring Steward’"'
    ),
    (
        'Explanation: Need: listen to people needs. Option D (Conduct reviews with stakeholders to discuss the potential benefits the approach may have to the project) fixes it."',
        'Explanation: Keywords: iterative tools adoption, benefit realization, PMO request, stakeholder input. Measuring the benefits of a new approach cannot be done by the PM alone — the people who worked within it are the best source of evidence. Stakeholder reviews surface the real-world impact of the iterative tools, giving the PMO meaningful data to inform future adoption decisions. (PMBOK Guide) – Seventh Edition, 2021, p. 32, ‘Focus on Value’"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option D (Promote collaboration to help remove the obstacles for the team) fixes it."',
        'Explanation: Keywords: agile transition, organizational impediments, retrospective, servant leadership. When the team surfaces obstacles in the retrospective, the servant leader’s role is to facilitate their removal — not by solving problems for the team, but by creating the conditions and collaboration needed for the team and organization to resolve them together. (PMBOK Guide) – Seventh Edition, 2021, p. 36, ‘Demonstrate Leadership Behaviors’"'
    ),
    (
        'Explanation: Need: control changes and baselines. Option C (Improve organizational readiness by addressing impediments to agile in the organization.) fixes it."',
        'Explanation: Keywords: agile transformation, organizational readiness, impediments, change strategy. Sustainable agile adoption fails when the organization’s structures and culture are not ready to support it. Identifying and removing the specific impediments that block agile ways of working builds the foundation that makes the transformation stick rather than reverting after initial rollout. (PMBOK Guide) – Seventh Edition, 2021, p. 48, ‘Embrace Adaptability and Resiliency’"'
    ),
    (
        'Explanation: Need: listen to people needs. Option A (Support the team as necessary to find the minimum viable product (MVP).) fixes it."',
        'Explanation: Keywords: servant leadership, hardware-software integration, MVP, accelerated testing. A servant leader does not direct — they support the team’s judgment and remove barriers to progress. When the team has already assessed feasibility and initiated accelerated testing, the PM’s role is to back that effort and ensure the team has what they need to reach the MVP. (PMBOK Guide) – Seventh Edition, 2021, p. 36, ‘Demonstrate Leadership Behaviors’"'
    ),
    (
        'Explanation: Need: listen to people needs. Option B (Hold a meeting with the client to address the issue) fixes it."',
        'Explanation: Keywords: client payment disputes, invoice challenges, late partial payments, procurement relationship. Repeated invoice disputes and late partial payments signal a breakdown in the client relationship that will not resolve itself. A direct meeting surfaces the real concern — whether it is a cash flow issue, a dissatisfaction, or a misunderstanding — so the PM can address it before it becomes a contractual or legal matter. (PMBOK Guide) – Seventh Edition, 2021, p. 30, ‘Effectively Engage with Stakeholders’"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option A (Coach the product owner on how to create a product backlog) fixes it."',
        'Explanation: Keywords: Scrum-Kanban hybrid, product owner confusion, product backlog, agile coaching. In a hybrid agile approach, the product backlog is the central tool through which the product owner manages and communicates priorities. Coaching the product owner on how to build it gives them the foundation they need to fulfil their role and unblock the team’s delivery. (PMBOK Guide) – Seventh Edition, 2021, p. 36, ‘Demonstrate Leadership Behaviors’"'
    ),
    (
        'Explanation: Need: listen to people needs. Option B (Have a meeting with project manager of the other project to find a resource optimization solution that works for both projects) fixes it."',
        'Explanation: Keywords: shared resource conflict, two projects, resource optimization, program-level dependency. A resource shared across two projects creates a cross-project dependency that neither PM can resolve unilaterally. Meeting with the other project manager to negotiate a solution recognizes that both projects are part of a larger system and that the best outcome requires coordinated decision-making. (PMBOK Guide) – Seventh Edition, 2021, p. 34, ‘Recognize, Evaluate, and Respond to System Interactions’"'
    ),
    (
        'Explanation: Need: listen to people needs. Option B (Perform a stakeholder evaluation) fixes it."',
        'Explanation: Keywords: sponsor dissatisfaction, requirements development, stakeholder realignment. When the sponsor — the project’s primary authority — is unhappy with how requirements are being developed, the first step is to understand their specific expectations and engagement level. A stakeholder evaluation surfaces the gap so the PM can realign the process to what the sponsor actually needs. (PMBOK Guide) – Seventh Edition, 2021, p. 30, ‘Effectively Engage with Stakeholders’"'
    ),
    (
        'Explanation: Need: listen to people needs. Option C (Defined the team ground rules and shared project vision.) fixes it."',
        'Explanation: Keywords: agile team, product owner expectation gap, retrospective, ground rules, shared vision. Unmet product owner expectations discovered in a retrospective trace back to the absence of a shared understanding from day one. Establishing ground rules and a common project vision at the start aligns the entire team — including the product owner — on what success looks like before any work begins. (PMBOK Guide) – Seventh Edition, 2021, p. 28, p. 29, ‘Create a Collaborative Team Environment’"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option A (Encourage frequent small team meetings with two or three team members.) fixes it."',
        'Explanation: Keywords: distributed team, three time zones, daily standup, communication adaptation. A single daily standup that no time zone finds convenient defeats the purpose of the ceremony. Encouraging smaller, overlapping meetings between team members in adjacent time zones preserves the communication intent of the standup while adapting the format to the team’s geographic reality. (PMBOK Guide) – Seventh Edition, 2021, p. 40, ‘Tailor Based on Context’"'
    ),
    (
        'Explanation: Need: listen to people needs. Option C (Award certificates of appreciation to encourage the team) fixes it."',
        'Explanation: Keywords: tight delivery schedule, sponsor pressure, team motivation, performance recognition. During high-pressure delivery, additional pressure from the PM rarely sustains performance — recognition does. Awarding certificates of appreciation acknowledges the team’s effort and reinforces the behaviours needed to carry performance through to completion. (PMBOK Guide) – Seventh Edition, 2021, p. 36, ‘Demonstrate Leadership Behaviors’"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option C (Review and adapt the appropriate project artifacts.) fixes it."',
        'Explanation: Keywords: schedule delay, excessive documentation, project artifacts, tailoring. When documentation activities are consuming time meant for delivery, the artifacts themselves need to be re-evaluated. Reviewing and adapting project artifacts to remove unnecessary documentation is a tailoring decision that realigns effort with value. (PMBOK Guide) – Seventh Edition, 2021, p. 40, ‘Tailor Based on Context’"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option B (Request the high-performing team member to mentor the other team members) fixes it."',
        'Explanation: Keywords: high performer, performance gap, team cohesion, mentoring. Channelling a high performer’s capability into mentoring turns individual excellence into collective growth. This approach addresses both concerns at once — the team member is recognized and retained through a meaningful expanded role, and the performance gap across the team begins to close. (PMBOK Guide) – Seventh Edition, 2021, p. 28, p. 29, ‘Create a Collaborative Team Environment’"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option D (The WBS dictionary) fixes it."',
        'Explanation: Keywords: WBS, lowest-level decomposition, missing detail, work package information. The WBS structure shows what work exists but not the full context behind each work package. The WBS dictionary provides the detailed descriptions, assumptions, and criteria for each package that the PM needs to fully understand the scope and identify what information appears to be missing. (PMBOK Guide) – Seventh Edition, 2021, p. 25, ‘Be a Diligent, Respectful, and Caring Steward’"'
    ),
    (
        'Explanation: Need: protect benefits for users. Options B and C (Set up a meeting with neighborhood representatives to win their cooperation; Analyze the situation and find out what is causing the neighborhood\'s negative attitude.) work together."',
        'Explanation: Keywords: neighborhood resistance, project impact, community engagement, root cause analysis. Community opposition that threatens the project deadline must be addressed through direct engagement, not avoidance. Meeting with neighborhood representatives opens dialogue while analyzing the root cause of their resistance ensures the PM responds to the real grievance rather than surface-level symptoms. (PMBOK Guide) – Seventh Edition, 2021, p. 30, ‘Effectively Engage with Stakeholders’"'
    ),
    (
        'Explanation: Need: keep plans flexible. Option A (Implement the planned risk response to handle the issue.) fixes it."',
        'Explanation: Keywords: data breach, archiving system, planned risk response, issue response. When a risk event materializes, the correct first action is to execute the pre-established risk response — not to improvise. The planned response exists precisely for this moment and executing it immediately limits impact and demonstrates disciplined risk management. (PMBOK Guide) – Seventh Edition, 2021, p. 46, ‘Optimize Risk Responses’"'
    ),
    (
        'Explanation: Need: listen to people needs. Option C (Review target benefits.) fixes it."',
        'Explanation: Keywords: regulatory change risk, product launch threat, iterative project, benefit realization. A potential regulation change that could block the product launch directly threatens the project’s reason for existing. Reviewing target benefits helps the PM assess whether the project can still deliver its intended value under the new regulatory scenario, and informs what adjustments are needed before committing further. (PMBOK Guide) – Seventh Edition, 2021, p. 32, ‘Focus on Value’"'
    ),
    (
        'Explanation: Need: listen to people needs. Option C (Incorporate design thinking practices into the project life cycle to better understand the product\'s personas and be more effective to match their needs.) fixes it."',
        'Explanation: Keywords: stakeholder feedback, feature misalignment, iterative delivery, design thinking. Missing the mark on features after multiple iterations indicates that requirements gathering has not produced genuine insight into user needs. Design thinking practices build empathy with the actual personas using the product, uncovering the needs behind the stated requirements so future iterations deliver features that truly match what stakeholders value. (PMBOK Guide) – Seventh Edition, 2021, p. 30, ‘Effectively Engage with Stakeholders’"'
    ),
]

updated = 0
failed = []

for old, new in replacements:
    if old in content:
        content = content.replace(old, new)
        updated += 1
    else:
        # Try to identify which Q number this is
        snippet = old[:60]
        failed.append(snippet)

with open(MD_FILE, 'w', encoding='utf-8') as f:
    f.write(content)

print(f'Done: {updated} updated, {len(failed)} failed.')
for s in failed:
    print(f'  NOT FOUND: {s!r}')
