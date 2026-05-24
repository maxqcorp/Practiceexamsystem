MD_FILE = './src/imports/project-management-questions-1.md'

with open(MD_FILE, 'r', encoding='utf-8') as f:
    content = f.read()

replacements = [
    # Q1243
    (
        'Explanation: Need: guide and calm the team. Option C (Review the process and remove the impediment.) fixes it."',
        'Explanation: Keywords: servant leader, certification delay, impediment removal, agile process. When a deliverable is blocked by another team\'s inaction, the servant leader\'s role is to review the process that is creating the bottleneck and actively work to remove it. Waiting indefinitely or escalating alone does not resolve the systemic issue — the impediment itself must be addressed to restore delivery flow. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    # Q1244
    (
        'Explanation: Need: listen to people needs. Option D (Move working windows so that team members can have increased overlap for the handover of status and issues to their counterparts.) fixes it."',
        'Explanation: Keywords: follow-the-sun, global team, handover issues, communication overlap. In a follow-the-sun delivery model, quality issues often stem from insufficient overlap time between shifts for effective handover of status and open issues. Adjusting working windows to increase the overlap period gives team members in different locations more time to communicate directly, reducing the information gaps that caused the post-release issues. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    # Q1245
    (
        'Explanation: Need: listen to people needs. Option A (Stakeholders who have been identified and who have needs and a potential impact on the project.) fixes it."',
        'Explanation: Keywords: stakeholder engagement plan, stakeholder identification, potential impact, inclusive approach. The stakeholder engagement plan must cover all identified stakeholders who have needs or can affect the project — not just those who are supportive or selected by the sponsor. Including stakeholders who disagree, as well as those who support the project, ensures that the full range of interests and influences is managed proactively. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    # Q1246
    (
        'Explanation: Need: guide and calm the team. Option D (Include compliance within the development tools.) fixes it."',
        'Explanation: Keywords: regulatory compliance, compliance adherence, development tools, embedded quality. The most effective way to ensure continuous compliance adherence is to embed compliance checks directly into the development tools and processes used by the team. This approach makes compliance a natural part of the workflow rather than a separate activity, reducing the risk of violations being discovered late. (PMBOK Guide) – Seventh Edition, 2021, p. 42, \'Build Quality into Processes and Deliverables\'"'
    ),
    # Q1247
    (
        'Explanation: Need: guide and calm the team. Option A (Seek help from experts to support the team member in fixing the problem.) fixes it."',
        'Explanation: Keywords: technical impediment, team member frustration, expert support, schedule risk. When a team member is stuck on a technical problem and reassigning the task would cause frustration, the project manager can resolve both the schedule risk and the interpersonal concern by bringing in expert help to support the team member. This approach keeps the team member engaged and productive while addressing the delay. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    # Q1248
    (
        'Explanation: Need: listen to people needs. Option C (Set the project\'s purpose, mission, and vision.) fixes it."',
        'Explanation: Keywords: hybrid project, organizational transformation, purpose, mission, vision. Before launching a hybrid project for organizational transformation, the project manager must establish a clear purpose, mission, and vision to align the team and stakeholders around a shared direction. This foundational step ensures that all subsequent planning and delivery decisions are anchored in a coherent strategic intent. (PMBOK Guide) – Seventh Edition, 2021, p. 32, \'Focus on Value\'"'
    ),
    # Q1249
    (
        'Explanation: Need: listen to people needs. Option D (Program managers) fixes it."',
        'Explanation: Keywords: program management, cross-organizational project, interdependencies, shared resources. When a project is part of a larger program and shares resources with other projects across multiple business units, the program manager holds the broadest view of interdependencies and resource conflicts. Consulting the program manager first ensures that cross-project dependencies are managed at the correct governance level before engaging individual stakeholders. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    # Q1250
    (
        'Explanation: Need: guide and calm the team. Option C (Organize a meeting with the project team and discuss the situation and its impact on project delivery.) fixes it."',
        'Explanation: Keywords: team lead conflict, experienced engineer, team dynamics, delivery impact. When an experienced team member challenges the authority of a newly promoted lead and disrupts team functioning, addressing the situation at the team level is more effective than managing it bilaterally. Organizing a team meeting to discuss the situation and its impact on delivery brings the issue into the open, reinforces collective accountability, and allows the team to agree on how to proceed. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    # Q1251
    (
        'Explanation: Need: listen to people needs. Option A (Finish to start) fixes it."',
        'Explanation: Keywords: activity sequencing, dependency type, finish-to-start, schedule logic. A finish-to-start dependency means that the predecessor activity must finish before the successor can begin. When a product must be tested before it is released to the customer, testing must be completed (finish) before the release activity can start (start), making finish-to-start the correct dependency type to capture this relationship. (PMBOK Guide) – Seventh Edition, 2021, p. 34, \'Recognize, Evaluate, and Respond to System Interactions\'"'
    ),
    # Q1252
    (
        'Explanation: Need: guide and calm the team. Option A (Meet with the functional managers to align the expected frequency and results reporting for the team members.) fixes it."',
        'Explanation: Keywords: performance plan alignment, functional managers, matrix organization, project contribution. When team members are concerned that their project work is not reflected in their individual performance plans, the project manager must coordinate with functional managers to align how project contributions will be documented and reported. This ensures that team members\' efforts are recognized appropriately within the organization\'s performance framework. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    # Q1253
    (
        'Explanation: Need: guide and calm the team. Option C (Coach team members to increase their engagement and collaboration) fixes it."',
        'Explanation: Keywords: servant leader, remote work, agile transition, team engagement. As a servant leader managing an agile transition in a remote setting, the project manager\'s role is to create the conditions for the team to thrive — not to impose compliance. When team members show declining commitment, coaching them to improve their own engagement and collaboration builds intrinsic motivation and sustainable team performance. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    # Q1254
    (
        'Explanation: Need: guide and calm the team. Option B (Ask the PMO to review the framework) fixes it."',
        'Explanation: Keywords: PMO framework, agile incompatibility, team motivation, organizational alignment. When a PMO framework is incompatible with agile delivery and is demotivating the project team, the project manager should escalate the issue to the PMO for review rather than working around or ignoring the framework. Requesting a review opens a formal dialogue that can lead to a framework adaptation, demonstrating respect for organizational structures while advocating for the team\'s needs. (PMBOK Guide) – Seventh Edition, 2021, p. 40, \'Tailor Based on Context\'"'
    ),
    # Q1255
    (
        'Explanation: Need: keep plans flexible. Option B (Suggest that each project develops a high-level plan to monitor the dependencies) fixes it."',
        'Explanation: Keywords: program dependencies, agile project, dependency management, high-level planning. In a program with multiple interconnected agile projects, managing dependencies requires at least a high-level plan that makes cross-project milestones and dependencies visible to all teams. A high-level plan for each project enables program-level coordination without imposing detailed predictive planning that would undermine agile flexibility. (PMBOK Guide) – Seventh Edition, 2021, p. 40, \'Tailor Based on Context\'"'
    ),
    # Q1256
    (
        'Explanation: Need: guide and calm the team. Option D (Make changes to reprioritize the backlog because of the obstacle.) fixes it."',
        'Explanation: Keywords: backlog blocker, obstacle prioritization, agile impediment, backlog management. When a blocker is preventing progress on specific backlog items, the project manager should reprioritize the backlog to allow the team to deliver value through other items while the obstacle is being addressed. This approach keeps the team productive and prevents the blocker from halting all project momentum. (PMBOK Guide) – Seventh Edition, 2021, p. 32, \'Focus on Value\'"'
    ),
    # Q1257
    (
        'Explanation: Need: listen to people needs. Option C (Request further clarification of the requirement) fixes it."',
        'Explanation: Keywords: unclear requirement, schedule impact, clarification, stakeholder communication. When a requirement is ambiguous and its potential schedule impact is uncertain, the project manager must seek clarity before analyzing risk or proceeding with design. Requesting further clarification from the stakeholder who raised the requirement ensures that the project responds to the actual need rather than assumptions that may lead to wasted effort. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    # Q1258
    (
        'Explanation: Need: control changes and baselines. Option C (Obtain approval to proceed with the feasibility study as a parallel activity while the prefeasibility study is approved) fixes it."',
        'Explanation: Keywords: parallel activities, schedule compression, approval governance, feasibility study. When timelines are critical and activities must proceed before full approval, the project manager should seek explicit authorization to run the feasibility study in parallel as a controlled exception. Obtaining approval for the parallel activity through proper governance channels ensures the work is sanctioned without bypassing the organization\'s control processes. (PMBOK Guide) – Seventh Edition, 2021, p. 25, \'Be a Diligent, Respectful, and Caring Steward\'"'
    ),
    # Q1259 - Note: Q1260 is missing from the file (skip)
    (
        'Explanation: Need: guide and calm the team. Option D (Continue with the sprint work as planned and keep monitoring.) fixes it."',
        'Explanation: Keywords: burndown chart, sprint day four, monitoring, normal progress. When a burndown chart on day four of a sprint shows progress that is still within expected parameters and provides buffers for potential interruptions, the appropriate action is to continue with the planned work and maintain monitoring. Disrupting a sprint based on early, inconclusive data creates unnecessary instability and undermines the team\'s delivery rhythm. (PMBOK Guide) – Seventh Edition, 2021, p. 34, \'Recognize, Evaluate, and Respond to System Interactions\'"'
    ),
    # Q1261
    (
        'Explanation: Need: keep plans flexible. Option C (Review the backlog and find opportunities to reprioritize the work and reduce the project scope) fixes it."',
        'Explanation: Keywords: budget exhaustion, agile project, backlog reprioritization, scope reduction. When budget is nearly depleted and significant work remains, adding more budget or accelerating the schedule are rarely viable options. The appropriate response is to review the backlog and reprioritize, ensuring that remaining budget is spent on the highest-value items and that the project delivers the maximum possible value within its financial constraints. (PMBOK Guide) – Seventh Edition, 2021, p. 32, \'Focus on Value\'"'
    ),
    # Q1262
    (
        'Explanation: Need: guide and calm the team. Option D (Meet with the data suppliers to explain the critical timing requirements of the project.) fixes it."',
        'Explanation: Keywords: data acquisition, supplier communication, schedule constraint, critical timing. When the project is stalled because required data is not being delivered by suppliers, the most direct path to resolution is to meet with the data suppliers and explain the project\'s critical timing requirements. Making the urgency explicit helps suppliers prioritize the request appropriately and understand the project consequences of further delay. (PMBOK Guide) – Seventh Edition, 2021, p. 34, \'Recognize, Evaluate, and Respond to System Interactions\'"'
    ),
    # Q1263
    (
        'Explanation: Need: keep plans flexible. Option C (Comply with the regulatory requirements and work to compress the project schedule.) fixes it."',
        'Explanation: Keywords: regulatory compliance, market demand, schedule compression, product launch. When a company is eager to launch a new product but regulatory approval is mandatory, the project manager cannot bypass or shortcut the approval process. The appropriate response is to fully comply with regulatory requirements while actively exploring schedule compression techniques to reduce the overall time to market as much as possible within those constraints. (PMBOK Guide) – Seventh Edition, 2021, p. 25, \'Be a Diligent, Respectful, and Caring Steward\'"'
    ),
    # Q1264
    (
        'Explanation: Need: keep plans flexible. Option A (Sprint plan and product roadmap) fixes it."',
        'Explanation: Keywords: Scrum framework, traditional artifacts, project schedule equivalent, sprint plan, product roadmap. In the Scrum framework, the project schedule is replaced by a combination of the sprint plan — which defines the detailed work for the current iteration — and the product roadmap — which provides the longer-term view of what will be delivered and when. Together, these artifacts provide the planning transparency that the traditional project schedule was designed to support. (PMBOK Guide) – Seventh Edition, 2021, p. 40, \'Tailor Based on Context\'"'
    ),
    # Q1265
    (
        'Explanation: Need: listen to people needs. Option B (Plan regular virtual meetings to motivate and support the team.) fixes it."',
        'Explanation: Keywords: virtual team, global project, team commitment, regular meetings. When a globally distributed team works independently with minimal in-person interaction, the risk is that individual performance remains acceptable while team cohesion and commitment deteriorate. Planning regular virtual meetings creates touchpoints that reinforce shared purpose, address concerns, and maintain the human connection essential for sustained team engagement. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    # Q1266
    (
        'Explanation: Need: guide and calm the team. Option C (Coordinate a one-to-one meeting with the specialist to assess the situation.) fixes it."',
        'Explanation: Keywords: new team member, average feedback, compliance specialist, one-on-one assessment. When a new team member receives average feedback from the team, the project manager\'s first step is to meet directly with that team member to understand their perspective, identify any specific gaps or obstacles, and agree on a path for improvement. A private conversation provides a more accurate picture of the situation than secondhand feedback alone. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    # Q1267
    (
        'Explanation: Need: guide and calm the team. Option A (Captured and reviewed all of the project work and related costs regularly) fixes it."',
        'Explanation: Keywords: delayed invoice, project closure, cost review, financial transparency. A delayed invoice that inflates reported completion costs indicates that costs were not being tracked and reconciled on a regular basis during execution. The project manager should have captured and reviewed all project work and related costs routinely throughout the project, enabling early detection of outstanding financial obligations before project closeout. (PMBOK Guide) – Seventh Edition, 2021, p. 25, \'Be a Diligent, Respectful, and Caring Steward\'"'
    ),
    # Q1268
    (
        'Explanation: Need: listen to people needs. Option D (Collaborate with the relevant stakeholders on implementing the risk response plan.) fixes it."',
        'Explanation: Keywords: risk materialization, issue management, risk response plan, stakeholder collaboration. When a risk transitions from the risk register to an actual issue, the response plan that was developed during risk planning should be activated. Collaborating with relevant stakeholders to implement the risk response plan ensures that the predefined mitigation actions are executed with the appropriate involvement and resources. (PMBOK Guide) – Seventh Edition, 2021, p. 46, \'Optimize Risk Responses\'"'
    ),
    # Q1269
    (
        'Explanation: Need: guide and calm the team. Option D (Facilitate a problem-solving session with the team to analyze the problem.) fixes it."',
        'Explanation: Keywords: technical problem, sprint impediment, agile team, problem-solving session. When an agile team encounters an unfamiliar technical problem during a sprint, the project manager\'s role is to facilitate a structured problem-solving session that leverages the team\'s collective expertise. This collaborative approach surfaces diverse perspectives, accelerates root cause identification, and builds the team\'s problem-solving capability for future challenges. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    # Q1270
    (
        'Explanation: Need: listen to people needs. Option C (Reviewed with the product owner that all acceptance criteria were met for the stories worked on in the iteration) fixes it."',
        'Explanation: Keywords: quality standards, stakeholder rejection, acceptance criteria, product owner review. When a stakeholder rejects deliverables at a system demo because they do not meet quality or regulatory standards, the root cause is typically a failure to validate acceptance criteria before presenting the increment. The project manager should have reviewed with the product owner that all acceptance criteria were satisfied for each story before the demo. (PMBOK Guide) – Seventh Edition, 2021, p. 42, \'Build Quality into Processes and Deliverables\'"'
    ),
    # Q1271
    (
        'Explanation: Need: listen to people needs. Option C (Organize networking sessions to allow the team members to get to know one another.) fixes it."',
        'Explanation: Keywords: team cohesion, new versus experienced members, communication gap, networking. When a newly formed team experiences communication gaps between longtime employees and new members, the underlying issue is often a lack of interpersonal connection and trust. Organizing networking sessions creates a structured environment for team members to get to know each other as individuals, which builds the relational foundation needed for effective collaboration. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    # Q1272
    (
        'Explanation: Need: keep plans flexible. Option C (Use a product backlog to manage changes.) fixes it."',
        'Explanation: Keywords: regulatory environment, change management, product backlog, visibility. A product backlog provides an adaptive, continuously prioritized list of work that can accommodate regulatory constraints and expected changes in a transparent and flexible way. It gives the PMO visibility into regulatory items while allowing the team to reprioritize in response to a changing regulatory landscape without the rigidity of a fixed plan. (PMBOK Guide) – Seventh Edition, 2021, p. 40, \'Tailor Based on Context\'"'
    ),
    # Q1273
    (
        'Explanation: Need: listen to people needs. Option A (Performed a stakeholder analysis when the sponsor joined the project) fixes it."',
        'Explanation: Keywords: new sponsor, stakeholder analysis, sponsor engagement, project continuity. When a project sponsor is replaced mid-project, the new sponsor arrives with no prior context, different priorities, and potentially different success criteria. Performing a stakeholder analysis at the point of the sponsor\'s arrival would have identified these gaps and enabled the project manager to proactively engage the new sponsor, building alignment before decisions were made without it. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    # Q1274
    (
        'Explanation: Need: listen to people needs. Option D (A hybrid approach will allow for management of the requirement uncertainties as well as the date restriction.) fixes it."',
        'Explanation: Keywords: hybrid approach rationale, requirement uncertainty, fixed delivery date, adaptive planning. A hybrid approach is appropriate when a project has both a fixed delivery date driven by regulatory requirements (a predictive constraint) and undefined requirements that need iterative refinement (an adaptive need). The hybrid model allows the project to manage scope uncertainty through iterative delivery while still committing to the defined regulatory deadline. (PMBOK Guide) – Seventh Edition, 2021, p. 40, \'Tailor Based on Context\'"'
    ),
    # Q1275
    (
        'Explanation: Need: listen to people needs. Option D (Train the team to first find the minimum viable product (MVP) that will deliver value to the customer.) fixes it."',
        'Explanation: Keywords: MVP, product development, expenditure overrun, customer value. When a project is too costly because the team attempts to build comprehensive functionality before validating market demand, the root cause is a failure to identify the minimum feature set that delivers real customer value. Training the team to define and build an MVP first allows the organization to test the market at lower cost and iterate based on actual customer feedback. (PMBOK Guide) – Seventh Edition, 2021, p. 32, \'Focus on Value\'"'
    ),
    # Q1276
    (
        'Explanation: Need: guide and calm the team. Option B (Ask the team member to bring up the concern in the next daily meeting.) fixes it."',
        'Explanation: Keywords: impediment, daily standup, team visibility, agile communication. The daily standup meeting exists precisely to surface impediments and schedule risks so the team can collectively address them. When a team member anticipates a delay that could block others, asking them to raise it in the next daily meeting ensures the issue is communicated transparently to the full team and can be resolved collaboratively. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    # Q1277
    (
        'Explanation: Need: listen to people needs. Option A (During the planning phase, when processes for scope definition and activity duration and sequencing will be performed) fixes it."',
        'Explanation: Keywords: milestone dates, planning phase, schedule development, initiation constraints. Providing concrete milestone dates requires completed scope definition and detailed activity sequencing, which are performed during the planning phase. Committing to specific dates during initiation — before this analysis is done — risks establishing baselines on incomplete information, leading to schedules that are unrealistic or that mislead stakeholders. (PMBOK Guide) – Seventh Edition, 2021, p. 40, \'Tailor Based on Context\'"'
    ),
    # Q1278
    (
        'Explanation: Need: listen to people needs. Option D (Add the risk to the risk register and reevaluate the register with help from the project team and stakeholders.) fixes it."',
        'Explanation: Keywords: newly identified risk, risk register, stakeholder involvement, risk reevaluation. When a new risk is identified during project execution, it must be formally added to the risk register and analyzed for its potential impact. Reevaluating the register with the project team and stakeholders ensures that the new risk is assessed in the context of all existing risks and that appropriate responses are collectively developed and owned. (PMBOK Guide) – Seventh Edition, 2021, p. 46, \'Optimize Risk Responses\'"'
    ),
    # Q1279
    (
        'Explanation: Need: keep plans flexible. Option C (Initiate the number of iterations to reduce the number of change requests.) fixes it."',
        'Explanation: Keywords: change request volume, high uncertainty, iterative approach, agile reduction. A high volume of change requests is often a symptom of uncertainty that was not managed through iterative development. Increasing the number of iterations allows stakeholders to see and respond to the product incrementally, incorporating changes naturally through the backlog rather than through formal change requests that disrupt the baseline. (PMBOK Guide) – Seventh Edition, 2021, p. 48, \'Embrace Adaptability and Resiliency\'"'
    ),
    # Q1280
    (
        'Explanation: Need: listen to people needs. Option C (Engage with the customer and rewrite all the stories.) fixes it."',
        'Explanation: Keywords: user stories, jargon, customer expectations, collaborative refinement. When user stories contain excessive technical jargon and fail to reflect the customer\'s expectations, the stories were likely written without sufficient customer involvement. Engaging directly with the customer to collaboratively rewrite the stories ensures that the language and content align with actual user needs, creating a shared understanding that guides the team\'s development work. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    # Q1281
    (
        'Explanation: Need: watch risks early. Option A (Update the risk register and take advantage of the opportunity.) fixes it."',
        'Explanation: Keywords: tax reduction opportunity, delivery delay, risk register, positive risk. When an external change — such as a new tax policy — transforms a project risk into an opportunity, the project manager should update the risk register to formally document and track this positive development. Taking advantage of the opportunity by allowing the delivery to shift into the favorable tax period turns a supply chain risk into a financial benefit. (PMBOK Guide) – Seventh Edition, 2021, p. 46, \'Optimize Risk Responses\'"'
    ),
    # Q1282
    (
        'Explanation: Need: guide and calm the team. Option C (Ask the product owner to prioritize the backlog with the project team.) fixes it."',
        'Explanation: Keywords: mandatory feature requests, sprint disruption, backlog prioritization, product owner role. When a product owner repeatedly injects mandatory features mid-sprint without going through the backlog prioritization process, it creates frustration and disrupts the team\'s delivery flow. Asking the product owner to prioritize new requests collaboratively with the project team restores the proper process and ensures that all changes are evaluated for value, effort, and timing before being committed. (PMBOK Guide) – Seventh Edition, 2021, p. 32, \'Focus on Value\'"'
    ),
    # Q1283
    (
        'Explanation: Need: listen to people needs. Option D (Incremental delivery, to ensure that mobile capability is released fast to the users) fixes it."',
        'Explanation: Keywords: competitive market, mobile extension, incremental delivery, time to market. When a competitor is developing a similar product and speed to market is critical, incremental delivery enables the team to release the mobile capability to users as soon as it is ready rather than waiting for all other features to be complete. This approach reduces competitive risk and gives users early access to the core value being delivered. (PMBOK Guide) – Seventh Edition, 2021, p. 32, \'Focus on Value\'"'
    ),
    # Q1284
    (
        'Explanation: Need: listen to people needs. Option A (Review the risks throughout project execution.) fixes it."',
        'Explanation: Keywords: risk register accuracy, executive reporting, ongoing review, risk management. When the project sponsor relies on the risk register for executive-level communication, the accuracy of that register is a direct reflection of the project\'s transparency and governance. The project manager must review and update the risks continuously throughout project execution to ensure that the register reflects the current state of threats and opportunities. (PMBOK Guide) – Seventh Edition, 2021, p. 46, \'Optimize Risk Responses\'"'
    ),
    # Q1285
    (
        'Explanation: Need: listen to people needs. Option D (Facilitate communication and team building.) fixes it."',
        'Explanation: Keywords: global team, group performance, individual performance, communication, team building. When individual performance is satisfactory but group performance is poor, the problem is not individual competence but the collaboration and communication between team members. Facilitating structured communication and team-building activities addresses the relational and coordination gaps that are preventing the team from performing collectively. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    # Q1286
    (
        'Explanation: Need: keep plans flexible. Option B (The project is earning less value an was planned.) fixes it."',
        'Explanation: Keywords: cost performance index, earned value, actual cost, CPI below 1. The ratio of earned value to actual cost is the cost performance index (CPI). A CPI of 0.9024 — less than 1.0 — means the project is earning less value per dollar spent than planned, indicating that costs are running above what the work accomplished would justify. The project is over budget relative to the value it has produced. (PMBOK Guide) – Seventh Edition, 2021, p. 34, \'Recognize, Evaluate, and Respond to System Interactions\'"'
    ),
    # Q1287
    (
        'Explanation: Need: watch risks early. Option B (Perform an analysis to assess the impact on the project.) fixes it."',
        'Explanation: Keywords: new financial regulation, scope impact, compliance requirement, impact analysis. When new mandatory regulations are introduced that may significantly change the project scope, the project manager must first perform a thorough analysis to understand the full extent of the impact before deciding on a course of action. Acting before this analysis is complete risks committing to responses that are either insufficient or disproportionate. (PMBOK Guide) – Seventh Edition, 2021, p. 46, \'Optimize Risk Responses\'"'
    ),
    # Q1288
    (
        'Explanation: Need: listen to people needs. Option D (Validated the iteration goals with the customer) fixes it."',
        'Explanation: Keywords: MVP, customer value, iteration goals, agile validation. When a customer indicates that the first deliverable lacks value, the root cause is typically that the iteration goals were defined without adequate customer input. The project manager should have validated the iteration goals with the customer before the sprint began to ensure the team was building what the customer actually considered valuable. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    # Q1289 - check for apostrophe in "team's"
    (
        "Explanation: Need: guide and calm the team. Option C (Examine the team's virtual needs.) fixes it.\"",
        "Explanation: Keywords: remote collaboration, virtual needs, same time zone, underlying factors. When team members in the same time zone still cannot collaborate effectively, the issue is unlikely to be scheduling conflicts and more likely to be unmet virtual collaboration needs — such as inadequate tools, access issues, or informal communication gaps. Examining the team's virtual needs identifies the specific barriers preventing remote members from participating fully. (PMBOK Guide) – Seventh Edition, 2021, p. 28, 'Create a Collaborative Team Environment'\""
    ),
    # Q1290
    (
        'Explanation: Need: guide and calm the team. Option D (Communicate with the resource on the roles and responsibilities of this project.) fixes it."',
        'Explanation: Keywords: role conflict, former supervisor, nonsupervisory resource, roles and responsibilities. When a team member who formerly held a supervisory role joins a project in a nonsupervisory capacity and challenges the current leadership, the conflict stems from an unclear understanding of their new role. Communicating clearly about the roles and responsibilities on this project establishes the expected behavior and authority structure without escalating the issue unnecessarily. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    # Q1291
    (
        'Explanation: Need: guide and calm the team. Option B (Possesses strong interpersonal skills to drive high-performing virtual teams) fixes it."',
        'Explanation: Keywords: virtual team management, global project, interpersonal skills, high-performing team. Managing a product development team distributed across four countries requires the ability to build trust, navigate cultural differences, facilitate communication, and motivate team members without physical proximity. Strong interpersonal skills are the foundational competency that enables a project manager to drive cohesion and high performance in a virtual environment. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    # Q1292
    (
        'Explanation: Need: guide and calm the team. Option C (Explore options with the IT department to expedite the necessary repairs based on criticality of the project.) fixes it."',
        'Explanation: Keywords: team member equipment failure, IT support delay, critical deliverable, escalation. When a team member\'s equipment failure is creating a risk to a critical project deliverable, the project manager must advocate for the team by escalating the urgency to the IT department. Exploring options to expedite repairs based on the project\'s criticality provides a path to resolution that is faster and less disruptive than procuring new equipment or creating workarounds. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
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
