MD_FILE = './src/imports/project-management-questions-1.md'

with open(MD_FILE, 'r', encoding='utf-8') as f:
    content = f.read()

replacements = [
    # Q824 - Need: keep plans flexible (not guide and calm)
    (
        'Explanation: Need: keep plans flexible. Option D (Perform tasks in parallel) fixes it."',
        'Explanation: Keywords: schedule compression, fast tracking, parallel tasks, delivery acceleration. When a project faces a critical deadline, performing independent tasks in parallel (fast tracking) is a schedule compression technique that reduces overall duration without changing scope. This approach accepts increased coordination risk in exchange for faster delivery of project value. (PMBOK Guide) – Seventh Edition, 2021, p. 32, \'Focus on Value\'"'
    ),
    # Q828 - Need: listen to people needs (not guide and calm)
    (
        'Explanation: Need: listen to people needs. Option D (Requirements) fixes it."',
        'Explanation: Keywords: project scope foundation, requirements baseline, scope definition, planning input. Requirements are the foundational input that defines what the project must deliver and establishes the basis for all subsequent planning. Without clearly defined and agreed-upon requirements, scope, schedule, and cost baselines cannot be reliably established or controlled. (PMBOK Guide) – Seventh Edition, 2021, p. 42, \'Build Quality into Processes and Deliverables\'"'
    ),
    # Q829 - Need: listen to people needs (not guide and calm)
    (
        'Explanation: Need: listen to people needs. Option B (Explain and communicate the new approach to the project sponsor and key stakeholders) fixes it."',
        'Explanation: Keywords: new approach introduction, stakeholder communication, agile transition, change buy-in. When adopting a new project approach, the project manager must proactively explain and communicate the rationale and implications to the project sponsor and key stakeholders. Ensuring their understanding and buy-in is essential to securing the organizational support needed for the approach to succeed. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    # Q830 - Need: listen to people needs (not guide and calm)
    (
        'Explanation: Need: listen to people needs. Option C (Ask country A to submit a change request that will be analyzed along with countries B and C) fixes it."',
        'Explanation: Keywords: multi-country project, unilateral change request, change control process, integrated scope management. When one country requests a scope change that affects the entire project, the project manager must route it through the formal change control process and evaluate it alongside impacts for all affected parties. Bypassing this process risks creating scope imbalances and conflicting baselines across project regions. (PMBOK Guide) – Seventh Edition, 2021, p. 50, \'Enable Change to Achieve the Envisioned Future State\'"'
    ),
    # Q831 - Need: listen to people needs (not guide and calm)
    (
        'Explanation: Need: listen to people needs. Option C (Inform the customer of the issue and discuss the options so that they are able to make a decision on cost versus timeline) fixes it."',
        'Explanation: Keywords: quality issue, customer decision, cost versus timeline trade-off, transparent communication. When a quality issue creates a cost-versus-timeline decision, the project manager must present the options transparently to the customer so they can make an informed decision aligned with their priorities. This respects customer ownership of key trade-off decisions and avoids the project manager unilaterally absorbing choices that belong to the client. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    # Q832 - Need: listen to people needs (not guide and calm)
    (
        'Explanation: Need: listen to people needs. Option B (Review the missed program deliverables with the project team) fixes it."',
        'Explanation: Keywords: missed deliverables, team review, root cause analysis, program accountability. When program deliverables are missed, the project manager must bring the team together to review what happened before escalating or reporting externally. A collaborative review surfaces root causes, maintains team accountability, and produces a clearer picture of what corrective action is needed. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    # Q836 - Need: listen to people needs (not guide and calm)
    (
        'Explanation: Need: listen to people needs. Option A (Assess the business value impact and review the product roadmap to include any changes) fixes it."',
        'Explanation: Keywords: new stakeholder requirements, business value assessment, product roadmap revision, agile prioritization. When new stakeholder requirements emerge, the project manager must assess their business value impact and reflect the changes in the product roadmap before committing to implementation. This value-driven evaluation ensures that accommodated changes genuinely strengthen the project\'s outcomes and are properly sequenced in the delivery plan. (PMBOK Guide) – Seventh Edition, 2021, p. 32, \'Focus on Value\'"'
    ),
    # Q837 - Need: listen to people needs (not guide and calm)
    (
        'Explanation: Need: listen to people needs. Option D (Implement a communications management plan) fixes it."',
        'Explanation: Keywords: communication breakdowns, global project, communications management plan, information flow. Recurring communication failures in a global project signal the absence of a structured communication framework. Implementing a communications management plan formalizes who receives what information, through which channels, and at what frequency — eliminating the ambiguity that causes breakdowns. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    # Q839 - Need: protect benefits for users (not guide and calm)
    (
        'Explanation: Need: protect benefits for users. Option C (Ensure that compliance is explicitly mentioned in the relevant requirements) fixes it."',
        'Explanation: Keywords: compliance integration, requirements documentation, explicit compliance language, regulatory traceability. Compliance requirements must be explicitly embedded in the relevant project requirements to ensure they are visible, traceable, and verifiable throughout delivery. Leaving compliance implicit creates a gap that may only surface during audits or post-delivery reviews when corrective action is more costly. (PMBOK Guide) – Seventh Edition, 2021, p. 42, \'Build Quality into Processes and Deliverables\'"'
    ),
    # Q841 - Need: watch risks early (not guide and calm)
    (
        'Explanation: Need: watch risks early. Option B (Focus on delivering incremental value through multiple smaller deliveries) fixes it."',
        'Explanation: Keywords: agile delivery, incremental value, smaller deliveries, continuous feedback. An agile project approach centers on delivering working increments of value frequently rather than waiting for a single large release. Multiple smaller deliveries allow stakeholders to validate outcomes, provide feedback, and adjust priorities — reducing the risk of delivering a complete solution that misses actual needs. (PMBOK Guide) – Seventh Edition, 2021, p. 32, \'Focus on Value\'"'
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
