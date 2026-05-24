MD_FILE = './src/imports/project-management-questions-1.md'

with open(MD_FILE, 'r', encoding='utf-8') as f:
    content = f.read()

replacements = [
    (
        'Explanation: Need: listen to people needs. Option A (Email, call, or meet with each stakeholder separately to obtain their input) fixes it."',
        'Explanation: Keywords: stakeholder availability, requirements gathering, charter approval, individual outreach. When stakeholders are not all available at once, waiting for a group meeting is not an option — the project must still collect their input. Reaching each stakeholder individually through their preferred channel ensures all perspectives are captured without holding up the planning process. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    (
        "Explanation: Need: listen to people needs. Option C (Cancel the project since the stakeholder's request is out of scope) fixes it.\"",
        'Explanation: Keywords: stakeholder conditional support, unrelated financial request, out-of-scope demands, project ethics. A stakeholder who conditions project support on unrelated financial benefits is placing demands that fall outside the project\'s authorized scope and may constitute a conflict of interest. When the project cannot proceed without this stakeholder and their demands cannot be accommodated ethically, cancelling is the responsible course of action. (PMBOK Guide) – Seventh Edition, 2021, p. 25, \'Be a Diligent, Respectful, and Caring Steward\'"'
    ),
    (
        "Explanation: Need: listen to people needs. Option A (Work to understand the key stakeholder's concerns and provide feedback in regular project status reports) fixes it.\"",
        'Explanation: Keywords: key stakeholder, site interruptions, status reports, stakeholder engagement. A stakeholder who is physically present and interrupting the team is signaling unmet information needs. Understanding what concerns are driving their behavior and addressing those concerns through regular status reports provides a structured channel that keeps the stakeholder informed without requiring them to seek information directly from the team. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option D (Inform the client of the problem and follow the change request process) fixes it."',
        'Explanation: Keywords: ERP design flaw, approved design, client notification, change request process. A flaw in an already-approved design is a significant event that the client must know about — not something the project team can quietly resolve internally. Informing the client and following the change request process ensures transparency, maintains trust, and keeps any design revision within the formal approval structure. (PMBOK Guide) – Seventh Edition, 2021, p. 50, \'Enable Change to Achieve the Envisioned Future State\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option B (Offer guidance and follow up with some developmental activity for the junior team member) fixes it."',
        'Explanation: Keywords: junior team member, risk mitigation guidance, coaching, development opportunity. A junior team member seeking direction is both a project need and a growth opportunity. Providing guidance addresses the immediate question, while following up with developmental activity builds the team member\'s capability for future situations — which is the PM\'s responsibility as a servant leader invested in team growth. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option C (Emotional intelligence training) fixes it."',
        'Explanation: Keywords: difficult stakeholder, team impact, emotional intelligence training, interpersonal resilience. A stakeholder with a pattern of anger and unreasonable behavior is a persistent environmental challenge. Emotional intelligence training equips the team with the self-awareness, empathy, and self-regulation skills to engage with difficult personalities without absorbing the emotional damage — keeping team performance and morale intact. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option D (Analyze the requirements that will need to be addressed under the requested method) fixes it."',
        'Explanation: Keywords: methodology change request, regulatory requirements, agile adoption, requirements analysis. Before committing to a methodology change, the PM must understand what the shift actually involves for this project. Analyzing which requirements would need to be addressed differently under agile provides the factual basis to evaluate whether the approach change is warranted and how it would affect delivery. (PMBOK Guide) – Seventh Edition, 2021, p. 40, \'Tailor Based on Context\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option C (• Work with the client on an acceptable amount of time for document approval) fixes it."',
        'Explanation: Keywords: lessons learned, client approval delays, turnaround time negotiation, kickoff meeting. Historical patterns of behavior are the most reliable predictor of future behavior. Using the kickoff meeting to jointly define an acceptable document approval timeline converts a known risk — backed by prior experience — into a mutually agreed standard, giving the PM a documented basis to hold the client accountable going forward. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option B (Perform a brainstorming session to address the issue and add the solution to the sprint.) fixes it."',
        'Explanation: Keywords: daily standup, technical impediment, brainstorming, sprint integration. A technical impediment surfaced in the standup needs an immediate collaborative response — not escalation or deferral to the next sprint. A brainstorming session engages the team\'s collective knowledge to solve the problem, and incorporating the solution into the current sprint keeps delivery on track without breaking the team\'s commitment. (PMBOK Guide) – Seventh Edition, 2021, p. 28, p. 29, \'Create a Collaborative Team Environment\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option C (Escalate the issue to the sponsor and debrief them about the situation) fixes it."',
        'Explanation: Keywords: resource shortage, approaching deadline, new project manager, sponsor escalation. A looming deadline miss caused by a resource gap is a significant issue that the sponsor must be aware of — it may require decisions that only the sponsor can authorize. Escalating with a clear debrief gives the sponsor the information they need to act before the miss becomes unavoidable. (PMBOK Guide) – Seventh Edition, 2021, p. 25, \'Be a Diligent, Respectful, and Caring Steward\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option B (Support the decisions of the team and transfer the decision making responsibility to them.) fixes it."',
        'Explanation: Keywords: experienced team, decision-making authority, servant leadership, team empowerment. When a reliable, experienced team demonstrates readiness and willingness to take on decisions the PM previously held, transferring that authority is the right leadership response. Supporting their decisions and delegating responsibility accelerates team development and frees the PM to focus on higher-level project concerns. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option B (Review the project backlog looking for high-priority items and come up with a minimum viable product (MVP) that fits the expected timeline) fixes it."',
        'Explanation: Keywords: aggressive timeline, compressed plan, MVP definition, backlog prioritization. When the full plan cannot fit the new timeline, the PM must identify which subset of deliverables provides enough value to justify launch. Reviewing the backlog for the highest-priority items and defining an MVP for the compressed timeline transforms an impossible request into a focused, deliverable outcome. (PMBOK Guide) – Seventh Edition, 2021, p. 32, \'Focus on Value\'"'
    ),
    (
        'Explanation: Need: keep plans flexible. Option A (Plan a working session focusing on the scope, vision, and mission of the initiative) fixes it."',
        'Explanation: Keywords: new line of business, R&D project, scope alignment, working session. A project that introduces a new line of business requires shared clarity on what it is trying to accomplish before planning can begin. A working session focused on scope, vision, and mission ensures all participants have a unified understanding of the initiative\'s purpose — the foundation everything else is built on. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    (
        "Explanation: Need: listen to people needs. Option A (Support the product owner's decision and seek better alignment with this stakeholder in order to avoid this type of issue in the future) fixes it.\"",
        'Explanation: Keywords: MVP launch, missing features, product owner authority, stakeholder alignment. In agile delivery, the product owner holds the authority to decide when a product is ready for release. The PM\'s role is to support that decision and use the disagreement as a signal that the marketing VP needs to be more closely involved in backlog prioritization — so future release decisions are not surprises. (PMBOK Guide) – Seventh Edition, 2021, p. 40, \'Tailor Based on Context\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option B (Train the executives on agile practices) fixes it."',
        'Explanation: Keywords: agile transformation, executive resistance, process conflicts, executive training. When executives resist agile practices because they do not understand them, the conflict is rooted in a knowledge gap rather than genuine disagreement with the outcomes. Training executives on agile practices builds the shared vocabulary and understanding needed for them to engage constructively with the team rather than defaulting to familiar predictive controls. (PMBOK Guide) – Seventh Edition, 2021, p. 48, \'Embrace Adaptability and Resiliency\'"'
    ),
    (
        'Explanation: Need: keep plans flexible. Option D (Update the resource management plan and resource allocation chart accordingly) fixes it."',
        'Explanation: Keywords: key resource unavailable, schedule impact, resource management plan, resource allocation. Any change in resource availability must be captured in the resource management plan and reflected in the allocation chart before any other response is planned. These documents define how resources are planned and tracked — an unrecorded change creates invisible risk and leaves the team working from an inaccurate picture of what is available. (PMBOK Guide) – Seventh Edition, 2021, p. 34, \'Recognize, Evaluate, and Respond to System Interactions\'"'
    ),
    (
        "Explanation: Need: watch risks early. Option B (Assessed the change's overall impact to the project before submission) fixes it.\"",
        'Explanation: Keywords: change request rejection, CCB, SME resistance, impact assessment. A change request that goes to the CCB without a thorough impact assessment is unlikely to be approved — and rejection with no preceding analysis leaves the requestor with no path to reconsideration. Assessing the full impact before submission gives both the CCB the information it needs to approve and the requestor a documented case to support their argument. (PMBOK Guide) – Seventh Edition, 2021, p. 50, \'Enable Change to Achieve the Envisioned Future State\'"'
    ),
    (
        "Explanation: Need: keep plans flexible. Option A (Make a change request regarding the project's scope to ensure compliance.) fixes it.\"",
        'Explanation: Keywords: new regulation, iterative project, compliance, change request. When a regulation is enacted mid-project that affects scope, the PM cannot simply adapt internally — the scope change must go through formal change control. A change request ensures the compliance requirement is officially recognized, its impact is assessed, and the project baseline is updated to reflect the new legal obligation. (PMBOK Guide) – Seventh Edition, 2021, p. 50, \'Enable Change to Achieve the Envisioned Future State\'"'
    ),
    (
        "Explanation: Need: listen to people needs. Option C (Explain that a project charter is necessary to ensure agreement on scope and deliverables and to define the project manager's responsibilities) fixes it.\"",
        'Explanation: Keywords: project charter, sponsor resistance, small project, PM authority. The project charter is not bureaucratic overhead — it formally authorizes the project, establishes the PM\'s authority, and ensures all parties have agreed on scope and deliverables. Without it, the PM has no formal mandate to lead the project, and scope disputes have no baseline to reference. (PMBOK Guide) – Seventh Edition, 2021, p. 25, \'Be a Diligent, Respectful, and Caring Steward\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option A (Work with the team to decompose the scope into a WBS and work packages in order to create required deliverables and timelines.) fixes it."',
        'Explanation: Keywords: iterative delivery, scope statement, WBS decomposition, team understanding. A scope statement defines what the project will produce; a WBS with work packages translates that scope into actionable tasks the team can plan and execute. Working with the team to decompose it collaboratively ensures the decomposition reflects realistic effort estimates and builds team ownership of the work ahead. (PMBOK Guide) – Seventh Edition, 2021, p. 28, p. 29, \'Create a Collaborative Team Environment\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option C (Ask the SMEs to share the knowledge transfer documents with all other members by placing the documents in the project management information system (PMIS)) fixes it."',
        'Explanation: Keywords: knowledge transfer, process deviations, PMIS, information sharing. Knowledge captured in the field has no value if it remains siloed in the individuals who captured it. Placing the knowledge transfer documents in the PMIS makes them accessible to the entire team simultaneously — ensuring that lessons from the client site inform everyone\'s work, not just the SMEs who were present. (PMBOK Guide) – Seventh Edition, 2021, p. 25, \'Be a Diligent, Respectful, and Caring Steward\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option B (Update the communications management plan based on the product owner’spreferences and distribute to the team) fixes it."',
        'Explanation: Keywords: communication tool preference, product owner, communications management plan, tool alignment. The communications management plan governs which tools and channels the team uses — and the product owner\'s preference for an approved tool is a legitimate input to that plan. Updating the plan formalizes the change and distributes it to the team, ensuring everyone communicates through the same agreed channel. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option B (Review the latest project status report and update the stakeholders) fixes it."',
        'Explanation: Keywords: stakeholder change, project closure, status report, transition management. A new customer PM arriving at the final stage will not have the history or context of the project. Reviewing the latest status report and updating all stakeholders — including the new PM — ensures that the transition does not create an information gap that delays acceptance or closure activities. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option A (Weekly colocated meetings with the relevant stakeholders) fixes it."',
        'Explanation: Keywords: hybrid project, operational environment, schedule coordination, collocated meetings. A hybrid project running while the plant is still operating creates coordination risks between the software and hardware workstreams. Weekly collocated meetings bring all relevant stakeholders together to synchronize progress, catch conflicts before they impact the operating environment, and maintain schedule alignment between the parallel delivery approaches. (PMBOK Guide) – Seventh Edition, 2021, p. 34, \'Recognize, Evaluate, and Respond to System Interactions\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option C (Review the requirements traceability matrix with the concerned stakeholder) fixes it."',
        'Explanation: Keywords: stakeholder concern, missing requirement, requirements traceability matrix, deliverables review. A concern that a requirement will not be addressed is best resolved by tracing that requirement through the traceability matrix — which links requirements to deliverables and confirms whether each is covered. Reviewing it with the concerned stakeholder either resolves the misunderstanding or confirms a genuine gap that needs to be addressed. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option A (Review the set of responsibilities with the team member) fixes it."',
        'Explanation: Keywords: recurring team conflict, meeting disruption, role clarity, responsibilities review. A persistent conflict with a specific team member at every meeting often signals underlying role ambiguity — the team member may be unclear about their boundaries or feel their contributions are being overlooked. Reviewing responsibilities together creates shared clarity that addresses the structural root cause rather than just managing the conflict symptoms. (PMBOK Guide) – Seventh Edition, 2021, p. 28, p. 29, \'Create a Collaborative Team Environment\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option D (Allow the team to self-organize and have them analyze the situation in their retrospective session and self correct) fixes it."',
        'Explanation: Keywords: team boredom, agile practices fatigue, self-organization, retrospective. When a performing team grows bored with routine practices, the retrospective is the designed mechanism to surface and address that dissatisfaction. Allowing the team to self-organize and diagnose the situation themselves respects their maturity and gives them genuine ownership over improving their own working environment. (PMBOK Guide) – Seventh Edition, 2021, p. 28, p. 29, \'Create a Collaborative Team Environment\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option B (Daily standup meetings were not held or enforced) fixes it."',
        'Explanation: Keywords: Scrum, first sprint, communication gap, daily standup. Daily standups are the primary synchronization mechanism in Scrum — they are the moment when team members align on progress, share blockers, and coordinate work. When team members fall out of sync mid-sprint, the most likely cause is that this synchronization ceremony was skipped or inconsistently applied. (PMBOK Guide) – Seventh Edition, 2021, p. 40, \'Tailor Based on Context\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option A (Communicate directly with the director and inform them of the communications management plan) fixes it."',
        'Explanation: Keywords: director-client direct communication, scope changes, communications management plan, governance. The communications management plan defines who has authority to communicate what to the client — including scope changes. Informing the director of this plan establishes the governance boundary directly with the person crossing it, which is more effective and respectful than escalating or redirecting the client unilaterally. (PMBOK Guide) – Seventh Edition, 2021, p. 34, \'Recognize, Evaluate, and Respond to System Interactions\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Options A and E (A lot of discussions that yield no results or possibly too many results; A focus on the negative and a disinterest in further improvements) work together."',
        'Explanation: Keywords: retrospective compression, insufficient preparation, unfocused discussions, team engagement. Reducing retrospective preparation and discussion time removes the structure that makes retrospectives productive. Without adequate time, discussions either fragment into too many unresolved topics or collapse into surface-level complaints — neither leading to actionable improvements, which erodes team confidence in the ceremony over time. (PMBOK Guide) – Seventh Edition, 2021, p. 48, \'Embrace Adaptability and Resiliency\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option C (Work with the stakeholder to understand what the concerns are while at the same time conveying the benefits of incremental deliveries) fixes it."',
        'Explanation: Keywords: incremental delivery resistance, experienced stakeholder, business value, stakeholder education. A senior stakeholder who resists incremental delivery likely has legitimate concerns — perhaps about customer readiness or operational disruption. Understanding those concerns before advocating for the incremental approach demonstrates respect for their experience while ensuring the PM can address the specific objections rather than delivering a generic defense of agile delivery. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option B (Because there are different perspectives perform a stakeholder analysis and act based on the outcome.) fixes it."',
        'Explanation: Keywords: matrix organization, multiple stakeholders, competing perspectives, stakeholder analysis. A matrix organization creates multiple lines of authority and differing stakeholder interests. Rather than defaulting to any one perspective, a stakeholder analysis maps who has influence, what they need, and how they are interconnected — providing a structured basis for deciding how to balance their competing expectations. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option B (Use lessons learned from the previous project as a guide for the current project\'s stakeholder register) fixes it."',
        'Explanation: Keywords: similar project, stakeholder analysis, lessons learned, historical reference. A recently completed similar project provides the most directly applicable reference point for stakeholder identification. Lessons learned from that project capture who was engaged, what worked, and what caused friction — serving as a practical starting point for the current project\'s stakeholder register rather than building it from scratch. (PMBOK Guide) – Seventh Edition, 2021, p. 25, \'Be a Diligent, Respectful, and Caring Steward\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option A (Ensure that the impediments are captured and prioritized based upon the highest valued features) fixes it."',
        'Explanation: Keywords: product backlog, team impediments, impediment prioritization, high-value features. Impediments that block the highest-value backlog items have the greatest impact on delivery — resolving them first maximizes the value the team can actually deliver. Capturing and prioritizing impediments against feature value ensures effort goes toward removing the obstacles with the most significant business consequence. (PMBOK Guide) – Seventh Edition, 2021, p. 32, \'Focus on Value\'"'
    ),
    (
        'Explanation: Need: keep plans flexible. Option B (Negotiate a contract and form a partnership with a local authority for medical and security support services.) fixes it."',
        'Explanation: Keywords: high-risk location, employee safety, health training, local authority partnership. When a project operates in a dangerous environment, safety cannot be managed with internal resources alone. Partnering with a local authority for medical and security services provides the specialized expertise and on-ground presence that only organizations embedded in that environment can offer — making it the most reliable safeguard for employee safety. (PMBOK Guide) – Seventh Edition, 2021, p. 25, \'Be a Diligent, Respectful, and Caring Steward\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option D (Perform Integrated Change Control) fixes it."',
        'Explanation: Keywords: vendor resource absence, alternative solution, cost impact, integrated change control. When an alternative solution introduces additional cost, the change must be formally evaluated and approved before being implemented — regardless of the project\'s current budget position. Integrated change control ensures the cost impact is assessed holistically across all project constraints before the decision to proceed is made. (PMBOK Guide) – Seventh Edition, 2021, p. 50, \'Enable Change to Achieve the Envisioned Future State\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option D (Implement a reward system aimed to keep the team engaged and motivated) fixes it."',
        'Explanation: Keywords: agile team motivation, new project manager, reward system, team engagement. Motivation in an agile context requires ongoing investment, not one-time interventions. A structured reward system creates consistent recognition for achievement, builds team morale over the project\'s duration, and signals to the team that their contributions are seen and valued by the PM. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    (
        'Explanation: Need: keep plans flexible. Option C (The updated project management plan) fixes it."',
        'Explanation: Keywords: strategic alignment, resource question, project management plan, organizational strategy. The project management plan documents the project\'s objectives, scope, and how it connects to the organization\'s strategy. Sharing the updated plan gives the key resource the comprehensive view they need to understand both what the project is delivering and why it matters to the organization. (PMBOK Guide) – Seventh Edition, 2021, p. 25, \'Be a Diligent, Respectful, and Caring Steward\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option D (Schedule meetings with key stakeholders to build the agile project charter and set clear expectations for the project) fixes it."',
        'Explanation: Keywords: agile project charter, scope creep, definition of done, clear expectations. When projects struggle because objectives and completion criteria were never clearly defined, the solution is to establish them before work begins. An agile project charter created collaboratively with key stakeholders sets shared expectations for objectives, scope boundaries, and what done looks like — the foundation that prevents scope creep from taking hold. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option A (Keep the stakeholder informed and consult with them based on their needs) fixes it."',
        'Explanation: Keywords: board director sponsor, low engagement, multiple priorities, tailored stakeholder engagement. A board-level sponsor with competing priorities needs an engagement approach calibrated to their constraints — not standard reporting that adds to their burden. Keeping them informed and consulting on their specific needs ensures they remain connected to the project without being overwhelmed, maintaining their support without monopolizing their time. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option B (A business case and scope document) fixes it."',
        'Explanation: Keywords: multiyear initiative, planning phase, business case, scope document. Before any plan, backlog, or communication channel can be meaningful, the project must establish what it is trying to achieve and why. The business case defines the rationale and expected value, while the scope document bounds what will and will not be done — together providing the foundation that all subsequent planning documents build upon. (PMBOK Guide) – Seventh Edition, 2021, p. 25, \'Be a Diligent, Respectful, and Caring Steward\'"'
    ),
    (
        "Explanation: Need: listen to people needs. Option B (Customized stakeholder communications based on the stakeholders’ needs) fixes it.\"",
        'Explanation: Keywords: disengaged stakeholder, feature rejection, customized communications, agile engagement. A stakeholder who becomes less involved over time is not receiving the information they need in a form that works for them. Customizing communications to match their evolving availability and preferences would have maintained engagement during the sprints — making it far less likely they would reject a deliverable they had not been following closely. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option B (Meet with the team on a regular basis to ensure they are aware of changes.) fixes it."',
        'Explanation: Keywords: organizational change, change management, team awareness, regular meetings. In a change management context, information gaps and speculation are more disruptive than the changes themselves. Regular meetings ensure the project team hears changes directly from the PM — with context and opportunity to ask questions — before rumors or misinterpretations create resistance. (PMBOK Guide) – Seventh Edition, 2021, p. 50, \'Enable Change to Achieve the Envisioned Future State\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Options B, D, and E (Create a change request with the scope of the new internal projects.; Create a work breakdown structure (WBS) of the new scope with the internal projects; Manage the quality of the delivery) work together."',
        'Explanation: Keywords: internship deliverable, scope expansion, change request, WBS, quality management. Adding internal projects to satisfy an internship deliverable represents a scope change that must be formally authorized. A change request captures the expanded scope, the WBS translates it into deliverable work packages, and quality management ensures the internships meet the standards committed in the original project. (PMBOK Guide) – Seventh Edition, 2021, p. 50, \'Enable Change to Achieve the Envisioned Future State\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option B (Develop the quality management plan, as quality is as equally important as cost and schedule management.) fixes it."',
        'Explanation: Keywords: quality management plan, task simplicity argument, cost savings pressure, quality priority. Simplicity of tasks does not eliminate the need for quality management — it changes the scale of the controls, not their necessity. Quality management is a core project constraint alongside scope, cost, and schedule: skipping it to save money trades short-term savings for the risk of delivering a product that does not meet requirements. (PMBOK Guide) – Seventh Edition, 2021, p. 42, \'Build Quality into Processes and Deliverables\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option B (Determining and aligning performance indicators that will help in assessing successful delivery) fixes it."',
        'Explanation: Keywords: product revamp, successful launch, performance indicators, success measurement. Success cannot be managed without defining what it looks like. Determining and aligning performance indicators with the marketing executive and team ensures there is a shared, measurable definition of success — making it possible to track progress toward launch readiness and identify risks to the outcome before they become problems. (PMBOK Guide) – Seventh Edition, 2021, p. 32, \'Focus on Value\'"'
    ),
    (
        'Explanation: Need: keep plans flexible. Option C (Reevaluate identified risks and update the risk register) fixes it."',
        'Explanation: Keywords: risk resolution, low-level risks remaining, risk reevaluation, risk register update. Risk conditions change continuously — a low-level risk earlier in the project may have grown in likelihood or impact as the project has progressed. Reevaluating all remaining risks and updating the register ensures the team\'s risk picture reflects current reality rather than assessments made under earlier project conditions. (PMBOK Guide) – Seventh Edition, 2021, p. 46, \'Optimize Risk Responses\'"'
    ),
    (
        'Explanation: Need: keep plans flexible. Option D (Break down the requirements and prioritize the requirements into iterative work packages) fixes it."',
        'Explanation: Keywords: unclear requirements, hybrid approach, iterative work packages, requirements decomposition. Unclear requirements are an argument for iterative delivery, not a reason to wait. Breaking them into iterative work packages allows the team to begin with what is known, deliver incrementally, and use each delivery to progressively clarify what comes next — turning uncertainty from a blocker into a managed condition. (PMBOK Guide) – Seventh Edition, 2021, p. 48, \'Embrace Adaptability and Resiliency\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option B (Review the deliverable requirements, check the customer approval criteria, and proceed accordingly) fixes it."',
        'Explanation: Keywords: project closure, deliverable shortfall, customer approval criteria, requirements review. A deliverable that does not meet customer expectations at closure requires objective grounding before any decision is made. Reviewing the original requirements and approval criteria determines whether the shortfall is a genuine deviation from agreed standards or a misalignment of expectations — the answer dictates whether corrective action, negotiation, or acceptance is the right path. (PMBOK Guide) – Seventh Edition, 2021, p. 32, \'Focus on Value\'"'
    ),
    (
        'Explanation: Need: watch risks early. Option C (Adopt an iterative rollout approach that delivers the highest business value earlier) fixes it."',
        'Explanation: Keywords: high-risk transformation, product development, iterative rollout, early business value. For a high-risk initiative where success is critical, an iterative rollout reduces the cost of failure by delivering value incrementally and learning from each release. Prioritizing the highest-value items first ensures that even if the transformation is not fully completed, the most important outcomes have already been realized. (PMBOK Guide) – Seventh Edition, 2021, p. 48, \'Embrace Adaptability and Resiliency\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option A (Organize regular meetings with all of the deployment teams to share issues and solutions) fixes it."',
        'Explanation: Keywords: multi-country deployment, parallel teams, siloed problem-solving, knowledge sharing. When parallel teams independently solve the same problems, the organization pays for that solution multiple times while each team carries the full risk of solving it incorrectly alone. Regular cross-team meetings convert individual problem-solving into a shared resource, letting teams build on each other\'s solutions rather than duplicating effort. (PMBOK Guide) – Seventh Edition, 2021, p. 28, p. 29, \'Create a Collaborative Team Environment\'"'
    ),
    (
        'Explanation: Need: keep plans flexible. Option C (Conduct periodical reviews of the project plans, objectives, and deliverables to ensure all relevant data are captured to continue making informed project decisions) fixes it."',
        'Explanation: Keywords: flagship solution, agility, market adaptation, periodic review. Agility in a competitive market is not a one-time configuration — it requires continuous validation that plans, objectives, and deliverables remain aligned with market conditions. Periodic reviews create the feedback loop that keeps the project\'s direction current as the environment around it changes, enabling timely course corrections before gaps become significant. (PMBOK Guide) – Seventh Edition, 2021, p. 44, \'Navigate Complexity\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option D (Validated each stakeholder\'s understanding during the kick-off meeting) fixes it."',
        'Explanation: Keywords: global project, cultural interpretation, kickoff meeting, understanding validation. Approval does not guarantee comprehension — especially across cultures and languages where the same document can be interpreted differently. Validating each stakeholder\'s understanding during the kickoff meeting converts passive approval into active confirmation, surfacing misinterpretations before they are built into the plan. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option B (Send an email to the project sponsor summarizing the project status and key concerns, and request an immediate face-to-face meeting to discuss them) fixes it."',
        'Explanation: Keywords: new sponsor, project issues, delivery impact, urgent escalation. A new sponsor who has not yet engaged with the PM cannot fully understand the urgency from a status report alone. An email summary establishes the context and severity of concerns, while requesting an immediate face-to-face meeting creates the direct conversation needed to get the sponsor fully briefed and engaged before issues worsen. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option D (Review conflicts during daily Scrum so they are handled in a timely manner) fixes it."',
        'Explanation: Keywords: Scrum master, team conflict, daily Scrum, timely resolution. Conflicts that are not surfaced quickly tend to compound. Reviewing conflicts during the daily Scrum makes conflict resolution a regular, structured part of team rhythm — ensuring that interpersonal friction is identified and addressed while it is still manageable rather than allowed to fester between formal retrospectives. (PMBOK Guide) – Seventh Edition, 2021, p. 28, p. 29, \'Create a Collaborative Team Environment\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option D (Coach the team both as a whole and individually) fixes it."',
        'Explanation: Keywords: new agile team, iteration failures, team conflict, dual-level coaching. A new team struggling on two fronts — delivery and interpersonal conflict — needs coaching at both levels simultaneously. Team-level coaching builds shared practices and norms, while individual coaching addresses the specific behaviours or skills gaps that are driving conflict and blocking commitment fulfillment. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option C (Context diagram) fixes it."',
        'Explanation: Keywords: KPI dispute, stakeholder disagreement, context diagram, shared understanding. When a stakeholder rejects performance results, the disagreement often stems from a different understanding of what the project is measuring and why. A context diagram makes the project\'s scope boundaries, inputs, and outputs explicit — creating a shared visual reference that can clarify whether the KPIs actually capture what the stakeholder believes they should be measuring. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option A (Modify the communications management plan to account for regional differences) fixes it."',
        'Explanation: Keywords: distributed team, time zones, languages, communications management plan. A communications management plan designed for a single-location team will not accommodate the complexities of a globally distributed one. Modifying it to account for regional differences — different time zones, preferred languages, and cultural communication norms — prevents the miscommunication and missed messages that most commonly derail virtual teams. (PMBOK Guide) – Seventh Edition, 2021, p. 34, \'Recognize, Evaluate, and Respond to System Interactions\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Options B, D, and E (Security and performance testing; Story testing; Tests based on behavior and test-driven development) work together."',
        'Explanation: Keywords: multiple agile teams, business model change, testing mechanisms, behavior-driven development. Comprehensive testing in a complex multi-team agile context requires approaches that address different layers of quality. Security and performance testing validates the system\'s non-functional robustness, story testing confirms user stories meet their acceptance criteria, and behavior-driven and test-driven development embeds quality verification directly into the development process. (PMBOK Guide) – Seventh Edition, 2021, p. 42, \'Build Quality into Processes and Deliverables\'"'
    ),
    (
        'Explanation: Need: keep plans flexible. Option A (Update project documents to include adaptive tools and artifacts and plan the first iterative session) fixes it."',
        'Explanation: Keywords: adaptive tools, design phase, proven effectiveness, incremental adoption. When adaptive tools have already demonstrated value in similar projects within the organization, the first step is to update the project documents to reflect their inclusion and plan the inaugural iterative session. Formalizing the adoption before beginning ensures the team works within an updated, shared framework rather than introducing the tools informally mid-stream. (PMBOK Guide) – Seventh Edition, 2021, p. 40, \'Tailor Based on Context\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option B (Meet with the project team to analyze the actual cost to determine deviations) fixes it."',
        'Explanation: Keywords: cost baseline overrun trend, budget management, actual cost analysis, deviation identification. Before the PM can respond to a cost trend, they must understand its source. Meeting with the team to analyze actual costs against the baseline identifies where and why deviations are occurring — the prerequisite to any targeted corrective action that can bring the budget back on track. (PMBOK Guide) – Seventh Edition, 2021, p. 32, \'Focus on Value\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option A (Identify the problem\'s root causes and define the ground rules with all project team members to minimize interferences) fixes it."',
        'Explanation: Keywords: iteration interruptions, external team requests, root cause, ground rules. Repeated interruptions from other teams during iterations are a systemic problem — not a one-off inconvenience. Identifying the root causes of the interference and establishing ground rules with all team members creates the structural boundaries needed to protect the team\'s capacity and maintain iteration commitments. (PMBOK Guide) – Seventh Edition, 2021, p. 28, p. 29, \'Create a Collaborative Team Environment\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option C (Ensure that both managers understand the requirements and search for a solution that best satisfies this deliverable) fixes it."',
        'Explanation: Keywords: functional manager conflict, contradictory requirements, consensus building, collaborative resolution. When two managers with contradictory requirements both refuse to meet, the PM must facilitate a session that focuses on the deliverable\'s purpose rather than each manager\'s position. Ensuring both understand the full requirement set and searching for a jointly satisfying solution is more likely to produce a workable outcome than choosing sides. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option B (Ask the client to verify and accept the tasks that have been completed) fixes it."',
        'Explanation: Keywords: project closure, completed tasks, client verification, formal acceptance. Deliverables are not complete until the client has verified and formally accepted them. Requesting client verification before closing out tasks ensures the acceptance process is followed correctly — preventing disputes at final closure about whether specific deliverables were properly handed over. (PMBOK Guide) – Seventh Edition, 2021, p. 32, \'Focus on Value\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option C (Schedule a meeting with the product owner and finance team to agree on course corrections) fixes it."',
        'Explanation: Keywords: finance team excluded, business case, ROI rejection, course correction. A finance team that was not involved in building the business case has no ownership of its assumptions and no reason to approve the ROI. Bringing the product owner and finance team together creates the shared accountability needed to agree on how the project must adjust to produce results both parties can support. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
]

updated = 0
failed = []

for old, new in replacements:
    if old in content:
        content = content.replace(old, new)
        updated += 1
    else:
        failed.append(old[:70])

with open(MD_FILE, 'w', encoding='utf-8') as f:
    f.write(content)

print(f'Done: {updated} updated, {len(failed)} failed.')
for s in failed:
    print(f'  NOT FOUND: {s!r}')
