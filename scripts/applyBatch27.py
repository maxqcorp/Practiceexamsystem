MD_FILE = './src/imports/project-management-questions-1.md'

with open(MD_FILE, 'r', encoding='utf-8') as f:
    content = f.read()

replacements = [
    # Q1293
    (
        'Explanation: Need: listen to people needs. Option A (Refer to the requirements traceability matrix and analyze the requirement.) fixes it."',
        'Explanation: Keywords: missed requirement, customer complaint, traceability matrix, requirements analysis. When a customer discovers that a requirement was not met, the first step is to analyze the situation objectively before committing to a response. Referring to the requirements traceability matrix clarifies whether the requirement was formally captured, how it was communicated to the team, and at what point the gap occurred, enabling a fact-based resolution. (PMBOK Guide) – Seventh Edition, 2021, p. 32, \'Focus on Value\'"'
    ),
    # Q1294
    (
        'Explanation: Need: guide and calm the team. Option D (Fast track the project.) fixes it."',
        'Explanation: Keywords: negative schedule variance, hybrid sprints, EV below PV, schedule recovery. When earned value falls below planned value, the project is behind schedule and must find ways to recover. Fast tracking — performing activities in parallel that were originally planned sequentially — is the appropriate technique to accelerate the schedule when cost is less of a concern than time. (PMBOK Guide) – Seventh Edition, 2021, p. 40, \'Tailor Based on Context\'"'
    ),
    # Q1295
    (
        'Explanation: Need: guide and calm the team. Option A (Develop different approaches based on team members\' motivation and ability.) fixes it."',
        'Explanation: Keywords: team performance assessment, poor performers, tailored leadership, motivation and ability. Effective performance management recognizes that team members have different motivations, experience levels, and developmental needs. Developing different approaches based on each team member\'s specific motivation and ability level ensures that the feedback and support provided are targeted and likely to drive genuine improvement. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    # Q1296
    (
        'Explanation: Need: listen to people needs. Option C (Communicate the benefit expectations and the action plan for the pending functionalities.) fixes it."',
        'Explanation: Keywords: savings exceeded, functionalities pending, benefits realization, stakeholder communication. When a project has exceeded its expected financial benefits but still has outstanding functional deliverables, the project manager must communicate both the positive performance and the realistic plan for completing what remains. This balanced approach provides stakeholders with an honest and value-focused picture of the project\'s status. (PMBOK Guide) – Seventh Edition, 2021, p. 32, \'Focus on Value\'"'
    ),
    # Q1297
    (
        'Explanation: Need: keep plans flexible. Option C (Review the quality management plan with the senior manager.) fixes it."',
        'Explanation: Keywords: senior manager quality concern, quality management plan, stakeholder alignment, quality standards. When a senior manager expresses concern about quality, the project manager must address this by reviewing the quality management plan together with the senior manager. This collaborative review clarifies what quality standards and processes are already in place, resolves any misalignment between expectations and reality, and builds the senior manager\'s confidence in the project\'s quality approach. (PMBOK Guide) – Seventh Edition, 2021, p. 42, \'Build Quality into Processes and Deliverables\'"'
    ),
    # Q1298
    (
        'Explanation: Need: guide and calm the team. Option A (Reject the workload back to the global team.) fixes it."',
        'Explanation: Keywords: scope boundary, local versus global team, workload misdirection, role clarity. When work that belongs to another team is being directed to the local project manager, accepting it would create unauthorized scope expansion and undermine the program\'s governance structure. Rejecting the workload and redirecting it to the appropriate global team maintains clear accountability and protects the local project\'s capacity and baselines. (PMBOK Guide) – Seventh Edition, 2021, p. 25, \'Be a Diligent, Respectful, and Caring Steward\'"'
    ),
    # Q1299
    (
        'Explanation: Need: guide and calm the team. Option A (Meet with the team member to understand their concerns and/or issues.) fixes it."',
        'Explanation: Keywords: experienced team member, missed deadlines, project delay, direct communication. When a previously reliable team member begins missing deadlines, a behavioral change like this typically signals an underlying issue — personal, technical, or organizational — rather than a capability gap. Meeting directly with the team member to understand what is happening is the first and most appropriate step before escalating or reassigning work. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    # Q1300
    (
        'Explanation: Need: guide and calm the team. Option A (Try to remove the barriers and empower team members.) fixes it."',
        'Explanation: Keywords: internal procedures, team autonomy, servant leadership, barrier removal. When internal processes are impeding the team\'s ability to work efficiently and autonomously, the project manager\'s role as a servant leader is to actively remove those barriers rather than training the team to work around them. Empowering team members by clearing procedural obstacles creates the conditions for high performance. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    # Q1301
    (
        'Explanation: Need: listen to people needs. Option D (Work with relevant stakeholders to determine possible solutions.) fixes it."',
        'Explanation: Keywords: schedule risk materialized, issue resolution, stakeholder collaboration, solutions development. When a schedule risk becomes an actual issue causing foreseen delays, the project manager must engage the relevant stakeholders collaboratively to develop and evaluate possible solutions. Stakeholder involvement in the resolution process ensures that proposed solutions account for all affected parties\' constraints and that the agreed response has broad support. (PMBOK Guide) – Seventh Edition, 2021, p. 46, \'Optimize Risk Responses\'"'
    ),
    # Q1302
    (
        'Explanation: Need: keep plans flexible. Option C (As the cost performance index (CPI) and schedule performance index (SPI) are less than 1.0, reevaluate and prioritize the remaining actions.) fixes it."',
        'Explanation: Keywords: EVM, CPI below 1, SPI below 1, contingency reserve, reevaluation. After completing two of five actions and spending 80% of the contingency reserve in 60% of the time, both the cost and schedule performance indices are below 1.0, signaling that the project is over budget and behind schedule. The project manager must reevaluate and reprioritize the remaining actions to make the most of the limited time and budget still available. (PMBOK Guide) – Seventh Edition, 2021, p. 34, \'Recognize, Evaluate, and Respond to System Interactions\'"'
    ),
    # Q1303
    (
        'Explanation: Need: guide and calm the team. Option C (Help cultivate self-awareness between the two team members through emotional intelligence (El).) fixes it."',
        'Explanation: Keywords: team conflict, emotional intelligence, self-awareness, interpersonal skills. When persistent conflict between two team members is harming project performance, the root cause is often a lack of self-awareness about how each person\'s behavior affects others. Helping both team members develop emotional intelligence and self-awareness creates the conditions for them to recognize and manage their reactions, building a more productive working relationship over time. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    # Q1304
    (
        'Explanation: Need: secure people or vendors. Option C (Remind the contractor that they committed to attending meetings and submitting reports per the contract.) fixes it."',
        'Explanation: Keywords: contractor non-compliance, contractual obligations, meeting attendance, status reports. When a contractor stops fulfilling contractual obligations — such as attending meetings and submitting reports — the first step is to formally remind them of the specific commitments they made in the contract. This approach establishes a clear record, signals that the project manager is monitoring compliance, and gives the contractor an opportunity to correct the behavior before formal claims or escalation become necessary. (PMBOK Guide) – Seventh Edition, 2021, p. 25, \'Be a Diligent, Respectful, and Caring Steward\'"'
    ),
    # Q1305
    (
        'Explanation: Need: keep plans flexible. Option A (Assess and prioritize the impact of the new law on the project plan.) fixes it."',
        'Explanation: Keywords: new zoning law, telecom towers, schedule and cost impact, regulatory change. When new legislation is introduced that may affect an ongoing project, the project manager must first assess and prioritize the specific impacts on the project plan before taking any corrective action. Understanding the full scope of the law\'s effect on cost, schedule, and scope enables an informed and proportionate response rather than a reactive change to the project baseline. (PMBOK Guide) – Seventh Edition, 2021, p. 46, \'Optimize Risk Responses\'"'
    ),
    # Q1306
    (
        'Explanation: Need: keep plans flexible. Option B (Clarify with the CFO that the prioritization process is based on business value.) fixes it."',
        'Explanation: Keywords: CFO concern, agile backlog, prioritization, business value. When an executive stakeholder is concerned that an important feature is being deferred in an agile project, the project manager should clarify that the backlog prioritization process is driven by business value — not by individual stakeholder preferences or function importance. This explanation helps the CFO understand that the feature\'s placement reflects a deliberate value-based decision that can be reviewed through the product owner. (PMBOK Guide) – Seventh Edition, 2021, p. 32, \'Focus on Value\'"'
    ),
    # Q1307
    (
        'Explanation: Need: listen to people needs. Option D (Determine the possible impact of this change on all aspects of the project.) fixes it."',
        'Explanation: Keywords: late change request, sponsor request, impact analysis, 70% complete. When a new deliverable is requested by the project sponsor at 70% completion, the project manager must first evaluate the full impact of the change before accepting or rejecting it. Determining the impact on scope, cost, schedule, and quality provides the factual basis needed to make an informed decision about how — and whether — to proceed. (PMBOK Guide) – Seventh Edition, 2021, p. 50, \'Enable Change to Achieve the Envisioned Future State\'"'
    ),
    # Q1308
    (
        'Explanation: Need: listen to people needs. Option B (Incorporate the needs of all stakeholders into the communications management plan.) fixes it."',
        'Explanation: Keywords: ERP initiative, stakeholder identification, communications management, stakeholder needs. The purpose of identifying, evaluating, and categorizing stakeholder relationships is to understand the full range of stakeholder needs and expectations so that these can be systematically incorporated into the communications management plan. This ensures that every stakeholder receives the right information, in the right format, at the right frequency to remain engaged and informed. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    # Q1309
    (
        'Explanation: Need: guide and calm the team. Option C (Engage the operation teams in the retrospectives and demo sessions and incorporate their feedback on project activities.) fixes it."',
        'Explanation: Keywords: agile transition, operations handover, production issues, retrospective engagement. When transitioning to agile creates problems at the handover to operations, the root cause is that the operations team was excluded from the development process. Engaging operations teams in retrospectives and demos — and incorporating their feedback — bridges the gap between development and operations, reducing the issues that arise when new features enter the support environment. (PMBOK Guide) – Seventh Edition, 2021, p. 48, \'Embrace Adaptability and Resiliency\'"'
    ),
    # Q1310
    (
        'Explanation: Need: keep plans flexible. Option C (Engage the agile resources through video conferencing on a daily basis.) fixes it."',
        'Explanation: Keywords: hybrid project, remote agile resources, daily engagement, video conferencing. When the only available resources with agile expertise are in a different location, daily video conferencing provides a practical and cost-effective way to maintain tight collaboration without requiring relocation or incurring the budget overrun of hiring additional local resources. This approach keeps the agile resources fully integrated with the project despite geographic separation. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    # Q1311
    (
        'Explanation: Need: listen to people needs. Option B (Establish a proactive knowledge-sharing plan.) fixes it."',
        'Explanation: Keywords: key resource departure, knowledge risk, knowledge transfer, proactive planning. When a key project resource with specialized knowledge is leaving, the most effective risk mitigation is to establish a proactive knowledge-sharing plan before their departure. This ensures that critical knowledge is systematically transferred to remaining team members, reducing the project\'s vulnerability to knowledge loss without disrupting current delivery momentum. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    # Q1312
    (
        'Explanation: Need: protect benefits for users. Option B (Choose the agile practices that can be implemented in this type of construction project and apply them.) fixes it."',
        'Explanation: Keywords: construction project, agile practices, tailoring, context-appropriate application. Agile principles are not limited to software development — many agile practices can be adapted and applied to construction projects to improve collaboration, transparency, and responsiveness. Rather than adopting agile wholesale or rejecting it entirely, the project manager should identify which specific practices are compatible with the project\'s physical and sequential constraints and apply those selectively. (PMBOK Guide) – Seventh Edition, 2021, p. 40, \'Tailor Based on Context\'"'
    ),
    # Q1313
    (
        'Explanation: Need: listen to people needs. Option A (Inform the relevant stakeholders.) fixes it."',
        'Explanation: Keywords: appointment delay, internet installation, stakeholder notification, schedule change. When a scheduled activity is delayed — such as a service installation — the project manager must immediately inform all stakeholders who are affected by that delay. Functional managers who arranged time off for the affected agents, the agents themselves, and any other dependent parties all need to be notified promptly so they can adjust their schedules accordingly. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    # Q1314
    (
        'Explanation: Need: protect benefits for users. Option A (Prioritize the projects, giving higher priority to projects that will increase profit.) fixes it."',
        'Explanation: Keywords: portfolio prioritization, profitability, resource overload, project prioritization. When a company\'s project portfolio has stretched resources across too many projects and financial objectives are at risk, the most effective response is to prioritize projects by their contribution to profitability. Focusing resources on higher-profit projects improves the likelihood of achieving financial objectives while reducing the overload that is causing schedule slippage across the portfolio. (PMBOK Guide) – Seventh Edition, 2021, p. 32, \'Focus on Value\'"'
    ),
    # Q1315
    (
        'Explanation: Need: guide and calm the team. Option D (Break down the deliverables into sprints and deliver value incrementally.) fixes it."',
        'Explanation: Keywords: digital product, cross-functional team, incremental delivery, early value. For a digital transformation project requiring ongoing refinement, breaking deliverables into sprints allows the team to deliver working increments of value early and continuously. This approach creates feedback opportunities, reduces the risk of misalignment with business expectations, and ensures that business value is realized well before the final product is complete. (PMBOK Guide) – Seventh Edition, 2021, p. 32, \'Focus on Value\'"'
    ),
    # Q1316
    (
        'Explanation: Need: guide and calm the team. Option D (Empowered the team to improve their processes, tools, and interactions to be more effective in delivery and removing impediments) fixes it."',
        'Explanation: Keywords: agile adoption, impediments, quality issues, team empowerment. When a newly agile team experiences delivery problems under pressure — producing fewer features or lower quality — the root cause is often a failure to allow the team to improve their own ways of working. The project leader should have empowered the team to identify and address the impediments to their own processes, tools, and interactions, rather than imposing fast-tracking directives that add pressure without addressing underlying issues. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    # Q1317
    (
        'Explanation: Need: guide and calm the team. Option A (Discuss the project manager\'s observations with the individual to determine why they are behaving this way.) fixes it."',
        'Explanation: Keywords: performance drop, aggressive behavior, behavioral change, one-on-one discussion. When a previously high-performing team member shows a sudden performance decline and aggressive behavior, this signals that something has changed — either personally or professionally — that the project manager does not yet know about. Discussing the observations directly and privately with the individual is the first step to understanding the root cause and determining how best to support them. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    # Q1318
    (
        'Explanation: Need: listen to people needs. Option C (Plan ahead and define the best way to review the deliverables with the customer.) fixes it."',
        'Explanation: Keywords: customer availability, review delays, iterative rework, proactive planning. When a customer is frequently unavailable for iteration reviews and this is causing rework, the project manager must proactively address the structural issue by defining a review approach that works within the customer\'s actual availability. Planning ahead to establish the review format and cadence that fits the customer reduces the dependency on impromptu scheduling and the downstream cost of unreviewed deliverables. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    # Q1319
    (
        'Explanation: Need: listen to people needs. Option A (Facilitate the next retrospective meeting, focusing the team on analyzing root causes and proposing solutions.) fixes it."',
        'Explanation: Keywords: software bugs, user experience, retrospective, root cause analysis. When a released product version has significant quality problems, the retrospective is the appropriate forum to collaboratively analyze the root causes and agree on corrective measures. Focusing the retrospective on understanding what went wrong and generating team-owned solutions builds both accountability and the capability to prevent similar issues in future iterations. (PMBOK Guide) – Seventh Edition, 2021, p. 48, \'Embrace Adaptability and Resiliency\'"'
    ),
    # Q1320 - curly apostrophe in "company's industry"
    (
        "Explanation: Need: protect value and acceptance. Option D (Propose a hybrid approach, leveraging the benefits of an agile approach while respecting some aspects of the company's industry.) fixes it.\"",
        "Explanation: Keywords: predictive approach, regulated market, competitive disadvantage, hybrid delivery. When a company in a regulated market is losing its competitive advantage because its predictive approach is too slow, a full pivot to agile is not always feasible given regulatory constraints. A hybrid approach allows the company to benefit from agile's speed and adaptability while still respecting the compliance and governance requirements that the industry demands. (PMBOK Guide) – Seventh Edition, 2021, p. 40, 'Tailor Based on Context'\""
    ),
    # Q1321
    (
        'Explanation: Need: listen to people needs. Option B (Put into place a project governance model in line with the requirements.) fixes it."',
        'Explanation: Keywords: project governance, compliance requirements, investment strategy, governance model. When a project operates in an organization without a project management governance structure, the project manager must establish governance that meets the project\'s specific strategy, investment, and compliance requirements. Creating a governance model tailored to these requirements is more immediately actionable and appropriate than attempting to create organization-wide governance structures. (PMBOK Guide) – Seventh Edition, 2021, p. 25, \'Be a Diligent, Respectful, and Caring Steward\'"'
    ),
    # Q1322
    (
        'Explanation: Need: listen to people needs. Option A (Ask the team member to submit a formal change request.) fixes it."',
        'Explanation: Keywords: product improvement suggestion, no schedule or cost impact, change control, formal process. Even when a suggested change appears to have no impact on schedule or cost, it must still go through the formal change control process to ensure proper evaluation, documentation, and authorization. Accepting changes without formal review — however beneficial they may seem — bypasses governance controls and sets a precedent for undocumented scope modifications. (PMBOK Guide) – Seventh Edition, 2021, p. 50, \'Enable Change to Achieve the Envisioned Future State\'"'
    ),
    # Q1323
    (
        'Explanation: Need: listen to people needs. Option D (Immediately discuss this with the project sponsor and request to revisit the budget to ensure its accuracy.) fixes it."',
        'Explanation: Keywords: charter review, missing budget items, project sponsor, budget accuracy. When major budget items necessary to achieve the project outcome are found to be missing from the approved charter, the project manager must immediately raise this with the project sponsor. Proceeding with an inaccurate budget creates a guaranteed shortfall that will surface at the worst possible time — raising it now provides the best chance of securing the funding needed before the project begins. (PMBOK Guide) – Seventh Edition, 2021, p. 25, \'Be a Diligent, Respectful, and Caring Steward\'"'
    ),
    # Q1324
    (
        'Explanation: Need: guide and calm the team. Option C (Have a meeting with the team to discuss the issue and propose solutions.) fixes it."',
        'Explanation: Keywords: break tardiness, gradual pattern, team meeting, collaborative resolution. When a behavioral pattern gradually develops — such as work breaks extending over successive weeks — the project manager should address it through open dialogue with the team before it becomes a larger issue. A meeting that discusses the pattern and invites solutions creates shared accountability and gives the team an opportunity to self-correct, which is more effective than disciplinary action for what may stem from unaddressed fatigue or workload issues. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    # Q1325
    (
        'Explanation: Need: watch risks early. Option D (An agile execution strategy) fixes it."',
        'Explanation: Keywords: new regulation, high uncertainty, evolving requirements, agile approach. When the requirements for a mandatory regulation are only partially defined and changes are expected as the regulation is clarified, an agile execution strategy is the most appropriate choice. The agile approach allows the team to incorporate new regulatory details iteratively as they emerge, rather than committing to a plan based on incomplete information that will be repeatedly disrupted. (PMBOK Guide) – Seventh Edition, 2021, p. 48, \'Embrace Adaptability and Resiliency\'"'
    ),
    # Q1326
    (
        'Explanation: Need: guide and calm the team. Option D (Investigate alternative tools for virtual meetings that are available to all team members.) fixes it."',
        'Explanation: Keywords: virtual meeting tool, geographic restriction, team inclusion, alternative tools. When a selected communication tool is not accessible to all team members due to geographic or regulatory restrictions, the project manager must find an alternative that works for everyone. Investigating accessible alternatives ensures that all team members can participate fully in virtual meetings from the start of the project, preventing a two-tier communication environment. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    # Q1327
    (
        'Explanation: Need: listen to people needs. Option A (Ensure a measurement system is in place like earned value analysis (EVA) to track project value for the project sponsor.) fixes it."',
        'Explanation: Keywords: project value reporting, sponsor communication, earned value analysis, measurement system. Reporting project value to a project sponsor requires quantitative, structured metrics that go beyond cost and schedule status. Ensuring an earned value measurement system is in place provides the sponsor with objective indicators of both the value being delivered and the efficiency with which budget is being used, which is essential for funding decisions and portfolio governance. (PMBOK Guide) – Seventh Edition, 2021, p. 32, \'Focus on Value\'"'
    ),
    # Q1328
    (
        'Explanation: Need: protect benefits for users. Option C (The engineer has "project burnout"" from working long hours and solving difficult problems.) fixes it."',
        'Explanation: Keywords: engineer refusal, project burnout, recognition, workload management. When a highly motivated and capable engineer declines a project invitation, the most likely cause — especially given their history of initiative and complex problem-solving — is burnout from sustained overwork. Project managers must be alert to signs of unsustainable workload and recognize that even highly capable team members need recovery time, or risk losing them entirely from future engagements. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    # Q1329
    (
        'Explanation: Need: listen to people needs. Option B (Update the stakeholder engagement plan with the specific communication needs for the stakeholder.) fixes it."',
        'Explanation: Keywords: stakeholder transition, PM resignation, informal communication, stakeholder engagement plan. When a project manager leaves without a formal handover, the informal communication practices they maintained — especially with stakeholders outside standard meeting structures — risk being lost. Updating the stakeholder engagement plan with the specific communication needs of this stakeholder ensures that the incoming project manager has a documented guide to maintaining the same level of engagement. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    # Q1330
    (
        'Explanation: Need: listen to people needs. Option D (Organize a team meeting to inform team members about a change in direction and work with them to change the task allocation.) fixes it."',
        'Explanation: Keywords: hierarchical organization, task reassignment, performance perception, transparent communication. In a hierarchical organization where task completion is tied to performance reviews, reassigning tasks without explanation can damage team members\' standing and morale. Organizing a team meeting to transparently explain the reason for the change in direction and collaboratively work through the reallocation respects team members\' professional standing while making the change in a way that maintains trust. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    # Q1331
    (
        'Explanation: Need: guide and calm the team. Option C (Laissez-faire) fixes it."',
        'Explanation: Keywords: leadership style, team autonomy, experienced team, laissez-faire. When a project manager has worked with the same experienced team across multiple projects and now wants to shift toward giving the team full decision-making autonomy, a laissez-faire leadership style is the appropriate choice. This style delegates authority and trusts the team to self-manage, which is suitable for high-performing, experienced teams that do not need close direction. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    # Q1332
    (
        'Explanation: Need: listen to people needs. Option C (Stakeholder engagement assessment matrix) fixes it."',
        'Explanation: Keywords: stakeholder unaware, engagement gap, assessment matrix, communications review. When a registered stakeholder is still unaware of project developments, the problem is not that they were missed in identification but that their engagement level is lower than required. The stakeholder engagement assessment matrix — which maps current versus desired engagement levels for each stakeholder — is the correct document to review to identify and address gaps in stakeholder engagement. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    # Q1333
    (
        'Explanation: Need: guide and calm the team. Option C (Support the team during the planning phase to only commit to what they are able to deliver.) fixes it."',
        'Explanation: Keywords: self-organizing team, over-commitment, stress, sustainable pace. When a consistently high-performing team is experiencing stress due to over-commitment, the root cause is that commitments made during planning exceed the team\'s realistic capacity. A servant leader\'s response is to support the team in calibrating their sprint commitments to a sustainable pace, ensuring long-term performance without burning out the team. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    # Q1334
    (
        'Explanation: Need: listen to people needs. Option C (Work with the team on the definition of a minimum viable product (MVP) and present it to the stakeholders.) fixes it."',
        'Explanation: Keywords: unclear vision, digital product, MVP definition, stakeholder alignment. When the vision for a product is unclear to stakeholders, starting with the full roadmap or technical spikes risks building in the wrong direction. Working with the team to define an MVP and presenting it to stakeholders creates a concrete, discussable artifact that aligns expectations, surfaces disagreements early, and ensures the first deliverable focuses on core value. (PMBOK Guide) – Seventh Edition, 2021, p. 32, \'Focus on Value\'"'
    ),
    # Q1335
    (
        'Explanation: Need: listen to people needs. Option B (Agree with the client on acceptance criteria.) fixes it."',
        'Explanation: Keywords: new quality standards, acceptance criteria, client alignment, delivery planning. When a client provides new quality standards during planning, the project manager must translate these into concrete, measurable acceptance criteria that both parties formally agree on. Without agreed acceptance criteria that reflect the new standards, there is no shared definition of what constitutes a successful deliverable, which creates a risk of rejection at delivery time. (PMBOK Guide) – Seventh Edition, 2021, p. 42, \'Build Quality into Processes and Deliverables\'"'
    ),
    # Q1336
    (
        'Explanation: Need: watch risks early. Option B (Assess the situation as an opportunity for improvement and perform a risk analysis.) fixes it."',
        'Explanation: Keywords: vendor SOW changes, procurement management, opportunity assessment, risk analysis. When a vendor is requesting changes to the statement of work that would actually improve the project outcome, the project manager should assess these requests as potential opportunities rather than automatically viewing them as threats. Performing a risk analysis on the proposed changes determines whether the improvements outweigh any associated risks to schedule, cost, or contractual terms. (PMBOK Guide) – Seventh Edition, 2021, p. 46, \'Optimize Risk Responses\'"'
    ),
    # Q1337
    (
        'Explanation: Need: guide and calm the team. Option B (Allocated proper resources for training on BMS in the project plan) fixes it."',
        'Explanation: Keywords: BMS commissioning, training gap, handover risk, resource planning. When neither the project team nor the operations team can properly operate a building management system at handover, the root cause is a failure to plan for training as part of the project. Allocating proper resources for BMS training in the project plan — well before commissioning — would have ensured both teams were prepared to operate the system, preventing the schedule delay and risk created by the knowledge gap. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    # Q1338
    (
        'Explanation: Need: guide and calm the team. Option D (Add the delay to the issue log and work with the vendor for a resolution that will bring the schedule back on track.) fixes it."',
        'Explanation: Keywords: vendor delay, status reporting, issue log, schedule recovery. When a vendor delay is confirmed as a current issue rather than a future risk, it must be formally logged in the issue log and addressed through collaborative problem-solving with the vendor. Working directly with the vendor on a resolution that restores the schedule is more likely to be effective than escalating to the sponsor or reviewing financial penalties, which would not recover lost time. (PMBOK Guide) – Seventh Edition, 2021, p. 34, \'Recognize, Evaluate, and Respond to System Interactions\'"'
    ),
    # Q1339 multi-select
    (
        'Explanation: Need: guide and calm the team. Options D and E (Cumulative flow diagram of completed features; Burndown chart) work together."',
        'Explanation: Keywords: agile team performance, momentum analysis, cumulative flow diagram, burndown chart. To analyze why an agile team is losing momentum, the project manager needs tools that visualize delivery trends over time. A cumulative flow diagram shows the flow of work items through each stage and can reveal bottlenecks or declining throughput, while a burndown chart shows whether the team\'s rate of completion is trending behind expectations across iterations. (PMBOK Guide) – Seventh Edition, 2021, p. 34, \'Recognize, Evaluate, and Respond to System Interactions\'"'
    ),
    # Q1340
    (
        'Explanation: Need: guide and calm the team. Option D (Work with the team members to define the overall objective and support them to engage around the goal.) fixes it."',
        'Explanation: Keywords: expert team, 6-month engagement, servant leadership, goal definition. When managing a team of highly qualified experts, the project manager\'s primary role is not to direct the work but to ensure that the team has a clear, shared objective they are collectively committed to achieving. Collaboratively defining the overall objective and supporting the team to engage around that goal channels their expertise productively while preserving their autonomy as subject matter experts. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    # Q1341
    (
        'Explanation: Need: keep plans flexible. Option B (Estimate the costs at the work package level and add those costs to calculate the total cost of the project and compare it to the allocated budget.) fixes it."',
        'Explanation: Keywords: bottom-up estimating, work packages, resource budget, cost comparison. The most reliable way to verify that an allocated project budget is sufficient is to estimate resource costs at the work package level — the lowest level of the WBS — and aggregate these estimates to calculate the total project cost. Comparing this bottom-up total to the allocated budget reveals whether the funding is adequate or whether a budget revision discussion is needed. (PMBOK Guide) – Seventh Edition, 2021, p. 40, \'Tailor Based on Context\'"'
    ),
    # Q1342
    (
        'Explanation: Need: keep plans flexible. Option C (Review the project management plan to see the impact of the possible delay.) fixes it."',
        'Explanation: Keywords: unforeseen event, public works shutdown, critical path delay, impact assessment. When an external event forces a 4-week shutdown of public works activities, the project manager must first review the project management plan to understand the full impact of the delay before taking action. This assessment determines which activities are affected, how the critical path is impacted, and what response options — such as crashing or fast-tracking — are available within the remaining constraints. (PMBOK Guide) – Seventh Edition, 2021, p. 46, \'Optimize Risk Responses\'"'
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
