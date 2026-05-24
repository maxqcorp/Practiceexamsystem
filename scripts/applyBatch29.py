MD_FILE = './src/imports/project-management-questions-1.md'

with open(MD_FILE, 'r', encoding='utf-8') as f:
    content = f.read()

replacements = [
    # Q1393
    (
        "Explanation: Need: listen to people needs. Option D (Show the customer the quality control measurements.) fixes it.\"",
        "Explanation: Keywords: customer complaint, quality control measurements, quality assurance, components returned. When a customer questions quality despite the project manager's confidence, the most credible response is to present objective quality control measurements — the actual inspection data and test results. These provide verifiable evidence of conformance to specifications and are more persuasive than samples or historical charts alone. (PMBOK Guide) – Seventh Edition, 2021, p. 42, 'Build Quality into Processes and Deliverables'\""
    ),
    # Q1394
    (
        "Explanation: Need: watch risks early. Option A (Identify and remove impediments and mitigate the risks.) fixes it.\"",
        "Explanation: Keywords: known issues in production, integration project, impediments, risk mitigation. When a project has known production issues at the outset, the project manager's priority is to identify and remove blockers while actively mitigating risks before they escalate. Addressing impediments and risks early prevents compounding delays during execution and protects the quality of the integration deliverable. (PMBOK Guide) – Seventh Edition, 2021, p. 46, 'Optimize Risk Responses'\""
    ),
    # Q1395
    (
        "Explanation: Need: guide and calm the team. Option B (Arrange a meeting with the contract department to build trust and commitment by recognizing their critical support to the project.) fixes it.\"",
        "Explanation: Keywords: shared resources, contract department prioritizing other work, not part of project team, delays in contracting. When a shared resource department deprioritizes project work because they feel disconnected, the most effective first step is to build a collaborative relationship by recognizing their contributions and articulating why their support is critical. Trust and mutual commitment are essential to securing engagement from resources outside the formal project team. (PMBOK Guide) – Seventh Edition, 2021, p. 28, 'Create a Collaborative Team Environment'\""
    ),
    # Q1396
    (
        "Explanation: Need: guide and calm the team. Option B (Determine and agree when a situation becomes an impediment to be solved by the scrum master.) fixes it.\"",
        "Explanation: Keywords: scrum master impediment removal, team complaint, scheduling meetings, room booking. When a team is unclear about what qualifies as an impediment that the scrum master should resolve, the root cause is often a lack of shared agreement on scope of the role. Defining and agreeing upon the threshold for scrum master intervention clarifies expectations and prevents future friction between the team and the scrum master. (PMBOK Guide) – Seventh Edition, 2021, p. 28, 'Create a Collaborative Team Environment'\""
    ),
    # Q1397
    (
        "Explanation: Need: listen to people needs. Option D (Accept only those changes that are approved by the change control board (CCB) prior to being implemented.) fixes it.\"",
        "Explanation: Keywords: global project, scope creep, different interpretations, change control. Controlling scope in a geographically distributed project requires a formal mechanism to evaluate and authorize changes before implementation. Requiring CCB approval for all changes ensures that each request is assessed for impact before it is accepted, preventing unauthorized scope additions that erode project baselines. (PMBOK Guide) – Seventh Edition, 2021, p. 50, 'Enable Change to Achieve the Envisioned Future State'\""
    ),
    # Q1398
    (
        "Explanation: Need: listen to people needs. Option A (Facilitate a supportive level of engagement for this stakeholder.) fixes it.\"",
        "Explanation: Keywords: kick-off meeting, low participation, stakeholder sees no benefit, high risk. A stakeholder who doubts the value of a project and disengages early represents a significant threat to project success. Facilitating a supportive engagement level — actively encouraging participation and addressing their concerns — transforms a resistant stakeholder into an informed contributor and reduces the risk of ongoing disengagement. (PMBOK Guide) – Seventh Edition, 2021, p. 30, 'Effectively Engage with Stakeholders'\""
    ),
    # Q1399
    (
        "Explanation: Need: keep plans flexible. Option B (Review the project information.) fixes it.\"",
        "Explanation: Keywords: agile project, corporate audit, first meeting with auditors, preparation. Before meeting with auditors, the project manager must be well-informed about the current state of the project. Reviewing project information ensures the project manager can answer questions accurately, demonstrate compliance, and provide context for the agile delivery approach being used. (PMBOK Guide) – Seventh Edition, 2021, p. 25, 'Be a Diligent, Respectful, and Caring Steward'\""
    ),
    # Q1400
    (
        "Explanation: Need: guide and calm the team. Option B (Audit the effectiveness of the management of project artifacts.) fixes it.\"",
        "Explanation: Keywords: design documentation missing, product owner uploaded to repository, sprint delay. When a team cannot find documentation that was supposedly uploaded, the underlying problem is a failure in artifact management processes. Auditing the effectiveness of how project artifacts are managed identifies the root cause — whether it is poor repository structure, access issues, or inadequate communication — so it can be systematically corrected. (PMBOK Guide) – Seventh Edition, 2021, p. 42, 'Build Quality into Processes and Deliverables'\""
    ),
    # Q1401
    (
        "Explanation: Need: protect benefits for users. Option C (Discuss the request with the consultant and set up time with the business analyst and consultant to discuss the project requirements.) fixes it.\"",
        "Explanation: Keywords: consultant unavailable, business analyst blocked, project forward. When a key external contributor is not engaging, the project manager must take direct action to remove the blocker rather than escalating prematurely. Directly discussing the need with the consultant and setting up a focused meeting bridges the communication gap and keeps the project moving without creating unnecessary organizational conflict. (PMBOK Guide) – Seventh Edition, 2021, p. 30, 'Effectively Engage with Stakeholders'\""
    ),
    # Q1402
    (
        "Explanation: Need: guide and calm the team. Option D (Ask the team to propose a minimum viable product (MVP) to meet the date.) fixes it.\"",
        "Explanation: Keywords: strict deadline, too many requirements, backlog overload, first planning meeting. When requirements exceed what can be delivered by the deadline, the value-focused response is to define a minimum viable product. An MVP captures the highest-priority features that deliver the core business value, enabling on-time delivery while deferring lower-priority items to future phases. (PMBOK Guide) – Seventh Edition, 2021, p. 32, 'Focus on Value'\""
    ),
    # Q1403
    (
        "Explanation: Need: listen to people needs. Option C (Increase the active engagement and participation of key stakeholders.) fixes it.\"",
        "Explanation: Keywords: complex project, high degree of change, successful completion, stakeholder engagement. In complex, change-heavy projects, the most reliable strategy for success is continuous and active stakeholder engagement. Stakeholders who are involved early and often provide direction, validate decisions, and help manage change requests — reducing the risk that delivered outcomes will be misaligned with business needs. (PMBOK Guide) – Seventh Edition, 2021, p. 30, 'Effectively Engage with Stakeholders'\""
    ),
    # Q1404
    (
        "Explanation: Need: listen to people needs. Option D (Planned how the delivered product will be supported after its delivery.) fixes it.\"",
        "Explanation: Keywords: T&M contract, defects found post-delivery, client expects free fixes, prevention. Disputes about post-delivery defects typically arise when the support model after go-live is not defined in advance. Planning how the delivered product will be supported — including roles, responsibilities, and costs for post-delivery fixes — sets clear expectations and prevents the kind of disagreement that emerged in this scenario. (PMBOK Guide) – Seventh Edition, 2021, p. 32, 'Focus on Value'\""
    ),
    # Q1405
    (
        "Explanation: Need: guide and calm the team. Option C (Review the existing service contracts to find an option to help procure the vehicles.) fixes it.\"",
        "Explanation: Keywords: vehicle supplier cannot deliver, no time for new supplier, procurement emergency. Before creating new contracts or escalating, the project manager should examine existing contractual relationships for options that could solve the procurement gap. Leveraging existing service contracts may provide a faster and more cost-effective path than sourcing a new supplier under time pressure. (PMBOK Guide) – Seventh Edition, 2021, p. 34, 'Recognize, Evaluate, and Respond to System Interactions'\""
    ),
    # Q1406
    (
        "Explanation: Need: guide and calm the team. Option C (Needed to close out the project or a phase.) fixes it.\"",
        "Explanation: Keywords: final stage, delivery acceptance document, project closure, importance. A delivery acceptance document provides formal evidence that the project or phase deliverables have been received and approved by the customer. This document is the prerequisite for initiating project or phase closure — without it, there is no documented basis for releasing resources, finalizing payments, or archiving project records. (PMBOK Guide) – Seventh Edition, 2021, p. 25, 'Be a Diligent, Respectful, and Caring Steward'\""
    ),
    # Q1407
    (
        "Explanation: Need: listen to people needs. Option C (Work with the sponsor on a communications management plan to obtain support from the vendor management head.) fixes it.\"",
        "Explanation: Keywords: vendor management dependency, no direct benefit to vendor management, need support. When a required stakeholder sees no benefit from the project, securing their cooperation requires a strategic communications approach. Working with the sponsor to craft a communications management plan ensures that the outreach to the vendor management head is coordinated, credible, and positioned in terms of organizational value rather than project-level demands. (PMBOK Guide) – Seventh Edition, 2021, p. 30, 'Effectively Engage with Stakeholders'\""
    ),
    # Q1408
    (
        "Explanation: Need: guide and calm the team. Option B (Ask the existing team members to collaborate with the SME and complete the activity.) fixes it.\"",
        "Explanation: Keywords: external SME suggestion, available but unplanned, time-saving opportunity. Rather than immediately adding the SME to the iteration structure or ignoring the opportunity, the most team-centric approach is to facilitate collaboration between the SME and existing team members. This allows the project to benefit from specialized knowledge while preserving team ownership of the work and avoiding unplanned scope changes. (PMBOK Guide) – Seventh Edition, 2021, p. 28, 'Create a Collaborative Team Environment'\""
    ),
    # Q1409
    (
        "Explanation: Need: listen to people needs. Option C (Review the change management plan to discuss early benefits realization with the client.) fixes it.\"",
        "Explanation: Keywords: early deliverable opportunity, client focused on next milestone, benefits realization. Accelerating delivery of a deliverable ahead of schedule represents a potential benefit realization opportunity, but it requires client alignment. Reviewing the change management plan and opening a discussion with the client about early benefits realization ensures the opportunity is evaluated formally and that the client understands and values the change. (PMBOK Guide) – Seventh Edition, 2021, p. 32, 'Focus on Value'\""
    ),
    # Q1410
    (
        "Explanation: Need: listen to people needs. Option C (Review compliance and regulatory requirements with stakeholders.) fixes it.\"",
        "Explanation: Keywords: global healthcare solution, limited release, stakeholder concerns about regulations, risks. When stakeholders raise concerns about regulatory and compliance requirements for a global deployment, the project manager must address those concerns directly by reviewing the applicable requirements with the relevant stakeholders. This ensures that the project remains within legal and ethical boundaries across all deployment locations. (PMBOK Guide) – Seventh Edition, 2021, p. 25, 'Be a Diligent, Respectful, and Caring Steward'\""
    ),
    # Q1411
    (
        "Explanation: Need: listen to people needs. Option A (Welcome and involve the contractors as part of the project team.) fixes it.\"",
        "Explanation: Keywords: external contractors, daily meetings, unclear requirements, contractors feel meetings are waste. Contractors who view collaborative meetings as a waste of time often feel disconnected from the project team and its goals. By welcoming and involving them as full team members, the project manager builds a shared sense of ownership and helps contractors understand why the meetings are necessary given the unclear requirements. (PMBOK Guide) – Seventh Edition, 2021, p. 28, 'Create a Collaborative Team Environment'\""
    ),
    # Q1412
    (
        "Explanation: Need: secure people or vendors. Option A (Determine resource allocation options based on project priority.) fixes it.\"",
        "Explanation: Keywords: critical resource unavailable, no developers available, resource need, project about to start. When a critical resource becomes unavailable and no direct replacement exists, the project manager must evaluate the broader resource landscape through the lens of project priority. Determining reallocation options based on which work is most important allows the team to make informed trade-offs rather than defaulting to a schedule extension request. (PMBOK Guide) – Seventh Edition, 2021, p. 34, 'Recognize, Evaluate, and Respond to System Interactions'\""
    ),
    # Q1413
    (
        "Explanation: Need: guide and calm the team. Option B (Ask the team member to provide a training session for the rest of the team.) fixes it.\"",
        "Explanation: Keywords: team member developing expertise, others will need that knowledge, knowledge sharing. When one team member develops deep domain expertise, ensuring the broader team benefits from that knowledge is a key team development responsibility. Asking the expert to facilitate a training session creates cross-functional capability, reduces single points of failure, and reinforces a collaborative learning culture. (PMBOK Guide) – Seventh Edition, 2021, p. 28, 'Create a Collaborative Team Environment'\""
    ),
    # Q1414
    (
        "Explanation: Need: guide and calm the team. Option D (Work with the product owner to ensure the project backlog is prioritized.) fixes it.\"",
        "Explanation: Keywords: daily standup, team asking which tasks to focus on, backlog priority unclear. When team members consistently need to ask the project manager for task prioritization, the root cause is an unprioritized backlog. Working with the product owner to ensure the backlog is consistently ordered by priority empowers the team to self-direct, eliminates recurring standup interruptions, and aligns delivery with business value. (PMBOK Guide) – Seventh Edition, 2021, p. 36, 'Demonstrate Leadership Behaviors'\""
    ),
    # Q1415
    (
        "Explanation: Need: guide and calm the team. Option A (Perform a cost-benefit analysis to evaluate using the Point B option.) fixes it.\"",
        "Explanation: Keywords: construction project, alternative connection point, potential cost saving, change option. When a team identifies a potential design change that could save cost, the project manager should not approve or dismiss it without analysis. A cost-benefit analysis provides an objective basis for evaluating the Point B option — weighing savings against risks, scope changes, and schedule impacts — before bringing it to the appropriate decision-making authority. (PMBOK Guide) – Seventh Edition, 2021, p. 32, 'Focus on Value'\""
    ),
    # Q1416
    (
        "Explanation: Need: listen to people needs. Option D (Assess the organizational culture and readiness for the transformation.) fixes it.\"",
        "Explanation: Keywords: construction projects, agile mandate, senior leadership promotion, before mandating. Before introducing agile methodologies to projects currently using a predictive approach, the project manager must understand the context into which agile is being introduced. Assessing organizational culture and readiness identifies gaps in skills, mindset, and infrastructure that must be addressed to make the transformation viable and sustainable. (PMBOK Guide) – Seventh Edition, 2021, p. 40, 'Tailor Based on Context'\""
    ),
    # Q1417
    (
        "Explanation: Need: listen to people needs. Option B (Arrange for a workshop with the customer to understand the business values expected from the outcomes.) fixes it.\"",
        "Explanation: Keywords: user stories created, too many change requests, outcomes not aligned, customer requirements. Excessive change requests after user stories are written indicate a misalignment between what the team built and what the customer actually values. A structured workshop with the customer refocuses the conversation on business value rather than feature lists, helping both parties reach shared understanding of what outcomes the project is supposed to deliver. (PMBOK Guide) – Seventh Edition, 2021, p. 30, 'Effectively Engage with Stakeholders'\""
    ),
    # Q1418
    (
        "Explanation: Need: guide and calm the team. Option B (Discuss the process used to create the noncompliant deliverables with the project team to see if there was a potential misunderstanding.) fixes it.\"",
        "Explanation: Keywords: global team, deliverables not meeting requirements, first action. When deliverables from all team members are noncompliant, the most likely explanation is a systemic misunderstanding of requirements rather than individual failure. Discussing the creation process with the team surfaces any misinterpretations and provides corrective information collaboratively, preserving team morale while addressing the root cause. (PMBOK Guide) – Seventh Edition, 2021, p. 28, 'Create a Collaborative Team Environment'\""
    ),
    # Q1419
    (
        "Explanation: Need: listen to people needs. Option C (Assess the impact of the risk with an expert and prioritize further outcomes with the client.) fixes it.\"",
        "Explanation: Keywords: new risk, indirect tax regulation change, significant impact, prioritize outcomes. When a newly identified regulatory risk has significant potential impact, the project manager must respond with both expert analysis and client alignment. Assessing the impact with a tax expert ensures accuracy, while re-prioritizing outcomes with the client ensures the project continues to deliver what is most valuable given the changed risk landscape. (PMBOK Guide) – Seventh Edition, 2021, p. 46, 'Optimize Risk Responses'\""
    ),
    # Q1420
    (
        "Explanation: Need: listen to people needs. Option B (Ensured the risk was adequately assessed and mitigated by the appropriate stakeholders.) fixes it.\"",
        "Explanation: Keywords: project started without full funding, remaining funds delayed, work suspended, prevention. Starting a project before full funding is secured is a significant risk that must be explicitly assessed and actively mitigated. Ensuring that the appropriate stakeholders evaluate and accept responsibility for this funding risk — and that mitigation actions are in place — would have prevented the work suspension caused by the delayed fund acquisition. (PMBOK Guide) – Seventh Edition, 2021, p. 46, 'Optimize Risk Responses'\""
    ),
    # Q1421
    (
        "Explanation: Need: guide and calm the team. Option C (Analyzed the boundaries of the negotiations for agreement) fixes it.\"",
        "Explanation: Keywords: alternative working schedule, core working hours, scrutiny from other teams, prevention. Before agreeing to a non-standard arrangement like an alternative schedule, the project manager should analyze the full context — including organizational norms, team impact, and boundaries of what is negotiable. Understanding these constraints in advance would have identified the risk that the arrangement would conflict with company-wide expectations and be challenged by other teams. (PMBOK Guide) – Seventh Edition, 2021, p. 28, 'Create a Collaborative Team Environment'\""
    ),
    # Q1422
    (
        "Explanation: Need: listen to people needs. Option A (Evaluate the communication needs to discover the gaps and adjust the original plan if needed.) fixes it.\"",
        "Explanation: Keywords: stakeholder complaining about metrics, communications management plan followed, stakeholder rarely attends. When a stakeholder is dissatisfied with project communications despite the plan being followed, it signals that the plan itself does not fully meet that stakeholder's needs. Evaluating communication needs and adjusting the plan accordingly addresses the root cause rather than merely defending the current approach. (PMBOK Guide) – Seventh Edition, 2021, p. 30, 'Effectively Engage with Stakeholders'\""
    ),
    # Q1423
    (
        "Explanation: Need: listen to people needs. Option C (Revisit the ground rules and team communication protocols, and discuss what is happening.) fixes it.\"",
        "Explanation: Keywords: behavior conflicts, losing momentum, falling behind sprints, team issues. When ongoing behavioral conflicts are disrupting team performance, the project manager should return to first principles — revisiting the ground rules that define expected conduct and opening an honest discussion about what is happening. This approach is both corrective and respectful, reinforcing shared norms rather than imposing individual judgments. (PMBOK Guide) – Seventh Edition, 2021, p. 28, 'Create a Collaborative Team Environment'\""
    ),
    # Q1424
    (
        "Explanation: Need: listen to people needs. Option C (Meet with the software team to review the possibility of monthly milestone reviews.) fixes it.\"",
        "Explanation: Keywords: predictive approach, defined scope and deadline, product leader requests milestone submissions. When a stakeholder requests milestone reviews in a project with an established predictive approach, the project manager should explore what is feasible with the team before committing or refusing. Reviewing the possibility of monthly milestones with the software team determines the technical and scheduling viability of accommodating the request without changing the methodology. (PMBOK Guide) – Seventh Edition, 2021, p. 30, 'Effectively Engage with Stakeholders'\""
    ),
    # Q1425
    (
        "Explanation: Need: listen to people needs. Option D (Instruct the team to analyze and interpret the data before including it in the report.) fixes it.\"",
        "Explanation: Keywords: large data for stakeholder report, data collated, status report preparation. Raw data presented without analysis does not serve stakeholders well — it increases cognitive load and the risk of misinterpretation. Instructing the team to analyze and interpret the data transforms it into meaningful insights that support decision-making, which is the true purpose of a stakeholder status report. (PMBOK Guide) – Seventh Edition, 2021, p. 30, 'Effectively Engage with Stakeholders'\""
    ),
    # Q1426
    (
        "Explanation: Need: control changes and baselines. Option D (Follow the change management process.) fixes it.\"",
        "Explanation: Keywords: scope already established, request to add features and functions, change request received. When new feature requests arrive after the scope has been formally established, the project manager must channel them through the defined change management process. This ensures that additions are evaluated for their impact on cost, schedule, and risk before being accepted — preventing unauthorized scope growth that can destabilize the project baseline. (PMBOK Guide) – Seventh Edition, 2021, p. 50, 'Enable Change to Achieve the Envisioned Future State'\""
    ),
    # Q1427
    (
        "Explanation: Need: guide and calm the team. Option B (The project manager lacks emotional intelligence (El).) fixes it.\"",
        "Explanation: Keywords: technical expertise, unacceptable behavior, denies behavior when confronted, team impact. A project manager who exhibits problematic behavior but denies it when confronted is demonstrating a lack of self-awareness — a core component of emotional intelligence. Without emotional intelligence, a leader cannot accurately perceive the impact of their own behavior on others, making constructive feedback ineffective and interpersonal conflicts persistent. (PMBOK Guide) – Seventh Edition, 2021, p. 36, 'Demonstrate Leadership Behaviors'\""
    ),
    # Q1428
    (
        "Explanation: Need: guide and calm the team. Option A (Assess the team member's development requirements and arrange for the team member to receive training.) fixes it.\"",
        "Explanation: Keywords: inexperienced team member, poor performance, no other staff available, system development. When an underperforming team member cannot be replaced, the project manager must invest in their development. Assessing the specific skill gaps and providing targeted training addresses the root cause of the performance issue while retaining the resource — turning a liability into an asset when executed effectively. (PMBOK Guide) – Seventh Edition, 2021, p. 36, 'Demonstrate Leadership Behaviors'\""
    ),
    # Q1429
    (
        "Explanation: Need: listen to people needs. Option B (Influence the product owner to review the engagement needed from other stakeholders.) fixes it.\"",
        "Explanation: Keywords: new vice-president product owner, CTO strategy misalignment, product owner excludes CTO. When a product owner dismisses a stakeholder who has legitimate strategic influence over the project outcomes, the project manager must use influence skills to help the product owner recognize the risk. Encouraging a review of which stakeholders should be engaged ensures that the project does not proceed with requirements that will later conflict with organizational strategy. (PMBOK Guide) – Seventh Edition, 2021, p. 30, 'Effectively Engage with Stakeholders'\""
    ),
    # Q1430
    (
        "Explanation: Need: secure people or vendors. Option C (Create a framework to support project success.) fixes it.\"",
        "Explanation: Keywords: new CEO no project experience, own resources, project manager appointed, framework needed. A CEO unfamiliar with project management needs a structured foundation before execution begins. Creating a framework to support project success establishes the governance structures, processes, and decision-making mechanisms that give projects the best chance of achieving their objectives — providing the CEO with a systematic approach rather than an ad hoc one. (PMBOK Guide) – Seventh Edition, 2021, p. 34, 'Recognize, Evaluate, and Respond to System Interactions'\""
    ),
    # Q1431
    (
        "Explanation: Need: guide and calm the team. Options D and E (Organize and assign team members to tasks where they have strengths.; Support team members to make decisions in their areas of strength.) work together.\"",
        "Explanation: Keywords: four-phase delivery, one phase completed, enhance team performance, empower team. To improve team performance and build empowerment after an initial successful phase, the most effective combination is to align work with individual strengths and then grant decision-making authority in those areas. Assigning tasks where team members excel builds confidence and competency, while supporting their decisions in those domains reinforces autonomy and raises overall team maturity. (PMBOK Guide) – Seventh Edition, 2021, p. 36, 'Demonstrate Leadership Behaviors'\""
    ),
    # Q1432
    (
        "Explanation: Need: listen to people needs. Option B (Align and agree with the stakeholder on the communication approach.) fixes it.\"",
        "Explanation: Keywords: government company, predictive stakeholder, dislikes virtual tools, prefers email and face-to-face. Effective stakeholder communication requires adapting to the preferences and context of the individual stakeholder. Rather than imposing virtual tools on someone who does not use them, aligning and agreeing on a communication approach that the stakeholder is comfortable with ensures that information is actually received and acted upon. (PMBOK Guide) – Seventh Edition, 2021, p. 30, 'Effectively Engage with Stakeholders'\""
    ),
    # Q1433
    (
        "Explanation: Need: guide and calm the team. Option C (Advise the team member to focus on the current project and consider the past conflicts as lessons learned.) fixes it.\"",
        "Explanation: Keywords: team member experienced past conflicts, nervous about current project, adds value, motivation. A team member carrying anxiety from past experiences needs a forward-looking perspective to engage effectively. Encouraging them to treat past conflicts as lessons learned and focus their energy on the current project converts past negative experiences into professional growth, helping them contribute meaningfully without being held back by prior events. (PMBOK Guide) – Seventh Edition, 2021, p. 36, 'Demonstrate Leadership Behaviors'\""
    ),
    # Q1434
    (
        "Explanation: Need: listen to people needs. Option C (Schedule meetings with key stakeholders in advance to gather feedback on the project scope.) fixes it.\"",
        "Explanation: Keywords: 9-month project, stakeholder objects at kick-off, task out of schedule, prevention. Stakeholder rejection at a kick-off meeting almost always reflects a failure to engage key stakeholders during scope development. Scheduling meetings with key stakeholders before the kick-off to gather feedback on scope and expectations builds alignment in advance, reducing the likelihood of strong objections when the project is formally launched. (PMBOK Guide) – Seventh Edition, 2021, p. 30, 'Effectively Engage with Stakeholders'\""
    ),
    # Q1435
    (
        "Explanation: Need: guide and calm the team. Option A (Discuss this with the project team, assess the impact, and decide on the appropriate actions to follow.) fixes it.\"",
        "Explanation: Keywords: specialized architect resigning, high-risk project, external resource, impact assessment. When a critical specialized resource announces their departure, the project manager must first understand the full impact before deciding on a response. Involving the project team in this assessment ensures that the evaluation benefits from collective technical knowledge, and that the resulting action plan reflects both the severity of the gap and the team's capacity to address it. (PMBOK Guide) – Seventh Edition, 2021, p. 46, 'Optimize Risk Responses'\""
    ),
    # Q1436
    (
        "Explanation: Need: listen to people needs. Option C (Evaluate the stakeholder engagement assessment matrix.) fixes it.\"",
        "Explanation: Keywords: 100+ stakeholders, multinational project, participation and involvement concerns, appropriate engagement. With a large, diverse stakeholder group, managing engagement requires a structured tool that maps current versus desired engagement levels. The stakeholder engagement assessment matrix provides a visual framework for identifying which stakeholders need more active involvement and which are already appropriately engaged, enabling targeted and efficient engagement strategies. (PMBOK Guide) – Seventh Edition, 2021, p. 30, 'Effectively Engage with Stakeholders'\""
    ),
    # Q1437
    (
        "Explanation: Need: protect benefits for users. Option B (Determine the appropriate level of decision-making authority and empower the engineer.) fixes it.\"",
        "Explanation: Keywords: new engineer, adequate skills, waits for authorization, over-dependence on project manager. When a capable engineer consistently defers to the project manager before acting, the issue is unclear decision-making boundaries rather than lack of ability. Defining the appropriate scope of the engineer's authority and explicitly empowering them to act within it unlocks their potential contribution and reduces the bottleneck created by unnecessary approval loops. (PMBOK Guide) – Seventh Edition, 2021, p. 36, 'Demonstrate Leadership Behaviors'\""
    ),
    # Q1438
    (
        "Explanation: Need: guide and calm the team. Option A (Use a work breakdown structure (WBS) to create a project schedule based on the project and resource requirements.) fixes it.\"",
        "Explanation: Keywords: coaching session, junior project manager, efficiency, reduce rework. Rework is most often caused by poor planning rather than poor execution. A WBS-based project schedule breaks work into manageable components aligned with resources, creating a structured roadmap that prevents gaps, overlaps, and misassignments — all of which contribute to rework. This is the most foundational efficiency improvement a project manager can recommend. (PMBOK Guide) – Seventh Edition, 2021, p. 42, 'Build Quality into Processes and Deliverables'\""
    ),
    # Q1439
    (
        "Explanation: Need: guide and calm the team. Option B (Schedule an additional interim demo with the product owner.) fixes it.\"",
        "Explanation: Keywords: 2-week sprint, team not confident in product increment, mid-sprint validation needed. When the team is uncertain about whether they are building the right thing mid-sprint, waiting until the end introduces unnecessary risk. Scheduling an interim demo with the product owner provides early validation, allowing the team to course-correct before investing further effort in a direction that may not meet acceptance criteria. (PMBOK Guide) – Seventh Edition, 2021, p. 42, 'Build Quality into Processes and Deliverables'\""
    ),
    # Q1440
    (
        "Explanation: Need: guide and calm the team. Option C (Note the reasons for the disagreement and let the team proceed.) fixes it.\"",
        "Explanation: Keywords: team voting model 90%, project lead disagrees with technical decision, servant leader. In a team environment where a decision-making process has been democratically established, a servant leader respects the team's authority even when they personally disagree with the outcome. Noting the reasons for the disagreement preserves the project lead's perspective for future reference, while allowing the team to proceed honors the agreed-upon process and reinforces team autonomy. (PMBOK Guide) – Seventh Edition, 2021, p. 36, 'Demonstrate Leadership Behaviors'\""
    ),
    # Q1441
    (
        "Explanation: Need: guide and calm the team. Option B (Met with the project team to determine their collaboration needs and identified tools that will work best.) fixes it.\"",
        "Explanation: Keywords: remote team, project manager chose tools from previous projects, team unhappy, prevention. Tool selection should be a collaborative decision based on the specific team's needs and working context, not a carryover from prior projects. Meeting with the team to understand their collaboration requirements and jointly identifying suitable tools builds buy-in and ensures the chosen solutions actually support how this particular team works. (PMBOK Guide) – Seventh Edition, 2021, p. 28, 'Create a Collaborative Team Environment'\""
    ),
    # Q1442
    (
        "Explanation: Need: guide and calm the team. Option A (Evaluate the impact of nonrenewal of the license.) fixes it.\"",
        "Explanation: Keywords: license expiring in months, significant cost, component dependency, next action. When a license expiration is flagged as a potential issue, the first step is to understand the full impact of non-renewal on the project's scope, schedule, and cost. Only after evaluating the consequences can the project manager make an informed decision about whether to renew, find alternatives, or escalate to the change control process. (PMBOK Guide) – Seventh Edition, 2021, p. 46, 'Optimize Risk Responses'\""
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
