MD_FILE = './src/imports/project-management-questions-1.md'

with open(MD_FILE, 'r', encoding='utf-8') as f:
    content = f.read()

replacements = [
    # Q1443
    (
        "Explanation: Need: guide and calm the team. Option B (Meet with the team members and developer individually to understand the situation and build an action plan accordingly.) fixes it.\"",
        "Explanation: Keywords: developer creating conflicts, high performer, team refusing to work with developer. Managing a high-performer who creates interpersonal conflict requires a nuanced approach that addresses both sides. Meeting individually with the developer and affected team members allows the project manager to gather unfiltered perspectives, identify the root causes, and build an action plan that preserves the developer's contributions while restoring a functional team dynamic. (PMBOK Guide) – Seventh Edition, 2021, p. 36, 'Demonstrate Leadership Behaviors'\""
    ),
    # Q1444
    (
        "Explanation: Need: guide and calm the team. Option C (Speak with the project management office (PMO) and request a 2-week extension of the schedule so the team can have rotational time off.) fixes it.\"",
        "Explanation: Keywords: healthcare project, 6 months working, low team morale, testing phase, motivation. Sustained effort over months without relief leads to declining morale and diminishing performance. Requesting a schedule extension to allow the team rotational time off acknowledges their human needs and addresses the root cause of the morale issue — fatigue — rather than relying on rewards or incentives that do not address burnout. (PMBOK Guide) – Seventh Edition, 2021, p. 36, 'Demonstrate Leadership Behaviors'\""
    ),
    # Q1445
    (
        "Explanation: Need: listen to people needs. Option B (Include the project stakeholders' needs while planning the project communications strategy.) fixes it.\"",
        "Explanation: Keywords: emails from stakeholders requesting status, project communications strategy, avoid in the future. When stakeholders proactively reach out for information the project has not provided, it signals a gap in the communications plan. Including stakeholder communication needs during planning — rather than after complaints arise — ensures that each stakeholder receives the right information at the right frequency, eliminating the need for ad hoc requests. (PMBOK Guide) – Seventh Edition, 2021, p. 30, 'Effectively Engage with Stakeholders'\""
    ),
    # Q1446
    (
        "Explanation: Need: listen to people needs. Option B (Engage the main stakeholders in the upcoming sprint review sessions.) fixes it.\"",
        "Explanation: Keywords: agile pilot, three sprints, negative feedback on features, acceptance criteria met, product rejection. When stakeholders reject a product that technically met the acceptance criteria, the issue is that the criteria did not fully capture what stakeholders actually value. Inviting main stakeholders into sprint reviews establishes a direct feedback loop, allowing misaligned expectations to be identified and corrected incrementally rather than after a full delivery. (PMBOK Guide) – Seventh Edition, 2021, p. 30, 'Effectively Engage with Stakeholders'\""
    ),
    # Q1447
    (
        "Explanation: Need: listen to people needs. Option A (Reviewed the acceptance criteria and obtained client approval.) fixes it.\"",
        "Explanation: Keywords: software installed, knowledge transferred, client sends unmet requirements after completion, prevention. Post-delivery disputes about unmet requirements almost always trace back to insufficient acceptance validation before closure. Formally reviewing the acceptance criteria with the client and obtaining their sign-off at each phase would have surfaced unmet requirements while the team was still in a position to address them within the original budget. (PMBOK Guide) – Seventh Edition, 2021, p. 42, 'Build Quality into Processes and Deliverables'\""
    ),
    # Q1448
    (
        "Explanation: Need: listen to people needs. Option D (Sent weekly status update reports to all of the stakeholders.) fixes it.\"",
        "Explanation: Keywords: incremental project, kanban board, external stakeholder requests hold on activities, status report. A stakeholder who halts project activities to demand a status report has not been receiving timely or sufficient information. Proactively sending weekly status updates to all stakeholders ensures they have the information they need to remain confident in project progress, preventing disruptive interventions triggered by information gaps. (PMBOK Guide) – Seventh Edition, 2021, p. 30, 'Effectively Engage with Stakeholders'\""
    ),
    # Q1449
    (
        "Explanation: Need: guide and calm the team. Option A (Support the team in identifying the area of development and address the gap.) fixes it.\"",
        "Explanation: Keywords: high-performing team, new domain, unable to deliver as expected. Even high-performing teams encounter capability gaps when entering unfamiliar domains. Supporting the team to self-diagnose the specific area where development is needed — rather than dissolving or reassigning them — respects their established performance history and provides a targeted path to closing the gap while retaining team cohesion. (PMBOK Guide) – Seventh Edition, 2021, p. 36, 'Demonstrate Leadership Behaviors'\""
    ),
    # Q1450
    (
        "Explanation: Need: guide and calm the team. Option B (Discuss it with the team member in confidence.) fixes it.\"",
        "Explanation: Keywords: team member late report, consolidated report not integrated, demonstrated lack of teamwork. When one team member's late delivery cascades into a broader impact, addressing it privately and directly is the most professionally appropriate response. A confidential one-on-one conversation allows the project manager to understand the reason for the delay, clarify expectations, and agree on corrective behavior without embarrassing the individual in front of the team. (PMBOK Guide) – Seventh Edition, 2021, p. 36, 'Demonstrate Leadership Behaviors'\""
    ),
    # Q1451
    (
        "Explanation: Need: guide and calm the team. Option B (Invite a design team member to the next daily meeting.) fixes it.\"",
        "Explanation: Keywords: second iteration, approval needed from design department, blocker, daily meeting. When a deliverable is blocked by an approval that only another team can grant, the fastest path to resolution is direct communication. Inviting a design team member to the next daily meeting creates an immediate dialogue, allows the team to explain the requirement in context, and typically results in a faster decision than formal escalation or written requests. (PMBOK Guide) – Seventh Edition, 2021, p. 28, 'Create a Collaborative Team Environment'\""
    ),
    # Q1452
    (
        "Explanation: Need: guide and calm the team. Option C (Review the list of risks to verify that this issue was considered and execute the detailed action plan.) fixes it.\"",
        "Explanation: Keywords: system failure, lottery tickets sold twice, highest demand period, issue management. When an incident occurs during project execution, the first step is to determine whether it was anticipated. Reviewing the risk register to check whether this failure scenario was previously identified ensures that any pre-planned response actions are executed correctly, rather than improvising a response that may be less effective or create additional issues. (PMBOK Guide) – Seventh Edition, 2021, p. 46, 'Optimize Risk Responses'\""
    ),
    # Q1453
    (
        "Explanation: Need: listen to people needs. Option C (Take action to reprioritize the backlog after every iteration to evaluate if user stories are still valuable to the business.) fixes it.\"",
        "Explanation: Keywords: agile project, changing business environment, benefits realization, sponsor concern. In a changing environment, backlog items that were valuable when written may become irrelevant as external conditions evolve. Reprioritizing the backlog after every iteration using current business context ensures that each sprint delivers the most relevant value and that outdated user stories are identified and deprioritized before resources are wasted on them. (PMBOK Guide) – Seventh Edition, 2021, p. 32, 'Focus on Value'\""
    ),
    # Q1454
    (
        "Explanation: Need: listen to people needs. Option C (Facilitate communication to ensure clarification of the requirements.) fixes it.\"",
        "Explanation: Keywords: distributed team, developer delay, misunderstanding of customer requirements, critical path. Delays caused by misunderstood requirements in distributed teams are fundamentally a communication problem. Facilitating direct communication between the remote developer and the requirement source addresses the root cause — the knowledge gap — rather than treating the symptom by changing the resource or adding pressure, which would not resolve the underlying confusion. (PMBOK Guide) – Seventh Edition, 2021, p. 30, 'Effectively Engage with Stakeholders'\""
    ),
    # Q1455
    (
        "Explanation: Need: guide and calm the team. Option A (Ensure that the schedule is aligned with the vision and objectives.) fixes it.\"",
        "Explanation: Keywords: project manager returns from leave, team built schedule, almost complete, what to do. When returning to a project where the team has already completed planning work, the project manager's priority is to verify that what was built is aligned with the project's purpose — not to redo the work or assert authority. Ensuring schedule alignment with vision and objectives provides the most value and validates the team's effort constructively. (PMBOK Guide) – Seventh Edition, 2021, p. 42, 'Build Quality into Processes and Deliverables'\""
    ),
    # Q1456
    (
        "Explanation: Need: listen to people needs. Option C (Communicate the decision to the stakeholder who requested the change.) fixes it.\"",
        "Explanation: Keywords: CCB-approved change request, bridge branch addition, next step after approval. Once the CCB approves a change, the first obligation is to close the communication loop with the person who initiated the request. Informing the regulatory stakeholder of the approval acknowledges their input, confirms that their request has been formally accepted, and sets the stage for implementation — making it the correct immediate next action. (PMBOK Guide) – Seventh Edition, 2021, p. 30, 'Effectively Engage with Stakeholders'\""
    ),
    # Q1457
    (
        "Explanation: Need: keep plans flexible. Option D (Design a negotiation strategy for this situation.) fixes it.\"",
        "Explanation: Keywords: project near completion, behind schedule, contingency used, SME needed in operations, negotiation. When a critical resource is being pulled away by another department, the resolution requires negotiation rather than unilateral action. Designing a negotiation strategy allows the project manager to approach the conversation with the SME's manager constructively — proposing sharing arrangements, phased availability, or priority agreements that serve both parties. (PMBOK Guide) – Seventh Edition, 2021, p. 46, 'Optimize Risk Responses'\""
    ),
    # Q1458
    (
        "Explanation: Need: keep plans flexible. Option C (Assess the schedule impact and evaluate the most feasible solution to keep the project on track.) fixes it.\"",
        "Explanation: Keywords: vendor product deficiencies, factory acceptance test, critical path, delivery delay risk. When deficiencies are discovered in a vendor product on the critical path, the project manager must first understand the schedule implications before committing to a response. Assessing the schedule impact and evaluating all feasible options — on-site rework, partial delivery, or expedited fix — ensures the decision selected minimizes overall project impact rather than applying a generic solution. (PMBOK Guide) – Seventh Edition, 2021, p. 46, 'Optimize Risk Responses'\""
    ),
    # Q1459
    (
        "Explanation: Need: listen to people needs. Option C (Help the customer find an alternative location to start the training.) fixes it.\"",
        "Explanation: Keywords: education project, customer responsible for training center, center unavailable in 2 weeks, unforeseen problems. When a customer-owned dependency fails unexpectedly, a collaborative project manager does not immediately invoke penalties or issue change requests — they help solve the problem. Assisting the customer in finding an alternative location maintains the project timeline while demonstrating partnership and goodwill that strengthens the working relationship. (PMBOK Guide) – Seventh Edition, 2021, p. 30, 'Effectively Engage with Stakeholders'\""
    ),
    # Q1460
    (
        "Explanation: Need: listen to people needs. Option B (Establish a pull communications method to access knowledge repositories and lessons learned.) fixes it.\"",
        "Explanation: Keywords: knowledge sharing emails, team overloaded with information, useful but unmanageable volume. When useful information is causing overload rather than enabling work, the solution is to shift from push communications (emails broadcasting to everyone) to pull communications (centralized repositories that team members access on demand). This preserves access to valuable knowledge while eliminating the cognitive burden of processing unsolicited information. (PMBOK Guide) – Seventh Edition, 2021, p. 30, 'Effectively Engage with Stakeholders'\""
    ),
    # Q1461
    (
        "Explanation: Need: listen to people needs. Option D (Work with the team to understand their views and add the appropriate dependencies and risks.) fixes it.\"",
        "Explanation: Keywords: agile software, client wants tasks and estimates, before sending information to client. Before delivering project estimates to a client, the project manager should work collaboratively with the team to surface dependencies, risks, and contextual insights that only the technical team can provide. Estimates submitted without this collaborative review are likely to be incomplete, leading to misaligned expectations and downstream rework. (PMBOK Guide) – Seventh Edition, 2021, p. 28, 'Create a Collaborative Team Environment'\""
    ),
    # Q1462
    (
        "Explanation: Need: listen to people needs. Option B (Continue the iteration and review the change with the customer.) fixes it.\"",
        "Explanation: Keywords: merger, information security consultant, requests software component changes mid-iteration, market requirements. A consultant's mid-iteration change request should not automatically halt work or be immediately implemented. Continuing the iteration while reviewing the proposed change with the customer ensures that any modification is evaluated through the proper channel — customer approval — before being incorporated, preserving iteration integrity and client alignment. (PMBOK Guide) – Seventh Edition, 2021, p. 30, 'Effectively Engage with Stakeholders'\""
    ),
    # Q1463
    (
        "Explanation: Need: guide and calm the team. Option A (Help the team members to resolve the conflict in a way that results in the best team performance.) fixes it.\"",
        "Explanation: Keywords: 1 week conflict, new team, taking things personally, tense atmosphere. Unresolved interpersonal conflicts degrade team cohesion and decision quality. The project manager's role in conflict resolution is to facilitate a solution that restores team effectiveness, not to impose a compromise or adjudicate who is right. Helping both parties work toward a resolution that optimizes team performance reframes the conflict as a team development opportunity. (PMBOK Guide) – Seventh Edition, 2021, p. 36, 'Demonstrate Leadership Behaviors'\""
    ),
    # Q1464
    (
        "Explanation: Need: listen to people needs. Option B (Add the activist group to the list of stakeholders and analyze the impact they may have on project delivery.) fixes it.\"",
        "Explanation: Keywords: construction near nature reserve, environmental activist group, customer says disregard, next step. A project manager has an ethical and professional obligation to identify and assess all stakeholders, regardless of whether the customer considers them relevant. Adding the activist group to the stakeholder register and analyzing their potential impact is both a risk management imperative and a demonstration of responsible stewardship for the broader community. (PMBOK Guide) – Seventh Edition, 2021, p. 30, 'Effectively Engage with Stakeholders'\""
    ),
    # Q1465
    (
        "Explanation: Need: guide and calm the team. Option D (Determine the impact to the project and implement mitigations per the project management plan.) fixes it.\"",
        "Explanation: Keywords: company reorganization, key team members may leave, execution phase, next action. When organizational changes threaten project resourcing, the structured response is to assess the actual impact before taking action. The project management plan — including risk and resource management sections — provides the framework for determining what mitigations are appropriate, ensuring the response is proportional and aligned with the project's established governance. (PMBOK Guide) – Seventh Edition, 2021, p. 46, 'Optimize Risk Responses'\""
    ),
    # Q1466
    (
        "Explanation: Need: secure people or vendors. Option C (US$40,000) fixes it.\"",
        "Explanation: Keywords: PERT estimate, external subcontractor cost, in-house delivery, cost savings calculation. Using PERT to calculate the expected duration of in-house delivery, the project manager determines the expected effort period and applies the monthly resource costs. With the calculated PERT duration of 4 months and total monthly expenses of US$5,000 (two engineers at $700 each, one PM at $1,600, plus $2,000 in additional expenses), in-house delivery costs $20,000, yielding savings of $40,000 compared to the external contract cost of $60,000. (PMBOK Guide) – Seventh Edition, 2021, p. 34, 'Recognize, Evaluate, and Respond to System Interactions'\""
    ),
    # Q1467
    (
        "Explanation: Need: protect value and acceptance. Option A (Review the change control process to ensure quality management artifacts are updated as part of the change.) fixes it.\"",
        "Explanation: Keywords: quality control rejected, RCA shows untested change request component, root cause in change process. When RCA reveals that a quality failure was caused by a change request that bypassed the testing cycle, the systemic fix is to improve the change control process itself. Ensuring that quality management artifacts — including test plans — are updated as mandatory components of every approved change prevents the same gap from recurring on future requests. (PMBOK Guide) – Seventh Edition, 2021, p. 42, 'Build Quality into Processes and Deliverables'\""
    ),
    # Q1468
    (
        "Explanation: Need: listen to people needs. Option D (Communicate with the vendor and project team and explore possibilities for resolving the issue) fixes it.\"",
        "Explanation: Keywords: vendor can only deliver half before UAT, one week notice, project manager next action. When a vendor discloses a partial delivery risk close to a milestone, the project manager should not escalate immediately to cancellation or legal action. Opening direct communication with both the vendor and the project team creates a collaborative problem-solving environment where creative options — partial UAT, phased acceptance, or renegotiation — can be explored before resorting to adversarial responses. (PMBOK Guide) – Seventh Edition, 2021, p. 30, 'Effectively Engage with Stakeholders'\""
    ),
    # Q1469
    (
        "Explanation: Need: listen to people needs. Option A (Help sponsors and stakeholders craft the product vision, and bring the team and product owner together to clarify expectations) fixes it.\"",
        "Explanation: Keywords: company adopting agile, general manager worried about scope definition, ensure completely defined scope. In agile delivery, scope is defined through a shared product vision and collaborative expectation-setting rather than a locked requirements document. Helping sponsors craft the product vision and aligning the team and product owner on expectations creates the foundation for adaptive scope management — addressing the general manager's concern about completeness while preserving the flexibility that agile requires. (PMBOK Guide) – Seventh Edition, 2021, p. 30, 'Effectively Engage with Stakeholders'\""
    ),
    # Q1470
    (
        "Explanation: Need: listen to people needs. Option B (By focusing on the delivery of incremental working products to the customer) fixes it.\"",
        "Explanation: Keywords: final 10% takes longer, predictive vs agile measurement, incremental delivery advantage. Predictive projects often struggle in their final stages because all value is withheld until completion, making progress in the last stretch hard to quantify or accelerate. Agile methods improve on this by continuously delivering working increments throughout the project — so even when the final features are delayed, the customer has already received substantial value and the remaining percentage is truly the last slice. (PMBOK Guide) – Seventh Edition, 2021, p. 32, 'Focus on Value'\""
    ),
    # Q1471
    (
        "Explanation: Need: listen to people needs. Option A (Lessons learned database) fixes it.\"",
        "Explanation: Keywords: new file vault vendor, sponsor considering, assist sponsor decision, project manager review. When evaluating a new vendor for a service similar to one previously used, the most relevant source of information is the organization's own experience with comparable procurement. The lessons learned database captures insights about vendor performance, risks encountered, and outcomes achieved in prior projects — providing the sponsor with empirical guidance rather than speculation. (PMBOK Guide) – Seventh Edition, 2021, p. 34, 'Recognize, Evaluate, and Respond to System Interactions'\""
    ),
    # Q1472
    (
        "Explanation: Need: listen to people needs. Option D (Create a change request for the change control board (CCB) to review) fixes it.\"",
        "Explanation: Keywords: project sponsor requests scope addition, project scope finalized, accommodation approach. Even when the request comes from the project sponsor, additions to an approved scope must follow the formal change control process. Creating a change request for CCB review ensures the addition is evaluated for its impact on schedule, cost, and risk before being approved — preventing sponsor-driven scope creep that bypasses established governance. (PMBOK Guide) – Seventh Edition, 2021, p. 50, 'Enable Change to Achieve the Envisioned Future State'\""
    ),
    # Q1473
    (
        "Explanation: Need: listen to people needs. Option C (Consider the stakeholder's concerns and review the project charter with the project sponsor.) fixes it.\"",
        "Explanation: Keywords: influential stakeholder unclear about purpose and benefits, questioning project viability, next action. When a key stakeholder questions the viability of a project, dismissing the concern creates a significant engagement risk. The appropriate response is to take the concern seriously — reviewing the project charter with the sponsor ensures the project's purpose and business case are clearly understood and can be communicated to rebuild the stakeholder's confidence. (PMBOK Guide) – Seventh Edition, 2021, p. 30, 'Effectively Engage with Stakeholders'\""
    ),
    # Q1474
    (
        "Explanation: Need: listen to people needs. Option A (Update the communications management plan to satisfy the client's request) fixes it.\"",
        "Explanation: Keywords: remote solution team, client uncomfortable, project context and decision-making concerns. When a client expresses discomfort about how the remote team communicates and makes decisions, the underlying issue is an inadequate communications management plan. Updating the plan to explicitly address the client's information needs — frequency, format, and channels — ensures the client feels informed and confident without disrupting the team's working patterns. (PMBOK Guide) – Seventh Edition, 2021, p. 30, 'Effectively Engage with Stakeholders'\""
    ),
    # Q1477
    (
        "Explanation: Need: listen to people needs. Option C (Validate the requirement change with the product owner and development team before redefining the scope.) fixes it.\"",
        "Explanation: Keywords: frequently changing project, customer requirement change at daily meeting, what to do. When a customer raises a requirement change during a daily meeting, the project manager must validate the change through the appropriate channels before acting on it. Involving the product owner and development team ensures the change is properly understood, technically feasible, and correctly incorporated into the backlog — rather than being informally accepted or prematurely escalated. (PMBOK Guide) – Seventh Edition, 2021, p. 30, 'Effectively Engage with Stakeholders'\""
    ),
    # Q1478
    (
        "Explanation: Need: keep plans flexible. Option A (Reprioritize the backlog based on value and cost of delay divided by duration.) fixes it.\"",
        "Explanation: Keywords: database migration, end-of-support date, new impediment requires old platform one more year, higher support price. When an impediment changes the project's cost structure and timeline, the product owner must reconsider which backlog items deliver the most value relative to the additional delay cost they incur. Using a value and cost-of-delay divided by duration (CD3) prioritization approach ensures that remaining work is sequenced to minimize the cost of the extended platform dependency. (PMBOK Guide) – Seventh Edition, 2021, p. 32, 'Focus on Value'\""
    ),
    # Q1479
    (
        "Explanation: Need: listen to people needs. Option A (Discuss with the team how the project objectives can be met.) fixes it.\"",
        "Explanation: Keywords: milestone targets, sponsor bonus, unforeseen challenges, poor communication, tensions high. When a team is under pressure from a missed deadline incentive and tensions are elevated, the most productive response is to refocus the conversation on the actual objective — meeting the project goals. Discussing with the team how objectives can still be met transforms the energy from anxiety about the bonus to collaborative problem-solving about deliverables. (PMBOK Guide) – Seventh Edition, 2021, p. 30, 'Effectively Engage with Stakeholders'\""
    ),
    # Q1480
    (
        "Explanation: Need: guide and calm the team. Option A (Work with the procurement team to find alternative options.) fixes it.\"",
        "Explanation: Keywords: large equipment needed first, procurement lengthy approval process, next action. When the procurement process threatens to delay a project's start, the project manager should work collaboratively with the procurement team to explore alternatives rather than bypassing or pressuring them. Jointly identifying options — such as phased orders, pre-approval templates, or alternative vendors — finds a path through the constraint while respecting procurement governance. (PMBOK Guide) – Seventh Edition, 2021, p. 30, 'Effectively Engage with Stakeholders'\""
    ),
    # Q1481
    (
        "Explanation: Need: keep plans flexible. Option C (Define a project management plan for the new approach, as needed.) fixes it.\"",
        "Explanation: Keywords: PMO manager bad experience with Scrum, recommends switching to predictive, what to do. When an organizational decision is made to change delivery methodology, the project manager's responsibility is to ensure the transition is properly structured. Defining a project management plan for the new approach ensures that the change is executed with appropriate governance, process documentation, and stakeholder alignment — preventing an ad hoc methodology shift that could create more risk than it resolves. (PMBOK Guide) – Seventh Edition, 2021, p. 40, 'Tailor Based on Context'\""
    ),
    # Q1482
    (
        "Explanation: Need: keep plans flexible. Option C (Perform trend analysis.) fixes it.\"",
        "Explanation: Keywords: software development project, performance data analysis, forecast future slippage. Trend analysis examines historical performance data to identify patterns that indicate where the project is heading. By analyzing trends in key metrics such as schedule variance and earned value, the project manager can forecast whether slippage is likely and take proactive corrective action before the schedule impact becomes irreversible. (PMBOK Guide) – Seventh Edition, 2021, p. 46, 'Optimize Risk Responses'\""
    ),
    # Q1483
    (
        "Explanation: Need: guide and calm the team. Option B (Schedule virtual sessions with the specialist to guide the team in completing the activity.) fixes it.\"",
        "Explanation: Keywords: travel restrictions, specialist cannot come on-site, activity cannot be completed without expertise. When a specialist is unable to physically attend due to travel restrictions, the project manager must bridge the knowledge gap through technology. Scheduling virtual sessions allows the specialist to guide the local team through the activity in real time, combining the expert's knowledge with the team's on-site access — an effective workaround for the physical constraint. (PMBOK Guide) – Seventh Edition, 2021, p. 28, 'Create a Collaborative Team Environment'\""
    ),
    # Q1484
    (
        "Explanation: Need: guide and calm the team. Option B (Discuss with the team and assess the reasons that led to the delay.) fixes it.\"",
        "Explanation: Keywords: execution stage, team member running behind, potential milestone impact, first action. Before escalating or reassigning work, the project manager should understand why the delay occurred. Discussing the situation with the team surfaces the root cause — whether it is a skill gap, an unclear requirement, a dependency issue, or an external blocker — enabling a targeted corrective action rather than a reactive one that may not address the real problem. (PMBOK Guide) – Seventh Edition, 2021, p. 36, 'Demonstrate Leadership Behaviors'\""
    ),
    # Q1485
    (
        "Explanation: Need: guide and calm the team. Option C (Establish a productive environment where all team members can assist one another with the workload.) fixes it.\"",
        "Explanation: Keywords: stressful situation, stress behavior spreading, coach team, change mindset, efficiency. When stress behavior begins to spread across a team, the most sustainable intervention is to create an environment of mutual support. Establishing a culture where team members actively help each other with the workload reduces individual burden, builds psychological safety, and converts the stress response from isolating to cooperative — directly addressing both efficiency and team well-being. (PMBOK Guide) – Seventh Edition, 2021, p. 36, 'Demonstrate Leadership Behaviors'\""
    ),
    # Q1486
    (
        "Explanation: Need: guide and calm the team. Option C (Delegate certain authorities and share information to allow fair decision-making.) fixes it.\"",
        "Explanation: Keywords: global team, different time zones, high trust, timely decisions needed, delegation approach. In a trusted global team that requires fast decisions across time zones, effective delegation means authorizing team members to act within defined boundaries while equipping them with the information they need. Delegating certain authorities alongside relevant information enables fair, timely decisions without creating either chaos from excessive delegation or bottlenecks from excessive control. (PMBOK Guide) – Seventh Edition, 2021, p. 36, 'Demonstrate Leadership Behaviors'\""
    ),
    # Q1487
    (
        "Explanation: Need: guide and calm the team. Option C (Detail the reason for the deliverable delay in the status report.) fixes it.\"",
        "Explanation: Keywords: second iteration, key deliverable depends on new device acquisition, what to do. When a deliverable is at risk due to a dependency that is not yet resolved, the project manager's immediate obligation is transparent reporting. Documenting the reason for the anticipated delay in the status report keeps stakeholders informed of the risk, creates a record of when the issue was identified, and sets expectations for recovery without overpromising. (PMBOK Guide) – Seventh Edition, 2021, p. 34, 'Recognize, Evaluate, and Respond to System Interactions'\""
    ),
    # Q1488
    (
        "Explanation: Need: guide and calm the team. Option C (Review lessons learned from similar projects with the team.) fixes it.\"",
        "Explanation: Keywords: adaptive approach, specialized experts, practical plans, high buy-in, lessons learned. Practical planning in a complex adaptive environment benefits most from empirical knowledge — what has worked and what has failed in comparable contexts. Reviewing lessons learned with the team before planning begins surfaces relevant insights, builds shared context, and fosters the collaborative ownership that drives genuine buy-in among experienced specialists. (PMBOK Guide) – Seventh Edition, 2021, p. 28, 'Create a Collaborative Team Environment'\""
    ),
    # Q1489
    (
        "Explanation: Need: guide and calm the team. Option D (Acknowledge that the risks will be handled in the corresponding iteration.) fixes it.\"",
        "Explanation: Keywords: agile team, brainstorming and prioritizing risks by severity, what to do about identified risks. In agile delivery, risks are not all addressed immediately — they are acknowledged and managed within the iteration cadence that is most contextually appropriate. Acknowledging that each identified risk will be handled during its corresponding iteration aligns risk management with the iterative delivery rhythm, avoiding premature action on risks that may not materialize or may change in nature before they are relevant. (PMBOK Guide) – Seventh Edition, 2021, p. 46, 'Optimize Risk Responses'\""
    ),
    # Q1490
    (
        "Explanation: Need: listen to people needs. Option B (Refer the stakeholder to the delivery specifications in the statement of work (SOW).) fixes it.\"",
        "Explanation: Keywords: customer stakeholder not in sales process, demands out-of-scope requirements without additional cost, vendor. When a stakeholder requests work that is not in scope and refuses to acknowledge the contract, the most appropriate response is to direct them to the contractual specifications. The statement of work defines the agreed-upon deliverables and forms the authoritative basis for scope discussions — referring the stakeholder to it is both professional and factually grounded. (PMBOK Guide) – Seventh Edition, 2021, p. 25, 'Be a Diligent, Respectful, and Caring Steward'\""
    ),
    # Q1491
    (
        "Explanation: Need: listen to people needs. Option C (Assess the impact to the scope and submit a change request for approval of the two locations before including them in the scope of the project.) fixes it.\"",
        "Explanation: Keywords: sponsor insists on two locations, project charter approved with one location, what to do. When a sponsor requests a scope expansion after the project charter has been approved, the change must be formally evaluated and authorized — even though the sponsor is the requester. Assessing the impact and submitting a change request ensures the additional scope is reviewed for its effect on cost, schedule, and risk before being incorporated into the project baseline. (PMBOK Guide) – Seventh Edition, 2021, p. 50, 'Enable Change to Achieve the Envisioned Future State'\""
    ),
    # Q1492
    (
        "Explanation: Need: guide and calm the team. Options B and E (Conduct training sessions with the team so that the team can understand what the agile approach and mindset are.; Brainstorm with the team to understand the specifics of the team's project and to identify possible alternative approaches for the team.) work together.\"",
        "Explanation: Keywords: banking IT team, 10+ years predictive, management wants agile, team resistant to change. Effective methodology transitions require both education and engagement. Training sessions help the team understand what agile actually involves — dispelling misconceptions — while brainstorming the team's specific project context identifies whether pure agile, hybrid, or a tailored approach is most appropriate. Together, these actions build informed consent rather than imposed compliance. (PMBOK Guide) – Seventh Edition, 2021, p. 40, 'Tailor Based on Context'\""
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
