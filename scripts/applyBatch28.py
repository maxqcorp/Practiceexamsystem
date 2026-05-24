MD_FILE = './src/imports/project-management-questions-1.md'

with open(MD_FILE, 'r', encoding='utf-8') as f:
    content = f.read()

replacements = [
    # Q1343 - ASCII apostrophes in customer's
    (
        'Explanation: Need: listen to people needs. Option A (The customer\'s requirements should have been captured in order to meet the customer\'s standards.) fixes it."',
        'Explanation: Keywords: product specification, customer requirements, lessons learned, requirements capture. When a product is delivered but the customer claims it was not designed to their specifications, the root cause is typically a failure to properly capture and document customer requirements at the beginning of the project. The project manager should have ensured that customer requirements were fully captured to serve as the baseline for design and acceptance criteria. (PMBOK Guide) – Seventh Edition, 2021, p. 42, \'Build Quality into Processes and Deliverables\'"'
    ),
    # Q1344
    (
        'Explanation: Need: listen to people needs. Option C (Review the business benefits realization plan with the stakeholders.) fixes it."',
        'Explanation: Keywords: business value, lessons learned, benefits realization plan, stakeholder review. When a stakeholder in a lessons learned session identifies that the project failed to deliver expected business value, the project manager should review the benefits realization plan with the stakeholders. This review reveals whether the planned benefits were clearly defined, measured, and tracked throughout the project, providing insight into where the value delivery approach fell short. (PMBOK Guide) – Seventh Edition, 2021, p. 32, \'Focus on Value\'"'
    ),
    # Q1345
    (
        'Explanation: Need: listen to people needs. Option A (Obtained all critical information ahead of time) fixes it."',
        'Explanation: Keywords: deployment delay, critical information, proactive planning, customer dependency. When a deployment is delayed because the customer fails to provide critical information in a timely manner, the preventive action was to identify and obtain all critical information ahead of the deployment date during the planning phase. Proactive information gathering eliminates last-minute dependencies that the project team cannot control. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    # Q1346
    (
        'Explanation: Need: guide and calm the team. Option B (Call each team member to gain their perspective on the problem, then bring the whole team together to discuss a solution.) fixes it."',
        'Explanation: Keywords: team disengagement, lack of commitment, individual conversations, collective solution. When a team as a whole is disengaged, the project manager needs to first understand each individual\'s perspective through private conversations, then bring the team together to collectively address the issue. This approach demonstrates genuine concern for each team member while creating shared ownership of the solution. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    # Q1347
    (
        'Explanation: Need: listen to people needs. Option C (Study the environment and the available resources to determine which approach to use.) fixes it."',
        'Explanation: Keywords: knowledge transfer, distributed teams, limited access, context-dependent approach. When standard knowledge transfer processes are not feasible due to team distribution and access constraints, the project manager must assess the specific environment and available resources to design an approach that actually works for this team. A one-size-fits-all solution will not be effective when the team\'s technology access and location vary significantly. (PMBOK Guide) – Seventh Edition, 2021, p. 40, \'Tailor Based on Context\'"'
    ),
    # Q1348
    (
        'Explanation: Need: guide and calm the team. Option D (Meet with the resources together and find common ground on viewpoints to compromise on an approach.) fixes it."',
        'Explanation: Keywords: resource disagreement, solution approach, compromise, collaborative decision. When two team members with different experience levels disagree on a solution approach and time is limited, bringing them together to find common ground is more effective than imposing a decision or escalating to their managers. A compromise reached through direct dialogue builds shared ownership and is more likely to result in a reliable, implementable solution. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    # Q1349
    (
        'Explanation: Need: guide and calm the team. Option B (Create an environment where the agreement is reached through discussion.) fixes it."',
        'Explanation: Keywords: consensus building, diverse team, discussion-based agreement, team engagement. True consensus is not achieved through majority voting but through facilitated discussion where all perspectives are heard and the group reaches a shared understanding. Creating an environment where agreement is reached through discussion ensures team members feel heard, builds genuine buy-in, and produces decisions that everyone is willing to commit to. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    # Q1350
    (
        'Explanation: Need: listen to people needs. Option C (Study the stakeholder analysis to understand which stakeholder holds the most influence and seek their assistance.) fixes it."',
        'Explanation: Keywords: lack of senior management support, new project manager, stakeholder influence, targeted engagement. When a project lacks senior management support and the project manager is new to the organization, the most effective path to securing backing is to identify the most influential stakeholder through the stakeholder analysis and engage their specific assistance. A targeted, evidence-based approach to building support is more effective than broad requests for involvement. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    # Q1351
    (
        'Explanation: Need: guide and calm the team. Option C (Conduct a product roadmap session with the team.) fixes it."',
        'Explanation: Keywords: agile team, new collaboration, product roadmap, shared direction. When a facilitator and team have not worked together before, the first priority is to establish a shared understanding of what the team is trying to build and why. Conducting a product roadmap session aligns everyone on the vision, priorities, and direction before committing to release plans or sprint cycles, creating a foundation for effective collaboration. (PMBOK Guide) – Seventh Edition, 2021, p. 32, \'Focus on Value\'"'
    ),
    # Q1352
    (
        'Explanation: Need: protect benefits for users. Option D (Work out a resolution in consultation with the sourcing department head.) fixes it."',
        'Explanation: Keywords: balanced matrix, sourcing department, work performance updates, resolution. When a key information source is too busy to provide required project updates through the agreed approach, the project manager must negotiate a workable solution directly with the department head rather than bypassing them or escalating immediately. A collaborative resolution that acknowledges the department head\'s constraints while meeting the project\'s needs is the most sustainable approach. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    # Q1353
    (
        'Explanation: Need: guide and calm the team. Option D (Request the respective teams to plan for knowledge-sharing sessions.) fixes it."',
        'Explanation: Keywords: cross-team dependency, domain knowledge, knowledge sharing, team collaboration. When a visual management tool reveals that one team\'s knowledge is a dependency for another team\'s delivery, the solution is to plan structured knowledge-sharing sessions between the respective teams. This transfers critical domain knowledge in a systematic way while preserving each team\'s separate identity and responsibilities. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    # Q1354
    (
        'Explanation: Need: listen to people needs. Option C (Discuss the changes with the client and jointly make the decision on how to proceed.) fixes it."',
        'Explanation: Keywords: client re-engagement, change requests, joint decision-making, collaboration. When a client who has been less engaged begins requesting changes, the project manager must re-engage them directly to discuss the changes and make decisions jointly. Unilateral decisions about scope changes — whether rejecting or accepting them — without client involvement risk either blocking legitimate needs or creating unauthorized scope expansion. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    # Q1355
    (
        'Explanation: Need: listen to people needs. Option A (Organize a one-on-one conversation with each stakeholder.) fixes it."',
        'Explanation: Keywords: stakeholder motivation, stakeholder register, one-on-one conversation, direct engagement. Understanding what drives a stakeholder\'s behavior and decisions requires direct, candid conversation rather than inference from documents or group meetings. Organizing one-on-one conversations with each stakeholder creates a private, trusting space where honest motivations are more likely to be shared. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    # Q1356
    (
        'Explanation: Need: listen to people needs. Option A (Needs of the customer) fixes it."',
        'Explanation: Keywords: agile values, customer priority, organizational processes, conflict resolution. In an agile project, when there is tension between organizational processes and customer value, the needs of the customer take the highest priority. Agile principles explicitly place customer satisfaction and delivering valuable outcomes above strict adherence to processes, guiding the project manager in resolving conflicts between organizational prescriptions and what actually serves the project. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    # Q1357
    (
        'Explanation: Need: listen to people needs. Option A (Discuss with the team, estimate the effort, and raise a change request.) fixes it."',
        'Explanation: Keywords: late scope change, go-live risk, change request, formal evaluation. When additional functionality is requested just before go-live and the team has identified delivery risks and scope conflicts, the request cannot be accepted or rejected informally. Discussing the details with the team, estimating the effort, and raising a formal change request ensures the decision is made with full information and proper authorization before any work begins. (PMBOK Guide) – Seventh Edition, 2021, p. 50, \'Enable Change to Achieve the Envisioned Future State\'"'
    ),
    # Q1358
    (
        'Explanation: Need: watch risks early. Option C (Audit meeting) fixes it."',
        'Explanation: Keywords: risk management effectiveness, audit, financial risks, process verification. Regularly verifying the strength and efficiency of the risk management process requires a structured review mechanism. An audit meeting provides a formal and systematic way to assess whether risks are being identified, assessed, monitored, and responded to effectively — which is particularly important for a project with significant financial exposure. (PMBOK Guide) – Seventh Edition, 2021, p. 46, \'Optimize Risk Responses\'"'
    ),
    # Q1359
    (
        'Explanation: Need: guide and calm the team. Option A (Inform team B of the dependency and ensure that the deliverable is planned.) fixes it."',
        'Explanation: Keywords: cross-team dependency, iteration planning, dependency communication, delivery planning. When a team identifies a dependency on another team\'s deliverable during iteration planning, the project manager must immediately communicate this dependency to the other team and ensure it is incorporated into their planning. Proactive communication prevents the dependency from becoming a blocker at the moment the deliverable is needed. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    # Q1360
    (
        'Explanation: Need: guide and calm the team. Option B (Performance improvement programs are organized for all team members who were assessed.) fixes it."',
        'Explanation: Keywords: performance assessment, skill gaps, performance improvement program, team development. When performance gaps are identified through an assessment, addressing them through organized improvement programs demonstrates a commitment to developing team members rather than simply evaluating them. Performance improvement programs provide a structured path for closing specific gaps, which benefits both the individual and the project. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    # Q1361
    (
        'Explanation: Need: guide and calm the team. Option B (Video conferencing) fixes it."',
        'Explanation: Keywords: global program, distributed teams, team interaction, video conferencing. For a global program where distributed teams need to collaborate effectively, video conferencing provides the richest communication medium available for virtual meetings — enabling facial expressions, real-time dialogue, and a sense of presence that phone, email, and chat cannot replicate. This supports the team interaction and relationship-building essential for program coordination. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    # Q1362
    (
        'Explanation: Need: guide and calm the team. Option B (Request the team to implement the compliance.) fixes it."',
        'Explanation: Keywords: compliance gap, mandatory regulation, product release, regulatory responsibility. When a mandatory compliance feature is found to be missing near product release, the project manager cannot seek exceptions, descope the requirement, or release without it. The responsible action is to request the team to implement the compliance feature before release, ensuring the product meets its regulatory obligations even if it delays the go-live date. (PMBOK Guide) – Seventh Edition, 2021, p. 25, \'Be a Diligent, Respectful, and Caring Steward\'"'
    ),
    # Q1363
    (
        'Explanation: Need: listen to people needs. Option D (Produce a value-added product for the customer in each phase of the project.) fixes it."',
        'Explanation: Keywords: backlog prioritization, product owner, iterative value delivery, phase-by-phase delivery. When a project team is prioritizing the product backlog in the initiating phase, the goal is to structure delivery so that value-added increments are produced in each project phase rather than only at the end. This iterative approach ensures stakeholders see progress throughout the project and that feedback can shape future phases. (PMBOK Guide) – Seventh Edition, 2021, p. 32, \'Focus on Value\'"'
    ),
    # Q1364
    (
        'Explanation: Need: keep plans flexible. Option C (Have a direct talk with the functional manager to understand the reasons behind their attitude.) fixes it."',
        'Explanation: Keywords: resource release, functional manager resistance, direct communication, understanding barriers. When a functional manager consistently makes excuses about not releasing requested staff, the project manager must address the issue directly and privately before escalating. A direct conversation to understand the functional manager\'s specific concerns or constraints provides the information needed to find a workable solution and preserve the working relationship. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    # Q1365
    (
        'Explanation: Need: keep plans flexible. Option C (Consult the risk register for an appropriate planned risk response and implement.) fixes it."',
        'Explanation: Keywords: risk materialization, planned risk response, contingency plan, technical resource absence. When a pre-identified risk occurs — such as a critical technical resource becoming unavailable — the project manager should consult the risk register for the pre-defined response plan and implement it. Having a planned response means the team is executing a decision made calmly during planning rather than improvising under pressure. (PMBOK Guide) – Seventh Edition, 2021, p. 46, \'Optimize Risk Responses\'"'
    ),
    # Q1366
    (
        'Explanation: Need: listen to people needs. Option C (Incorrect communication techniques applied during implementation) fixes it."',
        'Explanation: Keywords: communication failure, paired work, information sharing, root cause. When important information is not shared properly among team members working in pairs and this leads to delivery failure, the root cause is the use of incorrect communication techniques during implementation. The working arrangement and task assignments were not the problem — the lack of appropriate communication protocols and tools for sharing information between pairs was the underlying cause. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    # Q1367
    (
        'Explanation: Need: listen to people needs. Option B (Review budget-related lessons learned from similar projects.) fixes it."',
        'Explanation: Keywords: budget estimation, new project manager, lessons learned, similar projects. When a new project manager joins an organization and must estimate a budget for a recurring customer project, the most valuable source of guidance is the organization\'s historical budget data from similar projects. Reviewing budget-related lessons learned provides calibrated estimates based on actual experience, which is far more reliable than estimating without organizational context. (PMBOK Guide) – Seventh Edition, 2021, p. 40, \'Tailor Based on Context\'"'
    ),
    # Q1368
    (
        'Explanation: Need: guide and calm the team. Option D (4) fixes it."',
        'Explanation: Keywords: sprint velocity, story points, release planning, iteration calculation. When the team has a velocity of 10 story points per sprint and the total release contains approximately 40 story points of features, four sprints are required to complete the release. Release planning in agile uses velocity as the basis for estimating how many iterations will be needed to deliver the agreed scope within the team\'s known capacity. (PMBOK Guide) – Seventh Edition, 2021, p. 32, \'Focus on Value\'"'
    ),
    # Q1369
    (
        'Explanation: Need: listen to people needs. Option B (Escalate the risk to the project sponsor) fixes it."',
        'Explanation: Keywords: currency instability, budget risk, escalation, project sponsor. When currency volatility creates a significant budget risk that is beyond the project manager\'s authority or resources to manage independently, escalating the risk to the project sponsor is the appropriate action. The sponsor is positioned to make organizational decisions — such as securing hedging strategies, adjusting funding, or renegotiating contract terms — that the project manager cannot authorize alone. (PMBOK Guide) – Seventh Edition, 2021, p. 46, \'Optimize Risk Responses\'"'
    ),
    # Q1370
    (
        "Explanation: Need: listen to people needs. Option C (Use the Perform Integrated Change Control process and submit this to the change control board (CCB) for approval.) fixes it.\"",
        "Explanation: Keywords: change control, minor scope change, CCB, authorization uncertainty. When a project manager is uncertain whether they have authority to approve a change, even a minor one, the correct action is to submit it through the Perform Integrated Change Control process. The CCB exists precisely to ensure all changes are evaluated, authorized, and documented through the appropriate governance mechanism, regardless of the perceived size of the change. (PMBOK Guide) – Seventh Edition, 2021, p. 50, 'Enable Change to Achieve the Envisioned Future State'\""
    ),
    # Q1371
    (
        "Explanation: Need: guide and calm the team. Option B (Request the team to initiate a change request to execute the contract.) fixes it.\"",
        "Explanation: Keywords: contract timing, early execution, change request, plan deviation. When a contract that was planned for a specific point in the project schedule is needed earlier than originally planned, this represents a deviation from the project plan that must be managed through the formal change control process. Requesting the team to initiate a change request ensures the early contract execution is properly authorized and documented before proceeding. (PMBOK Guide) – Seventh Edition, 2021, p. 50, 'Enable Change to Achieve the Envisioned Future State'\""
    ),
    # Q1372
    (
        'Explanation: Need: listen to people needs. Option A (Engage key stakeholders to complete and deliver lessons learned.) fixes it."',
        'Explanation: Keywords: project closure, lessons learned, knowledge capture, organizational learning. As a project approaches closure with strong results, the project manager\'s priority should be to engage key stakeholders in completing and documenting lessons learned. This captures the institutional knowledge gained during the project in a way that will benefit the organization and the next project — particularly valuable since the same project manager has been asked to lead a similar engagement. (PMBOK Guide) – Seventh Edition, 2021, p. 48, \'Embrace Adaptability and Resiliency\'"'
    ),
    # Q1373
    (
        'Explanation: Need: keep plans flexible. Option C (Ensured that regulatory compliance was considered in the quality management plan.) fixes it."',
        'Explanation: Keywords: regulatory compliance, quality management plan, import restriction, stewardship. When equipment procurement decisions are influenced by cost savings without considering regulatory compliance, the result can be costly delays at point of delivery. Ensuring that regulatory compliance requirements — including import restrictions — are addressed in the quality management plan would have surfaced the restriction before the purchase was made, preventing the customs blockage entirely. (PMBOK Guide) – Seventh Edition, 2021, p. 25, \'Be a Diligent, Respectful, and Caring Steward\'"'
    ),
    # Q1374
    (
        'Explanation: Need: guide and calm the team. Option C (Conducted periodic reviews with the manager on resource availability.) fixes it."',
        'Explanation: Keywords: installation delay, resource capacity, periodic reviews, proactive monitoring. A resource capacity issue that causes a critical project delay could have been identified and addressed earlier through regular, structured reviews with the responsible manager. Conducting periodic reviews on resource availability creates a monitoring mechanism that surfaces capacity constraints before they become schedule-impacting issues. (PMBOK Guide) – Seventh Edition, 2021, p. 34, \'Recognize, Evaluate, and Respond to System Interactions\'"'
    ),
    # Q1375
    (
        'Explanation: Need: listen to people needs. Option D (Obtain formal acceptance for the completed work and submit a change request.) fixes it."',
        'Explanation: Keywords: project closure, scope extension request, formal acceptance, change request. When a client refuses to sign the closure report because they want additional scope not in the original agreement, the project manager must separate the two actions: obtain formal acceptance for the completed work as agreed, then submit a change request or initiate a new project for the additional scope. Bundling acceptance with new scope requests prevents proper project closure and creates ambiguity about what was actually delivered. (PMBOK Guide) – Seventh Edition, 2021, p. 50, \'Enable Change to Achieve the Envisioned Future State\'"'
    ),
    # Q1376
    (
        'Explanation: Need: guide and calm the team. Option A (A minimum viable product (MVP) should have been released to get feedback from the market.) fixes it."',
        'Explanation: Keywords: competitive market, MVP, early market release, feedback loop. When a competitor launches a similar product before the project team\'s product is ready, the root cause is often a failure to release an MVP early enough to establish a market presence and gather feedback. Releasing an MVP would have provided early customer validation and market visibility before the competition, reducing the risk of being overtaken in the market. (PMBOK Guide) – Seventh Edition, 2021, p. 32, \'Focus on Value\'"'
    ),
    # Q1377
    (
        'Explanation: Need: listen to people needs. Option A (Hybrid) fixes it."',
        'Explanation: Keywords: multiphased project, strict regulation, hybrid approach, flexibility. When some project phases are governed by strict regulatory requirements that demand complete upfront planning while others allow for scope and schedule flexibility, neither a fully predictive nor a fully agile approach is appropriate on its own. A hybrid approach allows the project manager to apply predictive methods where required by regulation and adaptive methods where the sponsor wants the ability to respond to new information. (PMBOK Guide) – Seventh Edition, 2021, p. 40, \'Tailor Based on Context\'"'
    ),
    # Q1378
    (
        'Explanation: Need: watch risks early. Option D (Evaluate the risks constantly and reprioritize work as the project progresses.) fixes it."',
        'Explanation: Keywords: innovation project, high uncertainty, agile risk management, continuous evaluation. In a high-uncertainty innovation project, risk conditions change rapidly and cannot be managed through a static register reviewed periodically. The agile approach to risk management is to continuously evaluate risks and reprioritize work as the project progresses, ensuring that the team\'s focus remains aligned with the most current risk landscape at all times. (PMBOK Guide) – Seventh Edition, 2021, p. 46, \'Optimize Risk Responses\'"'
    ),
    # Q1379
    (
        'Explanation: Need: listen to people needs. Option B (Invite stakeholders to discuss the impact of adding the regulatory feature.) fixes it."',
        'Explanation: Keywords: regulatory feature, missing backlog item, fixed release date, stakeholder discussion. When a significant mandatory feature is discovered missing from the backlog mid-project with a fixed release date, the project manager cannot simply add it without assessing the impact. Inviting stakeholders to discuss the impact enables an informed decision about scope, schedule, and resource adjustments needed to accommodate the new work within the existing constraints. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    # Q1380
    (
        'Explanation: Need: guide and calm the team. Option C (Empower the team to develop the necessary skills to move the project forward independently.) fixes it."',
        'Explanation: Keywords: servant leader, team empowerment, PM capacity, organizational transformation. When a project manager\'s time is divided across multiple projects as part of an organizational transformation, the servant leader\'s response is to prepare each team to function more independently by empowering them to develop the skills needed to move forward on their own. This builds team capability and resilience rather than creating a dependency on the project manager\'s constant involvement. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    # Q1381
    (
        'Explanation: Need: listen to people needs. Option A (Work with the stakeholders to create a prioritized backlog and release a roadmap.) fixes it."',
        'Explanation: Keywords: aggressive deadline, stakeholder alignment, prioritized backlog, release roadmap. When the CEO\'s 6-month deadline conflicts with the project\'s estimated 12-month duration, the project manager must work with all stakeholders to prioritize the backlog, identify which features deliver the most value by the deadline, and create a release roadmap that reflects a realistic plan. This brings stakeholder needs and expectations into alignment with what is actually achievable. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    # Q1382
    (
        'Explanation: Need: listen to people needs. Option D (Invite a consultant to review the process in order not to repeat the same issue and share the results with the team.) fixes it."',
        'Explanation: Keywords: process failure, data loss, consultant review, lessons learned during execution. When a process failure causes significant impact — such as user data loss — during an active deployment, the project manager cannot defer the analysis to a final lessons learned session. Inviting an external consultant to review the process immediately prevents the same failure from recurring in the remaining deployment, and sharing findings with the team builds quality awareness in real time. (PMBOK Guide) – Seventh Edition, 2021, p. 42, \'Build Quality into Processes and Deliverables\'"'
    ),
    # Q1383
    (
        'Explanation: Need: listen to people needs. Option A (Meet with the new project sponsor to review the current project scope and the requested changes.) fixes it."',
        'Explanation: Keywords: new sponsor, scope change request, sponsor engagement, project continuity. When a new project sponsor joins a politically significant project and requests changes the previous sponsor rejected, the project manager must meet with the new sponsor to review the current scope and evaluate the requested changes carefully. This engagement respects the new sponsor\'s authority while ensuring changes are assessed in the context of committed deliverables and stakeholder expectations. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    # Q1384
    (
        'Explanation: Need: listen to people needs. Option B (Arrange a luncheon for all team members and include team-building sessions.) fixes it."',
        'Explanation: Keywords: team reward, project stress, overtime, team-building. After a period of intense effort and interpersonal friction, a monetary award should be used to reinforce team cohesion rather than distributed as individual recognition. Arranging a team luncheon with team-building sessions addresses the relationship tensions that developed during the high-pressure period and creates a shared positive experience that rebuilds collaboration. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    # Q1385
    (
        'Explanation: Need: listen to people needs. Option D (An incremental approach with a minimum viable product (MVP).) fixes it."',
        'Explanation: Keywords: cryptocurrency payment, volatile value, iterative scope adjustment, incremental delivery, MVP. When a project\'s payment is tied to a volatile asset and scope must be adjusted at each iteration to match the asset\'s current value, an incremental delivery approach starting with an MVP is most appropriate. This model maximizes value delivery within the available funding at each checkpoint, ensuring the highest-priority features are built first and the project halts gracefully when the agreed value is reached. (PMBOK Guide) – Seventh Edition, 2021, p. 32, \'Focus on Value\'"'
    ),
    # Q1386
    (
        'Explanation: Need: guide and calm the team. Option C (Ask the team to define a team charter and agree on core working hours.) fixes it."',
        'Explanation: Keywords: staggered schedules, overlap time, core working hours, team charter. When team members have different start times that limit collaborative overlap, the solution is to establish shared core working hours through a team charter that all members agree to. This creates a predictable window for synchronous collaboration, standups, and problem-solving without requiring all members to work identical schedules. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    # Q1387
    (
        'Explanation: Need: guide and calm the team. Option A (Provide the team with support to solve their own problems.) fixes it."',
        'Explanation: Keywords: multinational team, delivery challenges, servant leadership, team empowerment. A servant leader\'s primary response to a team struggling with their deliverables is to provide the support, resources, and guidance needed for the team to solve their own problems. This approach builds team capability and autonomy rather than creating dependency on the project manager for every solution. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    # Q1388
    (
        'Explanation: Need: listen to people needs. Option B (Invite the stakeholders to discuss a new prioritization.) fixes it."',
        'Explanation: Keywords: regulatory feature, iteration capacity, reprioritization, stakeholder decision. When a mandatory regulatory feature is added in the 5th of 6 iterations and it exceeds remaining capacity, the decision about how to accommodate it requires stakeholder input. Inviting stakeholders to discuss reprioritization ensures the response is made with full awareness and authorization of the parties whose commitments will be affected by any scope or schedule adjustments. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    # Q1389 multi-select
    (
        'Explanation: Need: listen to people needs. Options B and C (Confirm the issues truly exist by conducting a survey and other analyses that may detect the real issue.; Deploy solutions that will track, prioritize, and resolve queries as soon as possible.) work together."',
        'Explanation: Keywords: customer queries, service overload, root cause analysis, systematic solutions. Addressing an overwhelming volume of unresolved customer queries requires both confirming the true nature of the problem and implementing operational solutions. A survey and supporting analysis provides evidence-based clarity on what is really driving the issue, while deploying systematic tracking and prioritization tools addresses the operational gap that is allowing queries to accumulate unresolved. (PMBOK Guide) – Seventh Edition, 2021, p. 34, \'Recognize, Evaluate, and Respond to System Interactions\'"'
    ),
    # Q1390
    (
        'Explanation: Need: listen to people needs. Option C (Perform a stakeholder analysis and update the communications management plan to reflect the new situation.) fixes it."',
        'Explanation: Keywords: new stakeholder, stakeholder analysis, communications management plan, organizational change. When a new organizational unit is created mid-project and its manager requests inclusion in project communications, the project manager must perform a stakeholder analysis to understand the new stakeholder\'s interests, influence, and information needs before updating the communications management plan. This ensures the new stakeholder is engaged appropriately rather than simply added to a distribution list. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    # Q1391
    (
        'Explanation: Need: keep plans flexible. Option C (Acknowledge the project closure criteria has been met and release the remaining budget and resources.) fixes it."',
        'Explanation: Keywords: project closure, excess budget, scope completeness, resource release. When a project has met its agreed-upon requirements and closure criteria, it should be closed — regardless of remaining time, budget, or stakeholder requests for additional features. Acknowledging that closure criteria have been met and releasing the remaining budget and resources ensures that organizational resources are available for other priorities rather than being consumed by gold-plating. (PMBOK Guide) – Seventh Edition, 2021, p. 25, \'Be a Diligent, Respectful, and Caring Steward\'"'
    ),
    # Q1392
    (
        'Explanation: Need: keep plans flexible. Option C (Introduce the agile aspect to the director and agree on a solution.) fixes it."',
        'Explanation: Keywords: predictive mindset, agile reporting, director expectations, collaborative adaptation. When a new stakeholder with a predictive background requests reporting that does not fit an agile project\'s cadence, the project manager must educate them on the agile approach and then collaborate to find a reporting solution that meets their information needs within the agile framework. Unilaterally refusing or simply complying without discussion both fail to address the underlying communication gap. (PMBOK Guide) – Seventh Edition, 2021, p. 40, \'Tailor Based on Context\'"'
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
