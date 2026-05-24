MD_FILE = './src/imports/project-management-questions-1.md'

with open(MD_FILE, 'r', encoding='utf-8') as f:
    content = f.read()

replacements = [
    (
        'Explanation: Need: guide and calm the team. Options A and E (Establish daily standups to review project progress and track the completion of deliverables; Work with the team to identify options to accelerate project delivery.) work together."',
        'Explanation: Keywords: shared resources, schedule delay, daily standups, accelerate delivery. When team members are pulled to other projects and tasks fall behind, the PM needs both visibility and action simultaneously. Daily standups restore real-time transparency into progress, while collaborating with the team on acceleration options addresses the recovery plan without the PM dictating the solution. (PMBOK Guide) – Seventh Edition, 2021, p. 28, p. 29, \'Create a Collaborative Team Environment\'"'
    ),
    (
        'Explanation: Need: watch risks early. Option C (Have the vendor issue the quality documentation prior to the next delivery.) fixes it."',
        'Explanation: Keywords: vendor quality failure, site delivery, quality documentation, proactive assurance. After a quality failure in delivery, waiting until items arrive to inspect them is reactive and costly. Requiring the vendor to issue quality documentation before the next delivery shifts quality verification upstream — catching potential nonconformances before they reach the project site. (PMBOK Guide) – Seventh Edition, 2021, p. 42, \'Build Quality into Processes and Deliverables\'"'
    ),
    (
        'Explanation: Need: watch risks early. Option C (1600 rpm is a project issue; 1,500 rpm is a project risk; and1,400 rpm is an event that triggers a response strategy) fixes it."',
        'Explanation: Keywords: risk trigger, risk threshold, project risk, project issue. A risk threshold defines the point at which action is triggered — at 1,400 rpm the engine reduces power, making it the trigger for the pre-planned response. At 1,500 rpm the situation is uncertain but not yet failed, making it a risk. At 1,600 rpm the engine has already crashed, making it a confirmed issue requiring immediate resolution. (PMBOK Guide) – Seventh Edition, 2021, p. 46, \'Optimize Risk Responses\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option C (Evaluate the impacts of the changes that were made to the project) fixes it."',
        'Explanation: Keywords: unauthorized scope change, change control, impact evaluation, scope creep. Before any unauthorized change can be accepted, rejected, or reversed, the PM must first understand its actual impact. Evaluating the change\'s effect on schedule, budget, and quality provides the factual basis for the decision — removing the change without evaluation could cause equal or greater disruption. (PMBOK Guide) – Seventh Edition, 2021, p. 50, \'Enable Change to Achieve the Envisioned Future State\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option A (Share this opportunity with another project) fixes it."',
        'Explanation: Keywords: opportunity outside scope, escalation, opportunity sharing, project boundaries. Once an opportunity has been confirmed as outside the project\'s scope and escalated appropriately, the responsible action is to route it where it can be acted upon. Sharing it with another project ensures the organization captures potential value without compromising the current project\'s focus. (PMBOK Guide) – Seventh Edition, 2021, p. 46, \'Optimize Risk Responses\'"'
    ),
    (
        'Explanation: Need: protect benefits for users. Option C (Meet with management to explain the potential problems with running a project without a project scope statement) fixes it."',
        'Explanation: Keywords: missing scope statement, management pressure, critical project, scope baseline. The project scope statement defines what is and is not included in the project — without it, the team cannot make informed decisions about deliverables, constraints, or acceptance criteria. Educating management on these specific risks is the PM\'s professional obligation before proceeding without a foundational control document. (PMBOK Guide) – Seventh Edition, 2021, p. 25, \'Be a Diligent, Respectful, and Caring Steward\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option C (Assess the required training per team member.) fixes it."',
        'Explanation: Keywords: hybrid approach, knowledge gap, predictive-only team members, training assessment. Not all team members will need the same level of hybrid training — some may already have enough agile exposure while others need foundational instruction. Assessing training needs per individual before investing in development ensures the right training reaches the right people at the appropriate depth. (PMBOK Guide) – Seventh Edition, 2021, p. 28, p. 29, \'Create a Collaborative Team Environment\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option C (Evaluate and initiate the change request process with the stakeholders) fixes it."',
        'Explanation: Keywords: quality deviation, contingency depleted, corrective action, change request. When corrective actions require additional funds on a project already over budget, the PM cannot authorize that spending unilaterally. Evaluating the change and routing it through the change request process ensures stakeholders understand the quality risk, the cost impact, and the alternatives — giving decision-makers the information they need. (PMBOK Guide) – Seventh Edition, 2021, p. 42, \'Build Quality into Processes and Deliverables\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option D (Let the team self-organize and determine the best means to prevent the issues from occurring again) fixes it."',
        'Explanation: Keywords: recurring issues, team agreements, self-organization, iteration retrospective. When the same issues reappear after agreements have been set, the agreements themselves are not working — something in how the team approaches the problem needs to change. Letting the team self-organize to find their own solution builds the ownership and accountability that externally imposed rules cannot provide. (PMBOK Guide) – Seventh Edition, 2021, p. 28, p. 29, \'Create a Collaborative Team Environment\'"'
    ),
    (
        'Explanation: Need: learn from data and lessons. Option D (Take ownership of documenting this information) fixes it."',
        'Explanation: Keywords: lessons learned, SME observation, documentation ownership, project stewardship. Lessons learned are the PM\'s stewardship responsibility — not the SME\'s. Taking ownership of documenting the observation ensures it is captured accurately, in the right format, and in the designated register where it will be discoverable and useful to future projects. (PMBOK Guide) – Seventh Edition, 2021, p. 25, \'Be a Diligent, Respectful, and Caring Steward\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option C (Option C) fixes it."',
        'Explanation: Keywords: business value, development effort, feature prioritization, value-to-effort ratio. In agile and hybrid environments, the highest-priority items are those that deliver the greatest value for the least effort. The feature with the best business value-to-effort ratio should be worked on first, ensuring that limited team capacity generates the maximum benefit. (PMBOK Guide) – Seventh Edition, 2021, p. 32, \'Focus on Value\'"'
    ),
    (
        'Explanation: Need: keep plans flexible. Option D (Monitoring and updating the benefits realization plan) fixes it."',
        'Explanation: Keywords: business value alignment, benefits realization plan, deviation prevention, ongoing monitoring. The benefits realization plan defines the expected value the project should deliver and how it will be measured. Monitoring and updating it throughout the project ensures that the work being done and the product being built remain traceable to the benefits that justified the project in the first place. (PMBOK Guide) – Seventh Edition, 2021, p. 32, \'Focus on Value\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Options C and D (Reiterate ground rules at the next meeting and ensure that all team members are clear about these rules.; Address the behavioral issue with each team member) work together."',
        'Explanation: Keywords: team conflict, sponsor bypass, ground rules, individual behavioral issue. Bypassing the PM to influence the sponsor is both a behavioral issue and a governance failure. Reiterating ground rules at the next meeting addresses the systemic norm — no unilateral sponsor escalation — while addressing each team member individually handles the specific conflict behavior before it undermines team trust further. (PMBOK Guide) – Seventh Edition, 2021, p. 28, p. 29, \'Create a Collaborative Team Environment\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option B (Invite the executive to the project\'s meeting space to determine if the project information radiators meet their needs) fixes it."',
        'Explanation: Keywords: agile project, executive update, information radiators, transparent reporting. In agile environments, project information is made visible through radiators — boards, burn-down charts, and backlogs — that are continuously updated and available. Inviting the executive to the project space allows them to access real-time information in its native format rather than receiving a translated summary that may obscure context. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Options C and E (Cost of delaying some features against business value; Length of time each feature has been on the backlog) work together."',
        'Explanation: Keywords: backlog reprioritization, missed deliverables, cost of delay, backlog age. When reprioritizing after missed deliverables, two factors dominate: the cost of further delaying a feature relative to its business value tells the team what is most urgent now, while how long a feature has been on the backlog prevents high-value items from being perpetually deferred in favor of newer arrivals. (PMBOK Guide) – Seventh Edition, 2021, p. 32, \'Focus on Value\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Options A and D (Issue log; Change log) work together."',
        'Explanation: Keywords: invoice errors, post-implementation issue, issue log, change log. Three invoices with errors represent an active problem requiring tracking and corrective action — both the issue itself and any resulting changes to the system must be documented. The issue log captures the problem and its resolution progress, while the change log records any system modifications made in response. (PMBOK Guide) – Seventh Edition, 2021, p. 46, \'Optimize Risk Responses\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option D (Collaborate with the compliance team member to review and prioritize the requirement\'s delivery) fixes it."',
        'Explanation: Keywords: hybrid project, compliance requirement, urgent priority, collaborative prioritization. A compliance requirement that must be delivered ahead of all others cannot be simply added to the backlog and left to be deprioritized — it has a mandated delivery position. Collaborating with the compliance team member ensures the requirement is properly understood before the team determines how and when it can be delivered. (PMBOK Guide) – Seventh Edition, 2021, p. 32, \'Focus on Value\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option D (The cross-functional team member work together to complete the activity) fixes it."',
        'Explanation: Keywords: complex iteration activity, time pressure, cross-functional collaboration, collective capability. When an activity becomes more complex than expected and speed is essential, the team\'s diverse skills are the most immediately available resource. Cross-functional members working together bring different perspectives and capabilities to bear without the delay and cost of bringing in external help. (PMBOK Guide) – Seventh Edition, 2021, p. 28, p. 29, \'Create a Collaborative Team Environment\'"'
    ),
    (
        'Explanation: Need: keep plans flexible. Option B (Evaluate the environmental and regulatory factors and identify high-level risks and assumptions) fixes it."',
        'Explanation: Keywords: new country expansion, no prior presence, environmental factors, regulatory risk. Entering a country where the organization has no established presence means operating with no institutional knowledge of local regulations, cultural norms, or business environment. Evaluating these factors first — before any tactical decisions — establishes the foundation of assumptions and risk awareness that all subsequent planning depends on. (PMBOK Guide) – Seventh Edition, 2021, p. 44, \'Navigate Complexity\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option C (Actively listen to the team member and identify ways to support their needs in completing the tasks.) fixes it."',
        'Explanation: Keywords: experienced team member, task complexity, overwhelm, active listening. An experienced team member who is overwhelmed and unhappy is signaling a genuine need that requires the PM\'s attention. Actively listening creates the psychological safety for the team member to articulate what specific support they need — which the PM cannot determine without first understanding the person\'s perspective. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option C (Give the team autonomy to make their own decisions on how to perform the tasks.) fixes it."',
        'Explanation: Keywords: agile team, functional manager task assignment, team empowerment, autonomy. Empowerment in agile means the team owns how they accomplish their work, not just that they are informed of it. When a functional manager has assigned tasks prescriptively, restoring autonomy — allowing the team to decide how they perform those tasks — returns the self-management that defines a high-functioning agile team. (PMBOK Guide) – Seventh Edition, 2021, p. 28, p. 29, \'Create a Collaborative Team Environment\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option B (Schedule a meeting with the concerned team member to review and update the issue log together) fixes it."',
        'Explanation: Keywords: critical problem, task blocked, issue log, collaborative issue resolution. When a team member raises a critical problem in a group setting, the PM should not attempt to resolve it on the spot in front of the full team — a focused meeting allows proper diagnosis. Reviewing and updating the issue log together ensures the problem is formally captured, ownership is assigned, and the resolution path is documented. (PMBOK Guide) – Seventh Edition, 2021, p. 46, \'Optimize Risk Responses\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option C (Convene a team building event to address key performance indicators (KPIs).) fixes it."',
        'Explanation: Keywords: team member replacement, velocity drop, team integration, team building. When team members change mid-project, the team effectively re-forms — established dynamics, trust, and shared context must be rebuilt. A team building event accelerates this re-integration by rebuilding the interpersonal connections and shared understanding that underpin velocity, rather than waiting for it to recover naturally. (PMBOK Guide) – Seventh Edition, 2021, p. 28, p. 29, \'Create a Collaborative Team Environment\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option C (Review the project\'s benefits management plan with the product owner.) fixes it."',
        'Explanation: Keywords: sprint review, no business value delivered, benefits management plan, product owner alignment. A product that meets all specifications but delivers no value indicates a disconnect between what was built and what the project was meant to achieve. Reviewing the benefits management plan with the product owner reconnects both parties to the outcomes the project was chartered to produce, clarifying whether the backlog is actually driving toward those benefits. (PMBOK Guide) – Seventh Edition, 2021, p. 32, \'Focus on Value\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option A (Determine the tools and techniques suitable for the project and ensure that testing is done early and continuously.) fixes it."',
        'Explanation: Keywords: agile quality standards, early testing, continuous testing, quality tools selection. In agile environments, quality is built in from the start rather than inspected at the end. Choosing tools and techniques that fit the project\'s specific context — and then applying them continuously throughout development — prevents defect accumulation and ensures the team catches issues when they are least expensive to fix. (PMBOK Guide) – Seventh Edition, 2021, p. 42, \'Build Quality into Processes and Deliverables\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option B (Develop protocols for resolving conflicts between team members) fixes it."',
        'Explanation: Keywords: geographically distributed team, collocated versus virtual, productivity loss, conflict protocols. Productivity losses between collocated and virtual team members often stem from ambiguity about how to resolve disagreements across locations and communication modes. Formal protocols give both groups a shared, agreed-upon process for working through conflicts — replacing improvised responses with a predictable framework both sides can rely on. (PMBOK Guide) – Seventh Edition, 2021, p. 28, p. 29, \'Create a Collaborative Team Environment\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option A (Review constraints in the ongoing sprint planning and evaluate options for the release plan) fixes it."',
        'Explanation: Keywords: Scrum team, operational issues, tech lead resignation, sprint replanning. Multiple simultaneous disruptions — recurring operational blocks and the loss of the technical lead — change what the sprint can realistically deliver. Reviewing constraints in sprint planning with the team establishes what is still achievable, and evaluating release plan options creates a realistic path to honoring the commitment with what is now available. (PMBOK Guide) – Seventh Edition, 2021, p. 48, \'Embrace Adaptability and Resiliency\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option C (Organize a face-to-face meeting with all stakeholders to understand their interests and concerns.) fixes it."',
        'Explanation: Keywords: large stakeholder group, contradictory requirements, face-to-face consensus, stakeholder interests. When 70 stakeholders express contradictory expectations, the conflict cannot be resolved by the PM alone — the stakeholders themselves must surface and negotiate their competing interests. A face-to-face meeting creates the environment where concerns can be heard, trade-offs can be explored, and consensus can emerge from direct dialogue rather than mediated summaries. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option B (Consult with team members and stakeholders to determine whether the organization has any informal governance policies procedures, and guidelines) fixes it."',
        'Explanation: Keywords: no PMO, no formal governance, informal governance discovery, organizational context. Before designing governance from scratch, the PM must determine what already exists informally. Organizations often have undocumented norms, shared expectations, and informal processes that have guided past projects — discovering these through consultation prevents the PM from imposing a framework that conflicts with how the organization actually operates. (PMBOK Guide) – Seventh Edition, 2021, p. 34, \'Recognize, Evaluate, and Respond to System Interactions\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option B (Build team connections and emotional bonds) fixes it."',
        'Explanation: Keywords: key stakeholder departure, low morale, poor teamwork, emotional connection. When a highly motivating stakeholder leaves, the team loses an external source of energy and purpose. Building connections and emotional bonds within the team itself creates an internal support structure that sustains motivation — shifting the team\'s source of cohesion from an individual to their shared identity as a team. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option B (Mentor the marketing director on hybrid approaches) fixes it."',
        'Explanation: Keywords: hybrid methodology, key stakeholder education, marketing director, mentoring. A stakeholder who lacks understanding of the methodology cannot meaningfully support it. Mentoring the marketing director directly builds the knowledge they need to make informed decisions and provide the backing the project requires — more effective than asking the team to do it or leaving the director uninformed. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    (
        'Explanation: Need: keep plans flexible. Option B (Implement plans to remove the obstacles) fixes it."',
        'Explanation: Keywords: project obstacles, impediment removal, servant leadership, delivery continuity. Obstacles that prevent the team from moving forward are the PM\'s primary target for action — not something to escalate, wait on, or work around. Implementing plans to remove them is the PM\'s core responsibility in servant leadership, keeping the team unblocked and delivery momentum intact. (PMBOK Guide) – Seventh Edition, 2021, p. 28, p. 29, \'Create a Collaborative Team Environment\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Options A and D (Conduct a stakeholder analysis.; Adopt an incremental approach) work together."',
        'Explanation: Keywords: excessive scope changes, multiple stakeholders, stakeholder analysis, incremental approach. Uncontrolled changes from multiple stakeholders signal that expectations were never properly aligned. A stakeholder analysis surfaces who is driving changes and why, while an incremental approach breaks the scope into visible, approvable chunks — together reducing the volume and impact of mid-project changes. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option B (Provide appropriate training to compensate for the mismatch.) fixes it."',
        'Explanation: Keywords: Scrum team, missed deadlines, competency mismatch, targeted training. When the root cause of missed deadlines is a mismatch between team skills and task requirements, the solution is to close the skills gap rather than accept the performance shortfall. Targeted training directly addresses the deficiency, enabling the team to deliver what is expected without adding headcount or reducing scope. (PMBOK Guide) – Seventh Edition, 2021, p. 28, p. 29, \'Create a Collaborative Team Environment\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option C (Paired work and the customer role method.) fixes it."',
        'Explanation: Keywords: complex research, high uncertainty, quality measurement, paired work. In a high-uncertainty research project, traditional quality metrics may not capture whether the deliverable actually serves its purpose. Paired work embeds quality review into the development process itself, while the customer role method ensures the person best positioned to judge fitness for purpose — the customer — is involved in evaluating the deliverable. (PMBOK Guide) – Seventh Edition, 2021, p. 42, \'Build Quality into Processes and Deliverables\'"'
    ),
    (
        'Explanation: Need: protect benefits for users. Option A (A release burndown chart) fixes it."',
        'Explanation: Keywords: agile project, time remaining estimate, release burndown chart, steering committee. A release burndown chart tracks how much remaining work exists relative to the release target, making the team\'s progress and expected completion date visible at a glance. It is the agile artifact specifically designed to answer the question of how much time is left before the release goal is reached. (PMBOK Guide) – Seventh Edition, 2021, p. 32, \'Focus on Value\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option C (Determine cross-dependencies and plan a spike in the next sprint) fixes it."',
        'Explanation: Keywords: prototyping approach, user story delays, cross-dependencies, spike planning. When user stories consistently take longer than expected, the likely cause is undiscovered dependencies or technical uncertainty. A spike — a time-boxed research effort — in the next sprint creates a safe space to investigate those dependencies and reduce the uncertainty that is slowing delivery. (PMBOK Guide) – Seventh Edition, 2021, p. 48, \'Embrace Adaptability and Resiliency\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option D (Set up a meeting with the sponsor to explain the importance of keeping a strict sprint cycle) fixes it."',
        'Explanation: Keywords: sprint disruption, daily scope changes, sponsor education, sprint commitment. A sprint commitment is a time-boxed agreement that the team needs to honor to deliver predictably. When the sponsor changes priorities daily, they are breaking the sprint\'s protective boundary. Educating the sponsor on why sprint stability matters — and what daily disruptions cost in delivered value — is the PM\'s responsibility to prevent further erosion of team capacity. (PMBOK Guide) – Seventh Edition, 2021, p. 40, \'Tailor Based on Context\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option B (Work with the product owner to define the minimum viable product(s)) fixes it."',
        'Explanation: Keywords: unclear customer requirements, past difficulty, minimum viable product, product owner collaboration. A customer who struggles to articulate requirements benefits from the discipline of MVP definition — it forces the conversation from abstract wants to concrete, deliverable increments. Working with the product owner to define the MVP establishes a bounded scope the customer can react to, replacing vague specifications with tangible feedback opportunities. (PMBOK Guide) – Seventh Edition, 2021, p. 32, \'Focus on Value\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option B (Review the velocity of the team over the last several sprints and adjust the plan accordingly) fixes it."',
        'Explanation: Keywords: sprint failures, unsustainable pace, velocity review, plan adjustment. Repeated sprint failures signal that the team\'s committed capacity exceeds what they can actually deliver. Reviewing historical velocity replaces optimistic estimation with evidence-based planning, and adjusting the plan to align with actual throughput creates a sustainable pace that the team can maintain without degrading quality. (PMBOK Guide) – Seventh Edition, 2021, p. 48, \'Embrace Adaptability and Resiliency\'"'
    ),
    (
        'Explanation: Need: keep plans flexible. Option D (Consult with a subject matter expert (SME) to see if the proposed change is acceptable) fixes it."',
        'Explanation: Keywords: vendor component substitution, specification compliance, SME assessment, change acceptability. A vendor-proposed part substitution changes what will actually be built — which may or may not be technically equivalent to what the specifications require. A subject matter expert is the right person to evaluate whether the substitute component meets the project\'s technical and performance requirements before any decision is made. (PMBOK Guide) – Seventh Edition, 2021, p. 44, \'Navigate Complexity\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option D (Ask the functional manager to create a specific responsible, accountable, consult, and inform (RACI) chart for the team member) fixes it."',
        'Explanation: Keywords: role confusion, team member, functional manager, RACI chart. When a team member is unclear about their responsibilities, a RACI chart provides explicit documentation of exactly what they are responsible for, accountable for, should be consulted on, and should be informed about. Involving the functional manager in creating it ensures the chart reflects both the project\'s needs and the organizational authority structure. (PMBOK Guide) – Seventh Edition, 2021, p. 28, p. 29, \'Create a Collaborative Team Environment\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option A (Share the project documents and invite the key stakeholder to discuss any concerns) fixes it."',
        'Explanation: Keywords: undefined strategy concern, stakeholder resistance, document sharing, informal engagement. A stakeholder who declines a formal working session but raises strategic concerns still needs to be engaged — the objection is to the format, not the topic. Sharing the project documents provides the factual context they need while inviting them to discuss concerns on their own terms removes the barrier that a structured session created. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option D (The team with the least amount of defects in their deliverables) fixes it."',
        'Explanation: Keywords: story points comparison, agile performance, cross-team measurement, quality indicator. Story points are internal calibration tools — each team\'s scale is relative to itself, making cross-team point comparisons meaningless. The most reliable indicator of which team is truly performing better is the quality of what they deliver: fewer defects represent a more productive and sustainable team output regardless of the points assigned. (PMBOK Guide) – Seventh Edition, 2021, p. 42, \'Build Quality into Processes and Deliverables\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option D (Provide mentoring to the newly appointed team leader) fixes it."',
        'Explanation: Keywords: new team leader, management inexperience, mentoring, performance risk. A newly appointed team leader who lacks management experience needs development, not replacement. Mentoring provides real-time guidance on the specific leadership challenges they are facing — building their capability in context rather than removing them from a role where they can grow. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option B (Defined product backlog priorities with the sponsor and key stakeholders to deliver business benefits) fixes it."',
        'Explanation: Keywords: technical success, business value failure, backlog priorities, stakeholder-defined benefits. Delivering on time and within budget while failing to deliver business value is the most costly kind of project failure — resources were spent producing the wrong outcomes. Involving the sponsor and business stakeholders in defining backlog priorities from the start ensures that what gets built is what the business actually values, not just what the team was asked to build. (PMBOK Guide) – Seventh Edition, 2021, p. 32, \'Focus on Value\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option C (Update the stakeholder engagement plan) fixes it."',
        'Explanation: Keywords: new stakeholder, strategic initiative, stakeholder engagement plan, awareness building. A new stakeholder with interest in a strategic project represents an engagement relationship that does not yet exist in the plan. Updating the stakeholder engagement plan formalizes how, when, and through what channels this stakeholder will be kept informed — ensuring their engagement is managed systematically rather than reactively. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
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
