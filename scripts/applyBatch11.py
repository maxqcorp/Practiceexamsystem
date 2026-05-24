MD_FILE = './src/imports/project-management-questions-1.md'

with open(MD_FILE, 'r', encoding='utf-8') as f:
    content = f.read()

replacements = [
    (
        'Explanation: Need: listen to people needs. Option B (Perform quality assurance to review the processes against the quality management plan and identify gaps.) fixes it."',
        'Explanation: Keywords: quality assurance, process compliance, audit findings, quality management plan. When an internal audit finds missing process documents and approvals on a project that is otherwise delivering good outcomes, quality assurance must be performed to understand the gap between actual processes and the quality management plan. This systematic review identifies where processes deviated from the plan and provides the basis for closing compliance gaps. (PMBOK Guide) – Seventh Edition, 2021, p. 42, \'Build Quality into Processes and Deliverables\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option B (External subject matter experts (SMEs) and the team) fixes it."',
        'Explanation: Keywords: technical issue, aerospace design, external SMEs, specialist expertise. A substantial technical issue in a specialized field like aerospace design requires expertise that may exceed what the internal team possesses — external SMEs provide the specialized knowledge needed to evaluate and resolve complex technical problems. Including both the external experts and the internal team in the discussion ensures that SME insights are contextualized by the team\'s project-specific knowledge. (PMBOK Guide) – Seventh Edition, 2021, p. 44, \'Navigate Complexity\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option D (Meet with the stakeholders regularly to share project objectives and mutually agree on common goals and plans.) fixes it."',
        'Explanation: Keywords: compliance project, stakeholder alignment, common goals, regular meetings. A project aimed at ensuring compliance with multiple regulatory standards across partner organizations succeeds when all parties share a common understanding of objectives and have agreed on the implementation approach. Regular meetings that focus on shared goals and mutual planning replace potential adversarial dynamics with collaborative ownership of compliance outcomes. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    (
        'Explanation: Need: protect value and acceptance. Option B (Statement of work (SOW)) fixes it."',
        'Explanation: Keywords: outsourced deliverables, statement of work, procurement documentation, SOW. When project deliverables will be outsourced, the statement of work is the formal document that describes what the vendor is expected to deliver, including the scope, specifications, and acceptance criteria. A well-defined SOW creates the contractual clarity needed to hold vendors accountable and ensures all parties share a common understanding of what must be produced. (PMBOK Guide) – Seventh Edition, 2021, p. 25, \'Be a Diligent, Respectful, and Caring Steward\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option B (Perform an impact analysis and share the overall schedule impact before deciding on a new priority.) fixes it."',
        'Explanation: Keywords: urgent sponsor request, impact analysis, schedule impact, priority decision. When a sponsor requests immediate reprioritization of a large requirement after a stakeholder has already been committed to a delivery timeline, the project manager must analyze the full schedule impact before making any priority decision. Sharing the impact analysis with stakeholders ensures that the reprioritization decision is made with full awareness of its consequences on current commitments. (PMBOK Guide) – Seventh Edition, 2021, p. 34, \'Recognize, Evaluate, and Respond to System Interactions\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option B (Update the stakeholder register and the stakeholder engagement plan to include the new manager.) fixes it."',
        'Explanation: Keywords: stakeholder change, new manager, stakeholder register, engagement plan update. When a key stakeholder is replaced during project execution, the stakeholder register and engagement plan must be updated to reflect the new individual\'s role, interests, and preferred engagement approach. This ensures the project manager\'s engagement strategy remains current and that the new manager receives appropriate communication and involvement from the start. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    (
        'Explanation: Need: keep plans flexible. Option A (Update the assumptions log and change log, and implement the change control process.) fixes it."',
        'Explanation: Keywords: changed assumptions, assumptions log, change log, change control process. When project assumptions that underpinned the scope and business value case change during execution, the project manager must formally document those changes and process them through change control. Updating the assumptions log and change log provides traceability and ensures that all consequential scope or plan adjustments are properly evaluated and approved. (PMBOK Guide) – Seventh Edition, 2021, p. 50, \'Enable Change to Achieve the Envisioned Future State\'"'
    ),
    (
        'Explanation: Need: watch risks early. Option B (Host a meeting with the vendor and infrastructure manager to help resolve their disagreement.) fixes it."',
        'Explanation: Keywords: vendor dispute, cabling standards, conflict resolution, facilitated meeting. When a disagreement between a vendor and an internal manager escalates into an argument, the project manager must step in as a facilitator to create a structured forum for resolution before the conflict causes further delays. Hosting a meeting with both parties allows the project manager to help them reach a shared understanding of the standards violation and agree on a corrective path forward. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option A (Provide feedback to the team and conduct a meeting to review the team rules.) fixes it."',
        'Explanation: Keywords: new team member, agile inexperience, team rules review, goal achievement. When a new team member without agile experience joins an ongoing sprint and the team begins missing goals, reviewing the team rules creates a shared understanding of expectations and agile working norms. Providing feedback alongside the rules review ensures the team understands what needs to change and gives the new member the behavioral guidance needed to contribute effectively. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option B (Prepare a report outlining the organizational structure and project parameters.) fixes it."',
        'Explanation: Keywords: external stakeholders, mining industry, project parameters, organizational structure. External stakeholders with no industry knowledge need a clear, structured communication that explains both the organizational context and the project\'s specific scope and parameters. Preparing a formal report provides a permanent reference document that allows these stakeholders to understand the project without relying solely on verbal explanations that may be misunderstood or forgotten. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option B (Applied requirements elicitation to involve engaging stakeholders consistently in the requirements process) fixes it."',
        'Explanation: Keywords: CRM implementation, changing requirements, requirements elicitation, consistent engagement. When stakeholders provide different or contradictory information in successive meetings, the root cause is typically an inconsistent requirements elicitation process that fails to maintain continuity and stakeholder alignment across sessions. Applying structured requirements elicitation techniques that consistently engage stakeholders in the same conversation maintains coherence and progressively builds toward a stable, agreed-upon set of requirements. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option B (Speak with the key team member to clarify the situation.) fixes it."',
        'Explanation: Keywords: confidentiality breach, ethical violation, clarification, team conflict. When a team member is accused of an ethical violation, the project manager must first gather the facts directly from that person before taking any action — acting on an accusation without clarification risks unfair outcomes. Speaking with the key team member ensures the project manager understands exactly what happened before determining an appropriate response. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option B (Guide the agile team to add the new scope to the product backlog.) fixes it."',
        'Explanation: Keywords: mid-sprint scope change, product backlog, sprint integrity, agile principles. Sprint goals and backlog items should not be changed mid-sprint — when new scope is identified during a sprint, the agile principle is to add it to the product backlog for prioritization in future sprints rather than disrupting the current commitment. Guiding the team to the backlog preserves sprint integrity while ensuring the new scope is properly captured and prioritized. (PMBOK Guide) – Seventh Edition, 2021, p. 48, \'Embrace Adaptability and Resiliency\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option D (The use of the Monte Carlo method can result in different estimations.) fixes it."',
        'Explanation: Keywords: budget estimation, Monte Carlo simulation, uncertainty modeling, estimation variance. Budget estimates for projects with significant uncertainty — such as those responding to new privacy regulations — legitimately differ when different probability distributions and simulation parameters are used in Monte Carlo analysis. The variance in outputs is a feature of the method that reflects the inherent uncertainty in the project, not an error in the estimation process. (PMBOK Guide) – Seventh Edition, 2021, p. 46, \'Optimize Risk Responses\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option A (Work with the finance team to transition to incremental budgeting.) fixes it."',
        'Explanation: Keywords: agile transformation, incremental budgeting, finance team, budget approach. An agile team delivering a product in an organization transforming to rapid response cannot operate effectively within a traditional annual budget model — incremental budgeting aligned with delivery iterations provides the financial flexibility agile requires. Collaborating with the finance team to adopt incremental budgeting aligns the financial governance model with the agile delivery approach. (PMBOK Guide) – Seventh Edition, 2021, p. 40, \'Tailor Based on Context\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option A (Empower team members to participate in decision-making and take ownership of actions.) fixes it."',
        'Explanation: Keywords: megaproject, multicultural team, team empowerment, decision-making participation. In a megaproject with geographically and culturally diverse stakeholders, productivity improves most when team members are empowered to make decisions and take ownership of their actions rather than waiting for top-down direction. Empowerment reduces coordination delays, builds individual accountability, and leverages the distributed expertise of a diverse team. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option A (Implemented sprint reviews with the product owner and retrospectives with the team to minimize gaps) fixes it."',
        'Explanation: Keywords: product owner expectations, sprint reviews, retrospectives, gaps minimization. Four iterations completed without the product owner\'s expectations being met indicates that the feedback loop between delivery and stakeholder validation was broken. Implementing sprint reviews with the product owner at the end of each iteration creates the continuous alignment checkpoint that surfaces expectation gaps before they accumulate over multiple sprints. (PMBOK Guide) – Seventh Edition, 2021, p. 42, \'Build Quality into Processes and Deliverables\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option B (Perform team-building activities and enhance collaboration.) fixes it."',
        'Explanation: Keywords: hybrid project, low morale, team-building, agile transition conflict. When a team that performed well in predictive stages begins showing conflict and low commitment during agile iterations, the transition has disrupted the team\'s established working dynamics and trust. Team-building activities and enhanced collaboration rebuild the interpersonal connections and shared norms needed for effective agile teamwork. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option C (Ask the product owner to determine if this requirement needs to be treated as a top priority.) fixes it."',
        'Explanation: Keywords: revenue risk, delivery delay, product owner prioritization, urgent requirement. When a stakeholder identifies a time-sensitive requirement with direct revenue implications, the product owner — not the project manager — holds the authority to determine its priority relative to current backlog items. Escalating to the product owner ensures that the prioritization decision is made by the person accountable for product value and business outcomes. (PMBOK Guide) – Seventh Edition, 2021, p. 32, \'Focus on Value\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option B (An iterative-based strategy to maximize value by releasing the product to each country as it is finalized and ready for release in that country) fixes it."',
        'Explanation: Keywords: multi-country launch, iterative release strategy, country-by-country delivery, value maximization. With equal revenue potential per country, releasing each country\'s product as soon as it is ready maximizes cumulative value delivery by avoiding the delay of bundling all countries into a single release. An iterative country-by-country release strategy ensures that value flows to market continuously as each localization is completed. (PMBOK Guide) – Seventh Edition, 2021, p. 32, \'Focus on Value\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option B (The project cost is 10% lower than planned.) fixes it."',
        'Explanation: Keywords: earned value analysis, CPI, budget performance, cost performance. With an EV of $5,000 (50% of $10,000 BAC) and an AC of $4,500, the CPI equals 1.11 — meaning the project is spending approximately 10% less than the budgeted amount for the work completed. This favorable cost performance confirms the project is under budget relative to its progress, making option B the accurate status assessment. (PMBOK Guide) – Seventh Edition, 2021, p. 34, \'Recognize, Evaluate, and Respond to System Interactions\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option A (Analyzed the sponsor\'s communication requirements.) fixes it."',
        'Explanation: Keywords: portal ineffective, sponsor communication, requirements analysis, communication preferences. When a communication tool that was implemented without prior stakeholder input proves ineffective for the sponsor, the root cause is a failure to analyze the sponsor\'s specific communication requirements before designing the solution. Analyzing communication requirements upfront ensures that the chosen tool and format match how each key stakeholder actually needs to receive and use project information. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option A (Escalate the issue to a higher authority.) fixes it."',
        'Explanation: Keywords: weak matrix, interpersonal conflict, escalation, irresolvable issue. In a weak matrix environment where the project manager has limited formal authority, interpersonal conflicts that resist direct resolution and threaten project delivery must be escalated to functional management or a higher authority. Escalation is the appropriate and necessary step when the project manager has exhausted direct resolution options and the conflict continues to impact performance. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option B (Discuss the impact of starting the item with the team.) fixes it."',
        'Explanation: Keywords: sponsor urgent request, Kanban board, WIP impact, team discussion. When a sponsor requests immediate prioritization of a backlog item while many tasks are still in progress on the Kanban board, the team must understand the WIP impact before committing to the change. Discussing the impact with the team ensures the decision is informed by the team\'s current capacity and workflow constraints rather than made unilaterally by the project manager. (PMBOK Guide) – Seventh Edition, 2021, p. 32, \'Focus on Value\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option A (Reaffirm the required project obligations directly with the team member.) fixes it."',
        'Explanation: Keywords: missed meetings, team obligations, direct communication, behavioral expectations. When a team member repeatedly misses meetings without proper communication, the project manager must directly reaffirm what the project obligations are rather than escalating or waiting for the behavior to resolve itself. A direct, private conversation about expectations establishes clear accountability and gives the team member the opportunity to align their behavior with project requirements. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option C (Ensure the project team understands the agreement and contract in place with the supplier.) fixes it."',
        'Explanation: Keywords: unauthorized scope addition, contract boundaries, supplier agreement, team awareness. When a team member informally expands a supplier\'s scope outside the agreed contract, the root cause is typically insufficient understanding of the contractual boundaries among the project team. Ensuring the team understands the supplier agreement prevents future unauthorized scope additions and protects the contractual relationship with the vendor. (PMBOK Guide) – Seventh Edition, 2021, p. 25, \'Be a Diligent, Respectful, and Caring Steward\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option B (Review the issues log to ensure the issues are captured.) fixes it."',
        'Explanation: Keywords: new project manager, serious issues, issues log, project takeover. When a new project manager is informed of serious issues during a project takeover, the first step is to review the issues log to understand what has already been documented, tracked, and assigned for resolution. The issues log provides the authoritative record that reveals the scope and status of known problems before the new PM acts. (PMBOK Guide) – Seventh Edition, 2021, p. 44, \'Navigate Complexity\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option A (Schedule a meeting between the team members to find a solution.) fixes it."',
        'Explanation: Keywords: team member conflict, divergent views, collaborative meeting, conflict resolution. When two team members have conflicting views on how to solve a project problem, the project manager should facilitate a joint meeting where both perspectives can be heard and a mutually acceptable solution can be developed. Bringing the parties together in a structured discussion leverages both viewpoints constructively rather than choosing one approach and dismissing the other. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    (
        'Explanation: Need: secure people or vendors. Option A (Escalate to the project steering committee.) fixes it."',
        'Explanation: Keywords: funding access issue, procurement delay, steering committee escalation, financial blocker. When a project cannot access its approved funding and procurement is stalled, the project manager faces a systemic constraint that is beyond their authority to resolve independently. Escalating to the project steering committee brings the funding blockage to the level of authority that can take action to release funds and unblock the procurement process. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option A (Consider cultural differences among stakeholders.) fixes it."',
        'Explanation: Keywords: global project, cultural differences, communication management, stakeholder diversity. Effective communication in a global project requires accounting for cultural differences that affect how messages are received, interpreted, and responded to by stakeholders from different backgrounds. Considering cultural context when planning communication ensures that the project manager adapts language, format, and style to what will be most effective for each stakeholder group. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option A (Schedule a meeting with the new sponsor in order to explain the agile approach and how teams are supposed to be self-organized.) fixes it."',
        'Explanation: Keywords: new sponsor, agile unfamiliarity, self-organizing teams, stakeholder education. When a new sponsor who is unfamiliar with agile begins requesting more control over the team, the project manager must educate them about agile principles — particularly team self-organization — before their intervention disrupts the team\'s effectiveness. Scheduling a meeting to explain the agile delivery model aligns the sponsor\'s expectations with how agile teams operate and prevents counterproductive micromanagement. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option B (Discuss the problem with the team and decide how to do the work together.) fixes it."',
        'Explanation: Keywords: resource constraint, new feature request, collaborative problem-solving, team capacity. When new work is requested without additional resources or budget, the project manager and team must collectively assess what is feasible within the current constraints rather than the project manager deciding unilaterally. Collaborative problem-solving with the team leverages their technical insight to find creative approaches and builds shared ownership of the solution. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option C (Clarify the relevance of reviewing the documentation on the intranet.) fixes it."',
        'Explanation: Keywords: OPA relevance, organizational process assets, new team member, documentation guidance. When there is disagreement about how much of the OPA documentation a new team member needs to review, the project manager should clarify which documents are relevant to their specific role and tasks rather than either requiring everything or allowing selective review. Explaining the relevance of each document type helps the new member make informed, efficient use of organizational process assets. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option D (Assess the organization\'s culture to determine if agile can be used in project delivery and determine the practices to be used.) fixes it."',
        'Explanation: Keywords: agile adoption, organizational culture assessment, practice selection, implementation readiness. Before implementing agile in any organization, the project manager must assess whether the culture supports the transparency, collaboration, and iterative delivery that agile requires — practices that work in one organization may fail in another with a different culture. Assessing cultural readiness and selecting appropriate agile practices ensures the adoption is tailored to the organization\'s actual context and capacity. (PMBOK Guide) – Seventh Edition, 2021, p. 40, \'Tailor Based on Context\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option D (Burndown chart) fixes it."',
        'Explanation: Keywords: team progress, release schedule, burndown chart, agile metrics. A burndown chart provides a visual representation of remaining work over time relative to the sprint or release target, making it the most direct tool for assessing whether the team is on track to complete work within the planned timeframe. The burndown\'s trend line reveals velocity patterns and signals whether the team needs to adjust its pace or scope to meet the release schedule. (PMBOK Guide) – Seventh Edition, 2021, p. 40, \'Tailor Based on Context\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option D (Encourage the stakeholders to collaborate by facilitating meetings and sharing knowledge.) fixes it."',
        'Explanation: Keywords: conflicting requirements, stakeholder collaboration, facilitated meetings, HR system. When multiple stakeholders submit conflicting requirements for the same system, the project manager must bring those stakeholders together to resolve the conflicts collaboratively rather than accepting contradictory requirements. Facilitating meetings where stakeholders share their perspectives and knowledge enables the group to identify common ground and agree on a unified set of requirements. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option C (Run the meeting and follow up with each one of the absent stakeholders to get their input.) fixes it."',
        'Explanation: Keywords: risk identification, absent stakeholders, follow-up, risk register completion. When stakeholders fail to attend a risk identification session despite confirming, the project manager should proceed with attendees and then follow up individually with each absent stakeholder to capture their risk perspectives. This approach avoids cancelling the session while ensuring all stakeholder viewpoints are eventually incorporated into the risk register. (PMBOK Guide) – Seventh Edition, 2021, p. 46, \'Optimize Risk Responses\'"'
    ),
    (
        'Explanation: Need: keep plans flexible. Option B (Retrospective results) fixes it."',
        'Explanation: Keywords: risk register development, retrospective results, previous event feedback, agile ceremonies. When developing a risk register for a recurring agile project, retrospective results from previous iterations provide the most directly relevant source of risks — they capture what actually went wrong and what improvements were identified in past deliveries. Using retrospective outputs as input to risk planning leverages organizational learning to proactively address known recurring risks. (PMBOK Guide) – Seventh Edition, 2021, p. 46, \'Optimize Risk Responses\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option C (Ask the team to self-organize and manage the work assigned.) fixes it."',
        'Explanation: Keywords: agile self-organizing team, sprint kickoff, team autonomy, servant leadership. In an agile project, once sprint requirements are defined, the team — not the project manager — decides how to organize and execute the work. Asking the team to self-organize reflects the servant leader role and enables the team to apply their collective expertise to determine the most effective way to complete the sprint commitments. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option A (Review the work allocation and reassign some tasks to shorten the critical path.) fixes it."',
        'Explanation: Keywords: work allocation, critical path optimization, task reassignment, schedule improvement. When a project manager identifies that a different task allocation would allow the project to finish earlier, acting to reassign tasks optimizes the schedule before the delay materializes. Reviewing work allocation and shortening the critical path is preferable to compressing tasks through overtime or accepting an avoidable two-week delay. (PMBOK Guide) – Seventh Edition, 2021, p. 34, \'Recognize, Evaluate, and Respond to System Interactions\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option B (Confirmed documentation requirements with stakeholders) fixes it."',
        'Explanation: Keywords: regulatory audit, documentation requirements, early planning, stakeholder confirmation. When a project must produce documentation that will satisfy an internal regulatory audit, the documentation requirements must be confirmed with stakeholders at the outset — not discovered at project close. Early confirmation ensures that documentation is created and maintained throughout the project in a format that will meet audit standards. (PMBOK Guide) – Seventh Edition, 2021, p. 42, \'Build Quality into Processes and Deliverables\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option D (Documented the technical reviews with the new change) fixes it."',
        'Explanation: Keywords: unauthorized change, customer specifications, technical documentation, change control. When a project manager incorporates a technology change that was not in the original customer specifications, the change must be documented through technical reviews and formally approved by the client before delivery. Proper documentation of the change would have created the opportunity for client review and sign-off, preventing the delivery of a product that differed from what the client contracted for. (PMBOK Guide) – Seventh Edition, 2021, p. 50, \'Enable Change to Achieve the Envisioned Future State\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option A (Express trust in the team\'s ability to fulfill the necessary deliverables.) fixes it."',
        'Explanation: Keywords: experienced agile team, trust, servant leadership, team empowerment. An experienced agile team that already knows how to deliver does not need close direction — it needs a project manager who demonstrates confidence in their capability and creates the conditions for them to do their best work. Expressing trust is the most effective way to influence an experienced team, as it reinforces their autonomy and intrinsic motivation. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Options A and D (Host a special meeting to talk about what happened.; Conduct a team-building workshop.) work together."',
        'Explanation: Keywords: team morale, incident impact, team meeting, team-building. When a significant incident damages team morale, both immediate and sustained responses are needed — a special meeting addresses the incident directly and allows the team to process what happened, while a team-building workshop rebuilds the interpersonal trust and cohesion that the incident eroded. Together these actions restore both psychological safety and collaborative effectiveness. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option C (Adopt the role of supporting and empowering the project team to do the work.) fixes it."',
        'Explanation: Keywords: hybrid project, servant leadership, team empowerment, control concerns. When a project manager new to hybrid delivery feels a loss of control, the correct response is not to assert more authority but to shift into the servant leadership role that hybrid and agile delivery requires. Supporting and empowering an experienced team to do the work leverages their capability and builds the trust-based collaboration that is more effective than hierarchical control in a high-uncertainty environment. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option C (Provided specialist training for all team members.) fixes it."',
        'Explanation: Keywords: knowledge silo, specialist resignation, cross-training, information access. When a senior team member departs and others cannot access critical information or complete deliverables, the root cause is a knowledge silo that was never addressed through cross-training. Providing specialist training to all team members prevents single-point-of-failure knowledge dependencies and ensures that project knowledge is distributed across the team. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
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
