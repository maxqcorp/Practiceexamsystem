MD_FILE = './src/imports/project-management-questions-1.md'

with open(MD_FILE, 'r', encoding='utf-8') as f:
    content = f.read()

replacements = [
    (
        'Explanation: Need: listen to people needs. Option D (Use the project management information system (PMIS) to share information.) fixes it."',
        'Explanation: Keywords: new stakeholders, deliverable access, PMIS, information sharing. When new stakeholders lack access to previously shared deliverables, the project manager should use the Project Management Information System (PMIS) to provide them with the access they need. The PMIS serves as the designated central repository for project information, ensuring all stakeholders can find current, authorized project artifacts through a single organized and access-controlled source. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option C (Team members, consultants from outside the project with experience in the field, and the customer) fixes it."',
        'Explanation: Keywords: risk workshop invitation, bridge construction, distribution list, relevant expertise. A risk workshop for an infrastructure project requires a distribution list that combines project familiarity, domain expertise, and business perspective. Team members provide project context, external consultants with field experience identify industry-specific risks, and the customer provides operational and business risk perspectives — together forming the most comprehensive risk identification capability. (PMBOK Guide) – Seventh Edition, 2021, p. 46, \'Optimize Risk Responses\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Options A, B, and E (Organizational process assets (OPAs); Lesson learned registers from past projects; Project management plan) work together."',
        'Explanation: Keywords: junior project manager, project success, organizational process assets, lessons learned. Ensuring project success depends on leveraging both the organization\'s accumulated knowledge and established planning frameworks. Organizational process assets, lessons learned registers, and the project management plan together provide the historical context, foundational guidance, and structured approach that enable a new project manager to make informed decisions and avoid repeating past mistakes. (PMBOK Guide) – Seventh Edition, 2021, p. 25, \'Be a Diligent, Respectful, and Caring Steward\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option D (Approach the team member with empathy and obtain agreement through collaboration.) fixes it."',
        'Explanation: Keywords: sprint goal disagreement, acceptance tester, empathy, collaborative agreement. When a team member is unable to agree on sprint goals during planning, the project manager should approach the situation with empathy and seek agreement through collaboration — not dismissal or majority override. Understanding the team member\'s perspective and working toward a shared resolution builds trust and ensures all voices contribute to a stronger, more inclusive sprint commitment. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option B (Assess the impact of the required change and consult with the executive sponsors to determine the best course of action.) fixes it."',
        'Explanation: Keywords: regulatory requirement mid-project, building scope change, impact assessment, executive sponsor consultation. When a municipality issues a new regulation mid-project that affects scope, the project manager must first assess the full impact of the required change and consult with executive sponsors before taking any action. Proper impact assessment and sponsor consultation ensure the organization makes a coordinated, informed decision about how to respond to the regulatory requirement. (PMBOK Guide) – Seventh Edition, 2021, p. 34, \'Recognize, Evaluate, and Respond to System Interactions\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option C (Recommend an agile approach so the project can be delivered iteratively.) fixes it."',
        'Explanation: Keywords: high uncertainty, expected changes, benefits demonstration, agile iterative delivery. When a project has high uncertainty and frequent changes are expected, an agile approach best supports incremental value demonstration and evolving requirements. Agile\'s iterative delivery directly addresses the sponsor\'s priority of showing benefits early and continuously, rather than deferring all value realization to a single final release at project end. (PMBOK Guide) – Seventh Edition, 2021, p. 48, \'Embrace Adaptability and Resiliency\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option D (Log the issue and assign it to the project team member(s).) fixes it."',
        'Explanation: Keywords: project closing, missed notification, issue log, team assignment. When a stakeholder reports they did not receive a notification during project closing, the project manager should log the issue formally and assign it to the appropriate team member(s) for resolution. Proper issue management ensures the gap is addressed systematically so the affected department receives the required notification before the project formally closes. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option D (Understand the reason for the team member\'s absence and encourage them to attend future meetings.) fixes it."',
        'Explanation: Keywords: team member absent from meetings, completed tasks, understand the reason, encourage participation. Before drawing conclusions about consistent meeting absences, the project manager should first understand the underlying reason — there may be a legitimate barrier or scheduling conflict that can be addressed. Empathetically understanding the cause before encouraging attendance demonstrates respectful leadership and is more likely to produce lasting engagement than mandating compliance. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    (
        'Explanation: Need: protect value and acceptance. Option B (Provide the failed test results along with the agreed-upon acceptance criteria) fixes it."',
        'Explanation: Keywords: vendor quality dispute, acceptance testing, failed test results, acceptance criteria evidence. To support a quality claim against a vendor, the project manager must provide objective, agreed-upon evidence — specifically the failed test results alongside the contractual acceptance criteria. This combination demonstrates not just that the system failed, but that it failed against standards the vendor explicitly agreed to, providing the strongest factual basis for resolving the quality dispute. (PMBOK Guide) – Seventh Edition, 2021, p. 42, \'Build Quality into Processes and Deliverables\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option A (Communicate the situation to the team and plan for the necessary training and coaching arrangements) fixes it."',
        'Explanation: Keywords: team knowledge gaps, core competencies, training planning, coaching arrangements. When the project team lacks the core competencies needed to deliver results, the project manager should communicate the situation transparently and plan for the necessary training and coaching to close the gaps. A servant leader addresses capability deficits by investing in team development rather than by reducing scope, replacing members, or alarming the customer prematurely. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option A (Speak with the team member about their engagement and contributions) fixes it."',
        'Explanation: Keywords: virtual team, entry-level colleague, demotivated, excluded from team. When a new virtual team member feels demotivated and excluded, the project manager should first speak directly with the team member about their engagement and contributions to understand the root cause and explore solutions together. This direct, empathetic conversation respects the individual, surfaces the specific barriers to inclusion, and provides the foundation for a targeted and effective intervention. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option A (Investigate the impact of this issue with the team and survey the market for alternative wires with similar characteristics) fixes it."',
        'Explanation: Keywords: wire incompatibility announcement, market coverage reduction, impact investigation, alternative wire survey. When a manufacturer announces a product change that will reduce the machine\'s market coverage, the project manager should investigate the full impact with the team and survey the market for alternative wires with similar characteristics. This measured response identifies the true scope of the problem and explores feasible solutions before making any drastic decisions such as stopping the project. (PMBOK Guide) – Seventh Edition, 2021, p. 34, \'Recognize, Evaluate, and Respond to System Interactions\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option A (Ensure participation from all team members) fixes it."',
        'Explanation: Keywords: multi-vendor integration, critical delivery stage, full team participation, complex project. During the most critical integration delivery stage — where solutions from multiple vendors must converge — ensuring participation from all team members is essential for successful coordination and issue resolution. Full team participation makes all relevant expertise available at the moment it is needed most, enabling faster identification and resolution of integration problems. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option D (Team member assessment) fixes it."',
        'Explanation: Keywords: hearing impaired team member, frustrated behavior, team member assessment, accessibility. A formal team member assessment at the start of the project would have identified the team member\'s hearing impairment, enabling the project manager to arrange appropriate accommodations for meetings and communications. Conducting team member assessments proactively ensures that every team member\'s needs are understood and addressed before communication challenges manifest as behavioral issues. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option D (Provide routine mentoring and coaching to the team members to identify any demotivating issues) fixes it."',
        'Explanation: Keywords: team performance decrease, schedule performance index, overtime, mentoring and coaching. When team members show signs of decreased performance and potential demotivation — despite the overall project being ahead of schedule — the project manager should provide routine mentoring and coaching to identify the underlying issues before they escalate. Sustained high performance requires ongoing attention to team wellbeing and motivation, not just tracking schedule and budget metrics. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option B (Communicate individually with the affected team members to negotiate the decision and confirm their willingness to relocate) fixes it."',
        'Explanation: Keywords: team member relocation abroad, individual negotiation, willingness confirmation, team member autonomy. When key team members must be asked to relocate abroad for an extended period, the project manager should communicate individually with each affected team member to negotiate the decision and confirm their willingness before proceeding. Respecting team members\' autonomy in significant personal decisions builds trust, reduces attrition risk, and ensures the relocation proceeds with informed consent rather than as an imposed directive. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option B (Support the product owners decision to change the priority of the product backlog items) fixes it."',
        'Explanation: Keywords: hybrid project, sprint review, product owner backlog priority change, servant leader. As a servant leader, the project manager should support the product owner\'s authority to reprioritize product backlog items — that is precisely the product owner\'s role and accountability in an agile or hybrid framework. Routing backlog reprioritization through a change control board inappropriately treats it as a formal scope change rather than the routine product management activity it is. (PMBOK Guide) – Seventh Edition, 2021, p. 32, \'Focus on Value\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option D (Share and discuss the pros and cons of adopting agile with the stakeholders and choose the approach they prefer for the new project) fixes it."',
        'Explanation: Keywords: agile adoption announcement, experienced predictive stakeholders, shared discussion, methodology choice. When shifting to a new project methodology with stakeholders who are familiar with the existing approach, the project manager should share and discuss the pros and cons of agile openly with them and let them participate in choosing the approach. Involving stakeholders in the methodology decision generates ownership and ensures the selected approach has their genuine support — critical for a successful transition. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option C (Support the team to find and execute the minimum viable product (MVP)) fixes it."',
        'Explanation: Keywords: overwhelmed team, 30 features, minimum viable product, scope prioritization. When a team feels overwhelmed by the breadth of a large project, the project manager should support the team in identifying and executing the minimum viable product (MVP) — the smallest, highest-value increment that satisfies the sponsor\'s core intent. The MVP approach makes the work manageable while ensuring the most critical business value is delivered first. (PMBOK Guide) – Seventh Edition, 2021, p. 32, \'Focus on Value\'"'
    ),
    (
        'Explanation: Need: protect value and acceptance. Option D (Break down the project into smaller tasks and estimate the durations of the activities) fixes it."',
        'Explanation: Keywords: unfamiliar project type, bottom-up estimation, work decomposition, activity duration. When facing a project type that differs significantly from prior experience — making analogical estimates unreliable — the project manager should break the project into smaller, well-understood tasks and estimate each activity\'s duration from first principles. This bottom-up decomposition provides the most accurate schedule basis when historical analogies cannot be directly applied. (PMBOK Guide) – Seventh Edition, 2021, p. 32, \'Focus on Value\'"'
    ),
    (
        'Explanation: Need: keep plans flexible. Option B (Develop an integrated change management plan) fixes it."',
        'Explanation: Keywords: change request process failures, inconsistent information, integrated change management, process control. When the change request process has historically been handled by fragmented parties with inconsistent information about schedule and budget, the solution is to develop an integrated change management plan that consolidates all change-related activities under a single, coherent framework. An integrated plan eliminates the information silos and process inconsistency that the CEO is experiencing across the organization. (PMBOK Guide) – Seventh Edition, 2021, p. 34, \'Recognize, Evaluate, and Respond to System Interactions\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option D (Facilitate the update of the product backlog) fixes it."',
        'Explanation: Keywords: agile project, post-sprint change request, product backlog update, sponsor change. In an agile project, when a sponsor requests a change after a sprint, the appropriate next step is to facilitate the update of the product backlog to incorporate and prioritize the change for a future sprint. This approach respects the agile change management process — capturing the request in the backlog rather than disrupting the current sprint or bypassing the backlog prioritization discipline. (PMBOK Guide) – Seventh Edition, 2021, p. 32, \'Focus on Value\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option B (Ensure that the communications management plan covers contractual obligations) fixes it."',
        'Explanation: Keywords: subcontractor direct client communication, past pattern, communications plan, contractual obligations. When a previous pattern of subcontractors bypassing the project manager to communicate directly with the client exists, the project manager must ensure the communications management plan explicitly covers the contractual obligations that govern communication boundaries. Embedding these obligations in the plan ensures that contractual communication protocols are documented and respected rather than just verbally asserted. (PMBOK Guide) – Seventh Edition, 2021, p. 25, \'Be a Diligent, Respectful, and Caring Steward\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option C (Help the management team understand how the change to an agile approach impacts the relevance of certain reports and key performance indicators (KPIs)) fixes it."',
        'Explanation: Keywords: agile organizational transition, management reporting, KPI relevance, adapting dashboards. When an organization transitions to agile, some traditional reports and KPIs become less relevant while new agile metrics emerge. The project manager should help the management team understand how the shift to agile changes which indicators are meaningful — respecting their visibility needs while educating them about how agile performance is best measured. (PMBOK Guide) – Seventh Edition, 2021, p. 40, \'Tailor Based on Context\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option A (Perform stakeholder engagement with the virtual team) fixes it."',
        'Explanation: Keywords: virtual team, late deliverables, status tracking gap, stakeholder engagement. When a virtual team is consistently missing deliverables, the root cause is often an engagement or communication gap rather than a process deficit. Performing stakeholder engagement with the virtual team allows the project manager to understand the team\'s challenges, align on expectations, and ensure virtual members feel as connected and accountable as co-located team members. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option B (Meet with both integration leads to understand the root cause and determine a resolution) fixes it."',
        'Explanation: Keywords: program integration misalignment, blaming team leads, root cause analysis, collaborative resolution. When two integration leads are blaming each other for a misalignment, the project manager should meet with both to understand the root cause and determine a joint resolution rather than assigning blame. This collaborative approach depersonalizes the conflict, leverages the combined expertise of both leads, and addresses the actual technical misalignment rather than just the interpersonal dynamic. (PMBOK Guide) – Seventh Edition, 2021, p. 44, \'Navigate Complexity\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option C (Inform the purchasing department that manages the supplier relationship) fixes it."',
        'Explanation: Keywords: supplier financial difficulty, news report, purchasing department, supplier relationship management. When a team member reports potential financial difficulties with a key supplier, the project manager should inform the purchasing department that manages the supplier relationship — the organizational unit with contractual authority and established supplier contact. Escalating to the procurement relationship owner ensures the right people assess and respond to the potential procurement risk. (PMBOK Guide) – Seventh Edition, 2021, p. 34, \'Recognize, Evaluate, and Respond to System Interactions\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option B (Evaluate various delivery options in order to immediately demonstrate value to the customer) fixes it."',
        'Explanation: Keywords: internal deliverables, customer unaware of progress, delivery options, demonstrate value externally. When a team is consistently delivering value internally but the customer cannot see it, the project manager should evaluate delivery options to make that value immediately visible to the customer. Customers must be able to observe and experience the value being delivered — otherwise iterative progress fails to build the trust and feedback loops that justify continued investment in the project. (PMBOK Guide) – Seventh Edition, 2021, p. 32, \'Focus on Value\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option C (Request a meeting with the disruptive team member and help to resolve the issue) fixes it."',
        'Explanation: Keywords: disruptive team member, difficult personal situation, argumentative behavior, empathetic meeting. When a team member is behaving disruptively in meetings and there is context suggesting a difficult personal situation, the project manager should request a direct meeting to address the concern empathetically and help resolve the underlying issue. A private, empathetic conversation acknowledges the behavioral impact while demonstrating care for the individual — more appropriate than escalation or team-wide activities as a first response. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option D (Building trust) fixes it."',
        'Explanation: Keywords: kick-off meeting, flexible attendance options, trust building, stakeholder engagement quality. Offering team members the flexibility to attend meetings from home or the office demonstrates that the project manager trusts team members to participate effectively regardless of location. This flexibility builds trust by respecting team members\' autonomy and work preferences — directly embodying the \'building trust\' stakeholder engagement quality described in PMBOK 7th Edition. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    (
        'Explanation: Need: keep plans flexible. Option C (Review project schedule because the project is under budget and behind schedule) fixes it."',
        'Explanation: Keywords: earned value analysis, under budget, behind schedule, schedule review. When a project is under budget but behind schedule, the project manager should review the project schedule to understand the cause of the delay and develop a recovery plan. Being under budget while behind schedule indicates that work is progressing more slowly than planned — requiring schedule intervention, not a cost or scope review which would address entirely different performance issues. (PMBOK Guide) – Seventh Edition, 2021, p. 40, \'Tailor Based on Context\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option C (Negotiate the impact of these changes with the client) fixes it."',
        'Explanation: Keywords: thin profit margin, constant change requests, schedule and budget impact, client negotiation. When a client\'s constant change requests are stretching both schedule and budget on a low-margin project, the project manager should negotiate the impact of those changes directly with the client. Transparent negotiation about the cumulative impact of change requests protects the project\'s viability while maintaining the client relationship through honest, data-driven communication about project constraints. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option A (Suggest an agile approach to refine these requirements and prioritize them according to the project objectives) fixes it."',
        'Explanation: Keywords: unstable strategic requirements, agile approach, requirement refinement, value prioritization. When key requirements are unstable but strategically important for value creation, an agile approach most effectively manages them — allowing continuous refinement through iterative feedback loops rather than attempting to lock them down prematurely. Agile\'s adaptive framework enables the team to evolve requirements progressively while keeping them prioritized according to the project\'s strategic objectives. (PMBOK Guide) – Seventh Edition, 2021, p. 48, \'Embrace Adaptability and Resiliency\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option C (Pull communication) fixes it."',
        'Explanation: Keywords: email overload, pull communication, on-demand information access, team productivity. Pull communication refers to information that stakeholders access on demand at their own discretion — such as shared repositories, project portals, and intranets — rather than receiving unsolicited push communications like email. The team member is requesting pull communication access so they can retrieve project information when needed, reducing the email volume that is diminishing productive work time. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option A (Assessed and analyzed personality indicators from the project team) fixes it."',
        'Explanation: Keywords: team-building activity, forming phase, personality indicators, inappropriate activity. Before planning team-building activities during the forming phase, the project manager should assess and analyze personality indicators across the team to select activities that are appropriate, inclusive, and engaging for all members. Understanding personality types and preferences prevents the mismatch between activity design and team needs that produced the negative feedback about the improvisational theater sessions. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option D (Built a shared repository for the project in the internal server and asked the team to create record and save all project deliverables to the server) fixes it."',
        'Explanation: Keywords: test report missing, engineer departure, shared repository, knowledge management. The previous project manager should have established a shared project repository and required all team members to save deliverables — including test reports — to that repository as they were completed. Systematic knowledge capture in a shared system ensures critical project artifacts are preserved regardless of team member turnover, preventing the loss of deliverable documentation when personnel leave the organization. (PMBOK Guide) – Seventh Edition, 2021, p. 25, \'Be a Diligent, Respectful, and Caring Steward\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option D (Allow the engineer and designer to cross-train with each other) fixes it."',
        'Explanation: Keywords: engineer skill gap, designer willingness to teach, cross-training, knowledge sharing. When a team member has the exact skill another needs and is willing to teach it, the project manager should encourage and allow cross-training between them. This leverages existing internal expertise, builds team capability without external cost, and strengthens the collaborative culture by encouraging team members to share knowledge and actively support each other\'s professional growth. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option C (Advise the team not to engage in modifications unless it follows the proper change approval process) fixes it."',
        'Explanation: Keywords: stakeholder direct feature requests, change approval bypass, hybrid project, scope creep prevention. When stakeholders bypass the formal change approval process by making modification requests directly to team members — even if this has been common organizational practice — the project manager must advise the team not to engage with such requests unless they follow the proper approval process. Enforcing the change process protects scope integrity and ensures all changes are evaluated for impact before work begins. (PMBOK Guide) – Seventh Edition, 2021, p. 25, \'Be a Diligent, Respectful, and Caring Steward\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option D (Establish team behavior and develop an understanding of how to work together) fixes it."',
        'Explanation: Keywords: hybrid project team formation, ground rules, working norms, shared understanding. At the start of a hybrid project after team formation and task assignment, the project manager should establish team behavioral norms and develop a shared understanding of how the team will work together. Establishing working agreements early creates the collaborative foundation that enables teams to navigate the hybrid approach\'s predictive and agile elements effectively throughout the project. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option C (Continue multiple rounds of planning poker and arrive at the size of the story) fixes it."',
        'Explanation: Keywords: inconsistent story sizing, planning poker, estimation consensus, agile sprint planning. When a team is producing inconsistent iteration results due to improper story sizing, continuing multiple rounds of planning poker until consensus is reached is the most effective approach to improving estimate accuracy. Planning poker\'s structured multi-round process drives team convergence on a shared size estimate through calibrated discussion, producing more reliable sprint plans than averaging or top-down assignment. (PMBOK Guide) – Seventh Edition, 2021, p. 42, \'Build Quality into Processes and Deliverables\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option A (Request a meeting with the project sponsor to discuss the viability of the project and determine the next actions) fixes it."',
        'Explanation: Keywords: major layoff, 25% team members affected, project viability, sponsor discussion. When a significant portion of the project team is included in a company-wide layoff, the project manager must first meet with the project sponsor to assess the project\'s viability and determine the next course of action. Only the sponsor has the authority and business context to decide whether the project should continue, be modified, or be cancelled given the loss of 25% of team capacity. (PMBOK Guide) – Seventh Edition, 2021, p. 34, \'Recognize, Evaluate, and Respond to System Interactions\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option D (inform the relevant stakeholders of this challenge and seek their support) fixes it."',
        'Explanation: Keywords: supplier payment dispute, critical service termination, stakeholder notification, organizational support. When a critical supplier threatens to terminate services due to a payment issue, the project manager should inform the relevant stakeholders of the challenge and seek their support. Payment disputes require organizational authority beyond the project manager\'s scope — notifying the right stakeholders ensures the issue receives the resources and decision-making needed to resolve it before the project is impacted. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    (
        'Explanation: Need: keep plans flexible. Option C (Review the procurement agreements to address the situation) fixes it."',
        'Explanation: Keywords: vendor delivery delay, iterative manufacturing project, procurement agreements, contractual review. When a vendor announces they cannot deliver equipment on the agreed dates, the project manager should review the procurement agreements to understand the contractual obligations, remedies, and delivery terms applicable to the situation. The procurement agreement is the governing document for supplier delivery commitments and provides the framework for determining what actions the project manager can require of the vendor. (PMBOK Guide) – Seventh Edition, 2021, p. 34, \'Recognize, Evaluate, and Respond to System Interactions\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option D (Have a discussion with the sponsor and recommend the project business value be reassessed) fixes it."',
        'Explanation: Keywords: market information, reduced business value, project reassessment recommendation, sponsor authority. When new market information suggests a project may no longer deliver its expected business value, the project manager should discuss this with the sponsor and recommend a formal business value reassessment. Only the sponsor has the authority to make the go/no-go decision, but the project manager has a professional obligation to surface the information and initiate the reassessment conversation. (PMBOK Guide) – Seventh Edition, 2021, p. 32, \'Focus on Value\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option D (Collaborate/problem solve) fixes it."',
        'Explanation: Keywords: quality dispute, new team member deliverable, conflicting assessments, collaborate problem solve. When a conflict involves a factual disagreement — the senior member claims poor quality while the project manager\'s own review confirms the deliverable meets requirements — the project manager should use a collaborative problem-solving approach to address the underlying misalignment. Collaboration/problem solve engages both parties to examine the facts together and reach a mutually acceptable resolution, rather than forcing a decision based on one party\'s assertion. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option A (Set up a meeting with the stakeholder to address their concerns directly) fixes it."',
        'Explanation: Keywords: stakeholder product dissatisfaction, daily standup attendance, team morale impact, direct stakeholder meeting. When a stakeholder\'s presence in daily standups is negatively affecting team morale and productivity, the project manager should set up a direct meeting with the stakeholder to address their concerns outside the team context. This protects the team\'s working environment while ensuring the stakeholder\'s legitimate product concerns are heard and addressed through a more appropriate engagement channel. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option B (Culture of the organization) fixes it."',
        'Explanation: Keywords: leadership style selection, organizational culture, context-appropriate leadership, situational awareness. When choosing a leadership style, the project manager must consider the culture of the organization — because leadership effectiveness depends on alignment with the norms, values, and expectations that shape how people respond to authority and guidance in that specific context. An approach that is effective in one culture may be counterproductive in another, making cultural fit the primary consideration in leadership style selection. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option D (Meet with the stakeholder to better understand their expectations and update the stakeholder engagement plan) fixes it."',
        'Explanation: Keywords: stakeholder not receiving reports, new project manager, expectation understanding, engagement plan update. When a stakeholder raises a concern about not receiving periodic reports, the project manager should meet with them first to fully understand their information needs and preferences before updating any plans or adding them to distribution lists. Understanding what the stakeholder actually needs ensures the project manager addresses the root of the concern rather than making assumptions about what to provide. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option A (Held a touchpoint with marketing before the demo to discuss any impediments) fixes it."',
        'Explanation: Keywords: iteration-based project, marketing team launch timeline, pre-demo touchpoint, impediment discovery. The team should have held a touchpoint with the marketing team before the iteration demo to surface any impediments — such as the marketing team\'s own preparation timeline — that could affect the project\'s launch plan. A pre-demo touchpoint creates an early warning mechanism that allows cross-functional dependencies to be identified and addressed before they become critical path issues. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
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
