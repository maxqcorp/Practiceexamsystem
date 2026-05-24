MD_FILE = './src/imports/project-management-questions-1.md'

with open(MD_FILE, 'r', encoding='utf-8') as f:
    content = f.read()

replacements = [
    # Q821
    (
        'Explanation: Need: guide and calm the team. Option C (Emotional intelligence) fixes it."',
        'Explanation: Keywords: emotional intelligence, leadership development, self-awareness, team management. Emotional intelligence is the foundational competency that allows a project manager to understand their own emotions and those of others, enabling effective responses to team dynamics and interpersonal challenges. Developing this skill directly improves the project manager\'s ability to build trust, resolve conflict, and motivate the team. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    # Q822
    (
        'Explanation: Need: guide and calm the team. Option D (Elaborate and socialize the team charter as per the resource management plan) fixes it."',
        'Explanation: Keywords: team charter, resource management plan, team alignment, socialization. A team charter that is elaborated and shared with all team members — as specified in the resource management plan — establishes shared norms, roles, and expectations that guide collaboration. Socializing the charter ensures every member understands and commits to the agreed ways of working before execution begins. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    # Q823
    (
        'Explanation: Need: guide and calm the team. Option A (Emphasize to the team that each member is responsible for their story but the team is collectively responsible for finishing the sprint) fixes it."',
        'Explanation: Keywords: individual accountability, collective sprint responsibility, agile team norms, ownership. In agile practice, each team member owns their individual user story while the entire team shares collective accountability for completing the sprint. This balance prevents both diffusion of responsibility and blame-shifting, and keeps the team oriented toward shared outcomes rather than individual performance alone. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    # Q824
    (
        'Explanation: Need: guide and calm the team. Option D (Perform tasks in parallel) fixes it."',
        'Explanation: Keywords: schedule compression, fast tracking, parallel tasks, delivery acceleration. When a project faces a critical deadline, performing independent tasks in parallel (fast tracking) is a schedule compression technique that reduces overall duration without changing scope. This approach accepts increased coordination risk in exchange for faster delivery of project value. (PMBOK Guide) – Seventh Edition, 2021, p. 32, \'Focus on Value\'"'
    ),
    # Q826
    (
        'Explanation: Need: guide and calm the team. Option C (Ask the team member if there is an impediment and help to remove the blockers) fixes it."',
        'Explanation: Keywords: servant leader, blocked team member, impediment removal, agile facilitation. When a team member is falling behind, a servant leader\'s first response is to ask whether an impediment is preventing progress and then work to remove it. This approach addresses the root cause rather than applying pressure, and maintains the trust and psychological safety the team needs to perform. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    # Q827
    (
        'Explanation: Need: guide and calm the team. Option D (Meet with the team member and work on a development plan for them to avoid missed deliverables in the future) fixes it."',
        'Explanation: Keywords: missed deliverables, development plan, coaching, performance improvement. Rather than escalating or reassigning after missed deliverables, the project manager should engage directly with the team member to understand the gap and create a forward-looking development plan. This coaching-first approach builds capability and addresses the root cause to prevent future recurrence. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    # Q828
    (
        'Explanation: Need: guide and calm the team. Option D (Requirements) fixes it."',
        'Explanation: Keywords: project scope foundation, requirements baseline, scope definition, planning input. Requirements are the foundational input that defines what the project must deliver and establishes the basis for all subsequent planning. Without clearly defined and agreed-upon requirements, scope, schedule, and cost baselines cannot be reliably established or controlled. (PMBOK Guide) – Seventh Edition, 2021, p. 42, \'Build Quality into Processes and Deliverables\'"'
    ),
    # Q829
    (
        'Explanation: Need: guide and calm the team. Option B (Explain and communicate the new approach to the project sponsor and key stakeholders) fixes it."',
        'Explanation: Keywords: new approach introduction, stakeholder communication, agile transition, change buy-in. When adopting a new project approach, the project manager must proactively explain and communicate the rationale and implications to the project sponsor and key stakeholders. Ensuring their understanding and buy-in is essential to securing the organizational support needed for the approach to succeed. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    # Q830
    (
        'Explanation: Need: guide and calm the team. Option C (Ask country A to submit a change request that will be analyzed along with countries B and C) fixes it."',
        'Explanation: Keywords: multi-country project, unilateral change request, change control process, integrated scope management. When one country requests a scope change that affects the entire project, the project manager must route it through the formal change control process and evaluate it alongside impacts for all affected parties. Bypassing this process risks creating scope imbalances and conflicting baselines across project regions. (PMBOK Guide) – Seventh Edition, 2021, p. 50, \'Enable Change to Achieve the Envisioned Future State\'"'
    ),
    # Q831
    (
        'Explanation: Need: guide and calm the team. Option C (Inform the customer of the issue and discuss the options so that they are able to make a decision on cost versus timeline) fixes it."',
        'Explanation: Keywords: quality issue, customer decision, cost versus timeline trade-off, transparent communication. When a quality issue creates a cost-versus-timeline decision, the project manager must present the options transparently to the customer so they can make an informed decision aligned with their priorities. This respects customer ownership of key trade-off decisions and avoids the project manager unilaterally absorbing choices that belong to the client. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    # Q832
    (
        'Explanation: Need: guide and calm the team. Option B (Review the missed program deliverables with the project team) fixes it."',
        'Explanation: Keywords: missed deliverables, team review, root cause analysis, program accountability. When program deliverables are missed, the project manager must bring the team together to review what happened before escalating or reporting externally. A collaborative review surfaces root causes, maintains team accountability, and produces a clearer picture of what corrective action is needed. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    # Q833
    (
        'Explanation: Need: guide and calm the team. Option D (Meet with the team member to understand the situation and provide feedback.) fixes it."',
        'Explanation: Keywords: underperforming team member, direct conversation, situational understanding, constructive feedback. The appropriate first response to a team member\'s performance issue is a private, direct conversation to understand the underlying situation before drawing conclusions or taking formal action. This empathetic approach demonstrates respect, gathers context, and allows the project manager to provide targeted and constructive feedback. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    # Q834
    (
        'Explanation: Need: guide and calm the team. Option A (Facilitate a team-building meeting to help this issue) fixes it."',
        'Explanation: Keywords: interpersonal conflict, team cohesion, team-building, collaborative environment. When team members experience interpersonal difficulties that impede collaboration, a facilitated team-building session creates a structured opportunity to surface issues and rebuild working relationships. This approach addresses the relational root cause rather than managing around the problem through task reassignment. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    # Q835
    (
        'Explanation: Need: guide and calm the team. Option C (Coordinate a video conference with the offending team member to resolve the issue) fixes it."',
        'Explanation: Keywords: virtual team conflict, direct resolution, video conference, distributed team member. When a virtual team member\'s behavior causes conflict, the project manager must engage the individual directly via video conference rather than relying on email or proxy communication. Face-to-face virtual interaction preserves tone and intent, making it more effective for resolving sensitive interpersonal issues across distances. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    # Q836
    (
        'Explanation: Need: guide and calm the team. Option A (Assess the business value impact and review the product roadmap to include any changes) fixes it."',
        'Explanation: Keywords: new stakeholder requirements, business value assessment, product roadmap revision, agile prioritization. When new stakeholder requirements emerge, the project manager must assess their business value impact and reflect the changes in the product roadmap before committing to implementation. This value-driven evaluation ensures that accommodated changes genuinely strengthen the project\'s outcomes and are properly sequenced in the delivery plan. (PMBOK Guide) – Seventh Edition, 2021, p. 32, \'Focus on Value\'"'
    ),
    # Q837
    (
        'Explanation: Need: guide and calm the team. Option D (Implement a communications management plan) fixes it."',
        'Explanation: Keywords: communication breakdowns, global project, communications management plan, information flow. Recurring communication failures in a global project signal the absence of a structured communication framework. Implementing a communications management plan formalizes who receives what information, through which channels, and at what frequency — eliminating the ambiguity that causes breakdowns. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    # Q839
    (
        'Explanation: Need: guide and calm the team. Option C (Ensure that compliance is explicitly mentioned in the relevant requirements) fixes it."',
        'Explanation: Keywords: compliance integration, requirements documentation, explicit compliance language, regulatory traceability. Compliance requirements must be explicitly embedded in the relevant project requirements to ensure they are visible, traceable, and verifiable throughout delivery. Leaving compliance implicit creates a gap that may only surface during audits or post-delivery reviews when corrective action is more costly. (PMBOK Guide) – Seventh Edition, 2021, p. 42, \'Build Quality into Processes and Deliverables\'"'
    ),
    # Q840
    (
        'Explanation: Need: guide and calm the team. Option A (Laissez-faire) fixes it."',
        'Explanation: Keywords: laissez-faire leadership, autonomous expert team, minimal intervention, high competence. Laissez-faire leadership delegates decision-making authority to team members who are highly skilled and self-motivated, trusting them to work without close oversight. This style is appropriate when the team has the expertise and drive to self-manage, and excessive direction would only reduce their autonomy and engagement. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    # Q841
    (
        'Explanation: Need: guide and calm the team. Option B (Focus on delivering incremental value through multiple smaller deliveries) fixes it."',
        'Explanation: Keywords: agile delivery, incremental value, smaller deliveries, continuous feedback. An agile project approach centers on delivering working increments of value frequently rather than waiting for a single large release. Multiple smaller deliveries allow stakeholders to validate outcomes, provide feedback, and adjust priorities — reducing the risk of delivering a complete solution that misses actual needs. (PMBOK Guide) – Seventh Edition, 2021, p. 32, \'Focus on Value\'"'
    ),
    # Q842
    (
        'Explanation: Need: guide and calm the team. Option D (Reassess the issue as part of monitoring and controlling) fixes it."',
        'Explanation: Keywords: recurring issue, monitoring and controlling, issue reassessment, performance oversight. When an issue resurfaces or evolves, the appropriate response is to formally reassess it within the monitoring and controlling process rather than treating it as a one-time exception. This keeps the issue visible in the project governance framework and ensures the response is proportional to the current impact. (PMBOK Guide) – Seventh Edition, 2021, p. 34, \'Recognize, Evaluate, and Respond to System Interactions\'"'
    ),
    # Q843
    (
        'Explanation: Need: listen to people needs. Option D (Provide project management training to the stakeholders and explain their responsibilities) fixes it."',
        'Explanation: Keywords: no PMO, unclear responsibilities, government project, stakeholder training. In an organization without a PMO or established project management processes, managers cannot fulfill their project responsibilities if they do not understand what those responsibilities are. The project manager must provide targeted training to close this knowledge gap and enable effective stakeholder participation in governance. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    # Q844
    (
        'Explanation: Need: guide and calm the team. Option D (Assist with the removal of impediments and blockers so that the project can continue) fixes it."',
        'Explanation: Keywords: vendor contract delay, daily standup, servant leadership, impediment removal. A project manager acting as a servant leader responds to blockers raised in daily standups by actively working to remove them rather than delegating the problem back to the team. Assisting with vendor contract delays is precisely the kind of organizational impediment that lies outside the team\'s authority to resolve independently. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    # Q845
    (
        'Explanation: Need: guide and calm the team. Option C (Provide feedback and coach the team member during the iterative design stage) fixes it."',
        'Explanation: Keywords: poor performance, iterative design stage, coaching, performance improvement. When a team member is underperforming during an iterative design phase, the project manager should provide real-time feedback and coaching rather than escalating or replacing the individual. This builds the team member\'s capability during the stage when it can be most effectively corrected before execution begins. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    # Q846
    (
        'Explanation: Need: guide and calm the team. Option A (Work with the team to understand and solve the issues) fixes it."',
        'Explanation: Keywords: low velocity, testing queue bottleneck, hybrid project, collaborative problem solving. When a hybrid project shows lower velocity and a testing backlog, the project manager must engage the team collaboratively to diagnose and resolve the root cause before the final sprints. Working with the team respects their expertise and produces solutions that are both technically sound and owned by those responsible for implementation. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    # Q847
    (
        'Explanation: Need: listen to people needs. Option C (Find and provide training to the project team members who do not have the required skills) fixes it."',
        'Explanation: Keywords: unclear requirements, missing technical skills, hybrid project, skill gap training. When team members lack critical skills and the customer will not accept scope changes, the project manager must address the internal capability gap through training. Investing in skill development enables the team to meet the unchanged requirements without violating the customer\'s constraints. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    # Q848
    (
        'Explanation: Need: keep plans flexible. Option C (The requirements gathering was inadequate) fixes it."',
        'Explanation: Keywords: borehole project, water access failure, CPI/SPI metrics, requirements inadequacy. A project that finishes on budget and near schedule but fails to deliver usable outcomes reveals a fundamental requirements gathering failure. Technical performance metrics like CPI and SPI measure execution efficiency, not whether the solution addresses the actual need — inadequate requirements allow a project to succeed on paper while failing in practice. (PMBOK Guide) – Seventh Edition, 2021, p. 42, \'Build Quality into Processes and Deliverables\'"'
    ),
    # Q849
    (
        'Explanation: Need: protect benefits for users. Option A (Work with the product owner to evaluate and prioritize the requirements) fixes it."',
        'Explanation: Keywords: agile project, requirements prioritization, product owner collaboration, incremental delivery. In an agile project delivering value through multiple versions, the product owner is the authoritative voice for prioritizing requirements based on business value. The project manager must work with the product owner to evaluate and sequence requirements — not prioritize independently — ensuring that each increment delivers the highest value to users. (PMBOK Guide) – Seventh Edition, 2021, p. 32, \'Focus on Value\'"'
    ),
    # Q850
    (
        'Explanation: Need: learn from data and lessons. Option B (Meet with the unsuccessful bidder to review their submission and the areas that led to the bid being unsuccessful) fixes it."',
        'Explanation: Keywords: unsuccessful bidder, community influence, bid debrief, procurement integrity. When an unsuccessful bidder with community influence continues to engage with hopes of influencing the award decision, the project manager should offer a professional debrief of the bid review results rather than avoiding or dismissing them. This transparent response honors procurement integrity, manages the relationship constructively, and reduces the risk of the bidder leveraging their community influence to disrupt the project. (PMBOK Guide) – Seventh Edition, 2021, p. 25, \'Be a Diligent, Respectful, and Caring Steward\'"'
    ),
    # Q851
    (
        'Explanation: Need: listen to people needs. Option D (Review the change request with the project stakeholders and evaluate the impact of the scope reduction) fixes it."',
        'Explanation: Keywords: scope reduction request, market changes, change control, stakeholder impact assessment. Even when a change involves removing scope, it must still be processed through the formal change control process with full stakeholder review. Evaluating the impact of a scope reduction ensures the project baseline is updated correctly and all parties understand the implications for schedule, cost, and deliverables. (PMBOK Guide) – Seventh Edition, 2021, p. 50, \'Enable Change to Achieve the Envisioned Future State\'"'
    ),
    # Q852
    (
        'Explanation: Need: guide and calm the team. Option D (Make sure that the product and sprint backlogs have the required level of documentation and both are visible to the team) fixes it."',
        'Explanation: Keywords: product owner change requests, iterative transition, backlog visibility, documentation clarity. When a team is confused about ongoing changes to features already developed, the root cause is often insufficient backlog documentation and visibility. Ensuring both the product and sprint backlogs are well-documented and accessible gives the team a single source of truth for understanding what has been requested, approved, and prioritized. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    # Q853
    (
        'Explanation: Need: listen to people needs. Option D (Exploited) fixes it."',
        'Explanation: Keywords: early delivery opportunity, top resource assignment, positive risk, exploit strategy. Assigning the most talented resource to accelerate delivery represents an exploit strategy for a positive risk (opportunity). Exploiting an opportunity means taking deliberate action to ensure it materializes — here, by removing the skill constraint that would otherwise prevent the early completion. (PMBOK Guide) – Seventh Edition, 2021, p. 46, \'Optimize Risk Responses\'"'
    ),
    # Q854
    (
        'Explanation: Need: listen to people needs. Option A (Send a formal communication regarding the missed milestone) fixes it."',
        'Explanation: Keywords: missed milestone, governance requirement, formal communication, project stewardship. Project governance that mandates formal communication upon milestone failures must be followed regardless of how the project manager feels it will reflect on the team. Stewardship requires the project manager to uphold agreed governance standards with transparency and integrity, even when the news is unfavorable. (PMBOK Guide) – Seventh Edition, 2021, p. 25, \'Be a Diligent, Respectful, and Caring Steward\'"'
    ),
    # Q856
    (
        'Explanation: Need: guide and calm the team. Option B (Validate the reason and add it as an issue in the issue log) fixes it."',
        'Explanation: Keywords: overtime pay discrepancy, issue log, validation, compensation fairness. When a specific team subgroup reports not receiving overtime pay while others do, the project manager must first validate the claim and formally log it as an issue to ensure it receives proper tracking and resolution. The issue log is the correct mechanism to escalate and monitor payroll concerns through the appropriate organizational channels. (PMBOK Guide) – Seventh Edition, 2021, p. 25, \'Be a Diligent, Respectful, and Caring Steward\'"'
    ),
    # Q858
    (
        'Explanation: Need: listen to people needs. Option C (Prioritize the user stories with issues and have the team resolve them) fixes it."',
        'Explanation: Keywords: risks materialized, velocity impact, user stories with issues, agile response. When multiple risks have become active issues reducing team velocity, the project manager must refocus the team on resolving the most impactful items by reprioritizing the affected user stories. This agile response addresses the immediate problem directly rather than escalating through slow bureaucratic channels. (PMBOK Guide) – Seventh Edition, 2021, p. 46, \'Optimize Risk Responses\'"'
    ),
    # Q860
    (
        'Explanation: Need: secure people or vendors. Option C (Meet with the product owner to confirm the minimum viable product (MVP) option) fixes it."',
        'Explanation: Keywords: emergency budget reallocation, hybrid project, minimum viable product, value prioritization. When more than half the project budget is unexpectedly removed, the project manager must immediately determine with the product owner what constitutes the minimum viable product deliverable within the new constraints. This value-focused decision preserves the project\'s core benefit while adapting pragmatically to the changed resource reality. (PMBOK Guide) – Seventh Edition, 2021, p. 32, \'Focus on Value\'"'
    ),
    # Q907 multi-select A,B,E
    (
        'Explanation: Need: guide and calm the team. Options A, B, and E (Confront the people causing the stress directly with the aim of finding amicable solutions; Seek support from the project management office (PMO) on addressing issues affecting the project; Talk to the human resources (HR) manager about these concerns) work together."',
        'Explanation: Keywords: hostile manager behavior, project stress, PMO support, HR escalation. Addressing repeated disrespectful behavior from functional managers requires a multi-pronged response: direct confrontation to seek resolution, PMO engagement to address project impacts, and HR involvement to handle the personal conduct issues. Together these three actions address the problem at the interpersonal, project governance, and organizational policy levels simultaneously. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    # Q908
    (
        'Explanation: Need: guide and calm the team. Option D (Assign an experienced resource to support the team member) fixes it."',
        'Explanation: Keywords: new system unfamiliarity, task delivery delay, experienced mentor, knowledge transfer. When a team member struggles with an unfamiliar system that is causing project delays, the most effective response is to pair them with an experienced colleague who can provide hands-on support. This approach accelerates the learning curve, addresses the immediate delivery risk, and builds the team member\'s capability for future tasks. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    # Q909 multi-select A,E
    (
        'Explanation: Need: keep plans flexible. Options A and E (Review with subject matter experts (SMEs) to ensure they have contributed to the schedule development; Evaluate the schedules for interdependencies to establish the critical path) work together."',
        'Explanation: Keywords: multiple project schedules, SME validation, interdependencies, critical path analysis. When consolidating schedules across multiple workstreams, the project manager must verify that subject matter experts contributed to each schedule\'s development and then map the interdependencies between streams to establish the overall critical path. These two actions ensure both the quality of individual estimates and the accuracy of the integrated project timeline. (PMBOK Guide) – Seventh Edition, 2021, p. 44, \'Navigate Complexity\'"'
    ),
    # Q910
    (
        'Explanation: Need: guide and calm the team. Option D (Review the work breakdown structure (WBS) to align the project teams) fixes it."',
        'Explanation: Keywords: overlapping responsibilities, WBS, scope clarity, team alignment. When two teams have unclear accountability for overlapping deliverables, the work breakdown structure is the authoritative document for resolving responsibility gaps. Reviewing the WBS with both teams establishes which deliverables belong to which team and eliminates the ambiguity causing the conflict. (PMBOK Guide) – Seventh Edition, 2021, p. 34, \'Recognize, Evaluate, and Respond to System Interactions\'"'
    ),
    # Q911
    (
        'Explanation: Need: listen to people needs. Option D (Agree with the project team on a suitable collaboration and make sure information is shared at all times) fixes it."',
        'Explanation: Keywords: communication channels, information delays, team collaboration, delivery consequences. When existing communication channels cause information to reach team members too slowly, the project manager should work collaboratively with the team to agree on more effective channels rather than unilaterally imposing alternatives. This ensures the chosen solution is practical for those using it and gains team commitment. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    # Q912
    (
        'Explanation: Need: keep plans flexible. Option D (Schedule a meeting with the provider to collaborate on the options) fixes it."',
        'Explanation: Keywords: provider-reported blocker, dependent deliverables, collaborative problem solving, vendor relationship. When a provider reports an issue blocking remaining deliverables, the project manager should convene a collaborative meeting to explore solutions together rather than waiting for the provider to resolve it independently. Joint problem-solving produces faster, more integrated solutions while maintaining a productive vendor relationship. (PMBOK Guide) – Seventh Edition, 2021, p. 34, \'Recognize, Evaluate, and Respond to System Interactions\'"'
    ),
    # Q913
    (
        'Explanation: Need: listen to people needs. Option B (Review this topic with the product owner before the next iteration planning) fixes it."',
        'Explanation: Keywords: stakeholder feedback, technical vs business features, product owner alignment, backlog prioritization. When stakeholders report that an iteration review showed too many technical features and too few business ones, the product owner must adjust the backlog prioritization before the next iteration is planned. Reviewing this feedback with the product owner first ensures that the corrective action is grounded in business value priorities rather than technical preference. (PMBOK Guide) – Seventh Edition, 2021, p. 32, \'Focus on Value\'"'
    ),
    # Q914
    (
        'Explanation: Need: listen to people needs. Option C (Start with the product prototype development, review with the customer, and gather feedback) fixes it."',
        'Explanation: Keywords: unclear requirements, agile team, prototype development, customer validation. When requirements are unclear and have already caused delays, the fastest path to clarity is developing a working prototype and reviewing it with the customer to gather concrete feedback. A prototype makes abstract requirements tangible, enabling the customer to validate or redirect the team\'s understanding with specificity. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    # Q917
    (
        'Explanation: Need: guide and calm the team. Option C (Establish a clear definition of done (DoD) for each task) fixes it."',
        'Explanation: Keywords: conflicting status updates, definition of done, task completion clarity, scrum master. When team members report conflicting statuses for the same task, the root cause is typically the absence of a shared definition of done. Establishing a clear DoD for each task creates an objective and agreed-upon completion standard that eliminates ambiguous or subjective status reporting. (PMBOK Guide) – Seventh Edition, 2021, p. 42, \'Build Quality into Processes and Deliverables\'"'
    ),
    # Q918 multi-select A,D
    (
        'Explanation: Need: listen to people needs. Options A and D (Consult the risk and issue logs.; Discuss with the project sponsor.) work together."',
        'Explanation: Keywords: new legislation, budget impact, risk log review, sponsor consultation. When a new law threatens the project budget, the project manager must first check whether this risk or a similar one was previously identified and documented in the risk and issue logs, then engage the sponsor to determine the organizational response. Together these actions leverage existing risk intelligence and bring the appropriate decision-making authority into the response immediately. (PMBOK Guide) – Seventh Edition, 2021, p. 46, \'Optimize Risk Responses\'"'
    ),
    # Q919
    (
        'Explanation: Need: guide and calm the team. Option C (Reward the developer according to their motivations and interests) fixes it."',
        'Explanation: Keywords: top performer recognition, individual motivation, tailored rewards, team morale. Effective recognition must be tailored to the individual\'s motivations and interests to be meaningful and sustainable. A reward that doesn\'t resonate with the recipient fails to reinforce the desired behavior and may even feel dismissive, whereas a personalized reward strengthens the relationship and encourages continued high performance. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    # Q920
    (
        'Explanation: Need: listen to people needs. Option A (Revise the project schedule and inform the stakeholders regarding any delays) fixes it."',
        'Explanation: Keywords: risk-caused delays, schedule revision, stakeholder communication, transparency. When identified risks materialize and cause schedule delays, the project manager must update the schedule to reflect the current forecast and proactively communicate the delays to stakeholders. Transparent reporting maintains stakeholder trust and enables informed decisions about how to respond to the changed timeline. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    # Q921
    (
        'Explanation: Need: listen to people needs. Option C (Build channels to extend communication efforts to the local community) fixes it."',
        'Explanation: Keywords: local community stakeholder, factory construction, speculation and rumors, proactive communication. When a local community is speculating about a project\'s impacts and spreading rumors, the project manager must establish direct communication channels to provide accurate and timely information. Proactive outreach replaces misinformation with facts and builds the trust needed to prevent the community from becoming an obstacle. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    # Q922
    (
        'Explanation: Need: guide and calm the team. Option D (Discuss with the consultant to understand why the risk was escalated) fixes it."',
        'Explanation: Keywords: bypassed risk process, direct management escalation, consultant behavior, process adherence. When a consultant bypasses the established risk process and escalates directly to management, the project manager must first understand the consultant\'s reasoning before evaluating the risk itself. Understanding why the process was bypassed may reveal legitimate concerns about the process or the team dynamics that need to be addressed. (PMBOK Guide) – Seventh Edition, 2021, p. 34, \'Recognize, Evaluate, and Respond to System Interactions\'"'
    ),
    # Q923 (same answer as Q908 but different question context - confirmed)
    (
        'Explanation: Need: guide and calm the team. Option A (Assign an experienced resource to support the team member) fixes it."',
        'Explanation: Keywords: system unfamiliarity, delivery delay risk, experienced peer support, capability building. When a team member\'s inability to use a newly implemented system threatens project delivery, assigning an experienced colleague to provide direct support is the most efficient response. This accelerates the struggling member\'s productivity while delivering the needed knowledge transfer without disrupting the overall project schedule. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    # Q924
    (
        'Explanation: Need: guide and calm the team. Option C (Review the compliance strategy and version history) fixes it."',
        'Explanation: Keywords: incoming project manager, compliance strategy, continuity review, version history. A new project manager assigned mid-execution must first review the existing compliance strategy and its version history to understand what was planned, what has changed, and what commitments the project has already made. This baseline review prevents duplicating work, overriding prior decisions, or missing compliance gaps created during the transition. (PMBOK Guide) – Seventh Edition, 2021, p. 25, \'Be a Diligent, Respectful, and Caring Steward\'"'
    ),
    # Q925
    (
        'Explanation: Need: listen to people needs. Option D (Organize a root cause analysis (RCA) workshop.) fixes it."',
        'Explanation: Keywords: phase delay, stakeholder concern, root cause analysis, schedule recovery. When a phase takes significantly longer than planned, the project manager must identify the root cause before taking any corrective action. An RCA workshop surfaces the true driver of the delay, enabling a targeted and effective response that addresses the actual problem rather than its symptoms. (PMBOK Guide) – Seventh Edition, 2021, p. 46, \'Optimize Risk Responses\'"'
    ),
    # Q926
    (
        'Explanation: Need: listen to people needs. Option A (Confirmed that the communication was understood and solicited feedback from the team) fixes it."',
        'Explanation: Keywords: communications management, feedback solicitation, two-way communication, misunderstanding prevention. Sending a project management plan without confirming comprehension is a one-way communication failure. The project manager should have solicited feedback and confirmed the team\'s understanding immediately after sending, as two-way communication is essential to ensure that complex documents are correctly interpreted. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    # Q927
    (
        'Explanation: Need: watch risks early. Option D (Liaise with the school to include nonworking project hours during school start and finish times) fixes it."',
        'Explanation: Keywords: community impact, school proximity, nonworking hours, proactive engagement. When a project is near a school and has already engaged with school management to understand their needs, the project manager must honor that engagement by scheduling project activities to avoid school start and finish times. This proactive adjustment demonstrates the caring stewardship expected of a project manager working near vulnerable community members. (PMBOK Guide) – Seventh Edition, 2021, p. 25, \'Be a Diligent, Respectful, and Caring Steward\'"'
    ),
    # Q928
    (
        'Explanation: Need: guide and calm the team. Option D (Use round-robin check-ins to facilitate the meeting so all participants have the opportunity to speak) fixes it."',
        'Explanation: Keywords: virtual meeting, low participation, round-robin facilitation, inclusive communication. When virtual meetings suffer from low participation and resulting misunderstandings, round-robin check-ins ensure every team member has a structured opportunity to contribute. This facilitation technique prevents dominant voices from monopolizing the discussion and creates the equal participation needed for accurate information sharing. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    # Q929 multi-select A,C
    (
        'Explanation: Need: listen to people needs. Options A and C (Collaborated with the functional manager to determine which critical activities could be accommodated by the budget; Conducted a meeting with the functional manager to explain why the activities needed to be stopped) work together."',
        'Explanation: Keywords: budget-constrained activity stoppage, functional manager disagreement, collaboration, explanation. When stopping activities creates conflict with a functional manager, the project manager should both explain the rationale for the decision and collaborate to identify which critical activities can still be accommodated within the budget. These two actions combine transparency with partnership to transform a confrontation into a jointly owned solution. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    # Q930
    (
        'Explanation: Need: guide and calm the team. Option A (Evaluate the impact of skipping the quality check for the deliverable.) fixes it."',
        'Explanation: Keywords: tight schedule, quality check skip request, impact evaluation, quality management. Before agreeing to skip any quality check, the project manager must evaluate what risks and consequences would result from that omission. Only after assessing the impact can an informed decision be made about whether the schedule pressure justifies the quality trade-off — this preserves decision quality even under time constraints. (PMBOK Guide) – Seventh Edition, 2021, p. 42, \'Build Quality into Processes and Deliverables\'"'
    ),
    # Q931
    (
        'Explanation: Need: secure people or vendors. Option B (Contact a subject matter expert (SME) for advice and consultation.) fixes it."',
        'Explanation: Keywords: urgent cost estimate, 4-hour timeline, expert judgment, construction project. When asked to produce a cost estimate within a very tight timeframe without sufficient information for bottom-up estimating, the project manager should immediately engage a subject matter expert whose domain knowledge enables rapid and credible estimates. Expert judgment is the most efficient path to a defensible estimate when time constraints prevent detailed analysis. (PMBOK Guide) – Seventh Edition, 2021, p. 40, \'Tailor Based on Context\'"'
    ),
    # Q932
    (
        'Explanation: Need: guide and calm the team. Option B (Empathize with the team member and discuss next steps.) fixes it."',
        'Explanation: Keywords: team member distress, late night call, empathy, emotional support. When a team member reaches out in emotional distress, the project manager\'s first responsibility is to respond with empathy and engage in a supportive conversation about next steps. Deferring to a scheduled meeting or written communication when someone is in acute distress fails the human duty of care that effective leadership requires. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    # Q933
    (
        'Explanation: Need: listen to people needs. Option C (Explain the third-party supplier situation to the client and request payment.) fixes it."',
        'Explanation: Keywords: third-party supplier cash flow, client payment dependency, team withdrawal risk, transparent communication. When a project payment chain threatens a supplier\'s ability to retain workers, the project manager must transparently explain the situation to the client and request accelerated payment. This honest disclosure protects the project from losing critical resources while respecting the contractual payment chain that governs the relationship. (PMBOK Guide) – Seventh Edition, 2021, p. 25, \'Be a Diligent, Respectful, and Caring Steward\'"'
    ),
    # Q934
    (
        'Explanation: Need: keep plans flexible. Option D (Review the lessons learned on similar projects so that they do not fall back into the same pattern.) fixes it."',
        'Explanation: Keywords: similar failed project, lessons learned, organizational knowledge, proactive risk mitigation. When a similar project in the organization was previously closed due to low performance, reviewing those lessons learned provides the most relevant and actionable intelligence for avoiding the same failure patterns. Organizational history is the most direct input for shaping a risk-aware project approach. (PMBOK Guide) – Seventh Edition, 2021, p. 48, \'Embrace Adaptability and Resiliency\'"'
    ),
    # Q935
    (
        'Explanation: Need: listen to people needs. Option D (Involved operations stakeholders during planning) fixes it."',
        'Explanation: Keywords: operations handover failure, day-to-day requirements gaps, operations team exclusion, stakeholder planning involvement. Operations stakeholders who will own and use the system after delivery must be involved during project planning to ensure their day-to-day requirements are captured and addressed. Excluding them from planning creates the exact gap between designed functionality and operational reality that caused the post-handover customer issues. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    # Q936
    (
        'Explanation: Need: listen to people needs. Option B (Suggest using an agile approach since customer and team collaboration is critical for project success.) fixes it."',
        'Explanation: Keywords: business collaboration, critical success factor, methodology selection, agile suitability. When business collaboration is a critical factor for project success, an agile approach is most appropriate because it is specifically designed to maximize ongoing customer and team collaboration throughout delivery. This methodology choice aligns the project\'s working model with its most important success driver. (PMBOK Guide) – Seventh Edition, 2021, p. 40, \'Tailor Based on Context\'"'
    ),
    # Q937
    (
        'Explanation: Need: listen to people needs. Option C (Use a variety of communication methods that respect cultural, practical, and personal preferences.) fixes it."',
        'Explanation: Keywords: stakeholder communication, cultural diversity, method variety, banking IT modernization. A global project with diverse stakeholders requires a communication approach that accommodates cultural norms, practical constraints, and personal preferences rather than imposing a single medium. Using a variety of communication methods maximizes comprehension and engagement across the different contexts and preferences stakeholders bring. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    # Q938
    (
        'Explanation: Need: listen to people needs. Option A (Established ground rules before the discussion had started.) fixes it."',
        'Explanation: Keywords: stakeholder disagreement, personal arguments, ground rules, meeting facilitation. Personal conflicts and non-productive disagreements in planning sessions are preventable when ground rules for respectful discourse are established before discussions begin. Pre-agreed behavioral norms create a shared framework that the facilitator can reference to redirect unproductive behavior without singling out individuals. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    # Q939
    (
        'Explanation: Need: guide and calm the team. Option B (Allow the teams to continue using their approaches and gradually adapt to a hybrid model.) fixes it."',
        'Explanation: Keywords: dual methodology teams, hybrid transition, gradual adaptation, predictive and agile coexistence. When two teams already using different approaches need to converge, forcing an immediate methodology switch disrupts established workflows and risks delivery. Allowing the teams to continue their current approaches while facilitating a gradual transition to a hybrid model reduces disruption while building toward a unified methodology. (PMBOK Guide) – Seventh Edition, 2021, p. 40, \'Tailor Based on Context\'"'
    ),
    # Q940
    (
        'Explanation: Need: protect value and acceptance. Option B (Calculate the costs for each option in each location and compare the net present value (NPV) for each.) fixes it."',
        'Explanation: Keywords: branch expansion decision, multiple options, NPV comparison, financial decision analysis. When evaluating mutually exclusive investment options across multiple locations, net present value analysis is the appropriate financial tool to compare the long-term economic benefit of each option. NPV accounts for the time value of money and enables a consistent comparison of building versus renting versus no expansion across all three cities. (PMBOK Guide) – Seventh Edition, 2021, p. 32, \'Focus on Value\'"'
    ),
    # Q941
    (
        'Explanation: Need: keep plans flexible. Option C (Identified all required skills during the planning of the project) fixes it."',
        'Explanation: Keywords: missing technical skill, mid-project, planning failure, skill identification. Discovering a required skill gap during execution indicates that the planning phase failed to identify all competencies needed for delivery. Identifying required skills during planning — not after kick-off — allows the project manager to acquire, train, or contract for those capabilities before they become critical path blockers. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    # Q942
    (
        'Explanation: Need: protect value and acceptance. Option C (Allocate the budget to the deliveries that have higher business value for the organization than those with lower business value.) fixes it."',
        'Explanation: Keywords: fixed budget, organizational transformation, business value prioritization, resource allocation. When budget is capped with no possibility of increase, the project manager must allocate it to the deliverables that yield the greatest business value. This value-driven prioritization ensures the organization gains maximum benefit from the available resources even if lower-value deliverables are deferred or descoped. (PMBOK Guide) – Seventh Edition, 2021, p. 32, \'Focus on Value\'"'
    ),
    # Q943
    (
        'Explanation: Need: guide and calm the team. Option B (Review the process that resulted in this situation.) fixes it."',
        'Explanation: Keywords: undocumented design handoff, misunderstanding, process review, agile team. When a recurring behavior (verbal handoffs without documentation) causes misunderstandings, the agile leader must review the process that allows or encourages this pattern rather than targeting the individual. Fixing the process produces a systemic improvement that prevents recurrence across the team. (PMBOK Guide) – Seventh Edition, 2021, p. 34, \'Recognize, Evaluate, and Respond to System Interactions\'"'
    ),
    # Q944
    (
        'Explanation: Need: watch risks early. Option D (Report the delay with rectifying actions to the change control board (CCB) for review,) fixes it."',
        'Explanation: Keywords: quality rework, critical path delay, CCB review, corrective action. When quality problems cause schedule delays that impact the critical path, the project manager must formally report the situation with proposed rectifying actions to the change control board. The CCB is the governance body authorized to approve corrective actions that affect the project baseline. (PMBOK Guide) – Seventh Edition, 2021, p. 50, \'Enable Change to Achieve the Envisioned Future State\'"'
    ),
    # Q945
    (
        'Explanation: Need: listen to people needs. Option A (Provide clear expectations around task requirements.) fixes it."',
        'Explanation: Keywords: incomplete tasks reported as complete, unclear expectations, task clarity, quality standard. When a team member marks tasks complete that are actually incomplete, the root cause is typically unclear expectations about what constitutes task completion. Providing explicit requirements and completion criteria eliminates the ambiguity that allows different interpretations of done. (PMBOK Guide) – Seventh Edition, 2021, p. 42, \'Build Quality into Processes and Deliverables\'"'
    ),
    # Q946
    (
        'Explanation: Need: listen to people needs. Option B (Gather all stakeholders and provide recommendations on a smaller, more feasible project scope,) fixes it."',
        'Explanation: Keywords: resource constraint, partial requirements, fixed budget, scope reduction recommendation. When not all requirements can be delivered within available resources but some requirements can still add business value, the project manager must bring stakeholders together to make an informed decision about scope reduction. Presenting a recommendation for a smaller feasible scope respects both the budget constraint and the stakeholders\' authority to approve scope changes. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    # Q947
    (
        'Explanation: Need: guide and calm the team. Option C (Agree with functional management and team members on a vacation schedule that would minimally impact the project schedule.) fixes it."',
        'Explanation: Keywords: company vacation policy, schedule impact, collaborative scheduling, functional management. When a company policy creates an unavoidable schedule impact, the project manager should work collaboratively with functional management and team members to optimize the vacation schedule in a way that minimizes disruption. This cooperative approach respects the policy while protecting the project timeline as much as possible. (PMBOK Guide) – Seventh Edition, 2021, p. 34, \'Recognize, Evaluate, and Respond to System Interactions\'"'
    ),
    # Q948
    (
        'Explanation: Need: listen to people needs. Option D (Issue log) fixes it."',
        'Explanation: Keywords: supplier labor problem, material delivery failure, issue log, stakeholder communication. When a supplier is unable to deliver due to a labor dispute — an active problem requiring management rather than future mitigation — the project manager must document it in the issue log, not the risk register. The issue log is the appropriate tool for tracking current problems that need resolution and communicating their status to stakeholders. (PMBOK Guide) – Seventh Edition, 2021, p. 34, \'Recognize, Evaluate, and Respond to System Interactions\'"'
    ),
    # Q949
    (
        'Explanation: Need: listen to people needs. Option D (Follow the company\'s standard vendor selection criteria process,) fixes it."',
        'Explanation: Keywords: sponsor-preferred vendor, vendor selection process, procurement integrity, urgency pressure. Even when a sponsor advocates for a specific vendor under urgency, the project manager must follow the organization\'s standard vendor selection process to maintain procurement integrity. Bypassing the established criteria process creates risks around vendor quality, fairness, and organizational compliance that outweigh the convenience of acting on a sponsor recommendation. (PMBOK Guide) – Seventh Edition, 2021, p. 25, \'Be a Diligent, Respectful, and Caring Steward\'"'
    ),
    # Q950
    (
        'Explanation: Need: listen to people needs. Option A (Meet with the team to review the backlog and create small iterations that can deliver incremental value to the client,) fixes it."',
        'Explanation: Keywords: agile project, predictive approach misalignment, incremental delivery, backlog review. An agile innovation project should deliver value incrementally throughout the lifecycle, not as a single release at the end. The new project manager must immediately realign the delivery approach by reviewing the backlog and establishing small iterations that create visible value for the client before the project is complete. (PMBOK Guide) – Seventh Edition, 2021, p. 32, \'Focus on Value\'"'
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
