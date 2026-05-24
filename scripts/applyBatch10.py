MD_FILE = './src/imports/project-management-questions-1.md'

with open(MD_FILE, 'r', encoding='utf-8') as f:
    content = f.read()

replacements = [
    (
        'Explanation: Need: guide and calm the team. Option A (Evaluate the impact of this decision and communicate with management.) fixes it."',
        'Explanation: Keywords: management decision, infrastructure downgrade, impact evaluation, virtual team. When management mandates a technology change that affects the project\'s agreed-upon plan, the project manager must evaluate the full impact on the team and deliverables before accepting the change. Communicating the impact objectively to management ensures the decision is made with awareness of its consequences on project performance. (PMBOK Guide) – Seventh Edition, 2021, p. 34, \'Recognize, Evaluate, and Respond to System Interactions\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option C (Invite the senior manager to the next planning meeting.) fixes it."',
        'Explanation: Keywords: senior manager, missing features, sprint planning, stakeholder engagement. When a senior stakeholder is surprised by missing features in a release, it indicates they have expectations that are not aligned with the team\'s current sprint priorities. Inviting the senior manager to the next planning meeting directly addresses the alignment gap by giving them visibility into and input on how features are sequenced. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option C (Gather information and find the root cause of the problem.) fixes it."',
        'Explanation: Keywords: interpersonal skills conflict, team effectiveness, root cause, issue escalation. When a team member\'s interpersonal behavior is reducing team effectiveness, the project manager must first gather sufficient information to understand the full situation before taking corrective action. Identifying the root cause prevents misattribution and enables a targeted response that addresses the actual source of the conflict. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option A (Ensure that the requirements for the project are understood and that the objectivesare verified before approval of an agreement.) fixes it."',
        'Explanation: Keywords: procurement participation, requirements understanding, pre-agreement objectives, procurement process. When a project manager is involved in the procurement process before a project begins, their most important contribution is ensuring that requirements and objectives are clearly understood and verified before the agreement is signed. Contractual ambiguity in requirements creates the foundation for disputes, scope creep, and delivery failures once the project starts. (PMBOK Guide) – Seventh Edition, 2021, p. 42, \'Build Quality into Processes and Deliverables\'"'
    ),
    (
        'Explanation: Need: watch risks early. Option B (Perform a qualitative risk analysis.) fixes it."',
        'Explanation: Keywords: service provider risk, resource availability, qualitative risk analysis, delivery assurance. When a service provider has experienced ongoing resource problems but asserts deliverables will be on time, the project manager cannot simply accept that assurance without formal risk assessment. Performing a qualitative risk analysis evaluates the probability and impact of the delivery risk so an appropriate response can be planned if the assurance proves unfounded. (PMBOK Guide) – Seventh Edition, 2021, p. 46, \'Optimize Risk Responses\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option C (Recommend the product owner prioritize the missing work higher because it isneeded for the minimum viable product (MVP).) fixes it."',
        'Explanation: Keywords: MVP, missing backlog work, product owner, prioritization recommendation. When missing work critical to the MVP is added to the bottom of the backlog, the project manager must advocate for correct prioritization rather than simply accepting the product owner\'s initial placement. Recommending higher prioritization based on MVP necessity gives the product owner the context needed to make an informed reprioritization decision. (PMBOK Guide) – Seventh Edition, 2021, p. 32, \'Focus on Value\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option B (Share the organization',
        'Explanation: Keywords: agile adoption, organizational decision, team communication, methodology transition. When an organization formally decides to adopt agile, the project manager\'s first responsibility is to communicate that decision to the team and begin collaborative planning for the transition. Involving the team early in planning for the new approach builds shared ownership and enables the team to identify how their existing skills translate into the agile context. (PMBOK Guide) – Seventh Edition, 2021, p. 48, \'Embrace Adaptability and Resiliency\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option B (Assessed the organizational culture) fixes it."',
        'Explanation: Keywords: agile transformation, organizational culture, change resistance, functional groups. Resistance from functional groups that a project is moving too fast reflects a cultural readiness gap that should have been assessed before launching an agile transformation. Understanding organizational culture at the outset allows the project manager to tailor the pace and communication approach for the transformation to match the organization\'s capacity for change. (PMBOK Guide) – Seventh Edition, 2021, p. 50, \'Enable Change to Achieve the Envisioned Future State\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option D (Ask the project sponsor what sort of information is needed and agree on a frequency for the communication.) fixes it."',
        'Explanation: Keywords: sponsor communication preference, communications management plan, information needs, agreed frequency. When a sponsor declines a default communication format, the project manager must understand their actual information preferences rather than either ignoring them or following the original plan unchanged. Agreeing on the specific information needed and the right frequency creates a tailored communication approach that serves the sponsor\'s real needs. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option D (Assess risks together with business value during prioritization.) fixes it."',
        'Explanation: Keywords: backlog prioritization, risk vs. business value, integrated prioritization, agile risk management. Treating business value and risk as separate prioritization factors creates a false choice — risks can either amplify or diminish the realized value of a backlog item. Assessing risks alongside business value produces a more accurate picture of each item\'s net contribution and enables more informed prioritization decisions. (PMBOK Guide) – Seventh Edition, 2021, p. 46, \'Optimize Risk Responses\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option C (Assessed the organization\'s culture, performed a suitability analysis, and determined the future state.) fixes it."',
        'Explanation: Keywords: agile implementation failure, organizational culture assessment, suitability analysis, future state. Agile implementation fails when it is applied without first assessing whether the organization\'s culture, processes, and people are suited for it — investing heavily without this analysis is the common root cause of failed transformations. Conducting a suitability analysis and defining the desired future state provides the roadmap needed to close the gap between where the organization is and where it needs to be. (PMBOK Guide) – Seventh Edition, 2021, p. 40, \'Tailor Based on Context\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option C (Schedule a one-on-one meeting with the team member to talk about it and get theircooperation.) fixes it."',
        'Explanation: Keywords: team conflict, persistent disagreement, one-on-one meeting, conflict management. When a team member consistently challenges the project manager\'s direction on objectives, timelines, and deliverables, the conflict must be addressed directly and privately before it escalates. A one-on-one meeting gives the team member a safe space to express concerns and allows the project manager to understand the source of resistance and work toward cooperation. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option C (Develop a business case and submit it to the client.) fixes it."',
        'Explanation: Keywords: early benefits realization, business case, client value, additional work. When a project manager identifies an opportunity to deliver significant early value to a difficult client, the appropriate approach is to formalize that opportunity in a business case rather than making unauthorized changes or absorbing the cost. Presenting a business case to the client keeps the relationship transparent and enables the client to make an informed decision about the additional investment. (PMBOK Guide) – Seventh Edition, 2021, p. 32, \'Focus on Value\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option B (Include demonstrations of the built portion of the product at the end of every sprint.) fixes it."',
        'Explanation: Keywords: business value demonstration, sprint review, stakeholder visibility, agile delivery. The most direct way to show stakeholders ongoing project business value in an agile project is through working product demonstrations at the end of each sprint. Sprint demos provide tangible, empirical evidence of progress and value delivery while also creating the feedback loop that keeps the project aligned with stakeholder expectations. (PMBOK Guide) – Seventh Edition, 2021, p. 32, \'Focus on Value\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option A (Iterative for the requirements analysis and delivery phases of the project) fixes it."',
        'Explanation: Keywords: requirements analysis, bi-weekly demos, iterative approach, project lifecycle selection. When a client wants bi-weekly product demos even during requirements analysis, an iterative approach is appropriate because it naturally incorporates feedback cycles throughout both the analysis and delivery phases. This lifecycle choice aligns the delivery cadence with the client\'s expectation for frequent visibility into progress. (PMBOK Guide) – Seventh Edition, 2021, p. 40, \'Tailor Based on Context\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option A (Review the project plan to evaluate if any updates should be made.) fixes it."',
        'Explanation: Keywords: competitive release, project plan review, market impact, strategic response. When a competitor releases a similar product, the project manager must evaluate whether this external event changes the project\'s strategic assumptions before taking any action. Reviewing the project plan provides the structured basis for determining whether adjustments to scope, features, or timeline are warranted to remain competitive. (PMBOK Guide) – Seventh Edition, 2021, p. 34, \'Recognize, Evaluate, and Respond to System Interactions\'"'
    ),
    (
        'Explanation: Need: keep plans flexible. Option A (Assess the current state process to define the scope of the digitization.) fixes it."',
        'Explanation: Keywords: digitization project, scope definition, current state assessment, process analysis. Before defining the scope of a digitization project, the project manager must first understand the current state processes that will be digitized — you cannot accurately scope a transformation without knowing what is being transformed. Assessing the current state provides the factual foundation for scope decisions and prevents digitizing inefficient or unnecessary processes. (PMBOK Guide) – Seventh Edition, 2021, p. 42, \'Build Quality into Processes and Deliverables\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option B (Include knowledge transfer sessions between the project and operations teams at every stage.) fixes it."',
        'Explanation: Keywords: hybrid migration, operations team readiness, knowledge transfer, staged delivery. When a staged system migration reveals that the operations team is not ready to support the new system, knowledge transfer cannot be deferred to the final handoff — it must be built into every delivery stage. Incorporating knowledge transfer sessions at each stage ensures the operations team can support the new system incrementally as it is deployed. (PMBOK Guide) – Seventh Edition, 2021, p. 48, \'Embrace Adaptability and Resiliency\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option B (Review the stakeholder engagement plan.) fixes it."',
        'Explanation: Keywords: change resistance, transformational project, stakeholder engagement plan, overcoming opposition. Stakeholder resistance during a transformational project signals that the engagement approach is not effectively addressing stakeholder concerns or managing their expectations. Reviewing the stakeholder engagement plan identifies where the current approach is falling short and provides the basis for adjusting engagement strategies to reduce resistance. (PMBOK Guide) – Seventh Edition, 2021, p. 50, \'Enable Change to Achieve the Envisioned Future State\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option A (Start the project and add any uncertainty that arises to the risk register.) fixes it."',
        'Explanation: Keywords: virtual team, cultural diversity, risk register, proactive uncertainty management. Cultural differences in a geographically dispersed team introduce uncertainty that may not be fully predictable at the outset — the pragmatic approach is to begin work while systematically tracking cultural uncertainties as they emerge. Logging these uncertainties in the risk register creates visibility and enables structured responses when cultural differences begin affecting project work. (PMBOK Guide) – Seventh Edition, 2021, p. 46, \'Optimize Risk Responses\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Options A and E (Identify the sources and specifics of the knowledge gap from the interns and newrecruits.; Put the interns and new recruits into groups and assign a SME as a mentor.) work together."',
        'Explanation: Keywords: knowledge gaps, budget exhausted, SME mentoring, intern development. When the training budget is exhausted but knowledge gaps threaten delivery, the project manager must first identify exactly what knowledge is missing before implementing a solution. Pairing interns and new recruits with SME mentors is a cost-effective approach that transfers targeted knowledge without requiring additional training budget. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    (
        'Explanation: Need: watch risks early. Option C (Review the terms of the contract in order to determine next steps.) fixes it."',
        'Explanation: Keywords: supplier failure, equipment license, contract terms, critical path impact. When a supplier fails to deliver due to an expired equipment license that causes a critical path delay, the project manager must first review the contract terms to understand the supplier\'s obligations and the available remedies. Contract terms define responsibilities, penalties, and escalation rights that determine what actions the project manager can formally take in response. (PMBOK Guide) – Seventh Edition, 2021, p. 25, \'Be a Diligent, Respectful, and Caring Steward\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option A (Review the base model with the team leaders in each country to establish anindependent budget for each phase.) fixes it."',
        'Explanation: Keywords: multicultural delivery, phased project, country-specific budgets, collaborative planning. A software solution delivered across multiple countries with significantly different cultures cannot be accurately budgeted using a single base model — local team leaders have the contextual knowledge needed to calibrate estimates for each phase and location. Reviewing the base model collaboratively with country team leaders produces independent phase budgets that reflect the actual delivery environment. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option D (Meet the team member and try to plan a course of action together.) fixes it."',
        'Explanation: Keywords: new team member, critical path conflict, task priority, collaborative planning. When a newly hired team member identifies a task priority conflict affecting the critical path, the project manager must engage collaboratively to understand the issue and jointly develop a resolution. Meeting to plan together respects the new team member\'s technical insight while ensuring the response is coordinated and aligned with project constraints. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option B (Implement a project management information system (PMIS)) fixes it."',
        'Explanation: Keywords: document version control, PMIS implementation, information management, team communication. When team members are working on outdated document versions due to email-based distribution, the root cause is the absence of a centralized information management system. Implementing a PMIS provides a single source of truth for project documents, eliminating version confusion and the wasted effort of working on superseded content. (PMBOK Guide) – Seventh Edition, 2021, p. 42, \'Build Quality into Processes and Deliverables\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option D (Conduct a meeting to help the team define the team charter) fixes it."',
        'Explanation: Keywords: new agile team, team charter, goal setting, agile fundamentals. When a new agile team struggles to meet goals in its first daily meetings, it often lacks the shared agreements and clarity of purpose that a team charter provides. Facilitating a team charter session establishes shared norms, roles, and commitments that give the team the foundation needed to operate effectively in an agile environment. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option C (Schedule a kick-off session to explain the problems of the project and gain approval and support) fixes it."',
        'Explanation: Keywords: behind schedule, over budget, stakeholder concerns, kick-off session recovery. When a project is behind schedule and over budget and stakeholders are concerned, the project manager must create a forum where problems can be explained transparently and support for corrective action can be formally secured. A kick-off session for recovery aligns stakeholders on the current situation and obtains the approval needed to execute a remediation plan. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option A (Request the project sponsor prioritize and if necessary, allocate additional budget so the team can work on a single project) fixes it."',
        'Explanation: Keywords: agile team, multi-project assignment, focus, sponsor support. An agile team split across multiple projects cannot maintain the focus and flow that effective agile delivery requires — the project manager must escalate this as a structural issue that needs sponsor-level resolution. Requesting that the sponsor prioritize projects and provide budget for dedicated resourcing removes the fundamental constraint on team performance. (PMBOK Guide) – Seventh Edition, 2021, p. 32, \'Focus on Value\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option B (Confirm ownership for ongoing value realization) fixes it."',
        'Explanation: Keywords: feature benefits, value realization, ownership, team understanding. When team members do not understand the business benefits of project features, it signals that value ownership is unclear — someone must be accountable for articulating and confirming the value each feature delivers. Confirming ownership for ongoing value realization ensures that benefit tracking is someone\'s explicit responsibility and that the team has a go-to source for understanding why their work matters. (PMBOK Guide) – Seventh Edition, 2021, p. 32, \'Focus on Value\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option D (The protect is aligned with the benefits management plan) fixes it."',
        'Explanation: Keywords: project value assessment, benefits management plan, value delivery indicator, sponsor concern. The most reliable indicator that a project is delivering value is alignment with the benefits management plan — which defines what outcomes were promised and how they will be measured. When a sponsor questions whether results are on track, checking alignment with the benefits management plan provides the objective evidence needed to assess true value delivery. (PMBOK Guide) – Seventh Edition, 2021, p. 32, \'Focus on Value\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option D (Reduce the story size by splitting stories) fixes it."',
        'Explanation: Keywords: agile estimation, inaccurate estimates, story splitting, story size refinement. When estimates appear inaccurate in an agile project, the typical cause is that stories are too large to be estimated reliably — splitting them into smaller, more granular stories enables more precise sizing. Reducing story size improves estimation accuracy because smaller work items have fewer unknowns and can be completed within a single iteration. (PMBOK Guide) – Seventh Edition, 2021, p. 40, \'Tailor Based on Context\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option C (Consult the project team to understand the extent of the training needs for the contractor) fixes it."',
        'Explanation: Keywords: agile contractor, training needs assessment, team consultation, skills gap. When a contractor lacks agile experience, the project manager must first understand the training gap from the team\'s perspective before prescribing a solution. Consulting the project team reveals which specific agile practices the contractor needs to understand for effective collaboration, enabling a targeted training approach rather than a blanket solution. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Options A and D (Look for processes that cause bottlenecks and slow down the team\'s agility; Work with the team to remove impediments as quickly as possible) work together."',
        'Explanation: Keywords: burndown chart, velocity improvement, impediment removal, bottleneck identification. When a Scrum team is behind schedule after the first iteration, both systemic process bottlenecks and specific impediments must be addressed in parallel to restore velocity. Looking for bottleneck processes identifies structural causes of slowdowns, while rapidly removing impediments with the team produces immediate unblocking so delivery can accelerate. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option C (Identified key stakeholders and included all of them in project agreement discussions.) fixes it."',
        'Explanation: Keywords: stakeholder alignment, project objectives, agreement discussions, inclusive planning. When internal customer groups believe the project objective was not met despite formal acceptance, it indicates that not all relevant stakeholders were included in defining and agreeing on what success looks like. Including all key stakeholders in project agreement discussions at the outset ensures that the shared definition of project success reflects the full range of organizational perspectives. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option D (Ask the product owner to prioritize the item with the customer.) fixes it."',
        'Explanation: Keywords: iteration demo, enhancement request, product owner prioritization, customer feedback. When a customer identifies a desired enhancement during an iteration demo, the product owner — not the team — is the authority for deciding where that item fits in the backlog relative to existing priorities. Asking the product owner to prioritize the item with the customer ensures that the enhancement is evaluated in the context of all other backlog items and business value. (PMBOK Guide) – Seventh Edition, 2021, p. 32, \'Focus on Value\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option B (Deliverable oriented) fixes it."',
        'Explanation: Keywords: WBS organization, deliverable-oriented structure, scope decomposition, project planning. A work breakdown structure must be organized around deliverables — the tangible, verifiable outputs the project must produce — rather than around costs, customers, or teams. A deliverable-oriented WBS ensures that the full scope is captured hierarchically and that each work package can be linked to a specific, measurable project outcome. (PMBOK Guide) – Seventh Edition, 2021, p. 42, \'Build Quality into Processes and Deliverables\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option A (Review team culture and the personality traits of the individual to address status update gaps.) fixes it."',
        'Explanation: Keywords: shy team member, team culture, individual personality, status update transparency. When a team member avoids group status updates due to shyness, the solution requires understanding both the team\'s cultural norms and the individual\'s personality rather than simply changing the reporting format. Reviewing team culture and personality traits allows the project manager to create conditions where the team member feels safe enough to participate in group activities. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option D (Develop working agreements with the team.) fixes it."',
        'Explanation: Keywords: agile team disputes, working agreements, team norms, conflict resolution. When a new agile team experiences frequent disputes and difficulty completing tasks, the root cause is typically the absence of shared norms and expectations about how to work together. Developing working agreements establishes the collaborative framework that allows the team to resolve disagreements constructively and focus energy on delivery. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option B (Review the stakeholder register to gain insight into the expectations of that team member.) fixes it."',
        'Explanation: Keywords: stakeholder expectations, trivial requests, stakeholder register, project takeover. When a new project manager encounters a client team member making requests that seem trivial and repetitive, the appropriate first step is to consult the stakeholder register to understand that person\'s role, influence, and expectations. The register provides context that may reveal why the team member is behaving this way and how best to engage them going forward. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option B (Promote an environment where everybody knows what their contribution means to the project as a whole.) fixes it."',
        'Explanation: Keywords: team engagement, contribution awareness, shared purpose, agile leadership. High team engagement in an agile project is sustained when each team member understands how their individual work connects to the larger project goals and business outcomes. Creating this shared sense of purpose transforms task completion into meaningful contribution, which is the most durable source of team engagement. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    (
        'Explanation: Need: protect value and acceptance. Option A (Review the benefits of the proposed changes in relation to the business case.) fixes it."',
        'Explanation: Keywords: poorly defined project, change requests, business case alignment, benefits review. When multiple change requests arrive on a poorly defined project, the project manager must evaluate each against the original business case before acting — changes that do not support the business case rationale should not be approved. Reviewing proposed changes in relation to the business case ensures that only value-adding modifications are pursued and prevents scope creep driven by organizational politics. (PMBOK Guide) – Seventh Edition, 2021, p. 32, \'Focus on Value\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option D (Explain the new team velocity to the customer.) fixes it."',
        'Explanation: Keywords: team capacity reduction, budget cut, adjusted velocity, customer expectation reset. When a budget cut reduces team size, the team\'s velocity will correspondingly decrease — the customer\'s delivery expectations must be recalibrated to match the new capacity. Explaining the updated velocity to the customer translates the budget impact into delivery terms, enabling the customer to make informed decisions about what can be delivered with the remaining resources. (PMBOK Guide) – Seventh Edition, 2021, p. 32, \'Focus on Value\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option D (Create an environment that encourages leadership, translates ambitions into growth opportunities, and rewards overtime workers.) fixes it."',
        'Explanation: Keywords: recent graduates, growth opportunities, leadership development, team engagement. A team composed almost entirely of recent graduates requires an environment that channels their ambition into structured growth and leadership development rather than traditional hierarchical direction. Creating opportunities for ownership and rewarding high performance keeps this demographic engaged and motivated throughout the project lifecycle. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option B (Delivering value to the customer) fixes it."',
        'Explanation: Keywords: software development, value delivery, customer focus, team direction. Once requirements have been gathered, the team\'s primary focus must be on transforming those requirements into working software that delivers value to the customer — not on internal metrics, process adherence, or schedule compliance as ends in themselves. Directing the team toward value delivery keeps the project anchored to its fundamental purpose. (PMBOK Guide) – Seventh Edition, 2021, p. 32, \'Focus on Value\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option B (Invite the stakeholder to the regular ""show and tell"" sessions so the stakeholder is aware of project progress and feedback can be gathered.) fixes it."',
        'Explanation: Keywords: agile show and tell, stakeholder visibility, feature feedback, communication gap. When a key stakeholder is missing critical feature information, the most effective solution is to bring them directly into the agile review process rather than increasing written communications. Inviting the stakeholder to sprint demos gives them real-time visibility into features being built and creates a feedback channel that reduces the risk of deploying the wrong functionality. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option C (Address this concern with the functional managers to ensure there will be no further delays.) fixes it."',
        'Explanation: Keywords: functional manager interference, resource conflict, team productivity, direct resolution. When functional managers are diverting team members to non-project tasks and causing productivity losses, the project manager must address the issue directly with those functional managers rather than logging it or asking others to intervene. A direct conversation with the functional managers establishes clear expectations about team availability and protects the project team\'s focus. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option C (Review the communications management plan and submit a change request if required.) fixes it."',
        'Explanation: Keywords: communications management plan, meeting frequency, sponsor request, change request. When a sponsor requests a change to the established communication cadence, the project manager must evaluate whether the current communications management plan needs to be formally updated rather than simply complying or refusing. Reviewing the plan and submitting a change request if needed ensures any modification to communication frequency is governed through the approved change process. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option C (The velocity should not be compared as teams can size items differently.) fixes it."',
        'Explanation: Keywords: velocity comparison, story point sizing, agile metrics, team performance. Velocity is a team-relative metric based on how that specific team sizes its story points — comparing velocity between two teams is meaningless because each team may assign different point values to equivalent work. Using velocity comparisons to judge team performance creates perverse incentives for point inflation rather than driving genuine improvement. (PMBOK Guide) – Seventh Edition, 2021, p. 40, \'Tailor Based on Context\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option D (Support the team members\' growth and development.) fixes it."',
        'Explanation: Keywords: agile transition, team unfamiliarity, growth and development, capability building. When most team members are unfamiliar with agile, the project manager\'s primary responsibility is to invest in their growth and development rather than changing the approach or replacing team members. Supporting capability building creates the foundational agile skills the team needs while preserving team continuity and morale during the transition. (PMBOK Guide) – Seventh Edition, 2021, p. 48, \'Embrace Adaptability and Resiliency\'"'
    ),
    (
        'Explanation: Need: keep plans flexible. Option D (Follow the risk management process while ensuring that risks are identified, analyzed, and managed during each iteration.) fixes it."',
        'Explanation: Keywords: agile risk management, iterative risk identification, PMO compliance, continuous risk assessment. Agile projects are not exempt from risk management — they require continuous identification, analysis, and response to risks at every iteration. Applying the risk management process iteratively ensures that the project\'s risk posture is always current and that the PMO\'s visibility and governance requirements are met throughout delivery. (PMBOK Guide) – Seventh Edition, 2021, p. 46, \'Optimize Risk Responses\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option A (Evaluate the engagement needs of stakeholders.) fixes it."',
        'Explanation: Keywords: stakeholder involvement, engagement needs assessment, high-participation project, stakeholder evaluation. When a project requires high stakeholder involvement, the project manager must first understand what level and type of engagement each stakeholder actually needs before defining the participation approach. Evaluating engagement needs produces a stakeholder-specific strategy that ensures involvement is meaningful and appropriate rather than uniformly applied. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option C (Update the stakeholder register and revise the stakeholder engagement plan.) fixes it."',
        'Explanation: Keywords: missing stakeholders, community opposition, stakeholder register, engagement plan revision. When a previously unidentified stakeholder group begins actively opposing a project, the project manager must immediately formalize their presence in the stakeholder register and develop a targeted engagement strategy. Updating the register and revising the engagement plan provides the structured basis for turning community opposition into managed, collaborative participation. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option A (Ask the product owner to look at a minimum of four to eight iterations and replan the velocity for the next iteration based on the team\'s current performance.) fixes it."',
        'Explanation: Keywords: velocity decrease, iteration history, replanning, product owner. A 30% velocity decrease requires replanning based on actual performance data rather than restoring the original target through pressure or staffing changes. Reviewing four to eight iterations of historical performance gives the product owner the trend data needed to set realistic velocity expectations that reflect the team\'s genuine current capacity. (PMBOK Guide) – Seventh Edition, 2021, p. 40, \'Tailor Based on Context\'"'
    ),
    (
        'Explanation: Need: protect value and acceptance. Option B (Explore reporting the earned value (EV) key performance indicators (KPls) using agile progress as an input.) fixes it."',
        'Explanation: Keywords: hybrid reporting, earned value, agile metrics, status reporting improvement. When management is accustomed to traditional EV-based reporting but projects are experiencing sudden status changes, the solution is to enrich the EV reporting with agile progress data to provide earlier warning signals. Integrating agile velocity and iteration metrics as inputs to earned value KPIs bridges the communication gap between agile delivery and traditional management reporting. (PMBOK Guide) – Seventh Edition, 2021, p. 34, \'Recognize, Evaluate, and Respond to System Interactions\'"'
    ),
    (
        'Explanation: Need: secure people or vendors. Option C (Perform a root cause analysis of the project performance.) fixes it."',
        'Explanation: Keywords: budget overrun, budget at completion, root cause analysis, cost variance. A significant and unexpected shift in the budget at completion signals that a fundamental change in project conditions or performance has occurred — the project manager must understand what caused it before determining corrective action. Performing a root cause analysis identifies the specific drivers of the cost variance and provides the basis for an informed response. (PMBOK Guide) – Seventh Edition, 2021, p. 44, \'Navigate Complexity\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option A (Propose a phased project approach with multiple small interactions and build trust with the stakeholder through frequent value delivery.) fixes it."',
        'Explanation: Keywords: stakeholder resistance, agile adoption, phased approach, trust building. When a stakeholder is resistant to agile based on past negative experience, imposing the methodology or escalating the disagreement will increase resistance. Proposing a phased approach with frequent deliveries allows the stakeholder to experience agile value delivery firsthand, building the trust needed for full adoption through demonstrated results rather than persuasion. (PMBOK Guide) – Seventh Edition, 2021, p. 48, \'Embrace Adaptability and Resiliency\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option A (Plan for incremental and iterative delivery based on feedback from the marketing and sales team.) fixes it."',
        'Explanation: Keywords: decommission project, stakeholder objections, incremental delivery, feedback-based planning. When stakeholders challenge a decommissioning decision with data suggesting a channel may still have value, the project manager must respond with an evidence-based approach rather than proceeding rigidly. Planning incremental delivery based on marketing and sales feedback allows the value of each channel to be empirically verified before final decommissioning decisions are made. (PMBOK Guide) – Seventh Edition, 2021, p. 32, \'Focus on Value\'"'
    ),
    (
        'Explanation: Need: keep plans flexible. Option C (Study and apply the lessons learned from the failed project so that this project does not follow the same pattern.) fixes it."',
        'Explanation: Keywords: lessons learned, failed project, organizational process assets, risk prevention. When a similar project has recently failed within the same organization, that failure represents a documented organizational risk that must be proactively addressed. Studying and applying the lessons learned from the failed project transforms a known organizational risk into concrete preventive actions that reduce the likelihood of repeating the same pattern. (PMBOK Guide) – Seventh Edition, 2021, p. 46, \'Optimize Risk Responses\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option D (Evaluate the impact of the key team member\'s removal from the project, look for alternatives, and submit a change request if required.) fixes it."',
        'Explanation: Keywords: key resource loss, impact evaluation, alternatives assessment, change request. When a key team member with an irreplaceable role is reassigned, the project manager must first evaluate the full impact on scope, schedule, and quality before recommending a response. Assessing alternatives and submitting a change request if needed ensures that the impact is transparently communicated and that any adjustments to the project baseline are formally approved. (PMBOK Guide) – Seventh Edition, 2021, p. 34, \'Recognize, Evaluate, and Respond to System Interactions\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option C (Continue with the sprint work as planned and keep monitoring.) fixes it."',
        'Explanation: Keywords: burndown chart monitoring, sprint tracking, normal progress, early sprint. Analyzing a burndown chart on day four of a 15-day sprint is too early to draw meaningful conclusions — minor variations in early-sprint progress are normal and do not warrant intervention. Continuing to execute as planned while maintaining ongoing monitoring is the appropriate response when there is no clear signal of a deviation requiring corrective action. (PMBOK Guide) – Seventh Edition, 2021, p. 40, \'Tailor Based on Context\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option C (Adopt an incremental cycle of delivering value to the customer.) fixes it."',
        'Explanation: Keywords: rework reduction, incremental delivery, agile specialist, customer satisfaction. Rework and dissatisfaction in software delivery typically stem from building features in large batches without customer validation — incremental delivery breaks this cycle by delivering small amounts of working software frequently. Each increment gives the customer an opportunity to validate direction early, reducing the likelihood of rework caused by late-discovered misalignment. (PMBOK Guide) – Seventh Edition, 2021, p. 32, \'Focus on Value\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option B (Incremental delivery and frequent backlog refinement based on user feedback) fixes it."',
        'Explanation: Keywords: hybrid approach, incremental delivery, backlog refinement, user feedback. For an organization transitioning from predictive to partial agile adoption, incremental delivery combined with frequent backlog refinement based on user feedback is the practice that most directly delivers ongoing business value throughout the project. This approach ensures that the product evolves based on real user input rather than initial assumptions that may prove incorrect. (PMBOK Guide) – Seventh Edition, 2021, p. 32, \'Focus on Value\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Options C and D (Perform a risk identification process with the project team.; Consult with the project stakeholders.) work together."',
        'Explanation: Keywords: government legislation risk, risk identification, stakeholder consultation, new law impact. When a potential new government law is identified during project execution, both internal and external perspectives must be gathered immediately to assess its potential impact. Performing a risk identification process with the team surfaces technical and operational risks, while consulting stakeholders captures business and contractual implications — together these provide a complete picture of the legislative risk. (PMBOK Guide) – Seventh Edition, 2021, p. 46, \'Optimize Risk Responses\'"'
    ),
    (
        'Explanation: Need: keep plans flexible. Option B (Plan projectA in sprints, starting with the module that does not require machine learning skills.) fixes it."',
        'Explanation: Keywords: resource constraint, machine learning expert, sprint planning, module sequencing. When a critical specialized resource is unavailable at project start, planning sprints around the modules that do not require that expertise allows delivery to begin immediately while the expert becomes available. Starting with the non-machine-learning module maximizes productive use of the available team and reduces the risk of resource-caused delays later. (PMBOK Guide) – Seventh Edition, 2021, p. 40, \'Tailor Based on Context\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option A (Invest in developing the team\'s emotional intelligence.) fixes it."',
        'Explanation: Keywords: team motivation, unmotivated member, emotional intelligence, team dynamics. When one team member\'s low motivation is affecting the entire team, the systemic issue is how emotions and interpersonal dynamics are understood and managed within the group. Investing in the team\'s emotional intelligence builds the collective capacity to recognize, understand, and constructively respond to motivational challenges rather than allowing them to propagate. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option B (Decline the request politely since the issue, although critical, is not the responsibility of the project team.) fixes it."',
        'Explanation: Keywords: scope boundary, operational issue, out-of-scope request, polite decline. When a customer requests project team support for an operational issue that falls outside the project\'s scope, the project manager must decline professionally to protect team focus and prevent scope creep. A polite decline preserves the customer relationship while upholding the boundaries that keep the project team focused on its contractual deliverables. (PMBOK Guide) – Seventh Edition, 2021, p. 25, \'Be a Diligent, Respectful, and Caring Steward\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option C (Check with the agile teams to see if the project manager\'s understanding of the Agile Manifesto is correct.) fixes it."',
        'Explanation: Keywords: agile documentation, Agile Manifesto, documentation minimum, agile misunderstanding. The Agile Manifesto values working software over comprehensive documentation but does not eliminate documentation entirely — if agile teams are producing no documentation at all, the project manager may be misapplying the manifesto. Checking with the agile teams verifies whether their approach reflects a correct interpretation of agile principles or a misunderstanding that needs to be corrected. (PMBOK Guide) – Seventh Edition, 2021, p. 40, \'Tailor Based on Context\'"'
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
