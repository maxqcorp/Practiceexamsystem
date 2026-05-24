MD_FILE = './src/imports/project-management-questions-1.md'

with open(MD_FILE, 'r', encoding='utf-8') as f:
    content = f.read()

replacements = [
    (
        'Explanation: Need: guide and calm the team. Option C (Initiate rewards and incentives according to assessment results) fixes it."',
        'Explanation: Keywords: team fatigue, final sprint, recognition, motivation. When a team is showing weariness near project completion, the project manager must use rewards and recognition aligned with individual motivations to sustain performance. Incentives tied to assessed contributions reinforce effort and rebuild morale without ignoring the real human cost of extended effort. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option C (Show empathy and praise the marketing executive\'s strengths) fixes it."',
        'Explanation: Keywords: emotional intelligence, declining performance, empathy, team member wellbeing. A project manager demonstrating emotional intelligence recognizes that performance decline may stem from personal stress and responds with empathy rather than accountability measures. Praising strengths while acknowledging challenges helps re-engage the executive and models the caring stewardship PMBOK emphasizes for team leaders. (PMBOK Guide) – Seventh Edition, 2021, p. 25, \'Be a Diligent, Respectful, and Caring Steward\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option B (Validate the reason and add it as an issue in the issue log) fixes it."',
        'Explanation: Keywords: overtime pay dispute, issue log, validation, HR issue. When a team subgroup reports a compensation discrepancy, the project manager must first validate the claim and formally record it in the issue log before escalating. Logging the issue ensures it receives proper tracking and resolution through the appropriate governance channel rather than being dismissed or mishandled. (PMBOK Guide) – Seventh Edition, 2021, p. 25, \'Be a Diligent, Respectful, and Caring Steward\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option A (Pay attention to team dynamics and understand that coaching is done simultaneously at an individual and whole-team level) fixes it."',
        'Explanation: Keywords: agile lead, team dynamics, coaching, individual and team level. An agile lead sets the team up for success by attending to both individual needs and collective group dynamics simultaneously. Coaching at both levels allows the leader to address personal blockers while fostering the shared behaviors and norms needed for sustainable high performance. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option C (Prioritize the user stories with issues and have the team resolve them) fixes it."',
        'Explanation: Keywords: risks materialized as issues, velocity impact, user story prioritization, backlog management. When multiple risks become active issues that reduce team velocity, the project manager must refocus the team on resolving the highest-impact items by prioritizing the affected user stories. This agile response addresses the root cause directly rather than deferring through bureaucratic channels. (PMBOK Guide) – Seventh Edition, 2021, p. 46, \'Optimize Risk Responses\'"'
    ),
    (
        'Explanation: Need: protect value and acceptance. Option C (Show empathy and praise the marketing executive\'s strengths) fixes it."',
        'Explanation: Keywords: declining performance, stress, empathy, emotional intelligence. When a team member\'s performance is declining due to apparent stress, the project manager\'s first responsibility is to show empathy and acknowledge strengths rather than escalate or reassign work. This servant leadership response creates psychological safety and gives the individual the support needed to recover their performance. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    (
        'Explanation: Need: secure people or vendors. Option C (Meet with the product owner to confirm the minimum viable product (MVP) option) fixes it."',
        'Explanation: Keywords: budget reallocation, hybrid project, minimum viable product, product owner alignment. When over half the project budget is unexpectedly reallocated, the project manager must immediately work with the product owner to determine what can still be delivered as an MVP within the remaining constraints. This value-focused decision protects the project\'s core benefits while responding pragmatically to the changed resource reality. (PMBOK Guide) – Seventh Edition, 2021, p. 32, \'Focus on Value\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option D (Assess the repository to check for inconsistencies.) fixes it."',
        'Explanation: Keywords: benefits management plan, inconsistent data, repository audit, stakeholder concern. Before revising any plan, the project manager must first assess the full repository to understand the scope and root cause of the reported inconsistencies. This systematic diagnostic step ensures any updates address the actual problem rather than creating further misalignment. (PMBOK Guide) – Seventh Edition, 2021, p. 34, \'Recognize, Evaluate, and Respond to System Interactions\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option A (Political, economic social, technological legal, and environmental (PESTLE)) fixes it."',
        'Explanation: Keywords: global solution, government regulations, scope impact, environmental scanning. When new government regulations threaten a globally deployed project, the project manager needs a macro-environmental analysis framework to categorize and assess the full range of political, legal, and systemic impacts. PESTLE is the appropriate tool to map these external forces and inform backlog prioritization decisions. (PMBOK Guide) – Seventh Edition, 2021, p. 34, \'Recognize, Evaluate, and Respond to System Interactions\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option D (Understand the user concerns and revisit the stakeholder engagement plan) fixes it."',
        'Explanation: Keywords: resistant departments, stakeholder engagement, enterprise-wide software, user concerns. When departments resist a project despite senior management support, the project manager must diagnose the root cause by listening to their concerns before trying to overcome resistance. Revisiting the stakeholder engagement plan with new understanding allows for a tailored approach that addresses department-specific objections. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    (
        'Explanation: Need: keep plans flexible. Option A (Check the change management plan) fixes it."',
        'Explanation: Keywords: quality issue, change to quality standard, no available budget, change management. When a quality concern requires modifying an established standard but no budget exists, the project manager must follow the change management plan to formally evaluate the request. The change management process ensures all impacts are assessed and approved through governance before any standards are altered. (PMBOK Guide) – Seventh Edition, 2021, p. 48, \'Embrace Adaptability and Resiliency\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option B (Review the requirements traceability matrix with the team lead and the client to adequately resolve the issue) fixes it."',
        'Explanation: Keywords: acceptance criteria dispute, requirements traceability, agile project, client-team conflict. When client and team lead have opposing views on whether a deployment met acceptance criteria, the project manager must use the requirements traceability matrix as the objective reference to resolve the dispute. This evidence-based approach replaces subjective arguments with documented agreements and protects both parties. (PMBOK Guide) – Seventh Edition, 2021, p. 42, \'Build Quality into Processes and Deliverables\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option D (Review the risk management plan and mitigation plan to understand the impact of this issue) fixes it."',
        'Explanation: Keywords: team member departure, hybrid project, mitigation plan, resource risk. When a team member leaves near project completion, the project manager must immediately consult the risk management and mitigation plans to understand the pre-planned response for this type of resource loss. Acting on documented mitigation strategies is faster and more coordinated than improvising a response under pressure. (PMBOK Guide) – Seventh Edition, 2021, p. 46, \'Optimize Risk Responses\'"'
    ),
    (
        'Explanation: Need: keep plans flexible. Option B (Review the schedule baseline and consider adopting a schedule performance indicator) fixes it."',
        'Explanation: Keywords: budget deviation, revenue tracking, missing schedule performance, performance measurement gap. A project that measures only budget and revenue misses critical schedule health data needed for complete performance oversight. The project manager should review the schedule baseline and propose adding a schedule performance index (SPI) to give stakeholders a full picture of project health. (PMBOK Guide) – Seventh Edition, 2021, p. 40, \'Tailor Based on Context\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option B (Create a contingency plan in case the project deviates from the initial plan.) fixes it."',
        'Explanation: Keywords: fixed-cost contract, internal constraints, iterations at risk, contingency planning. When a project manager identifies constraints that will prevent completing the project as planned, creating a contingency plan is the proactive response that protects the project\'s commitments. This approach anticipates deviation rather than reacting to it, enabling the team to execute a fallback while still working toward the original plan. (PMBOK Guide) – Seventh Edition, 2021, p. 46, \'Optimize Risk Responses\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option C (Review and clarify roles, responsibilities, and the governance model at the next sprintreview meeting.) fixes it."',
        'Explanation: Keywords: escalation confusion, unclear governance, client escalation path, roles and responsibilities. When clients escalate without direction due to unclear rates and responsibilities, the project manager must establish explicit governance structures and escalation paths. Using the next sprint review to clarify roles and the governance model addresses the systemic gap transparently with all relevant parties. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option A (Verified applicable budget inputs related to this project) fixes it."',
        'Explanation: Keywords: historical project reference, baseline cost discrepancy, budget inputs, market conditions. Using a past project as a cost baseline without verifying current budget inputs leads to inaccurate estimates due to changes in market conditions, inflation, and resource costs. The project manager should have validated all applicable budget inputs before finalizing the plan to ensure the estimate reflected the current environment. (PMBOK Guide) – Seventh Edition, 2021, p. 25, \'Be a Diligent, Respectful, and Caring Steward\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option D (Servant) fixes it."',
        'Explanation: Keywords: servant leadership, team autonomy, risk identification, step definition. When the project manager needs the team to define their own process steps and identify risks for a migration, servant leadership is the most effective style. A servant leader facilitates the team\'s thinking, removes impediments, and empowers them to own the analysis rather than directing them prescriptively. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    (
        'Explanation: Need: secure people or vendors. Option A (Ask the vendor if the minimally sufficient materials can be produced in time to meet the deadline.) fixes it."',
        'Explanation: Keywords: vendor delay, key component shortage, critical milestone, minimum viable delivery. When a supplier cannot deliver full quantities on time, the project manager should first explore whether a minimal sufficient quantity can meet the immediate milestone rather than escalating or seeking replacements. This pragmatic negotiation preserves the vendor relationship while protecting the critical deadline. (PMBOK Guide) – Seventh Edition, 2021, p. 34, \'Recognize, Evaluate, and Respond to System Interactions\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option B (Work with the project sponsor to determine an appropriate response.) fixes it."',
        'Explanation: Keywords: hostile executive, resource reallocation threat, sponsor engagement, political risk. When a senior executive actively works to undermine a project by threatening to reallocate key resources, the project manager must escalate to the project sponsor who has the organizational authority to address executive-level interference. This protects the project team and leverages appropriate governance channels rather than confronting the executive unilaterally. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option C (Plan for training on agile tools and techniques used in the defined hybrid methodologyfor consistent application by all team members.) fixes it."',
        'Explanation: Keywords: hybrid transition, distributed team, varied agile knowledge, consistent application. When a distributed team has uneven agile knowledge, inconsistent methodology application becomes a schedule and delivery risk. Planning targeted training ensures all team members apply the hybrid approach consistently, reducing the variability that threatens timely delivery. (PMBOK Guide) – Seventh Edition, 2021, p. 40, \'Tailor Based on Context\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option C (Meet with the compliance team and make sure that their requirements are covered in thedefinition of done (DoD) for each story.) fixes it."',
        'Explanation: Keywords: agile project, compliance standards, definition of done, regulatory integration. Integrating compliance requirements into the definition of done for each user story ensures that every delivered increment meets regulatory standards without requiring a separate compliance layer. This approach embeds quality and compliance into the iterative process rather than treating it as a gate at the end. (PMBOK Guide) – Seventh Edition, 2021, p. 42, \'Build Quality into Processes and Deliverables\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option B (Time management and stakeholder engagement) fixes it."',
        'Explanation: Keywords: high-visibility project, medium complexity, ready-to-use delivery, focus areas. A high-visibility project with a fixed ready-to-use delivery requirement demands strong schedule discipline and proactive stakeholder engagement throughout the lifecycle. These two focus areas ensure the project delivers on time while maintaining trust and alignment with those who will judge its success. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    (
        'Explanation: Need: keep plans flexible. Option C (Look for cost-saving opportunities.) fixes it."',
        'Explanation: Keywords: CPI below 1.0, final iteration, budget shortfall risk, cost optimization. A CPI of 0.9 in the final iteration signals that the project is spending more than planned per unit of work, creating a real risk of budget shortfall. The project manager should actively identify cost-saving opportunities in remaining work to recover the variance rather than accepting the overrun. (PMBOK Guide) – Seventh Edition, 2021, p. 32, \'Focus on Value\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option B (Schedule a meeting with the project sponsor to determine if it is appropriate to accept the director\'s request to provide a decision.) fixes it."',
        'Explanation: Keywords: go/no-go decision, director authority claim, project sponsor consultation, RACI clarification. When a business director demands decision-making authority during a kick-off, the project manager must first consult the project sponsor before accepting or rejecting the request. The sponsor has the governance standing to determine whether this change in accountability is appropriate and how it should be formalized. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Options A, B, and D (Create a quality assurance plan for the documentation.; Identify the components of the project documentation.; Ensure that the documents are in an easily retrievable form.) work together."',
        'Explanation: Keywords: project closure, documentation update, quality assurance, retrievability. At project closure, the project specialist must identify all documentation components, create a quality assurance plan for their completeness, and ensure they are stored in a retrievable format. Together these three actions fulfill the stewardship responsibility to preserve institutional knowledge and support future audits or lessons learned activities. (PMBOK Guide) – Seventh Edition, 2021, p. 25, \'Be a Diligent, Respectful, and Caring Steward\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option B (Conduct project reviews.) fixes it."',
        'Explanation: Keywords: compliance monitoring, user data protection, regulatory requirements, project reviews. Formal compliance with data protection regulations must be monitored through structured project reviews that systematically assess adherence to legal requirements. Unlike retrospectives or sprint reviews which focus on process improvement, project reviews provide the formal audit mechanism required for regulatory compliance tracking. (PMBOK Guide) – Seventh Edition, 2021, p. 25, \'Be a Diligent, Respectful, and Caring Steward\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option D (Request a change through the change control process to manage the new cybersecurityrequirements.) fixes it."',
        'Explanation: Keywords: cybersecurity regulatory change, change control process, no additional cost, scope governance. Even when a required change carries no additional cost, all scope changes including new government regulatory requirements must flow through the change control process. This ensures proper documentation, traceability, and governance approval before any modifications are made to the project baseline. (PMBOK Guide) – Seventh Edition, 2021, p. 50, \'Enable Change to Achieve the Envisioned Future State\'"'
    ),
    (
        'Explanation: Need: learn from data and lessons. Option D (Shift the way the company views, reviews, and assesses employees.) fixes it."',
        'Explanation: Keywords: agile transformation, organizational mindset, employee assessment, cultural change. True agile transformation requires changing how the organization evaluates and rewards people, not just adopting new tools or assigning people to agile projects. Shifting assessment criteria to reinforce agile behaviors creates the cultural foundation that sustains the methodology over time. (PMBOK Guide) – Seventh Edition, 2021, p. 50, \'Enable Change to Achieve the Envisioned Future State\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option D (Assess the information requirements of the community) fixes it."',
        'Explanation: Keywords: construction project, local community stakeholders, stakeholder engagement plan, information requirements. To effectively customize a stakeholder engagement plan for a local community, the project manager must first understand what information those stakeholders need. Assessing their information requirements enables the project manager to tailor communication content, frequency, and format to build and sustain the relationship. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option B (Continue work and ask the product owner to assess the changes and add/remove thestories as needed in the backlog.) fixes it."',
        'Explanation: Keywords: mid-iteration regulatory change, product owner responsibility, backlog management, agile adaptability. When regulatory changes arrive mid-iteration, the agile team should continue current sprint work while delegating backlog updates to the product owner, who is responsible for prioritizing and reflecting regulatory requirements. Interrupting an active sprint for assessment is disruptive and the product owner\'s role is specifically designed to manage this kind of change. (PMBOK Guide) – Seventh Edition, 2021, p. 48, \'Embrace Adaptability and Resiliency\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option A (Validate assumptions using appropriate tools to assess the risks.) fixes it."',
        'Explanation: Keywords: uncertain environment, feasibility doubts, assumption validation, risk assessment. When a project manager has doubts about feasibility in an uncertain environment, the appropriate first step is to validate the underlying assumptions using risk assessment tools rather than halting or escalating without evidence. Structured validation transforms vague concern into actionable data that can inform decisions about how to proceed. (PMBOK Guide) – Seventh Edition, 2021, p. 46, \'Optimize Risk Responses\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Options A, B, and C (Rolling wave planning and an adaptive approach; Relative estimation to determine the task or deliverable sizes; Iterations and reviews to continuously keep adapting the plan) work together."',
        'Explanation: Keywords: limited information, scheduling difficulty, adaptive planning, relative estimation. When a team lacks sufficient detail for traditional planning, rolling wave planning defers detailed scheduling to when information is available, relative estimation sizes work without requiring full decomposition, and iterative reviews continuously refine the plan as more is learned. Together these three techniques enable productive planning under uncertainty. (PMBOK Guide) – Seventh Edition, 2021, p. 48, \'Embrace Adaptability and Resiliency\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option C (Ensure every user story has acceptance criteria.) fixes it."',
        'Explanation: Keywords: product increment planning, acceptance criteria, user story quality, requirements verification. Acceptance criteria for each user story define the specific conditions that must be met for the increment to be considered complete and aligned with customer expectations. Without these criteria, there is no objective basis for verifying that delivered features meet the anticipated requirements. (PMBOK Guide) – Seventh Edition, 2021, p. 42, \'Build Quality into Processes and Deliverables\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option D (Work with both the team member and the key stakeholder to reach a consensus.) fixes it."',
        'Explanation: Keywords: scope misunderstanding, stakeholder-team conflict, consensus building, facilitation. When a key stakeholder and team member disagree about scope features, the project manager must facilitate a joint resolution rather than favoring either side. Working toward consensus ensures both perspectives are heard and produces an outcome that all parties can commit to. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option B (Study the new regulations with the team and evaluate if there is any impact on theproject variables.) fixes it."',
        'Explanation: Keywords: regulatory change, pharmaceutical project, impact evaluation, project variables. When new government regulations are announced mid-project, the project manager must first study them with the team to understand their full scope before taking any action. Evaluating the impact on all project variables — cost, schedule, scope, quality — ensures the response addresses the complete set of consequences. (PMBOK Guide) – Seventh Edition, 2021, p. 34, \'Recognize, Evaluate, and Respond to System Interactions\'"'
    ),
    (
        'Explanation: Need: keep plans flexible. Option A (Start scheduling the training for key workers now to ensure compliance.) fixes it."',
        'Explanation: Keywords: changing legislation, worker licenses, compliance risk, proactive training. When a project manager identifies a future legislative change that will make existing worker licenses noncompliant, proactive scheduling of training is the correct response. Acting now prevents a compliance gap at the moment the law takes effect, protecting the project from regulatory disruption during execution. (PMBOK Guide) – Seventh Edition, 2021, p. 46, \'Optimize Risk Responses\'"'
    ),
    (
        'Explanation: Need: keep plans flexible. Option C (Engage in a time and materials (T&M) contract and hire a local vendor to support development.) fixes it."',
        'Explanation: Keywords: agile project, resource shortage, vendor strategy, time and materials contract. In an agile environment with uncertain scope and evolving requirements, a time and materials contract with a local vendor provides the flexibility to scale effort up or down as the project needs change. Fixed-price contracts require stable, well-defined scope that is not available in the early iterations of an agile project. (PMBOK Guide) – Seventh Edition, 2021, p. 40, \'Tailor Based on Context\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option D (Make sure that the team has a full understanding of the scope.) fixes it."',
        'Explanation: Keywords: underperforming team, KPI shortfall, scope understanding, performance root cause. When a team is not meeting KPIs, the first corrective action is to verify they fully understand the scope of what they are expected to deliver. Scope ambiguity is a common root cause of performance problems and resolving it is faster and more effective than escalating or conducting a full skill assessment. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option A (Review the process and remove the impediment) fixes it."',
        'Explanation: Keywords: servant leader, certification bottleneck, impediment removal, second team delay. A servant leader\'s primary responsibility when a deliverable is blocked by an unresponsive external team is to review the process and actively remove the impediment rather than escalating or bypassing the requirement. This approach preserves quality requirements while protecting team velocity. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Options A and D (Add a user story during sprint planning that gives recognition to behaviors that are aligned with the new values; Give recognition to team members\' behaviors that are aligned with the new values during the sprint retrospectives) work together."',
        'Explanation: Keywords: organizational transformation, values promotion, behavioral recognition, agile ceremonies. Promoting new organizational values through agile ceremonies creates reinforcement at both the forward-planning level (sprint planning) and the reflective level (retrospectives). Together these actions embed value-aligned behaviors into the team\'s working rhythm through positive recognition rather than mandated compliance. (PMBOK Guide) – Seventh Edition, 2021, p. 50, \'Enable Change to Achieve the Envisioned Future State\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Options B, C, and D (Form a core group of team leads representing members from each country and encourage them to collaborate; Ask team members to agree on a meeting time prior to setting up virtual meetings \' Set up a discussion board that allows team members to collaborate online at any time of the day; Establish virtual one-on-one\'s with team members to address any issues and/or concerns privately) work together."',
        'Explanation: Keywords: global distributed team, low engagement, time zone barriers, virtual collaboration. Disengagement in a distributed global team requires structural solutions that address both timezone fairness and communication access. Forming regional core groups, allowing teams to agree on meeting times, and creating asynchronous discussion channels combined with private one-on-ones creates a multi-layered engagement strategy that respects diverse constraints. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    (
        'Explanation: Need: keep plans flexible. Option C (Accommodate the critical and urgent changes in the current iteration) fixes it."',
        'Explanation: Keywords: seventh iteration, continuous external changes, regulatory and market changes, critical urgent accommodation. In an agile project absorbing continuous external changes, the project manager should work with the product owner to accommodate only the most critical and urgent changes within the current iteration. This balances responsiveness to the environment with the need to protect the iteration\'s committed scope. (PMBOK Guide) – Seventh Edition, 2021, p. 48, \'Embrace Adaptability and Resiliency\'"'
    ),
    (
        'Explanation: Need: keep plans flexible. Option C (Include a risk response in the resource management plan) fixes it."',
        'Explanation: Keywords: printing resource contention, priority conflict, recurring deliverable, risk response. When a shared resource is routinely deprioritized for higher-revenue work, the project manager must document a risk response in the resource management plan to ensure a mitigation strategy exists for this recurring constraint. This formalizes the risk and assigns accountability for managing it rather than leaving it to chance. (PMBOK Guide) – Seventh Edition, 2021, p. 46, \'Optimize Risk Responses\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option D (Select members for their skill or potential) fixes it."',
        'Explanation: Keywords: high-performing team, project authorization, team formation, skill-based selection. Building an effective high-performing team begins with selecting members who have the right skills or the potential to develop them for the project\'s needs. This foundation of capability is the prerequisite for all subsequent team development activities. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    (
        'Explanation: Need: secure people or vendors. Option C (Include projected inflation rates) fixes it."',
        'Explanation: Keywords: long-term project, 4-year duration, CEO budget estimate, inflation adjustment. For a project spanning four years, the project manager must include projected inflation rates in the budget estimate to account for the real cost increase of resources, materials, and services over time. Ignoring inflation in multi-year projects systematically underestimates costs and creates future budget shortfalls. (PMBOK Guide) – Seventh Edition, 2021, p. 25, \'Be a Diligent, Respectful, and Caring Steward\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option C (Review this issue with the team lead for possible ways to resolve this situation) fixes it."',
        'Explanation: Keywords: verbal status reporting, distributed team, documentation gap, team lead alignment. When a cross-border team member claims verbal reporting to a team lead as sufficient, the project manager must address the reporting gap collaboratively with the team lead rather than issuing directives. This approach preserves relationships, clarifies expectations, and produces shared solutions for improving documentation practices. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option C (Consult the project reports from the previous project manager) fixes it."',
        'Explanation: Keywords: conflicting report data, product value discrepancy, incoming project manager, prior documentation. When a newly assigned project manager encounters conflicting data in project reports, consulting the previous project manager\'s reports provides the historical baseline needed to trace where the discrepancy originated. This evidence-based approach is faster and more accurate than collecting fresh data from departments. (PMBOK Guide) – Seventh Edition, 2021, p. 34, \'Recognize, Evaluate, and Respond to System Interactions\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Options B, C, and D (Arrange and conduct team-building sessions to improve team effectiveness; Obtain feedback from the isolated team member to understand the situation; Get feedback from other team members to understand what led to this situation) work together."',
        'Explanation: Keywords: team isolation, social exclusion, team-building, 360-degree feedback. When a team member is being isolated, the project manager must investigate by gathering perspectives from both the isolated individual and their peers while simultaneously creating positive shared experiences through team building. These actions address the interpersonal root cause while rebuilding a collaborative environment. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Options B and D (Perform team-building activities; Revisit the communications management plan) work together."',
        'Explanation: Keywords: distributed team, task distribution misunderstanding, communications management plan, team building. Low performance due to unclear task distribution in a global team requires both improving interpersonal trust through team building and clarifying communication protocols through the communications management plan. These two actions address the human and structural dimensions of the misunderstanding simultaneously. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
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
