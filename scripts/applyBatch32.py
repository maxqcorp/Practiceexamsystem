MD_FILE = './src/imports/project-management-questions-1.md'

with open(MD_FILE, 'r', encoding='utf-8') as f:
    content = f.read()

replacements = [
    # Q1543
    (
        "Explanation: Need: watch risks early. Option D (Update resolution approaches and action assignments.) fixes it.\"",
        "Explanation: Keywords: periodic progress review meetings, first agenda item, issues discussion. The primary purpose of a progress review meeting is to monitor and control open issues and risks. Starting with updating resolution approaches and action assignments ensures that the most current status of known issues is established first, enabling meaningful discussion of priorities and progress before new topics are introduced. (PMBOK Guide) – Seventh Edition, 2021, p. 46, 'Optimize Risk Responses'\""
    ),
    # Q1544
    (
        "Explanation: Need: listen to people needs. Option D (Continue the meeting and use facilitation techniques to improve communication within the team.) fixes it.\"",
        "Explanation: Keywords: project charter review, conflict between sponsor and product owner, how to deal. When a conflict erupts during a meeting, ending the session or redirecting the parties offline forfeits the opportunity to reach alignment while key stakeholders are together. Using facilitation techniques to manage the discussion in real time — setting ground rules, reframing positions, and guiding toward shared understanding — is the project manager's highest-value contribution in this moment. (PMBOK Guide) – Seventh Edition, 2021, p. 36, 'Demonstrate Leadership Behaviors'\""
    ),
    # Q1545
    (
        "Explanation: Need: listen to people needs. Options A and D (Hold daily virtual meetings to review progress.; Utilize a web-based kanban board.) work together.\"",
        "Explanation: Keywords: agile software project, virtual team, ensure performance expectations, colocated comparison. For a virtual team, two complementary mechanisms best replicate the transparency and accountability of a colocated environment. Daily virtual meetings provide the regular synchronization and face-to-face check-ins that colocated teams benefit from naturally, while a web-based kanban board provides continuous visual visibility into work in progress — together creating the situational awareness needed to maintain performance standards remotely. (PMBOK Guide) – Seventh Edition, 2021, p. 28, 'Create a Collaborative Team Environment'\""
    ),
    # Q1546
    (
        "Explanation: Need: listen to people needs. Option D (Schedule one-to-one meetings and team-building meetings.) fixes it.\"",
        "Explanation: Keywords: internal virtual team, daily meetings plus technical and stakeholder calls, team disengaged. Team disengagement in a meeting-heavy environment often signals that the team feels their interactions are purely transactional and task-focused. Scheduling one-to-one meetings builds individual relationships and surfaces personal concerns, while team-building sessions restore a sense of shared identity and mutual trust — addressing the human dimension of engagement that task-focused meetings neglect. (PMBOK Guide) – Seventh Edition, 2021, p. 30, 'Effectively Engage with Stakeholders'\""
    ),
    # Q1547
    (
        "Explanation: Need: watch risks early. Option D (Launch an enterprise governance structure comprised of division leaders to establish policies for code releases.) fixes it.\"",
        "Explanation: Keywords: project managers not seeking approval before deploying to production, PMO requests solution, cybersecurity and operations impact. When multiple project managers across an organization share the same governance gap, the solution must be systemic rather than individual. Launching an enterprise governance structure that brings division leaders together to establish formal code release policies creates a durable, organization-wide standard that addresses the root cause — absent policy — rather than patching individual behavior. (PMBOK Guide) – Seventh Edition, 2021, p. 44, 'Navigate Complexity'\""
    ),
    # Q1548
    (
        "Explanation: Need: listen to people needs. Option B (Include the business stakeholders in the iteration review.) fixes it.\"",
        "Explanation: Keywords: product feature rollout, backlog grooming, business stakeholders don't understand feature integration. When stakeholders struggle to understand feature integration during backlog grooming, the sprint review is the most effective venue for demonstrating it. Including business stakeholders in the iteration review gives them direct exposure to the working product in an interactive environment where they can ask questions and provide real-time feedback, bridging the comprehension gap more effectively than documentation. (PMBOK Guide) – Seventh Edition, 2021, p. 30, 'Effectively Engage with Stakeholders'\""
    ),
    # Q1549
    (
        "Explanation: Need: listen to people needs. Option D (Communicated with the stakeholder directly regarding the delivery delay.) fixes it.\"",
        "Explanation: Keywords: deliverable not delivered on time, team member emailed stakeholder, stakeholder still complained. Leaving a critical delivery communication to an individual team member creates accountability gaps and inconsistent messaging. The project manager should have communicated the delivery delay directly to the stakeholder — ensuring the message was delivered with appropriate context, authority, and follow-through rather than relying on a team-level email that the stakeholder may not have interpreted as an official notification. (PMBOK Guide) – Seventh Edition, 2021, p. 30, 'Effectively Engage with Stakeholders'\""
    ),
    # Q1550
    (
        "Explanation: Need: protect value and acceptance. Option D (Business case) fixes it.\"",
        "Explanation: Keywords: product owner promoted, new project lead joins, hybrid delivery, identify project benefits. The business case is the foundational document that establishes why the project exists and what benefits it is intended to deliver. When a new project lead needs to understand what benefits have been identified for a project in progress, the business case provides the authoritative source — connecting the project's objectives to the organizational value it is expected to create. (PMBOK Guide) – Seventh Edition, 2021, p. 32, 'Focus on Value'\""
    ),
    # Q1551
    (
        "Explanation: Need: guide and calm the team. Option D (Invest in a virtual collaboration/colocation environment.) fixes it.\"",
        "Explanation: Keywords: global project team, travel not viable, all virtual, how to engage team. When a globally distributed team cannot travel, investing in a dedicated virtual collaboration or colocation environment replicates the persistent shared workspace that colocated teams experience. This infrastructure investment creates the ambient team presence, spontaneous interaction, and shared visibility that are critical for building cohesion and sustaining engagement among geographically separated team members. (PMBOK Guide) – Seventh Edition, 2021, p. 28, 'Create a Collaborative Team Environment'\""
    ),
    # Q1552
    (
        "Explanation: Need: guide and calm the team. Option C (Facilitate the discussion until the team reaches an agreement about the two items.) fixes it.\"",
        "Explanation: Keywords: sprint planning, high business value easy item vs dependency low value complex item, prioritization support. When a dependency creates a tension between high-value and low-complexity items, the team needs to reach a shared understanding of how to sequence the work. Facilitating the discussion until consensus is reached ensures that the prioritization decision reflects the full picture — including technical constraints — rather than being driven by a single perspective, producing a plan the whole team can commit to. (PMBOK Guide) – Seventh Edition, 2021, p. 28, 'Create a Collaborative Team Environment'\""
    ),
    # Q1553
    (
        "Explanation: Need: listen to people needs. Option D (Evaluate the nature of the request and plan communication accordingly.) fixes it.\"",
        "Explanation: Keywords: formally closed project, operational functional manager requests additional scope, small and simple. When a request arrives for work on a formally closed project, the first step is to determine its nature — is it truly a new project, an operational change, or a warranty issue? Evaluating the request's nature and planning the appropriate communication path ensures it is routed correctly, whether that means initiating a new project, directing it to operations, or addressing it under a support agreement. (PMBOK Guide) – Seventh Edition, 2021, p. 32, 'Focus on Value'\""
    ),
    # Q1554
    (
        "Explanation: Need: listen to people needs. Option A (Facilitate the meeting so anyone can share their ideas and is heard during the session.) fixes it.\"",
        "Explanation: Keywords: urgent meeting, quality issues, product owner recommends RCA, what should project lead do. When an urgent meeting is convened to address a quality problem, the project lead's primary contribution is facilitation — creating a space where all team members can share observations and ideas without hierarchy suppressing key insights. Effective facilitation ensures the root cause analysis benefits from diverse perspectives, increasing the likelihood of identifying the actual cause rather than the most visible symptom. (PMBOK Guide) – Seventh Edition, 2021, p. 36, 'Demonstrate Leadership Behaviors'\""
    ),
    # Q1555
    (
        "Explanation: Need: guide and calm the team. Option D (The project manager and the project management team should select the appropriate artifacts for use in the specific project.) fixes it.\"",
        "Explanation: Keywords: unique project, dissimilar to organization, tailoring artifacts, who decides. Artifact selection is a tailoring decision that belongs to the project manager and project management team because they are closest to the specific project context — its complexity, delivery method, stakeholder needs, and regulatory environment. Standardized artifacts from a database or sponsor-directed selections may not fit the unique characteristics of the project, making contextual tailoring essential for effectiveness. (PMBOK Guide) – Seventh Edition, 2021, p. 40, 'Tailor Based on Context'\""
    ),
    # Q1556
    (
        "Explanation: Need: guide and calm the team. Option B (Manage time efficiently using the agenda and ask each participant to contribute.) fixes it.\"",
        "Explanation: Keywords: virtual conference calls, one member continuously interrupts, others cannot speak. When a single participant dominates meeting discussions, the most effective intervention is structural rather than confrontational. Managing time through the agenda and explicitly inviting each participant to contribute distributes speaking opportunities fairly, prevents dominance without singling out the disruptive member, and maintains a constructive meeting culture. (PMBOK Guide) – Seventh Edition, 2021, p. 36, 'Demonstrate Leadership Behaviors'\""
    ),
    # Q1557
    (
        "Explanation: Need: guide and calm the team. Option D (Assist the team in proposing a minimum viable product (MVP).) fixes it.\"",
        "Explanation: Keywords: new product before summer season, requirements very uncertain, team realizes after discovery. When requirements are uncertain and a deadline is firm, the best strategy is to define the minimum set of features that delivers core value and can be built confidently within the timeline. Helping the team propose an MVP focuses development on what is essential, reduces planning uncertainty, and allows the product to reach the market by the summer deadline while future enhancements can follow. (PMBOK Guide) – Seventh Edition, 2021, p. 32, 'Focus on Value'\""
    ),
    # Q1558
    (
        "Explanation: Need: guide and calm the team. Option A (Guide the team to determine alternatives.) fixes it.\"",
        "Explanation: Keywords: no access to data, known dependency, team unsure of available options, iteration blocker. When a team is blocked and uncertain about how to proceed, the project manager's role is to guide their problem-solving rather than prescribe a solution or immediately escalate. Helping the team work through the available alternatives builds their capability to resolve similar blockers independently and typically produces faster, more contextually appropriate solutions than external escalation. (PMBOK Guide) – Seventh Edition, 2021, p. 36, 'Demonstrate Leadership Behaviors'\""
    ),
    # Q1559
    (
        "Explanation: Need: guide and calm the team. Option B (Encourage further and deeper discussions among team members.) fixes it.\"",
        "Explanation: Keywords: junior team member suggestions rejected as unrealistic, senior members request removal. When senior team members dismiss a junior colleague's ideas as impractical, there may be value in those ideas that is being overlooked due to experience bias. Encouraging deeper discussion between the team members — rather than accepting the removal request — allows the junior's thinking to be examined more thoroughly and builds the collaborative culture needed for innovation to thrive. (PMBOK Guide) – Seventh Edition, 2021, p. 36, 'Demonstrate Leadership Behaviors'\""
    ),
    # Q1560
    (
        "Explanation: Need: listen to people needs. Option B (Evaluate the impact and submit a change request.) fixes it.\"",
        "Explanation: Keywords: key stakeholder requests out-of-scope work, sponsor may not approve, first action. When an out-of-scope request is received, the project manager's first obligation is to evaluate its impact before either accepting or refusing it. Submitting a formal change request captures the request, triggers a structured impact assessment, and routes it to the appropriate authority for decision — regardless of whether the sponsor ultimately approves it. (PMBOK Guide) – Seventh Edition, 2021, p. 50, 'Enable Change to Achieve the Envisioned Future State'\""
    ),
    # Q1561
    (
        "Explanation: Need: listen to people needs. Option A (Discuss the issue with the team member in a one-on-one meeting.) fixes it.\"",
        "Explanation: Keywords: critical milestone missed, team member tasks incomplete, heated discussion during demo, next action. After a public incident caused by a team member's failure to complete their work, the appropriate response is a private one-on-one conversation rather than a public discussion. This approach allows the project manager to understand the reasons for the delay without embarrassing the individual, establishes clear expectations for future performance, and preserves the team member's dignity and motivation. (PMBOK Guide) – Seventh Edition, 2021, p. 36, 'Demonstrate Leadership Behaviors'\""
    ),
    # Q1562
    (
        "Explanation: Need: listen to people needs. Option A (Hybrid approach) fixes it.\"",
        "Explanation: Keywords: project with high uncertainty, customer concerned about many iterations, mandatory delivery date. A hybrid approach addresses both the customer's concern about an excessive number of iterations and the project's requirement to manage uncertainty. By combining predictive elements — such as a fixed delivery date and milestone structure — with adaptive delivery of features within those milestones, the project can manage uncertainty iteratively while satisfying the customer's need for deadline certainty. (PMBOK Guide) – Seventh Edition, 2021, p. 40, 'Tailor Based on Context'\""
    ),
    # Q1563
    (
        "Explanation: Need: listen to people needs. Option D (Discuss the suggestions with the staff responsible for the compliance issues.) fixes it.\"",
        "Explanation: Keywords: stakeholder informs about compliance gaps, presents suggestions, what to do. When a stakeholder identifies compliance gaps and offers suggestions, those suggestions are most effectively evaluated and implemented by the people who are directly responsible for the affected processes. Discussing the suggestions with the responsible staff both informs them of the concern and ensures that the response is technically grounded and operationally feasible. (PMBOK Guide) – Seventh Edition, 2021, p. 30, 'Effectively Engage with Stakeholders'\""
    ),
    # Q1564
    (
        "Explanation: Need: listen to people needs. Option B (Clarify the current work progress, causes for delays, existing risks, and planned corrective actions.) fixes it.\"",
        "Explanation: Keywords: hybrid project, technical difficulties, new dependencies, stakeholder asks about contract deadlines. When a stakeholder asks about meeting contractual deadlines, the most helpful and transparent response is a clear factual summary — current progress, causes of delay, risk exposure, and the corrective actions already planned. This response demonstrates accountability and confidence in recovery, which is more reassuring to the stakeholder than either deflecting with contract terms or expressing unqualified optimism. (PMBOK Guide) – Seventh Edition, 2021, p. 30, 'Effectively Engage with Stakeholders'\""
    ),
    # Q1565
    (
        "Explanation: Need: guide and calm the team. Option D (Expert judgment) fixes it.\"",
        "Explanation: Keywords: project closing, PMO asks to confirm knowledge transfer to operations, technique to verify. Confirming that knowledge transfer to an operations team has been successfully completed requires subject matter expertise to assess whether the operations team genuinely understands and can independently apply what was shared. Expert judgment — drawing on experienced practitioners who can evaluate operational readiness — provides the most credible and accurate verification of whether the transfer was effective. (PMBOK Guide) – Seventh Edition, 2021, p. 25, 'Be a Diligent, Respectful, and Caring Steward'\""
    ),
    # Q1566
    (
        "Explanation: Need: listen to people needs. Option A (Present the benefits of a hybrid approach to key stakeholders to get their support.) fixes it.\"",
        "Explanation: Keywords: complex research project, organization only has predictive experience, hybrid approach, how to strategize. When introducing an unfamiliar delivery approach to an organization, the first priority is building stakeholder buy-in. Presenting the specific benefits of a hybrid approach to key stakeholders — framed in terms of the project's complexity and uncertainty — creates the organizational alignment needed before the approach can be formally adopted and supported. (PMBOK Guide) – Seventh Edition, 2021, p. 40, 'Tailor Based on Context'\""
    ),
    # Q1567
    (
        "Explanation: Need: listen to people needs. Option B (Ask the sponsor to authorize the launch and then wait for approval.) fixes it.\"",
        "Explanation: Keywords: medical implant, global compliance, one country approval lengthy, impact on launch date. When a regulatory approval process for one market would delay the entire launch, the project manager should work with the sponsor to determine whether authorization can be granted to proceed in compliant markets while the slow approval continues in parallel. This approach allows value to be realized in approved markets without compromising compliance obligations in the delayed jurisdiction. (PMBOK Guide) – Seventh Edition, 2021, p. 25, 'Be a Diligent, Respectful, and Caring Steward'\""
    ),
    # Q1568
    (
        "Explanation: Need: guide and calm the team. Option B (Meet with the team to review internal actions to resolve the situation.) fixes it.\"",
        "Explanation: Keywords: first iteration 50% velocity, complexity underestimated, retrospective discovery, what to do. When a team retrospective reveals that work complexity was systematically underestimated, the project manager must work with the team to understand the gap and develop corrective actions from within the team's own knowledge. Meeting to review internal actions — adjusting estimation techniques, breaking stories into smaller pieces, or updating technical approaches — addresses the root cause collaboratively. (PMBOK Guide) – Seventh Edition, 2021, p. 28, 'Create a Collaborative Team Environment'\""
    ),
    # Q1569
    (
        "Explanation: Need: protect value and acceptance. Option B (Metrics and key performance indicators (KPIs) that objectively reflect the status of deliverables.) fixes it.\"",
        "Explanation: Keywords: complex project, many regulatory requirements, management review with senior executives, what to review. Management reviews with senior executives are most valuable when they are grounded in objective, quantifiable information that reflects actual delivery status. Metrics and KPIs provide an evidence-based foundation for the discussion, enabling executives to make informed governance decisions rather than relying on subjective narratives that may obscure the true state of the project. (PMBOK Guide) – Seventh Edition, 2021, p. 25, 'Be a Diligent, Respectful, and Caring Steward'\""
    ),
    # Q1570
    (
        "Explanation: Need: guide and calm the team. Option A (Acknowledge the impediments and facilitate their resolutions.) fixes it.\"",
        "Explanation: Keywords: scrum master role, daily standup, developers complain about noise, laptops, meeting rooms. A scrum master's core responsibility is removing impediments that prevent the team from working effectively. Acknowledging the impediments validates the team's concerns and signals that they will be addressed, while facilitating their resolution ensures follow-through. Logging them for later or delegating upward would leave the team blocked longer than necessary. (PMBOK Guide) – Seventh Edition, 2021, p. 36, 'Demonstrate Leadership Behaviors'\""
    ),
    # Q1571
    (
        "Explanation: Need: watch risks early. Option C (Analyze the impact of the change request on the project.) fixes it.\"",
        "Explanation: Keywords: building first baseline, change request received from functional manager, what to do. A change request submitted before the project baseline is even established must be analyzed carefully, as its acceptance or rejection will shape the scope, schedule, and cost baseline being built. Analyzing the impact of the change before deciding how to respond ensures the project manager has a complete picture of what the change would mean for the overall project plan. (PMBOK Guide) – Seventh Edition, 2021, p. 46, 'Optimize Risk Responses'\""
    ),
    # Q1572
    (
        "Explanation: Need: watch risks early. Option C (Mapped environmental compliance requirements, identified risks to achieving them, and prepared mitigations.) fixes it.\"",
        "Explanation: Keywords: public transportation construction, severely delayed due to noncompliance, environmental codes, prevention. Environmental compliance failures in construction projects are a foreseeable category of risk, not an unforeseen event. Proactively mapping all applicable compliance requirements, identifying the risks associated with each, and preparing mitigation strategies would have ensured the project team understood and planned for the compliance obligations before the delays materialized. (PMBOK Guide) – Seventh Edition, 2021, p. 46, 'Optimize Risk Responses'\""
    ),
    # Q1573
    (
        "Explanation: Need: listen to people needs. Option D (Analyze the probability and impact of the risks linked with the situation and implement the proper response plan.) fixes it.\"",
        "Explanation: Keywords: cross-departmental project, diverse stakeholder groups, different expectations, frequent confusion. When diverse stakeholder groups create ongoing confusion and conflict, the underlying risk to project delivery must be formally assessed. Analyzing the probability and impact of stakeholder misalignment as a risk — and implementing a structured response plan — moves from reactive firefighting to proactive management, addressing the root cause rather than responding to each incident individually. (PMBOK Guide) – Seventh Edition, 2021, p. 46, 'Optimize Risk Responses'\""
    ),
    # Q1574
    (
        "Explanation: Need: listen to people needs. Option B (Probabilistic analysis was used to develop the budget to address future uncertainties.) fixes it.\"",
        "Explanation: Keywords: end of initiation, approval board, how budget was developed for future uncertainties. When an approval board asks how the budget accounts for future uncertainties, the most credible answer is that probabilistic analysis — such as Monte Carlo simulation or expected monetary value calculations — was used to quantify uncertainty and size the contingency reserve accordingly. This response demonstrates rigorous financial stewardship that the board can have confidence in. (PMBOK Guide) – Seventh Edition, 2021, p. 46, 'Optimize Risk Responses'\""
    ),
    # Q1575
    (
        "Explanation: Need: listen to people needs. Option A (An adaptive approach with clearly defined user stories.) fixes it.\"",
        "Explanation: Keywords: new product launch, test market readiness, business transformation, open delivery channels, delivery approach. A product designed to test market readiness benefits from adaptive delivery because market feedback will shape the product's direction as it is released. Using an adaptive approach with clearly defined user stories enables incremental delivery of tested features, rapid response to market signals, and progressive refinement of the product based on actual customer behavior — exactly what a market readiness test requires. (PMBOK Guide) – Seventh Edition, 2021, p. 40, 'Tailor Based on Context'\""
    ),
    # Q1576
    (
        "Explanation: Need: guide and calm the team. Option C (Business value) fixes it.\"",
        "Explanation: Keywords: sprint planning, 95% of items can be delivered, product owner asks for prioritization advice. When not all planned items can fit within a sprint, the prioritization criterion should be business value — ensuring that the 95% of items selected deliver the greatest possible benefit to the customer and organization. Technical complexity and risk to delivery are secondary considerations; value alignment is the primary driver of agile prioritization decisions. (PMBOK Guide) – Seventh Edition, 2021, p. 32, 'Focus on Value'\""
    ),
    # Q1577
    (
        "Explanation: Need: listen to people needs. Option C (Invite the PMO manager to the daily standup with the project team and product owner.) fixes it.\"",
        "Explanation: Keywords: agile pilot, PMO manager asks how communications will be managed, kanban board in use. Inviting the PMO manager to the daily standup provides real-time transparency into team progress without creating a separate reporting overhead. This approach shares visibility into agile delivery practices directly — allowing the PMO to observe the kanban board and team interactions firsthand — while keeping the communication lightweight and consistent with how agile teams naturally share status. (PMBOK Guide) – Seventh Edition, 2021, p. 30, 'Effectively Engage with Stakeholders'\""
    ),
    # Q1578
    (
        "Explanation: Need: listen to people needs. Option A (Risk management plan) fixes it.\"",
        "Explanation: Keywords: procurement risk identified, sponsor forwards to project manager, preventive action decided, which document to review. When a procurement risk has been identified and the project manager has decided to take preventive action, the risk management plan provides the framework for how to respond — including the escalation thresholds, risk response strategies, and the team roles responsible for execution. Reviewing it with the team ensures the preventive action is implemented consistently with the project's established risk governance. (PMBOK Guide) – Seventh Edition, 2021, p. 46, 'Optimize Risk Responses'\""
    ),
    # Q1579
    (
        "Explanation: Need: listen to people needs. Option A (Reschedule on-site training to online sessions.) fixes it.\"",
        "Explanation: Keywords: on-site training in acceptance criteria, all team members working remotely, unforeseen circumstances. When on-site training becomes impossible due to remote work requirements, the project manager should adapt the delivery format rather than rescheduling or canceling. Rescheduling on-site sessions to online equivalents maintains the training timeline, preserves the acceptance criteria, and demonstrates the kind of adaptive problem-solving that ensures delivery commitments are honored despite environmental constraints. (PMBOK Guide) – Seventh Edition, 2021, p. 48, 'Embrace Adaptability and Resiliency'\""
    ),
    # Q1580
    (
        "Explanation: Need: listen to people needs. Option B (Focus on the recipients' needs and not the information itself.) fixes it.\"",
        "Explanation: Keywords: matrix organization, specialist resources, diverse departments, effective communications setup. Effective communication in a complex, multi-department environment requires the project manager to prioritize what each recipient needs to know — not what the project manager wants to convey. Focusing on the recipients' needs shapes the format, level of detail, and timing of communications to maximize comprehension and action, reducing the misunderstandings that arise when information is broadcast uniformly regardless of audience. (PMBOK Guide) – Seventh Edition, 2021, p. 30, 'Effectively Engage with Stakeholders'\""
    ),
    # Q1581
    (
        "Explanation: Need: keep plans flexible. Option C (Invite the manager to the scheduled sprint review.) fixes it.\"",
        "Explanation: Keywords: rollout in stages, manager from later business unit asks to attend sprint review, what to do. Sprint reviews are designed to be transparent demonstrations of progress and are open to interested stakeholders. Inviting the manager from a later-stage business unit to the scheduled sprint review gives them early insight into the product, builds engagement for their upcoming rollout, and costs nothing — there is no good reason to restrict access to an event whose purpose is broad visibility. (PMBOK Guide) – Seventh Edition, 2021, p. 30, 'Effectively Engage with Stakeholders'\""
    ),
    # Q1582
    (
        "Explanation: Need: guide and calm the team. Option B (Meet with the IT team to evaluate how fast the software license can be renewed.) fixes it.\"",
        "Explanation: Keywords: software license expired, team cannot continue project tasks, first action. When a license expiration blocks the team, the most direct path to unblocking them is to determine how quickly the license can be restored. Meeting with the IT team to assess renewal timelines establishes the fastest viable resolution path, allowing the project manager to set a realistic recovery timeline and decide whether alternative approaches are needed while renewal is processed. (PMBOK Guide) – Seventh Edition, 2021, p. 34, 'Recognize, Evaluate, and Respond to System Interactions'\""
    ),
    # Q1583
    (
        "Explanation: Need: guide and calm the team. Option C (Ask the team members to proceed independently while examining needs and alternatives.) fixes it.\"",
        "Explanation: Keywords: sudden travel restrictions, team in different geographic locations, next action. When travel restrictions are suddenly imposed, a project manager cannot wait for a complete solution before allowing work to continue. Asking team members to proceed with what they can do independently — while simultaneously examining communication needs and alternative working arrangements — keeps the project moving while the adaptive response is developed in parallel. (PMBOK Guide) – Seventh Edition, 2021, p. 48, 'Embrace Adaptability and Resiliency'\""
    ),
    # Q1584
    (
        "Explanation: Need: guide and calm the team. Option B (Facilitate a priority resolution of the issue with the IT department.) fixes it.\"",
        "Explanation: Keywords: fourth iteration, team member computer not working, iteration planning, next action. A non-functional computer is an impediment that prevents a team member from contributing to the iteration. Rather than simply directing the team member to contact IT themselves, the project manager should actively facilitate a priority resolution — ensuring the issue is treated with the urgency it deserves given the ongoing iteration and the team's need for the resource to be productive. (PMBOK Guide) – Seventh Edition, 2021, p. 28, 'Create a Collaborative Team Environment'\""
    ),
    # Q1585
    (
        "Explanation: Need: listen to people needs. Option B (Stakeholder Register) fixes it.\"",
        "Explanation: Keywords: requirements not approved, user party leader not included in communications, which document missed. When a key stakeholder is excluded from the requirements process, the root cause is typically an incomplete or poorly maintained stakeholder register. A comprehensive stakeholder register captures all parties who have an interest in or influence over the project — including user representatives — ensuring they are included in the appropriate communications and decisions throughout the project lifecycle. (PMBOK Guide) – Seventh Edition, 2021, p. 30, 'Effectively Engage with Stakeholders'\""
    ),
    # Q1586
    (
        "Explanation: Need: listen to people needs. Option B (Discuss this with the team and review the project requirements documentation.) fixes it.\"",
        "Explanation: Keywords: stakeholder concern during deliverable review, what to do first. When a stakeholder raises a concern about a deliverable, the project manager must first understand whether the concern reflects a genuine gap in requirements fulfillment. Discussing the issue with the team and reviewing the requirements documentation establishes the factual basis — determining whether the concern is valid and whether the deliverable actually meets the agreed-upon specifications before any escalation or rework is initiated. (PMBOK Guide) – Seventh Edition, 2021, p. 30, 'Effectively Engage with Stakeholders'\""
    ),
    # Q1587
    (
        "Explanation: Need: guide and calm the team. Option B (Add a subject matter expert (SME) to the project team.) fixes it.\"",
        "Explanation: Keywords: first iteration, hard timeline, project team lacks skills, what to do. When a team lacks the skills needed to execute in a hard-deadline context, the fastest path to capability is to add a subject matter expert who can both contribute directly and transfer knowledge to the team. This addresses both the immediate delivery risk and the longer-term skill gap without compromising the timeline by waiting for internal training to take effect. (PMBOK Guide) – Seventh Edition, 2021, p. 34, 'Recognize, Evaluate, and Respond to System Interactions'\""
    ),
    # Q1588
    (
        "Explanation: Need: guide and calm the team. Option D (Meet with the team together and in one-on-one meetings to set clear, shared targets.) fixes it.\"",
        "Explanation: Keywords: global project, remote teams, past experience of poor quality from remote teams, ensure quality. The most common reason remote teams underperform is unclear expectations — not lack of skill or commitment. Setting clear, shared targets through both group and individual meetings ensures every team member understands what is expected, builds personal accountability, and creates the alignment needed for consistent quality delivery in a distributed environment. (PMBOK Guide) – Seventh Edition, 2021, p. 28, 'Create a Collaborative Team Environment'\""
    ),
    # Q1589
    (
        "Explanation: Need: guide and calm the team. Option C (Review the options and possible solutions with the project team.) fixes it.\"",
        "Explanation: Keywords: sixth iteration, key function takes longer than anticipated, what to do. When a delay is identified during an active iteration, the team's collective knowledge is the best resource for identifying solutions. Reviewing options together — renegotiating scope, redistributing work, or adjusting the iteration plan — ensures the response is informed by the technical realities of the work and builds team ownership of the recovery approach. (PMBOK Guide) – Seventh Edition, 2021, p. 28, 'Create a Collaborative Team Environment'\""
    ),
    # Q1590
    (
        "Explanation: Need: listen to people needs. Options B and D (Review the lessons learned from similar past projects.; Update the risk log and bring this up in the meeting with the client.) work together.\"",
        "Explanation: Keywords: external dependency delayed, risk management meeting with client, project manager does not know exact impact. Before a risk management meeting where the client will expect an informed discussion, the project manager should simultaneously gather impact information and ensure the issue is formally logged. Reviewing lessons learned from similar delays provides context for estimating impact, while updating the risk log ensures the client receives an accurate, documented status update rather than an improvised verbal summary. (PMBOK Guide) – Seventh Edition, 2021, p. 46, 'Optimize Risk Responses'\""
    ),
    # Q1591
    (
        "Explanation: Need: watch risks early. Option D (Ask the steering committee to approve a new technical design.) fixes it.\"",
        "Explanation: Keywords: technical design approved, later discovered it impacts production system, new design needed, 3-month delay. When a post-approval discovery reveals that the approved design will create a production system impact, the project manager cannot implement an unauthorized redesign — even a necessary one. The steering committee, which approved the original design, must be the authority that approves its replacement. Proceeding without their approval would bypass the project governance that was deliberately established. (PMBOK Guide) – Seventh Edition, 2021, p. 46, 'Optimize Risk Responses'\""
    ),
    # Q1592
    (
        "Explanation: Need: guide and calm the team. Option B (Ask each experienced member to be the mentor to one of the less-experienced members.) fixes it.\"",
        "Explanation: Keywords: project team with varying experience levels, approved schedule, experts and less than 1 year experience. Pairing experienced team members with less-experienced ones creates a structured mentoring relationship that accelerates skill development while keeping knowledge transfer integrated with actual project work. This approach is more efficient than formal training programs during execution and builds team cohesion by connecting senior and junior members around shared work goals. (PMBOK Guide) – Seventh Edition, 2021, p. 28, 'Create a Collaborative Team Environment'\""
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
