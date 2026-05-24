MD_FILE = './src/imports/project-management-questions-1.md'

with open(MD_FILE, 'r', encoding='utf-8') as f:
    content = f.read()

replacements = [
    (
        'Explanation: Need: keep plans flexible. Option A (Create an entry in the impediment board and assign it.) fixes it."',
        'Explanation: Keywords: impediment board, temporary assignment, former department, delayed iteration. When a dependency on an external team creates a blocker, the proper agile response is to log it in the impediment board and assign ownership so it is tracked and resolved systematically. Creating transparency around blockers allows the team to address delays without the project manager bypassing organizational boundaries. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option A (Meet with the project sponsor as soon as possible to discuss the matter further) fixes it."',
        'Explanation: Keywords: project sponsor, unauthorized access, sensitive specifications, direct discussion. When a sponsor requests information they are not authorized to access, the project manager must address the situation directly and promptly rather than either complying or escalating immediately. A face-to-face discussion allows the project manager to understand the underlying need and explain the access restrictions with respect and clarity. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option B (Ask the team member to work with their peers to knowledge share) fixes it."',
        'Explanation: Keywords: specialized resource departure, knowledge transfer, key deadline, agile team. When a specialist must leave imminently, the highest-priority action is to ensure their critical knowledge is transferred to the remaining team members so work can continue. Peer knowledge sharing leverages the two available workdays effectively and preserves the team\'s ability to deliver against the approaching deadline. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option D (Use the standup meeting to assess impediments and problems) fixes it."',
        'Explanation: Keywords: team velocity, review gate, sprint impediments, standup meeting. When velocity is insufficient to meet a review gate, the first step is to surface and understand the root causes — the daily standup is specifically designed for this purpose by exposing blockers and coordination issues. Addressing impediments directly allows the team to self-correct without changing scope, timelines, or methodology prematurely. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option C (Use fixed-price increments as user stories are completed.) fixes it."',
        'Explanation: Keywords: hybrid project, agile vendor contract, fixed-price increments, user stories. In a hybrid environment where the information systems component uses agile delivery, contracting must reflect the incremental nature of value delivery rather than a single lump sum. Fixed-price increments tied to completed user stories align payment structure with agile cadence while maintaining cost predictability for both parties. (PMBOK Guide) – Seventh Edition, 2021, p. 40, \'Tailor Based on Context\'"'
    ),
    (
        'Explanation: Need: keep plans flexible. Option C (Consult a senior project manager within the organization and request their expert judgement) fixes it."',
        'Explanation: Keywords: unfamiliar industry, new project manager, expert judgment, strategic project. When a project manager lacks domain knowledge needed to understand the interdependencies of a new project, consulting an experienced internal senior PM provides the expert judgment necessary to plan effectively. Leveraging organizational knowledge assets is the appropriate first step before committing to a project management plan. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option A (The acceptance criteria should have been properly defined in the contract) fixes it."',
        'Explanation: Keywords: acceptance criteria, defect rate, contract definition, client dispute. A client dispute over the acceptable defect rate at project close indicates that quality acceptance criteria were not formally agreed upon in the contract — each party was relying on a different standard. Defining explicit, measurable acceptance criteria in the contract prevents ambiguity and creates a shared baseline for project completion. (PMBOK Guide) – Seventh Edition, 2021, p. 42, \'Build Quality into Processes and Deliverables\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option B (Consult with the project management office (PMO) for guidance on project artifacts.) fixes it.\"\n\"Question 351',
        'Explanation: Keywords: cancelled project, project artifacts, PMO guidance, archive requirement. Even for cancelled projects, organizational governance typically requires proper archiving of project artifacts for future reference, audits, and lessons learned. Consulting the PMO ensures the project manager follows established organizational standards rather than complying with informal instructions that may conflict with policy. (PMBOK Guide) – Seventh Edition, 2021, p. 25, \'Be a Diligent, Respectful, and Caring Steward\'"\n"Question 351'
    ),
    (
        'Explanation: Need: guide and calm the team. Option A (Call for a team meeting to identify the root cause for the declining performance) fixes it."',
        'Explanation: Keywords: new project manager, declining performance, execution phase, root cause. A team that has previously delivered well on similar projects but is now underperforming suggests the cause is situational rather than capability-based — the new project manager must first understand why before intervening. Calling a team meeting to surface the root cause is the most direct way to diagnose and address the performance decline. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option C (Evaluate the impact that the inclusion of this new requirement will have on project performance) fixes it."',
        'Explanation: Keywords: late requirement, scope change, impact evaluation, end of execution. When a high-level stakeholder identifies a missing requirement late in the project, the project manager must first assess its full impact on schedule, cost, and scope before deciding on a course of action. Evaluating the impact provides the factual basis needed to communicate with the sponsor and change control board about the right response. (PMBOK Guide) – Seventh Edition, 2021, p. 34, \'Recognize, Evaluate, and Respond to System Interactions\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option D (Consult with the client to determine if project execution should be continued.) fixes it."',
        'Explanation: Keywords: incomplete blueprints, construction project, client consultation, project decision. Discovering that client-provided blueprints appear incomplete is a significant risk to the project that the project manager cannot resolve unilaterally — the client must confirm whether execution should proceed or blueprints must be revised. Consulting the client first ensures no irreversible construction work is performed on incomplete specifications. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option A (Focus on remediation not merely on correcting symptoms) fixes it."',
        'Explanation: Keywords: performance decline, retrospective, root cause, remediation focus. Repeated performance decline over three iterations signals a systemic issue that surface-level fixes will not resolve — remediation requires identifying and addressing the underlying cause rather than patching individual symptoms. Focusing on root cause analysis during the retrospective gives the team a genuine path to sustainable improvement. (PMBOK Guide) – Seventh Edition, 2021, p. 44, \'Navigate Complexity\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option A (Check with the team to learn what can be done, and consult an expert) fixes it."',
        'Explanation: Keywords: inapplicable feature, contract requirement, lessons learned, expert consultation. When a contracted feature is identified as not applicable, the project manager must not immediately accept that conclusion without verifying it through the team and subject matter expertise. Checking with the team and consulting an expert establishes whether the constraint is real and what alternatives exist before escalating or abandoning the scope item. (PMBOK Guide) – Seventh Edition, 2021, p. 44, \'Navigate Complexity\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option C (Address and remove obstacles and blockers for the team) fixes it."',
        'Explanation: Keywords: hybrid project, servant leadership, obstacles, blocker removal. A core servant leadership responsibility is shielding the team from external interference so they can focus on delivering value — addressing and removing obstacles and blockers is the project manager\'s primary duty in this role. Empowering the team by clearing their path is more effective than simply logging issues or redirecting communication. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option D (Review the work in progress with the product owner to determine the next step) fixes it."',
        'Explanation: Keywords: team member absence, work in progress, product owner, next steps. When a key team member takes unexpected leave during an iteration, the value of unfinished work must be assessed before deciding how to proceed — the product owner is the authority on value and priority. Reviewing work in progress with the product owner ensures that any decision about reassignment or deferral is aligned with business priorities. (PMBOK Guide) – Seventh Edition, 2021, p. 32, \'Focus on Value\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option D (Discuss the project scope statement with the key stakeholder and build prototypes) fixes it."',
        'Explanation: Keywords: scope changes, initiating phase, prototypes, scope statement refinement. Frequent scope change requests during initiation signal that requirements are not yet well understood — building prototypes is the most effective way to help stakeholders visualize and refine their needs. Discussing the scope statement alongside prototypes aligns stakeholder expectations with a concrete representation of the solution early in the project. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option A (Provide opportunity for team members to learn and adjust to the technology.) fixes it."',
        'Explanation: Keywords: new technology, velocity reduction, learning opportunity, self-organizing team. A self-organizing team accepting a task with unfamiliar technology will naturally experience a temporary velocity reduction during the learning curve — this is expected, not a failure. Providing time and opportunity to learn is the adaptive response that builds long-term capability and preserves team integrity. (PMBOK Guide) – Seventh Edition, 2021, p. 48, \'Embrace Adaptability and Resiliency\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option A (Prioritize the product backlog looking for high business value and low effort, and adjust the project budget and staffing to account for those items.) fixes it."',
        'Explanation: Keywords: budget reduction, backlog prioritization, high business value, constrained resources. When a 30% budget cut forces resource reductions on an agile project, maintaining value delivery requires ruthless backlog prioritization — focusing on high-value, low-effort items maximizes outcomes within the new constraint. Adjusting staffing and scope together ensures the project remains viable and continues to deliver meaningful results. (PMBOK Guide) – Seventh Edition, 2021, p. 32, \'Focus on Value\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option A (Make sure the analyst has regular pairing meetings with the other team member throughout task execution) fixes it."',
        'Explanation: Keywords: functional organization, technical skill gap, peer pairing, knowledge support. When a team member lacks the specific technical expertise needed for a task, the most constructive response is to pair them with an expert throughout execution rather than replacing them or deferring training. Regular pairing sessions build the analyst\'s skills while ensuring the work is completed to the required standard. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option C (Allocated additional time for mentoring) fixes it."',
        'Explanation: Keywords: resource replacement, intern mentoring, sprint velocity, project delay prevention. When an intern replaces a critical resource mid-sprint, the mentoring overhead is a predictable cost that must be explicitly planned into the schedule. Failing to allocate additional time for mentoring underestimates the capacity impact and leads to the milestone delays that ultimately put the project in critical status. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option D (Engage the project team to look for alternatives to find a solution) fixes it."',
        'Explanation: Keywords: material delay, construction project, team collaboration, alternative solutions. A missing critical material with a looming delivery date requires creative problem-solving that goes beyond waiting — engaging the full team to explore alternatives leverages collective knowledge and experience to find a path forward. Collaborative solution-finding empowers the team and increases the likelihood of discovering viable options the project manager might not identify alone. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option C (Conduct a focused retrospective to help the team to discover the root cause) fixes it."',
        'Explanation: Keywords: overtime, iteration overcommitment, focused retrospective, root cause discovery. When a team consistently works extra hours to meet iteration commitments, the pattern signals a systemic estimation or capacity issue that requires dedicated investigation. A focused retrospective creates a structured forum for the team to diagnose the underlying cause and agree on corrective measures before the next iteration. (PMBOK Guide) – Seventh Edition, 2021, p. 48, \'Embrace Adaptability and Resiliency\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option D (Make transactional decisions focusing on the project goals) fixes it."',
        'Explanation: Keywords: client change request, design change, project goals, value assessment. When a client requests a design change during a progress meeting, the project manager must evaluate it against project objectives rather than simply accommodating or rejecting it. Making transactional decisions anchored to project goals ensures that changes are assessed for their true impact on value, schedule, and scope before any commitment is made. (PMBOK Guide) – Seventh Edition, 2021, p. 32, \'Focus on Value\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option C (Set expectations with the new team member and explain what is needed) fixes it."',
        'Explanation: Keywords: new team member integration, agile-to-predictive transition, expectations setting, role clarity. Integrating a team member from an agile background into a predictive environment requires clear communication about what behaviors, practices, and outputs are expected in the new context. Setting explicit expectations early gives the new team member the direction they need to contribute effectively while the project manager plans how to leverage their agile experience. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Options A, C, and E (High-level product backlog; Product vision; Product roadmap) work together."',
        'Explanation: Keywords: agile product delivery, product backlog, product vision, product roadmap. Successful agile product delivery requires three foundational elements: a product vision that defines the purpose and direction, a product roadmap that outlines how the vision will be achieved over time, and a high-level product backlog that captures the initial set of requirements. Together these three artifacts align the team and stakeholders around a shared understanding of what is being built and why. (PMBOK Guide) – Seventh Edition, 2021, p. 32, \'Focus on Value\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option C (Describe to the team members how specific tools and techniques can be used to finish on time) fixes it."',
        'Explanation: Keywords: contingency exhausted, team resistance, tools and techniques, project completion. When contingency is fully consumed and the team is resisting a rigorous process near project end, the project manager must channel resistance into productive action by explaining how the tools and techniques will enable on-time delivery. Providing concrete, practical guidance replaces resistance with direction and maintains team focus during the critical final phase. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option A (Follow the change management process and work with procurement if needed) fixes it."',
        'Explanation: Keywords: subcontractor, new requirement, change management process, procurement. When a key stakeholder requests a new feature during a vendor delivery presentation, the change must be routed through the formal change management process to assess scope, cost, and contract implications. Engaging procurement ensures any modification to the vendor\'s scope of work is handled contractually and does not create unauthorized obligations. (PMBOK Guide) – Seventh Edition, 2021, p. 50, \'Enable Change to Achieve the Envisioned Future State\'"'
    ),
    (
        'Explanation: Need: watch risks early. Option C (Evaluate the impact the new regulations will have on the project and submit a change request) fixes it."',
        'Explanation: Keywords: regulatory change, new government standards, impact evaluation, change request. When new government regulations emerge mid-project that require deliverable changes, the project manager must first evaluate the full impact on scope, schedule, and cost before taking corrective action. Submitting a change request formalizes the necessary scope adjustments through the approved change control process. (PMBOK Guide) – Seventh Edition, 2021, p. 34, \'Recognize, Evaluate, and Respond to System Interactions\'"'
    ),
    (
        'Explanation: Need: control changes and baselines. Option B (Identify adequate change management tools to conduct the project) fixes it."',
        'Explanation: Keywords: change management tools, flexible baseline, time to market, hybrid project. When business stakeholders need a more responsive way to incorporate changes, the solution is not to abandon change control but to identify tools that enable faster, structured change management. Selecting appropriate change management tools balances the need for flexibility and speed with the governance required to maintain project integrity. (PMBOK Guide) – Seventh Edition, 2021, p. 50, \'Enable Change to Achieve the Envisioned Future State\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option A (Product owner) fixes it.\"\n\"Question 373',
        'Explanation: Keywords: hybrid project, change request, direct team approach, product owner authority. In a hybrid project, the product owner is the designated authority for managing requirements and changes to the product backlog — stakeholders must route new requirements through the product owner rather than approaching team members directly. This ensures changes are properly evaluated for business value and priority before entering the delivery pipeline. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"\n"Question 373'
    ),
    (
        'Explanation: Need: listen to people needs. Option C (The change should be considered because it will help the team work more efficiently) fixes it."',
        'Explanation: Keywords: process improvement suggestion, team efficiency, internal change, no customer impact. A change that improves team efficiency has direct value to the project even if it adds no new customer-facing features — more efficient processes reduce delivery risk and improve throughput for future iterations. The project manager should consider such improvements as legitimate investments in team performance. (PMBOK Guide) – Seventh Edition, 2021, p. 48, \'Embrace Adaptability and Resiliency\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option D (Product owner) fixes it.\"\n\"Question 375',
        'Explanation: Keywords: hybrid project, conflicting requirements, stakeholder vs product owner, decision authority. The product owner is responsible for managing and prioritizing all product requirements in a hybrid project — when a stakeholder requirement conflicts with the product owner\'s requirements, the product owner has final authority to analyze the conflict and make the prioritization decision. This clear ownership of the product backlog prevents competing requirements from creating confusion in the delivery team. (PMBOK Guide) – Seventh Edition, 2021, p. 32, \'Focus on Value\'"\n"Question 375'
    ),
    (
        'Explanation: Need: control changes and baselines. Option D (Spend a short amount of time defining the scope and building prototypes to refine the requirements.) fixes it."',
        'Explanation: Keywords: predictive-to-agile transition, scope management, prototypes, requirement refinement. When transitioning to an agile approach, scope is not locked upfront but progressively elaborated through short definition cycles and prototypes that help stakeholders articulate their actual needs. Spending minimal time on initial scope definition while using prototypes to refine requirements embraces the empirical nature of agile delivery. (PMBOK Guide) – Seventh Edition, 2021, p. 40, \'Tailor Based on Context\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option C (Collaborate with the product owner and the team to plan the following sprint) fixes it."',
        'Explanation: Keywords: sprint review, missing features, backlog gaps, collaborative sprint planning. When a sprint review reveals that key backlog features were not included in the delivered increment, the appropriate response is collaborative replanning with the product owner and team — not escalation or change requests. This ensures the missing features are correctly prioritized and incorporated into the next sprint planning session. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option B (Work with the product manager and the rest of the team to update the project backlog.) fixes it."',
        'Explanation: Keywords: agile demo, customer feedback, new feature requirement, backlog update. In an agile project, a product demonstration that surfaces new customer requirements is a success — this feedback loop is exactly what the process is designed to capture. Working with the product manager and team to update the backlog translates customer insight into actionable backlog items that can be prioritized and delivered. (PMBOK Guide) – Seventh Edition, 2021, p. 32, \'Focus on Value\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option D (Consult with the project management office (PMO) for guidance on project artifacts.) fixes it.\"\n\"Question 379',
        'Explanation: Keywords: cancelled project, project artifacts, PMO guidance, administrative closure. Proper archiving of project artifacts is an organizational governance requirement that applies even to cancelled projects — these records provide value for future audits, lessons learned, and litigation protection. Consulting the PMO ensures the project manager follows established policy rather than informal instructions that may contravene organizational standards. (PMBOK Guide) – Seventh Edition, 2021, p. 25, \'Be a Diligent, Respectful, and Caring Steward\'"\n"Question 379'
    ),
    (
        'Explanation: Need: listen to people needs. Option C (Get agreement from stakeholders on high-level deliverables and requirements.) fixes it."',
        'Explanation: Keywords: hybrid delivery, phased approach, review gates, stakeholder agreement. In a multi-product-line hybrid project with phase gates, establishing stakeholder agreement on high-level deliverables and requirements at the outset creates the shared baseline that enables consistent governance across phases. Without this agreement, each phase gate review lacks a common standard against which progress can be measured. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option A (Evaluate the impact to the users and create a plan to address it.) fixes it."',
        'Explanation: Keywords: organizational change, environmental project, user impact evaluation, change management plan. A project that significantly changes how all users work requires a structured understanding of that impact before implementation begins. Evaluating user impact first enables the project manager to create a targeted change management plan that addresses adoption barriers and ensures the project delivers its intended organizational benefits. (PMBOK Guide) – Seventh Edition, 2021, p. 50, \'Enable Change to Achieve the Envisioned Future State\'"'
    ),
    (
        'Explanation: Need: protect value and acceptance. Option C (Meet with the project management office (PMO)/compliance entity to work onprocess tailoring to ensure that the agile deliverables support the compliance requirements of the organization.) fixes it."',
        'Explanation: Keywords: agile adoption, compliance requirements, process tailoring, PMO collaboration. When an organization adopts agile for the first time, compliance requirements do not disappear — they must be reconciled with agile practices through deliberate process tailoring. Collaborating with the PMO and compliance entity ensures that agile deliverables are shaped to satisfy governance obligations without undermining agility. (PMBOK Guide) – Seventh Edition, 2021, p. 40, \'Tailor Based on Context\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option D (Communicated the project management plan to the procurement division) fixes it."',
        'Explanation: Keywords: procurement alignment, project management plan, equipment specification, early communication. The project management plan documents the approved scope, including specific equipment requirements — sharing it with the procurement division early in the project ensures they understand why deviations from approved specifications are not acceptable. Proactive communication prevents procurement decisions that contradict documented and approved project requirements. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option D (Schedule a team event with the project sponsor to highlight the importance of the project and recognize the work of the team.) fixes it."',
        'Explanation: Keywords: project fatigue, team motivation, sponsor recognition, performance risk. Near the end of a long project, team morale and motivation can erode even when performance has been strong — servant leadership requires proactively addressing this risk before it impacts delivery. Organizing a team event with sponsor recognition reinforces the value of the project and acknowledges the team\'s contributions, which is the most effective response to late-project fatigue. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option C (Include this in the risk register.) fixes it."',
        'Explanation: Keywords: lessons learned, late delivery history, risk register, proactive risk management. Historical evidence from lessons learned that a team has repeatedly missed delivery dates is a specific, known risk that must be formally captured in the risk register before planning begins. Documenting and planning responses to this risk proactively gives the project manager the basis to implement preventive measures rather than reacting to schedule delays after they occur. (PMBOK Guide) – Seventh Edition, 2021, p. 46, \'Optimize Risk Responses\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option C (Approach the team member to identify any issues and then plan a resolution accordingly.) fixes it."',
        'Explanation: Keywords: new team member integration, team cohesion, issue identification, resolution planning. When a new team member struggles to integrate with an established team, the project manager must first understand the specific barriers before prescribing a solution. Proactively approaching the team member to identify issues demonstrates servant leadership and enables a targeted resolution that addresses the actual integration challenge. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option D (Established ground rules for the team) fixes it."',
        'Explanation: Keywords: external stakeholder meeting, team ground rules, role clarity, conflict prevention. When team members disagree about who should represent the project at an external stakeholder meeting in the project manager\'s absence, it reflects a gap in defined team protocols and role clarity. Establishing ground rules that include decision rights and representation responsibilities prevents such coordination failures before they escalate into stakeholder relationship issues. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option B (Develop a minimum viable product (MVP) for assessment from a select customer group.) fixes it."',
        'Explanation: Keywords: product value uncertainty, MVP development, customer validation, feature assessment. When a product owner cannot determine the business value of individual features, the solution is to test assumptions with real customers rather than speculating. Developing an MVP for a select customer group generates empirical feedback that enables the product owner to prioritize features based on actual perceived value. (PMBOK Guide) – Seventh Edition, 2021, p. 32, \'Focus on Value\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option C (Meet with the stakeholders to recommend the use of a time and materials (T&M) contract to address the problem.) fixes it."',
        'Explanation: Keywords: agile delivery, evolving requirements, fixed-price contract, T&M contract recommendation. A fixed-price contract is fundamentally misaligned with agile delivery when requirements are expected to evolve — the 40% EAC deviation confirms that the contract structure cannot accommodate the actual delivery model. Recommending a time and materials contract to stakeholders aligns the commercial arrangement with the agile approach and manages the financial risk going forward. (PMBOK Guide) – Seventh Edition, 2021, p. 40, \'Tailor Based on Context\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option D (Define the ground rules, responsibilities, and conflict management strategies.) fixes it."',
        'Explanation: Keywords: new agile practices, team resistance, ground rules, conflict management. When team members challenge the introduction of new practices like daily standups, the project manager must establish clear ground rules and conflict management strategies rather than forcing compliance or abandoning the approach. Defining shared norms and responsibilities creates the team structure within which new practices can be adopted effectively. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option B (Mediator) fixes it."',
        'Explanation: Keywords: procurement conflict, component delay, mediator role, conflict resolution. When a conflict between two stakeholders is causing project delay, the project manager steps in as a neutral mediator to facilitate resolution between the parties rather than imposing a decision. The mediator role enables both the procurement lead and contracts manager to work toward a mutually acceptable solution while the project manager focuses on restoring project momentum. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option C (Request an architecture review.) fixes it."',
        'Explanation: Keywords: design flaw, new architect, quality impact, architecture review. When a newly assigned architect identifies a potential design flaw with quality implications, an independent architecture review is needed to validate the finding before making changes that affect scope and schedule. The review provides the objective assessment required to determine the actual impact and the appropriate corrective action. (PMBOK Guide) – Seventh Edition, 2021, p. 42, \'Build Quality into Processes and Deliverables\'"'
    ),
    (
        'Explanation: Need: keep plans flexible. Option B (Review the backlog with the product owner and prioritize the tasks that are least likely to be affected by a change in legislation.) fixes it."',
        'Explanation: Keywords: legislation changes, design rework, backlog prioritization, cost minimization. When frequent legislative changes are causing design rework and resource waiting, the risk mitigation strategy is to prioritize backlog items that are stable and least susceptible to regulatory change. Working with the product owner to reprioritize around stable tasks protects the budget and keeps resources productive while volatile items await legislative clarity. (PMBOK Guide) – Seventh Edition, 2021, p. 46, \'Optimize Risk Responses\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option D (Analyze the impacts and create a plan for team decision making) fixes it."',
        'Explanation: Keywords: project manager absence, team empowerment, decision-making plan, continuity. When the project manager will be unavailable during project execution, the team must be prepared to make decisions independently without losing momentum or direction. Analyzing the impacts of the absence and creating an explicit decision-making plan ensures the team is empowered with the authority and guidance needed to keep the project on track. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option D (Meet with the project team to understand their skills and identify potential gaps and training requirements.) fixes it."',
        'Explanation: Keywords: skill gap assessment, team capability, training needs, SME requirements. When an SME defines the technical skills required for a research project, the project manager must verify whether the already-assigned team possesses those skills before the project begins execution. Meeting with the team to assess their current capabilities identifies gaps that can be addressed through training or resource adjustments before they become delivery issues. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option D (Update the issue log and define the mitigation strategy.) fixes it."',
        'Explanation: Keywords: new hire training delay, performance impact, issue log, mitigation strategy. When a new team member\'s extended training is actively affecting project performance, the situation must be formally tracked as an issue and addressed with a defined mitigation strategy. Updating the issue log ensures visibility and accountability, while the mitigation strategy provides a concrete plan to restore normal team performance. (PMBOK Guide) – Seventh Edition, 2021, p. 44, \'Navigate Complexity\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option B (Review the resources required for the tasks on the critical path.) fixes it."',
        'Explanation: Keywords: resource sharing, critical path, government fine risk, resource review. When shared resources are causing delays on a project with a government penalty risk, the project manager must focus protective action on the tasks that directly drive the deadline — those on the critical path. Reviewing critical path resource requirements enables targeted discussions about priority and reallocation that are grounded in schedule data. (PMBOK Guide) – Seventh Edition, 2021, p. 34, \'Recognize, Evaluate, and Respond to System Interactions\'"'
    ),
    (
        'Explanation: Need: keep plans flexible. Option B (Log the issue and follow the planned actions in the risk response plan.) fixes it."',
        'Explanation: Keywords: labor union negotiation, documented risk, risk response plan, planned response. When a risk that was identified and planned for during project planning materializes, the correct response is to execute the predetermined risk response plan rather than improvising a new approach. Following the planned actions demonstrates that the risk management process was effective and provides the most structured path to resolving the delay. (PMBOK Guide) – Seventh Edition, 2021, p. 46, \'Optimize Risk Responses\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option C (Review the stakeholder engagement plan and communication strategy.) fixes it.\"\n\"Question 400',
        'Explanation: Keywords: disengaged stakeholder, legal department, stakeholder engagement plan, communication review. A legal department stakeholder who is uninterested in product design meetings still has compliance requirements that are critical to the project — disengagement is a risk that must be managed through the stakeholder engagement plan. Reviewing the engagement plan and communication strategy identifies whether the current approach is appropriate for this stakeholder\'s needs and how to increase their participation. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"\n"Question 400'
    ),
    (
        'Explanation: Need: guide and calm the team. Option D (Validate if the training is within scope and budget.) fixes it."',
        'Explanation: Keywords: training budget, specialized training request, scope validation, budget alignment. When training funding has been approved but specific courses not yet defined, individual training requests must be evaluated against the project\'s scope and the approved budget before approval. Validating alignment ensures that specialized training investments are justified by project needs and do not consume resources needed for other team development priorities. (PMBOK Guide) – Seventh Edition, 2021, p. 32, \'Focus on Value\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option A (Meet with the stakeholders to understand their concerns and define an action plan to resolve issues.) fixes it."',
        'Explanation: Keywords: PM transition, stakeholder concerns, action plan, trust building. When stakeholders are dissatisfied with a project manager\'s performance, the most constructive first response is to engage directly to understand their specific concerns and demonstrate a commitment to resolving them. Meeting with stakeholders to define an action plan shows accountability and gives the project manager an opportunity to rebuild trust while addressing the underlying project issues. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option A (Discuss the issue with all stakeholders and work on a communications management plan to meet all stakeholder requirements.) fixes it.\"\n\"Question 403',
        'Explanation: Keywords: multinational team, time zones, communication gaps, communications management plan. When a group of stakeholders in a multinational project are consistently uninformed despite regular update meetings, the communications management plan is inadequate for their needs. Working with all stakeholders to develop a revised plan ensures that communication methods, timing, and frequency are tailored to the actual requirements of each stakeholder group. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"\n"Question 403'
    ),
    (
        'Explanation: Need: guide and calm the team. Option C (Mentor the team member and provide the necessary training.) fixes it."',
        'Explanation: Keywords: new technology, self-organizing team, mentoring, technical training. A new team member struggling with unfamiliar technology needs targeted support rather than reassignment — mentoring and training develop capability while preserving team membership and morale. Investing in the team member\'s growth aligns with the principle of creating collaborative, high-performing teams that can adapt to new technical challenges. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    (
        'Explanation: Need: secure people or vendors. Option D (Performed administrative closure of the project) fixes it."',
        'Explanation: Keywords: project closure, administrative closure, budget open, financial reconciliation. Failing to perform administrative closure leaves the project\'s financial records open and creates confusion in accounting systems — the budget remaining open months later is a direct consequence of skipping formal closure procedures. Administrative closure formally documents completion and triggers the financial reconciliation steps that close project accounts. (PMBOK Guide) – Seventh Edition, 2021, p. 25, \'Be a Diligent, Respectful, and Caring Steward\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option D (Determine the communication needs, environment, and tools to get the message across.) fixes it."',
        'Explanation: Keywords: remote team, requirement clarity, communication tools, daily standup gaps. When a remote development team consistently misunderstands requirements communicated in daily standups, the issue lies in the communication approach rather than the content. Determining the appropriate tools and environment for the remote context ensures that technical requirements are conveyed with the clarity and mutual understanding needed for successful delivery. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    (
        'Explanation: Need: keep plans flexible. Option C (Demonstrate the project alignment to the organizational strategy.) fixes it."',
        'Explanation: Keywords: portfolio alignment, organizational strategy, project justification, suspension threat. When a portfolio management office threatens to suspend a project for lack of strategic alignment, the project manager must present evidence that the project does support organizational strategy rather than simply advocating for continuation. Demonstrating alignment with facts gives decision-makers the information they need to make an informed portfolio prioritization decision. (PMBOK Guide) – Seventh Edition, 2021, p. 32, \'Focus on Value\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option D (Set up a meeting with stakeholders to validate and confirm acceptance of the deliverables.) fixes it."',
        'Explanation: Keywords: vendor scope completion, stakeholder validation, formal acceptance, deliverable review. When a vendor declares scope completion and requests approval, the project manager cannot approve unilaterally — formal stakeholder validation is required to confirm that deliverables meet the agreed specifications. Setting up a validation meeting ensures acceptance is based on objective review rather than the vendor\'s self-assessment. (PMBOK Guide) – Seventh Edition, 2021, p. 42, \'Build Quality into Processes and Deliverables\'"'
    ),
    (
        'Explanation: Need: protect benefits for users. Option D (Engage in creative and iterative negotiations with the leaders of each entity toagree on the launch date.) fixes it."',
        'Explanation: Keywords: organizational deployment, stakeholder negotiation, adoption success, launch date agreement. Successful adoption of an organization-wide product requires buy-in from the leaders of each impacted entity — a date imposed from above risks resistance that undermines adoption. Engaging each entity\'s leaders in iterative negotiation builds the ownership and commitment needed to achieve timely and successful rollout. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option A (Meet with the stakeholder to understand the concern and business impact, reprioritize as necessary, and invite them to join the sprint planning session.) fixes it."',
        'Explanation: Keywords: disengaged stakeholder, sprint planning, delivery date delay, stakeholder engagement. A key stakeholder who is repeatedly disappointed by delayed delivery and not participating in sprint planning is both disengaged and uninformed about the delivery process — the project manager must address both dimensions. Meeting to understand the business impact, reprioritizing accordingly, and inviting the stakeholder into sprint planning reconnects them with the team\'s work and aligns delivery with their actual needs. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option D (Encourage participation in decision making and empower the team.) fixes it."',
        'Explanation: Keywords: team direction, lack of enthusiasm, decision-making participation, team empowerment. A team of senior developers and SMEs that lacks direction and enthusiasm is likely suffering from insufficient autonomy and ownership — the solution is to involve them in decisions rather than directing them. Empowering the team to participate in decision-making restores engagement and leverages the expertise of a high-caliber group. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option B (Update the change management plan to define the level of control required forthese types of modifications.) fixes it."',
        'Explanation: Keywords: unauthorized small changes, change management plan, control threshold, contractor. When a contractor makes minor engineering changes without formal change requests, the problem is not the specific changes but the absence of a defined threshold for what level of modification requires formal approval. Updating the change management plan to specify control requirements for different modification types prevents future undocumented changes while avoiding bureaucracy for truly inconsequential adjustments. (PMBOK Guide) – Seventh Edition, 2021, p. 50, \'Enable Change to Achieve the Envisioned Future State\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option C (Employ Monitor Communications techniques, which may eventually trigger changes to the communications management plan.) fixes it."',
        'Explanation: Keywords: stakeholder comprehension, status reports, monitor communications, communications management plan. When new stakeholders consistently fail to understand status reports that worked for a previous stakeholder group, the communications management plan needs to be revised to reflect the new audience\'s needs. Employing monitor communications techniques provides the diagnostic process to identify what is failing and determine whether the plan requires updating. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option D (Schedule a virtual meeting so onsite and remote stakeholders can attend at the same time.) fixes it."',
        'Explanation: Keywords: kickoff meeting, scheduling challenge, virtual meeting, stakeholder availability. When stakeholders across different locations cannot all be present onsite simultaneously, a virtual meeting eliminates the geographic constraint and allows all required attendees to participate in the kickoff at the same time. This inclusive approach ensures the project begins with full stakeholder alignment without delaying the meeting indefinitely. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option B (Included all relevant criteria in the agreed upon definition of done (DoD), and crafted a shared product vision.) fixes it."',
        'Explanation: Keywords: customer rejection, definition of done, product vision, expectation alignment. When a customer rejects final deliverables because they did not meet expectations, the root cause is typically an inadequate definition of done that failed to capture all acceptance criteria. Including all relevant quality and acceptance criteria in the DoD and establishing a shared product vision ensures both the team and customer have a common understanding of what success looks like. (PMBOK Guide) – Seventh Edition, 2021, p. 42, \'Build Quality into Processes and Deliverables\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option A (Refer to the requirements traceability matrix.) fixes it."',
        'Explanation: Keywords: end of project, deliverable dispute, requirements traceability matrix, scope verification. When a customer disputes deliverable completion near project close, the requirements traceability matrix provides the documented evidence of which requirements were agreed upon, how they were implemented, and whether they were verified. This objective reference resolves the dispute by grounding the discussion in the formally approved scope baseline. (PMBOK Guide) – Seventh Edition, 2021, p. 42, \'Build Quality into Processes and Deliverables\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option C (Review the stakeholder engagement and communications management plans.) fixes it.\"\n\"Question 418',
        'Explanation: Keywords: status update request, distribution list, communications management plan, stakeholder engagement. When a stakeholder who is not on the distribution list requests regular status updates, the project manager must consult the stakeholder engagement and communications management plans before acting. These plans define who should receive what information and at what frequency — verifying them ensures any changes are consistent with the overall stakeholder communication strategy. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"\n"Question 418'
    ),
    (
        'Explanation: Need: guide and calm the team. Option A (Organize a planning session with the development team and use their estimations to complete the schedule.) fixes it."',
        'Explanation: Keywords: resource availability, hybrid delivery, schedule planning, team estimation. In hybrid delivery, schedule accuracy depends on estimates from the people doing the work — the development team has the best insight into their capacity and the complexity of their tasks. Organizing a collaborative planning session with the team produces more realistic schedule commitments than top-down or expert-judgment approaches when resource availability is uncertain. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option A (Organize a discussion with the product team to clarify the missing information.) fixes it."',
        'Explanation: Keywords: stakeholder concerns, requirement clarity, product team discussion, information gaps. When a key stakeholder believes requirement information is insufficient but the product team disagrees, the conflict must be resolved through direct dialogue rather than accepting either position as correct. Organizing a discussion between the stakeholder and the product team surfaces the specific gaps in understanding and enables collaborative resolution. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Options A and B (Ask the agile team to review the updated sprint velocity with the customer.; Ask the product owner to review the prioritized backlog with the customer.) work together."',
        'Explanation: Keywords: budget reduction, team reduction, sprint velocity, backlog prioritization. When team members are released due to budget cuts, both sprint velocity and backlog priorities must be recalibrated to reflect the reduced capacity and align with what the customer truly values. Reviewing updated velocity and reprioritized backlog with the customer together resets expectations honestly and ensures the remaining team focuses on the highest-value deliverables. (PMBOK Guide) – Seventh Edition, 2021, p. 32, \'Focus on Value\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option D (Have the product owner review the user stories in the product backlog with thecompliance officer on a regular basis to identify any gaps.) fixes it."',
        'Explanation: Keywords: regulated industry, agile compliance, product backlog review, compliance officer. In a regulated industry transitioning to Scrum, compliance requirements must be embedded into the product backlog rather than discovered after delivery — the product owner and compliance officer must collaborate continuously. Regular backlog reviews with the compliance officer ensure that each user story is assessed for regulatory alignment before it enters the sprint, preventing non-compliant features from reaching the customer. (PMBOK Guide) – Seventh Edition, 2021, p. 42, \'Build Quality into Processes and Deliverables\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option B (Reinforce the definition of done (DoD) during sprint planning so that the team has a common understanding of expectations.) fixes it."',
        'Explanation: Keywords: quality specifications, SPI decline, definition of done, sprint planning clarity. When deliverables are consistently rejected due to unmet quality specifications, the root cause is typically a misalignment between the team\'s understanding of "done" and the stakeholder\'s expectations. Reinforcing the definition of done during sprint planning closes that gap by establishing a shared, explicit quality standard before each iteration begins. (PMBOK Guide) – Seventh Edition, 2021, p. 42, \'Build Quality into Processes and Deliverables\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option A (Request that the team identifies, documents, and registers the issues to locate the source of the problems.) fixes it."',
        'Explanation: Keywords: quality review failures, cascading problems, issue identification, root cause tracking. When every corrective action reveals additional problems, the team is dealing with systemic complexity that requires structured issue identification rather than ad-hoc fixes. Documenting and registering each issue systematically allows patterns to emerge and the true source of the recurring quality problems to be located and addressed. (PMBOK Guide) – Seventh Edition, 2021, p. 44, \'Navigate Complexity\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option A (Review the communication needs of key stakeholders.) fixes it."',
        'Explanation: Keywords: missing report information, sponsor feedback, communication needs, stakeholder requirements. When a sponsor consistently receives timely reports but finds key information missing, the communications management approach does not match what the sponsor actually needs. Reviewing the communication needs of key stakeholders identifies the specific gaps and enables the project manager to update the reporting format and content accordingly. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
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
