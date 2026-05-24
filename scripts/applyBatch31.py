MD_FILE = './src/imports/project-management-questions-1.md'

with open(MD_FILE, 'r', encoding='utf-8') as f:
    content = f.read()

replacements = [
    # Q1493
    (
        "Explanation: Need: listen to people needs. Option C (Review the approved exit criteria for the product.) fixes it.\"",
        "Explanation: Keywords: customer concerned about quality, production deployment approaching, ensure acceptance. The most authoritative reference for evaluating whether a product is ready for deployment is the pre-approved exit criteria. Reviewing these criteria ensures that both the project team and the customer are evaluating readiness against the same standard — preventing subjective quality disputes and providing a clear basis for acceptance or rejection. (PMBOK Guide) – Seventh Edition, 2021, p. 42, 'Build Quality into Processes and Deliverables'\""
    ),
    # Q1494
    (
        "Explanation: Need: listen to people needs. Option D (Ensure that the reports comply with the communications management plan.) fixes it.\"",
        "Explanation: Keywords: key stakeholder says reports inadequate, first action, communications management plan. When a stakeholder complains about report quality, the first step is to verify whether the reports actually comply with the agreed communications management plan. If they do, the plan itself may need updating; if they do not, the reporting process must be corrected. Starting from the plan establishes the objective baseline for what constitutes adequate communication. (PMBOK Guide) – Seventh Edition, 2021, p. 30, 'Effectively Engage with Stakeholders'\""
    ),
    # Q1495
    (
        "Explanation: Need: guide and calm the team. Option A (Reach an agreement with the team on how to handle the situation.) fixes it.\"",
        "Explanation: Keywords: mid-iteration, team member leaves for personal issues, no replacement from procurement, activities reassignment. When a team member unexpectedly leaves during an iteration, the most effective response in a self-organizing agile team is to involve the team in deciding how to handle the redistribution. Reaching a collective agreement respects the team's autonomy, leverages their knowledge of the work involved, and builds shared ownership of the solution. (PMBOK Guide) – Seventh Edition, 2021, p. 28, 'Create a Collaborative Team Environment'\""
    ),
    # Q1496
    (
        "Explanation: Need: listen to people needs. Option A (Iterative scheduling) fixes it.\"",
        "Explanation: Keywords: agile project, oil and gas client, various unknowns, scheduling method. When a project has significant unknowns, iterative scheduling is the appropriate technique because it allows the schedule to be developed progressively as more information becomes available. Rather than committing to a detailed timeline upfront, iterative scheduling embraces uncertainty and adapts planning to each iteration's reality, maintaining flexibility while providing structure. (PMBOK Guide) – Seventh Edition, 2021, p. 40, 'Tailor Based on Context'\""
    ),
    # Q1497
    (
        "Explanation: Need: guide and calm the team. Option D (Schedule a meeting with the team to assess the impact of the change.) fixes it.\"",
        "Explanation: Keywords: mid-execution agile project, strategic shift to digital transformation, organization-level change. When an organization-level strategic change is announced mid-project, the project manager must first understand how it affects the current work. Meeting with the team to assess the impact provides a grounded analysis before any response to the product owner, sponsor, or backlog is considered — ensuring that any subsequent actions are informed rather than reactive. (PMBOK Guide) – Seventh Edition, 2021, p. 34, 'Recognize, Evaluate, and Respond to System Interactions'\""
    ),
    # Q1498
    (
        "Explanation: Need: keep plans flexible. Option B (Assess the impact of the change and review the project management plan for next steps.) fixes it.\"",
        "Explanation: Keywords: HR acquisition process changed, longer processing, project urgently needs new resources. When an organizational process changes in a way that affects project execution, the project manager must first quantify the impact before deciding on a response. Assessing the impact and reviewing the project management plan identifies whether schedule buffers can absorb the delay, whether escalation is warranted, or whether a plan adjustment is needed. (PMBOK Guide) – Seventh Edition, 2021, p. 34, 'Recognize, Evaluate, and Respond to System Interactions'\""
    ),
    # Q1499
    (
        "Explanation: Need: listen to people needs. Option C (Perform an analysis of the key cost drivers and present alternatives.) fixes it.\"",
        "Explanation: Keywords: new technology project, sponsor wants to reduce labor cost without introducing risk, analysis needed. Reducing labor cost without increasing project risk requires a careful analysis of where costs originate and which drivers can be modified. Identifying key cost drivers and presenting alternatives gives the sponsor options to evaluate — supporting an informed decision rather than an arbitrary cut that could inadvertently compromise the delivery. (PMBOK Guide) – Seventh Edition, 2021, p. 32, 'Focus on Value'\""
    ),
    # Q1500
    (
        "Explanation: Need: listen to people needs. Option B (Schedule a quality review meeting and include the sponsor's complaints.) fixes it.\"",
        "Explanation: Keywords: closing phase, sponsor complains about quality, acceptance document signed, building next phase plan. Even when quality acceptance documents have been signed, a sponsor's post-phase quality complaint must be taken seriously rather than dismissed. Scheduling a quality review meeting that includes the sponsor's concerns treats them as actionable feedback, allows root cause investigation, and informs the planning for the next phase to prevent the same issues from recurring. (PMBOK Guide) – Seventh Edition, 2021, p. 42, 'Build Quality into Processes and Deliverables'\""
    ),
    # Q1501
    (
        "Explanation: Need: secure people or vendors. Option B (Amend the contract terms and sign a revised contract with the successful bidder.) fixes it.\"",
        "Explanation: Keywords: power-generation facility, financial regulation change on company tax, contract terms must be revised before signing. When contract terms must change due to new regulatory requirements before a contract is executed, the correct action is to formally amend the terms and execute the revised contract with the selected bidder. This maintains the procurement result while ensuring that the signed document reflects the current legal and compliance environment. (PMBOK Guide) – Seventh Edition, 2021, p. 25, 'Be a Diligent, Respectful, and Caring Steward'\""
    ),
    # Q1502
    (
        "Explanation: Need: listen to people needs. Option B (Invite the stakeholders to discuss a mitigation plan.) fixes it.\"",
        "Explanation: Keywords: fifth iteration, team member left unexpectedly, next action. When a team member departs unexpectedly late in a project, the impact assessment and mitigation decisions benefit from stakeholder input. Inviting stakeholders to discuss a mitigation plan ensures that recovery options — scope adjustment, resource reallocation, or timeline extension — are evaluated collaboratively with the people who have the authority and context to approve changes. (PMBOK Guide) – Seventh Edition, 2021, p. 30, 'Effectively Engage with Stakeholders'\""
    ),
    # Q1503
    (
        "Explanation: Need: listen to people needs. Option C (Stakeholder's needs) fixes it.\"",
        "Explanation: Keywords: additional planning sessions, international stakeholder, product not meeting client needs, factor to consider. When a project requires unplanned planning sessions because stakeholder concerns were not initially incorporated, the root cause is typically a failure to consider stakeholder needs comprehensively during requirements development. Identifying and prioritizing each stakeholder's actual needs — not just their stated requirements — during planning prevents the type of retroactive rework that the international stakeholder's concerns triggered. (PMBOK Guide) – Seventh Edition, 2021, p. 30, 'Effectively Engage with Stakeholders'\""
    ),
    # Q1504
    (
        "Explanation: Need: listen to people needs. Option A (Incorporate and prioritize the risks in the risk register according to impact.) fixes it.\"",
        "Explanation: Keywords: early development, already delivering functionality, risks identified, mitigation strategy in development. When an agile team identifies risks during early delivery, the appropriate next step is to formally incorporate them into the risk register and prioritize them by impact. This creates a structured record that guides the mitigation strategy development and ensures that high-impact risks receive appropriate attention relative to lower-priority items. (PMBOK Guide) – Seventh Edition, 2021, p. 46, 'Optimize Risk Responses'\""
    ),
    # Q1505
    (
        "Explanation: Need: guide and calm the team. Option D (Facilitated cross-functional knowledge transfer during the project.) fixes it.\"",
        "Explanation: Keywords: team member sick, only one skilled in component, team concerned, prevention. Single points of knowledge create brittle teams that are vulnerable to any individual's absence. The root cause of the team's predicament was insufficient cross-training during the project. Facilitating cross-functional knowledge transfer from the beginning of the project would have ensured that multiple team members could support any given component, eliminating the single point of failure. (PMBOK Guide) – Seventh Edition, 2021, p. 28, 'Create a Collaborative Team Environment'\""
    ),
    # Q1506
    (
        "Explanation: Need: guide and calm the team. Option B (Allow the project team to discuss the problem with this team member.) fixes it.\"",
        "Explanation: Keywords: agile testing team member, poor performance two iterations, team difficulty meeting goals. In an agile environment, the team shares collective responsibility for performance. Allowing the team to address the performance concern with the underperforming member respects the self-organizing nature of the team and leverages peer accountability — which is often more effective and less disruptive than manager-led intervention for individual performance issues. (PMBOK Guide) – Seventh Edition, 2021, p. 28, 'Create a Collaborative Team Environment'\""
    ),
    # Q1508
    (
        "Explanation: Need: listen to people needs. Option B (Develop a new strategy for communication and management of resources.) fixes it.\"",
        "Explanation: Keywords: outsourced resources, all working remotely due to unforeseen risk, deliver assurance. When a sudden shift to remote work affects both internal and outsourced team members, existing communication and management approaches may not translate effectively to the new environment. Developing a new strategy that explicitly addresses how remote outsourced vendors will be coordinated, monitored, and held accountable ensures delivery continuity despite the disruption. (PMBOK Guide) – Seventh Edition, 2021, p. 30, 'Effectively Engage with Stakeholders'\""
    ),
    # Q1509
    (
        "Explanation: Need: listen to people needs. Option A (Developed a detailed, phased procurement management plan including all activities required and had the client approve it.) fixes it.\"",
        "Explanation: Keywords: consultancy contracted 18 months, 32-month project, client asks why, unplanned second bidding. The misalignment between the contract duration and the project duration reflects a failure to plan and communicate the full procurement lifecycle. A detailed, phased procurement management plan — reviewed and approved by the client — would have made the multi-phase contracting approach explicit from the beginning, preventing the client's surprise and the costly unplanned rebidding process. (PMBOK Guide) – Seventh Edition, 2021, p. 25, 'Be a Diligent, Respectful, and Caring Steward'\""
    ),
    # Q1510
    (
        "Explanation: Need: listen to people needs. Option B (Integrate the acceptance criteria review into the definition of ready (DoR) for each feature and associated tests into the feature's definition of done (DoD).) fixes it.\"",
        "Explanation: Keywords: broad product features, different user profiles, acceptance criteria not common, how to ensure appropriateness. When features serve diverse user profiles and no single acceptance criteria applies to all, quality must be embedded at the individual feature level. Integrating acceptance criteria into the DoR ensures each feature is properly specified before work begins, while incorporating tests into the DoD ensures each feature is validated against its own quality standard before being declared complete. (PMBOK Guide) – Seventh Edition, 2021, p. 42, 'Build Quality into Processes and Deliverables'\""
    ),
    # Q1511
    (
        "Explanation: Need: guide and calm the team. Option D (Advise the team that solely focusing on artifacts will not produce successful project deliverables.) fixes it.\"",
        "Explanation: Keywords: team prioritizing artifacts, enforcing rigidly, delays in deliverables, how to respond. Artifacts are tools that support project delivery, not ends in themselves. When a team is so focused on documentation that it delays working deliverables, the project manager must reorient the team's priorities. Advising that artifact creation alone does not produce successful outcomes redirects effort toward what actually creates value — the deliverables the customer needs. (PMBOK Guide) – Seventh Edition, 2021, p. 32, 'Focus on Value'\""
    ),
    # Q1512
    (
        "Explanation: Need: listen to people needs. Option D (Meet with the new representative to determine their understanding of the project and address their concerns.) fixes it.\"",
        "Explanation: Keywords: customer new representative, concerns about status meetings, wants to contact team directly, multiyear project. When a newly delegated customer representative expresses concerns about communication and access, the most effective first response is to understand their perspective directly. Meeting with the representative allows the project manager to identify gaps in their project understanding, explain the existing communication structure, and determine what adjustments might be needed to meet their legitimate needs. (PMBOK Guide) – Seventh Edition, 2021, p. 30, 'Effectively Engage with Stakeholders'\""
    ),
    # Q1513
    (
        "Explanation: Need: keep plans flexible. Option B (Quality management plan) fixes it.\"",
        "Explanation: Keywords: industry standards not reflected in project deliverables, what to review. The quality management plan defines the quality standards, metrics, and processes that the project has committed to following — including relevant industry standards. If deliverables do not appear to reflect those standards, reviewing the quality management plan identifies whether the standards were correctly captured, whether they were communicated to the team, and whether the planned quality processes are being followed. (PMBOK Guide) – Seventh Edition, 2021, p. 42, 'Build Quality into Processes and Deliverables'\""
    ),
    # Q1514
    (
        "Explanation: Need: listen to people needs. Option A (Defined acceptance criteria in a quality checklist agreed upon before starting the build phase) fixes it.\"",
        "Explanation: Keywords: building construction, client complains components don't meet requirements, firm milestones, prevention. Post-build quality disputes typically arise because the standards for acceptance were never made explicit and mutually agreed upon. Defining detailed acceptance criteria in a quality checklist before the build phase begins — and securing client agreement — creates an objective reference that both parties can use to evaluate the completed work, preventing the subjective disputes that occurred. (PMBOK Guide) – Seventh Edition, 2021, p. 42, 'Build Quality into Processes and Deliverables'\""
    ),
    # Q1515
    (
        "Explanation: Need: guide and calm the team. Option D (Agree on a new time and reschedule the daily standups.) fixes it.\"",
        "Explanation: Keywords: virtual daily standups, half the team late or missing, what to do. When attendance at daily meetings is consistently poor, the most likely cause is a scheduling conflict rather than disengagement. Agreeing on a new meeting time that works for the full team — rather than modifying the meeting format or format — addresses the practical root cause and restores the effectiveness of the standup as a coordination tool. (PMBOK Guide) – Seventh Edition, 2021, p. 28, 'Create a Collaborative Team Environment'\""
    ),
    # Q1516
    (
        "Explanation: Need: listen to people needs. Option D (Invite the Scrum team members as mandatory participants.) fixes it.\"",
        "Explanation: Keywords: hybrid project deployed, lessons learned workshops, stakeholder says Scrum team is waste of time. Excluding the people who did the work from lessons learned workshops produces an incomplete picture of what happened and limits the quality of the insights captured. The Scrum team's firsthand experience with the delivery process is irreplaceable — making them mandatory participants ensures that the lessons learned reflect the full reality of how the project was executed, not just the management perspective. (PMBOK Guide) – Seventh Edition, 2021, p. 48, 'Embrace Adaptability and Resiliency'\""
    ),
    # Q1517
    (
        "Explanation: Need: guide and calm the team. Option C (Support the team to identify an approach to resolve the problem.) fixes it.\"",
        "Explanation: Keywords: cumulative flow chart, testing bottleneck, self-organizing team, testing skills gap. When a bottleneck is identified in a self-organizing team, a servant leader's role is to support the team's problem-solving rather than prescribe a solution. Helping the team identify their own approach to the testing skills gap respects their autonomy, leverages their contextual knowledge of the work, and builds their capability to resolve similar issues independently in the future. (PMBOK Guide) – Seventh Edition, 2021, p. 36, 'Demonstrate Leadership Behaviors'\""
    ),
    # Q1518
    (
        "Explanation: Need: guide and calm the team. Option C (Work breakdown structure (WBS)) fixes it.\"",
        "Explanation: Keywords: project charter approved, project manager subdividing work packages, what is this called. Subdividing project deliverables into smaller, more manageable components is the defining activity of WBS creation. The WBS hierarchically organizes the total scope of work into work packages that can be scheduled, cost estimated, monitored, and assigned — it is the foundation upon which the entire project schedule and budget are built. (PMBOK Guide) – Seventh Edition, 2021, p. 42, 'Build Quality into Processes and Deliverables'\""
    ),
    # Q1519
    (
        "Explanation: Need: guide and calm the team. Option B (Support the developers with their intention to learn the new technology.) fixes it.\"",
        "Explanation: Keywords: key product requires new technology, experienced developers volunteer to learn, what to do. When capable team members proactively volunteer to develop the skills the project needs, the project manager's role is to support and enable that initiative. Backing their intention to learn demonstrates trust in the team, avoids the cost and integration risks of external hiring, and builds long-term capability within the organization. (PMBOK Guide) – Seventh Edition, 2021, p. 36, 'Demonstrate Leadership Behaviors'\""
    ),
    # Q1520
    (
        "Explanation: Need: listen to people needs. Option A (Collect feedback from the team to discuss alternatives to enhance the communication.) fixes it.\"",
        "Explanation: Keywords: distributed global team, communications management plan, continually evaluate virtual engagement effectiveness. Effective communication for distributed teams is not a one-time setup — it requires ongoing calibration. Regularly collecting feedback from the team surfaces issues with the current approach and opens discussions about alternatives, ensuring that the communication strategy evolves with the team's actual experience rather than remaining static while effectiveness degrades. (PMBOK Guide) – Seventh Edition, 2021, p. 30, 'Effectively Engage with Stakeholders'\""
    ),
    # Q1521
    (
        "Explanation: Need: listen to people needs. Option B (Escalate the issue of project impact to the project sponsor.) fixes it.\"",
        "Explanation: Keywords: mandatory compliance requirement, iterative project execution phase, team aware, next action. When a mandatory compliance requirement surfaces mid-project, the project manager must escalate to the sponsor because compliance changes often have implications for funding, schedule, and strategic priorities that only the sponsor can authorize. The product owner manages backlog, but a mandatory regulatory change affecting the project goes beyond product decisions and requires executive-level attention. (PMBOK Guide) – Seventh Edition, 2021, p. 30, 'Effectively Engage with Stakeholders'\""
    ),
    # Q1522
    (
        "Explanation: Need: guide and calm the team. Option C (Three-point estimating) fixes it.\"",
        "Explanation: Keywords: software developers new to company, never developed similar application, estimation technique. Three-point estimating is ideal when the development team lacks historical experience with a particular type of work. By capturing optimistic, pessimistic, and most likely estimates, it explicitly accounts for the uncertainty that characterizes first-time work and produces a more realistic estimate range than analogous or parametric methods, which both require comparable prior data. (PMBOK Guide) – Seventh Edition, 2021, p. 44, 'Navigate Complexity'\""
    ),
    # Q1523
    (
        "Explanation: Need: guide and calm the team. Option B (Record the changes using the risk register and continue monitoring.) fixes it.\"",
        "Explanation: Keywords: complex project, numerous change requests from various teams, may not meet objectives. When the volume of change requests creates a risk that project objectives may not be met, the project manager must track this as a formal risk rather than processing each request in isolation. Recording the cumulative change impact in the risk register and continuing to monitor ensures that the risk is visible to decision-makers and that threshold-based escalation can be triggered if the situation deteriorates. (PMBOK Guide) – Seventh Edition, 2021, p. 46, 'Optimize Risk Responses'\""
    ),
    # Q1524
    (
        "Explanation: Need: guide and calm the team. Option B (Prepared an inception deck and clearly explained the purpose of agile ceremonies and their benefits to the project.) fixes it.\"",
        "Explanation: Keywords: company adopted agile, team members consider ceremonies unnecessary, prevention. Resistance to agile ceremonies typically stems from a lack of understanding of their purpose and value. An inception deck prepared before the project begins is the ideal vehicle for explaining the rationale for each ceremony, connecting it to project outcomes, and building shared commitment to the process. Without this upfront alignment, ceremonies are experienced as imposed overhead rather than valuable collaboration tools. (PMBOK Guide) – Seventh Edition, 2021, p. 40, 'Tailor Based on Context'\""
    ),
    # Q1525
    (
        "Explanation: Need: guide and calm the team. Option D (Encourage the team to collaborate to resolve their understanding of the feature.) fixes it.\"",
        "Explanation: Keywords: first agile project, team struggling to agree on feature scope, sprint, how to help. When team members disagree on the scope of a feature, the most productive response is to facilitate collaboration rather than deciding for the team or bypassing the discussion. Encouraging the team to work through the disagreement together builds their collective understanding of the feature and develops the collaborative problem-solving muscle they need for the rest of the project. (PMBOK Guide) – Seventh Edition, 2021, p. 28, 'Create a Collaborative Team Environment'\""
    ),
    # Q1526
    (
        "Explanation: Need: guide and calm the team. Option C (Individual and personal objectives) fixes it.\"",
        "Explanation: Keywords: coaching model, support and recognize team growth, define coaching strategy. Effective coaching must be tailored to the individual being coached, not delivered uniformly. A coaching strategy grounded in individual and personal objectives ensures that the support, development activities, and recognition mechanisms resonate with what each team member actually cares about — making coaching more motivating and more likely to produce lasting growth. (PMBOK Guide) – Seventh Edition, 2021, p. 36, 'Demonstrate Leadership Behaviors'\""
    ),
    # Q1527
    (
        "Explanation: Need: guide and calm the team. Option D (Delegate the decision-making authority of some tasks to the team.) fixes it.\"",
        "Explanation: Keywords: team refers all decisions to project manager, PM in meetings all day, delays in tasks. When the project manager is a bottleneck for all team decisions, the solution is not better scheduling — it is structural delegation. Distributing decision-making authority to the team for appropriate tasks empowers team members to proceed autonomously, eliminates unnecessary queuing, and allows the project manager to focus on decisions that genuinely require their level of oversight. (PMBOK Guide) – Seventh Edition, 2021, p. 36, 'Demonstrate Leadership Behaviors'\""
    ),
    # Q1528
    (
        "Explanation: Need: guide and calm the team. Option D (Invite the board member to the next sprint review.) fixes it.\"",
        "Explanation: Keywords: technically complex project, first agile project in program, board member wants to see scope delivery progress. The sprint review is the designed agile event for demonstrating completed work to stakeholders and gathering feedback on progress. It is the appropriate and most informative venue for a board member who wants to assess how the project is delivering against its scope — more so than a standup or retrospective, which serve different purposes. (PMBOK Guide) – Seventh Edition, 2021, p. 30, 'Effectively Engage with Stakeholders'\""
    ),
    # Q1529
    (
        "Explanation: Need: guide and calm the team. Option C (Submit a change request to the cost baseline through the governance process to fund the additional testing.) fixes it.\"",
        "Explanation: Keywords: government accounting compliance change, testing costs exceeding budget, matrix organization. When a project's testing costs exceed the approved budget — even due to a change that was made at no development cost — the additional funding must be formally authorized through the governance process. Submitting a change request to the cost baseline ensures transparency, creates an auditable record, and allows the appropriate authority to approve the reallocation of funds. (PMBOK Guide) – Seventh Edition, 2021, p. 50, 'Enable Change to Achieve the Envisioned Future State'\""
    ),
    # Q1530
    (
        "Explanation: Need: guide and calm the team. Option D (Discuss with the project team alternative options to deliver as planned.) fixes it.\"",
        "Explanation: Keywords: vendor may not deliver on time, internal team ahead of schedule, team asks if should continue. When a vendor delay threatens the project timeline while the internal team has available capacity, the project manager should explore whether that capacity can be redirected to absorb the impact. Discussing alternative options with the project team identifies creative solutions — such as supporting the vendor, front-loading other work, or finding substitute resources — that can keep the project on track. (PMBOK Guide) – Seventh Edition, 2021, p. 34, 'Recognize, Evaluate, and Respond to System Interactions'\""
    ),
    # Q1531
    (
        "Explanation: Need: guide and calm the team. Option A (Ask the project planner to identify the critical path and respective delayed activities, and then investigate the reasons for the delay.) fixes it.\"",
        "Explanation: Keywords: midway execution, possible schedule delay, team working hard, many deliverables completed. When a potential schedule delay is identified despite high team effort, the first step is to determine precisely where the delay is occurring and why. Identifying the critical path and the specific delayed activities focuses the investigation on the most schedule-sensitive work, ensuring that corrective actions are targeted rather than broad and that the root cause of the variance is addressed. (PMBOK Guide) – Seventh Edition, 2021, p. 46, 'Optimize Risk Responses'\""
    ),
    # Q1532
    (
        "Explanation: Need: guide and calm the team. Option A (Meet with the project team to review the work breakdown structure (WBS) and confirm deliverables have been delivered.) fixes it.\"",
        "Explanation: Keywords: successful deployment, transitioning to operational state, before closeout, what to do. Before formally closing a project and declaring readiness for operational transition, the project manager must verify that all committed deliverables have actually been completed. Reviewing the WBS with the team provides a systematic checklist of all planned work, ensuring that nothing has been overlooked before resources are released and the project is officially handed over to operations. (PMBOK Guide) – Seventh Edition, 2021, p. 42, 'Build Quality into Processes and Deliverables'\""
    ),
    # Q1533
    (
        "Explanation: Need: guide and calm the team. Option D (Provide team members with the necessary coaching and mentoring.) fixes it.\"",
        "Explanation: Keywords: enthusiastic team, lacks experience, reduce risk of project failure. When a team has the right attitude but insufficient experience, the most sustainable investment is direct coaching and mentoring from the experienced project manager. This builds the team's capability in context, provides real-time guidance during actual project work, and reduces failure risk more effectively than adding external resources or quality checks that do not address the underlying skill gap. (PMBOK Guide) – Seventh Edition, 2021, p. 36, 'Demonstrate Leadership Behaviors'\""
    ),
    # Q1534
    (
        "Explanation: Need: listen to people needs. Option A (Re-visit the project charter and seek other alternatives.) fixes it.\"",
        "Explanation: Keywords: strategic project, only one bidder, significantly large price, sponsor not convinced about ROI. When the sole bid received significantly exceeds the acceptable investment threshold and the sponsor doubts the return on investment, continuing with the procurement as-is would be imprudent. Revisiting the project charter allows the project manager and sponsor to reassess the project's business justification and explore alternatives — including scope changes, phased delivery, or alternative sourcing approaches — before committing to an uncertain ROI. (PMBOK Guide) – Seventh Edition, 2021, p. 32, 'Focus on Value'\""
    ),
    # Q1535
    (
        "Explanation: Need: guide and calm the team. Option B (Arrange formal training for this member to gain sufficient knowledge to reduce the impact on team performance.) fixes it.\"",
        "Explanation: Keywords: strict time constraints, team member silent, not knowledgeable about technology solution, concerned. When a team member's knowledge gap is creating a productivity risk in a time-constrained project, the most direct and effective intervention is formal training. Targeted training addresses the specific skill deficit, brings the team member to an operational level, and provides a faster return than informal peer learning in a high-pressure environment. (PMBOK Guide) – Seventh Edition, 2021, p. 36, 'Demonstrate Leadership Behaviors'\""
    ),
    # Q1536
    (
        "Explanation: Need: guide and calm the team. Option D (Discuss the conflict early among the affected team members using a direct, collaborative approach.) fixes it.\"",
        "Explanation: Keywords: two team members conflicting, technical and interpersonal levels, first two actions. Conflict that spans both technical and interpersonal dimensions requires direct engagement rather than deferral or delegation to HR. Addressing the conflict early — before it escalates — through a direct conversation with the affected team members uses a collaborative approach that respects the individuals while establishing clear expectations for how conflict should be managed within the team. (PMBOK Guide) – Seventh Edition, 2021, p. 36, 'Demonstrate Leadership Behaviors'\""
    ),
    # Q1537
    (
        "Explanation: Need: listen to people needs. Option C (Allow the team to work through it on their own unless help is needed.) fixes it.\"",
        "Explanation: Keywords: design discussion, collective disagreement not outright conflict, self-organizing agile team, user experience. In agile environments, self-organizing teams are expected and capable of working through collaborative disagreements about approach or design. A project manager who intervenes prematurely in a healthy debate undermines team autonomy and trust. Allowing the team to work through the disagreement independently — unless they explicitly need assistance — respects the self-organizing principle and allows the best solution to emerge organically. (PMBOK Guide) – Seventh Edition, 2021, p. 28, 'Create a Collaborative Team Environment'\""
    ),
    # Q1538
    (
        "Explanation: Need: protect value and acceptance. Option B (Projects will deliver early and use value based on priority.) fixes it.\"",
        "Explanation: Keywords: organization adopting agile, business transformation, implement agile project delivery, main reason. The primary advantage of agile over traditional delivery is the continuous delivery of value based on what matters most to the business, rather than waiting until the end of the project for all value to be realized. Projects using agile methods deliver working increments early and prioritize the backlog to ensure that the highest-value features are always addressed first — the defining characteristic that justifies agile adoption. (PMBOK Guide) – Seventh Edition, 2021, p. 32, 'Focus on Value'\""
    ),
    # Q1539
    (
        "Explanation: Need: guide and calm the team. Option D (Discuss the team members' concern with the construction manager and seek solutions.) fixes it.\"",
        "Explanation: Keywords: multicultural team, two members not responding to construction manager, cultural differences, improve situation. Cultural differences that affect working relationships require a facilitated dialogue rather than directives to one party or the other. Discussing the team members' concerns directly with the construction manager — and jointly seeking solutions — addresses the issue collaboratively and builds the cross-cultural awareness needed to prevent similar tensions from recurring. (PMBOK Guide) – Seventh Edition, 2021, p. 36, 'Demonstrate Leadership Behaviors'\""
    ),
    # Q1540
    (
        "Explanation: Need: listen to people needs. Option C (Assess the environmental changes and recommend a pivot for the project.) fixes it.\"",
        "Explanation: Keywords: travel app, travel restrictions, features not useable, hybrid project, first action. When external environmental changes render the planned deliverable largely valueless, the project manager must reassess the project's direction before continuing to invest in work that will not achieve its intended outcome. Assessing the changes and recommending a pivot repositions the project toward a viable objective, demonstrating the adaptive thinking that preserves business value in the face of unforeseen disruption. (PMBOK Guide) – Seventh Edition, 2021, p. 48, 'Embrace Adaptability and Resiliency'\""
    ),
    # Q1541
    (
        "Explanation: Need: listen to people needs. Option B (Prioritize deliverables based on business value and define frequent releases.) fixes it.\"",
        "Explanation: Keywords: customer wants fewer iterations, reduce number of iterations for on-time completion. When a customer wants to reduce iterations without compromising the timeline, the solution is to ensure that each iteration delivers maximum business value through rigorous prioritization and more frequent releases. Prioritizing by business value and defining clear release milestones satisfies the customer's desire for faster visible progress while maintaining the iterative cadence that reduces delivery risk. (PMBOK Guide) – Seventh Edition, 2021, p. 32, 'Focus on Value'\""
    ),
    # Q1542
    (
        "Explanation: Need: listen to people needs. Option D (Use a shared collaboration platform.) fixes it.\"",
        "Explanation: Keywords: multiple countries, new technology, ambiguities and uncertainties, keep stakeholders engaged. When a project involves distributed stakeholders, novel technology, and significant uncertainty, a shared collaboration platform provides a persistent space where all parties can access the same information, contribute to discussions, and track decisions in real time. This reduces the communication gaps that occur in geographically distributed environments and supports the continuous engagement that managing ambiguity requires. (PMBOK Guide) – Seventh Edition, 2021, p. 30, 'Effectively Engage with Stakeholders'\""
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
