MD_FILE = './src/imports/project-management-questions-1.md'

with open(MD_FILE, 'r', encoding='utf-8') as f:
    content = f.read()

replacements = [
    (
        'Explanation: Need: keep plans flexible. Option B (Create a definition of ready (DoR) for the backlog items.) fixes it."',
        'Explanation: Keywords: agile work overruns, unrefined backlog items, definition of ready, quality entry criteria. Work overruns caused by insufficiently refined backlog items indicate that the team is beginning work before items are clear and estimable enough for implementation. Creating a Definition of Ready (DoR) establishes explicit entry criteria for backlog items entering a sprint, ensuring the team only commits to work that is adequately understood and scoped. (PMBOK Guide) – Seventh Edition, 2021, p. 42, \'Build Quality into Processes and Deliverables\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option D (Product owner) fixes it."',
        'Explanation: Keywords: product owner, vague business ideas, backlog development, feature prioritization. In agile projects, the product owner is solely responsible for defining, developing, and prioritizing the list of features and functionalities based on business value and stakeholder needs. The product owner bridges the gap between vague business concepts and actionable backlog items, ensuring the team works on the highest-value features in the right sequence. (PMBOK Guide) – Seventh Edition, 2021, p. 32, \'Focus on Value\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option A (Assess the impact of the features and refer it to the change control board (CCB).) fixes it."',
        'Explanation: Keywords: late scope addition, near-complete project, change control board, sponsor pressure. Even when a sponsor insists on new features at near-project-completion, the project manager must assess the full impact of those changes and route them through the change control board for formal evaluation and approval. The CCB exists precisely to prevent scope creep driven by sponsorial pressure, ensuring additions are evaluated against schedule, cost, and quality baselines before any commitment is made. (PMBOK Guide) – Seventh Edition, 2021, p. 34, \'Recognize, Evaluate, and Respond to System Interactions\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option A (Notify all team members that all steps in the process must be completed.) fixes it."',
        'Explanation: Keywords: COO process shortcut, process compliance, team notification, stewardship obligation. When a senior leader directs the team to skip required process steps, the project manager has a professional obligation to ensure those steps are completed and to notify all team members accordingly. Reinforcing process integrity — rather than accommodating executive shortcuts — reflects the project manager\'s stewardship role in upholding governance standards that protect quality outcomes. (PMBOK Guide) – Seventh Edition, 2021, p. 25, \'Be a Diligent, Respectful, and Caring Steward\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option B (Ensure that a kick-off meeting is planned and invite relevant stakeholders toparticipate.) fixes it."',
        'Explanation: Keywords: baseline schedule, team assignments, kick-off meeting, stakeholder engagement. When assigning team members to project activities during baseline schedule development, the project manager should ensure a kick-off meeting is planned and all relevant stakeholders are invited. A well-run kick-off aligns the team and stakeholders on project objectives, roles, and expectations before execution begins — a critical step for engaging stakeholders early and building project momentum. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option B (Organize a formal session led by a skilled facilitator with defined rules for howparticipants will interact with one another.) fixes it."',
        'Explanation: Keywords: joint requirements session, technology and operations teams, skilled facilitator, interaction ground rules. A potentially chaotic joint requirements session benefits most from a formal structure led by a skilled facilitator who sets clear rules for how participants interact. Defined facilitation rules prevent domination by vocal participants, ensure all voices are heard, and keep the session productive — yielding more collaborative and comprehensive requirements in less time. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option C (Review user roles and update the team charter.) fixes it."',
        'Explanation: Keywords: concentrated workload, few team members carrying all work, user roles, team charter. When only a few team members are carrying all the work across releases, the root cause is likely an uneven distribution of roles and responsibilities. Reviewing user roles and updating the team charter redistributes work equitably and ensures all team members understand their contributions and accountabilities, preventing the bottleneck from recurring. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option D (Explore a training program that is within the project budget for the team members.) fixes it."',
        'Explanation: Keywords: servant leader, skill gap, team capability building, training investment. A servant leader prioritizes the growth and enablement of their team members over quick fixes like replacing personnel. Exploring a training program within the project budget directly addresses the skill gap while demonstrating investment in team members\' professional development — consistent with the servant leadership model of removing obstacles and building lasting team capability. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option D (Have the team member transferred to another project and add other resources to theproject.) fixes it."',
        'Explanation: Keywords: persistent low morale, team member disengagement, project performance, resource replacement. When a team member\'s persistent disengagement and low morale continue to negatively impact project performance despite the initial excitement, reallocating the individual to a more suitable project and adding fresh resources protects the overall team\'s productivity and delivery commitments. This action reflects the project manager\'s responsibility to maintain a high-performing team environment in service of project success. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option C (Determine whether other cross-functional team members are able to take over thework.) fixes it."',
        'Explanation: Keywords: developer departure mid-iteration, cross-functional team, task continuity, shared ownership. In an agile cross-functional team, members are expected to be capable of contributing beyond their primary specialization. When a developer unexpectedly leaves mid-iteration, the project manager should first assess whether other cross-functional team members can absorb the remaining work — leveraging the team\'s shared capabilities before escalating to management or rescheduling the deliverable. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option C (Motivate the team members to speak freely in the meeting.) fixes it."',
        'Explanation: Keywords: quiet team member, email contributions, meeting participation, open communication. A team member who contributes excellent ideas via email but stays silent in meetings is not fully participating in the collaborative process that effective teams depend on. The project manager should motivate the team member to speak freely in meetings, removing barriers to real-time contribution and ensuring the team benefits from all perspectives during discussions. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option C (Identified the appropriate response and had it implemented) fixes it."',
        'Explanation: Keywords: risk mitigation delay, schedule impact, risk response execution, proactive management. The project manager\'s core responsibility when managing risks is not merely to identify or communicate them, but to identify the appropriate response strategy and drive its timely implementation. Failing to execute mitigation actions despite having identified risks is a failure of the Optimize Risk Responses principle — meaning the project manager must actively pursue and implement selected responses, not merely document or escalate them. (PMBOK Guide) – Seventh Edition, 2021, p. 46, \'Optimize Risk Responses\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option B (Organizational process assets (OPAs)) fixes it."',
        'Explanation: Keywords: meeting notes, stakeholder insights, organizational knowledge, organizational process assets. Meeting notes that capture key stakeholder insights and contribute to project value represent organizational knowledge that should be preserved for future projects. Organizational Process Assets (OPAs) are the appropriate repository for lessons, templates, and records that can benefit future project managers across the organization — not project management plans, which are project-specific and close with the project. (PMBOK Guide) – Seventh Edition, 2021, p. 25, \'Be a Diligent, Respectful, and Caring Steward\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option D (Hybrid) fixes it."',
        'Explanation: Keywords: complex equipment, long research phase, incremental delivery, hybrid methodology. A project combining a lengthy research phase — which requires sequential, predictive execution — with incremental delivery to the customer — which requires iterative, adaptive execution — is a textbook case for a hybrid methodology. The hybrid approach allows each portion of the project to use the most appropriate delivery framework based on the nature and certainty of that work stream. (PMBOK Guide) – Seventh Edition, 2021, p. 40, \'Tailor Based on Context\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option A (Conduct a consensus-building session to decide how to approach the next set of work.) fixes it."',
        'Explanation: Keywords: technical environment constraint, schedule crashing, team disagreement, consensus building. When a team cannot agree on how to overcome a technical constraint blocking schedule acceleration, the project manager should facilitate a consensus-building session to align the team on a shared path forward. Consensus ensures team buy-in, leverages collective problem-solving, and avoids the dysfunction of proceeding with unresolved disagreements about approach. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    (
        'Explanation: Need: keep plans flexible. Option C (Facilitate sprint planning sessions with a focus on defining the minimum viable product(MVP).) fixes it."',
        'Explanation: Keywords: incremental feature release, product owner preference, minimum viable product, sprint planning. When a product owner explicitly values incremental feature delivery over a single large release, sprint planning sessions focused on defining and delivering the Minimum Viable Product (MVP) ensure each iteration produces a usable, valuable increment. The MVP focus aligns team sprint commitments with the product owner\'s release strategy, enabling early and continuous delivery of value. (PMBOK Guide) – Seventh Edition, 2021, p. 32, \'Focus on Value\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option A (Recognize the stakeholder\'s skills are important for the project and evaluate thepossibility of the stakeholder supporting the project team.) fixes it."',
        'Explanation: Keywords: lessons learned, tax expert stakeholder, stakeholder skills, project support. Lessons learned from previous projects are valuable inputs for identifying opportunities to enhance current project performance. Recognizing the tax expert stakeholder\'s skills and evaluating their potential support role demonstrates proactive stakeholder engagement — leveraging organizational knowledge to reduce project risk and improve the quality of outcomes. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option D (Assign team member roles and responsibilities based on past experience.) fixes it."',
        'Explanation: Keywords: mixed-experience team, system replacement, role assignment, past experience alignment. When a team includes both legacy system experts and less experienced members, assigning roles and responsibilities based on each member\'s past experience positions the right people for the tasks that best match their expertise. This deliberate role alignment maximizes team effectiveness and reduces execution risk on a technically complex system replacement project. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option D (Discuss the issue with the team members at fault.) fixes it."',
        'Explanation: Keywords: status reports not submitted, team accountability, communication compliance, direct discussion. When team members fail to complete required status reports, the project manager should discuss the issue directly with the team members at fault to understand why reports were not submitted and reinforce expectations. Reprimanding publicly or justifying the behavior are both ineffective — a direct conversation builds accountability and may reveal systemic barriers the project manager can address. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option B (Follow the proper change control process and evaluate the change for further impact.) fixes it."',
        'Explanation: Keywords: unauthorized feature addition, gold plating, change control process, scope management. When an additional feature is added to a deliverable outside the approved scope, it represents an unauthorized change that must be evaluated through the formal change control process — even if the feature appears beneficial. Following the change control process protects the project baseline, ensures the customer\'s risk concerns are properly assessed, and prevents scope creep from recurring. (PMBOK Guide) – Seventh Edition, 2021, p. 42, \'Build Quality into Processes and Deliverables\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option C (Assess the situation to understand how the organization\'s culture impacts the decisionmaking process, and coach the team toward a new model.) fixes it."',
        'Explanation: Keywords: agile adoption, decision-making challenge, organizational culture, coaching toward change. When a team transitioning to agile struggles to make timely decisions, the root cause often lies in an organizational culture that historically has centralized decision-making at the top rather than empowering teams. Assessing the cultural impact on the decision-making process and coaching the team toward a new model addresses the systemic barrier rather than treating symptoms with imposed rules or authority. (PMBOK Guide) – Seventh Edition, 2021, p. 40, \'Tailor Based on Context\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option D (Explain the benefits of the approach and the effects of positive psychology.) fixes it."',
        'Explanation: Keywords: strengths-based workshop, team non-participation, positive psychology, engagement. When team members are passively resisting a strengths identification workshop, the project manager should explain the benefits of the approach and the science of positive psychology that underpins it. Understanding why the approach works and how it benefits them personally transforms passive resistance into meaningful participation, creating the engagement needed for the workshop to succeed. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option B (Implement communication techniques and ensure the teams follow a relay pattern ofhanding off work from one team to the other.) fixes it."',
        'Explanation: Keywords: geographically dispersed agile teams, sprint relay handoff, cross-team communication, sprint continuity. In a multi-city agile setup where each team handles a distinct phase, a structured relay handoff pattern with clear communication ensures work flows seamlessly from data capture to development to testing. This approach maintains sprint continuity across time zones and prevents integration gaps that would arise if teams operated without explicit handoff coordination. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option D (Earned value analysis (EVA)) fixes it."',
        'Explanation: Keywords: agile-skeptical stakeholder, performance reporting, earned value analysis, traditional metrics. For a stakeholder who is familiar with traditional project reporting and uncomfortable with agile approaches, presenting earned value analysis provides performance data in a language and format they already understand and trust. EVA translates agile project progress into schedule variance, cost performance, and earned value metrics — bridging the gap between agile delivery and predictive reporting expectations. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option C (Request that the receiving manager issue a change request to prolong the project bytwo weeks.) fixes it."',
        'Explanation: Keywords: project handover, receiving organization not ready, change request responsibility, formal closure. When the receiving organization is not ready for the planned handover, the responsible party to initiate a change request for extending the project timeline is the receiving manager — not the project manager. The project manager has fulfilled their obligations; any extension required to accommodate the receiving side\'s readiness is the receiving organization\'s responsibility to formally request and justify. (PMBOK Guide) – Seventh Edition, 2021, p. 25, \'Be a Diligent, Respectful, and Caring Steward\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option A (Ask the legal team to review the RFP.) fixes it."',
        'Explanation: Keywords: procurement disputes, hardware RFP, legal review, risk mitigation. When a project manager knows from prior experience that a particular type of procurement frequently leads to supplier disputes, having the legal team review the RFP before release is the most effective way to mitigate that risk. Legal review ensures contract terms are clear, enforceable, and protective of the company\'s interests — directly addressing the root cause of historical procurement conflicts. (PMBOK Guide) – Seventh Edition, 2021, p. 46, \'Optimize Risk Responses\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option A (Change management plan) fixes it."',
        'Explanation: Keywords: sponsor scope change, last-minute floor plan addition, change management plan, integrated change control. When a sponsor requests a scope change during project execution, the project manager\'s first reference should be the change management plan, which defines the process for submitting, evaluating, and approving changes. The change management plan governs how all changes are handled — consulting it first ensures the sponsor\'s request is processed correctly without creating unintended schedule or cost impacts. (PMBOK Guide) – Seventh Edition, 2021, p. 34, \'Recognize, Evaluate, and Respond to System Interactions\'"'
    ),
    (
        'Explanation: Need: protect benefits for users. Option C (Understand the project success criteria and objectives.) fixes it."',
        'Explanation: Keywords: newly assigned project manager, project purpose, success criteria, project objectives. When a project manager joins an in-progress project and needs to understand why the project is being executed, the first step is to understand the project\'s success criteria and objectives — which define what the project must achieve to be considered successful. These criteria provide the lens through which all project decisions and trade-offs should be evaluated going forward. (PMBOK Guide) – Seventh Edition, 2021, p. 32, \'Focus on Value\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option D (Schedule a session with the team to discuss the issues and work with them to define aplan to manage the sprints going forward.) fixes it."',
        'Explanation: Keywords: hybrid team, sprint disruptions, support items, team stress. When a team\'s sprint work is repeatedly disrupted by unplanned support activities causing stress and emotional outbursts, the project manager should schedule a collaborative session with the team to discuss the challenges and co-develop a plan for managing both sprint work and support obligations. A jointly developed plan builds team ownership and ensures the solution is both practical and sustainable. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option B (Discuss the issue with the functional manager to understand the reason for thecomplaint.) fixes it."',
        'Explanation: Keywords: functional manager complaint, team member performance, understanding the concern, dialogue. When a functional manager lodges a serious complaint about a project team member, the project manager\'s first response should be a constructive discussion with the functional manager to fully understand the nature and basis of the complaint. Acting on incomplete information — whether by defending the team member or taking disciplinary action — risks making a poor decision that damages both relationships. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option A (Explain the impact of the scenario to the project team member.) fixes it."',
        'Explanation: Keywords: team member arguing with client, meeting disruption, impact feedback, behavior correction. When a team member\'s behavior toward a client is negatively affecting meetings, the project manager should privately explain the specific impact of that behavior on the client relationship and project outcomes. Direct, constructive feedback addresses the issue at its source and gives the team member the opportunity to adjust their approach — more effective than exclusion or formal performance plans as a first response. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option D (Reconsider necessary schedule reserves.) fixes it."',
        'Explanation: Keywords: base station rollout, behind target, ROI impact, schedule reserves adjustment. When a hybrid project is falling behind its monthly installation targets, the project manager should reconsider the schedule reserves to identify where buffer time can be reallocated to recover the plan. Adjusting schedule reserves rather than changing the project approach or simply increasing reporting directly addresses the scheduling gap without disrupting the broader project framework. (PMBOK Guide) – Seventh Edition, 2021, p. 40, \'Tailor Based on Context\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option C (Recommend to the project sponsor that a predictive approach is appropriate for theproject due to the stable product requirements.) fixes it."',
        'Explanation: Keywords: hybrid approach exploration, stable product specification, predictive approach recommendation, methodology selection. When a detailed product specification has already been prepared and requirements are stable, the most appropriate approach is predictive — not hybrid. Despite a sponsor\'s initial interest in hybrid, the project manager should recommend the approach best suited to the project\'s actual characteristics, since stable and fully documented requirements are precisely the conditions that favor predictive planning. (PMBOK Guide) – Seventh Edition, 2021, p. 40, \'Tailor Based on Context\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option D (Contact the other project manager to request the resource.) fixes it."',
        'Explanation: Keywords: resource conflict, concurrent projects, contact other project manager, resource negotiation. When a resource originally committed to a project is currently assigned to another project, the most direct resolution is for the project manager to contact the other project manager to discuss and negotiate the resource\'s availability. This peer-level conversation respects both projects\' needs and is more likely to produce a workable arrangement than escalating to procurement or the project sponsor prematurely. (PMBOK Guide) – Seventh Edition, 2021, p. 34, \'Recognize, Evaluate, and Respond to System Interactions\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option B (Engage with the town\'s authorities to discuss the reason for the change in commitmentand agree on a solution.) fixes it."',
        'Explanation: Keywords: town blocking project work, stakeholder commitment reversal, direct engagement, negotiated solution. When a previously committed stakeholder changes their position and blocks project work, the project manager should engage directly with the relevant authorities to understand the reason for the change and collaboratively agree on a solution. This engagement-first approach honors the relationship established during pre-project stakeholder engagement and seeks resolution without forcing confrontation. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option A (Develop an approved responsibility assignment matrix (RAM) to confirm internal andexternal resource requirements.) fixes it."',
        'Explanation: Keywords: part-time site engineers, competing production imperatives, responsibility assignment matrix, resource clarity. When key team members may not be fully available due to competing operational commitments, the project manager should develop an approved Responsibility Assignment Matrix (RAM) that formally confirms each resource\'s roles, responsibilities, and level of commitment. A documented RAM provides clarity and creates a reference for managing resource constraints and accountability throughout project execution. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option C (Perform a root cause analysis) fixes it."',
        'Explanation: Keywords: functionality failure, product demo, root cause analysis, corrective action. When a functionality fails during a stakeholder demonstration, the immediate priority is to perform a root cause analysis to understand why the failure occurred before pursuing corrective action. Acting on an undiagnosed defect — whether through change requests or scope updates — risks applying the wrong fix and allowing the underlying issue to persist in other parts of the product. (PMBOK Guide) – Seventh Edition, 2021, p. 42, \'Build Quality into Processes and Deliverables\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option D (Backlog grooming, product backlog, minimum viable product (MVP)) fixes it."',
        'Explanation: Keywords: agile project initiation, release timeline estimation, backlog grooming, minimum viable product. To estimate initial release timelines at the start of an agile project, the project manager uses backlog grooming to refine and size requirements, the product backlog to understand full scope, and the MVP definition to identify the earliest releasable increment. These three tools together provide the basis for meaningful delivery estimates without requiring complete requirements upfront. (PMBOK Guide) – Seventh Edition, 2021, p. 32, \'Focus on Value\'"'
    ),
    (
        'Explanation: Need: keep plans flexible. Option B (B. Add penalty clauses to the contract and update the risk register.) fixes it."',
        'Explanation: Keywords: unreliable supplier, only qualified vendor, penalty clauses, risk register. When the only available supplier has a known history of late deliveries, the project manager must proactively address this risk by including penalty clauses in the contract to incentivize performance and documenting the risk in the risk register with planned response strategies. This combination protects the project schedule while creating a contractual mechanism for accountability and formally acknowledging the identified threat. (PMBOK Guide) – Seventh Edition, 2021, p. 46, \'Optimize Risk Responses\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option D (Speak directly with the team member about improvements and commit to an agreed-upon time frame.) fixes it."',
        'Explanation: Keywords: team member consistently late on deliverables, training gap, direct feedback, improvement commitment. When a team member consistently misses deliverables and a training gap is suspected, the most effective action is a direct, private conversation to discuss specific improvement expectations and agree on a time frame. This targeted discussion enables the team member to acknowledge challenges, commit to a plan, and receive coaching — more effective than broad team reminders or task reassignment. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    (
        'Explanation: Need: secure people or vendors. Option D (Company\'s resource calendars) fixes it."',
        'Explanation: Keywords: new project resource determination, resource calendars, availability planning, initiation phase. When determining the resources required for a new project, the project manager should first consult the company\'s resource calendars to understand which resources are available, when, and for how long. Resource calendars provide the foundation for realistic resource planning by identifying existing commitments and constraints before roles and responsibilities are assigned. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    (
        'd. Predictive\n\nAnswer: C\n\nExplanation: Need: listen to people needs. Option C (Hybrid) fixes it."',
        'd. Predictive\n\nAnswer: C\n\nExplanation: Keywords: research phase, incremental delivery, hybrid approach, complex equipment. A project combining a sequential research phase with incremental delivery to the customer requires a hybrid methodology — using predictive execution for the research component and an iterative approach for the incremental delivery component. Tailoring the methodology to the nature of each distinct work stream is the defining characteristic of effective hybrid project management. (PMBOK Guide) – Seventh Edition, 2021, p. 40, \'Tailor Based on Context\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option C (Include the burndown chart in a monthly report that is distributed to all stakeholders.) fixes it."',
        'Explanation: Keywords: burndown chart, agile transition, monthly stakeholder report, broad communication. Including the burndown chart in a monthly report distributed to all stakeholders ensures consistent, broad communication of project progress during an organizational agile transition. A regularly distributed report makes sprint performance visible to stakeholders who may not attend agile ceremonies, maintaining alignment and trust across the organization as it adapts to the new methodology. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    (
        'd. iterative\n\nAnswer: C\n\nExplanation: Need: listen to people needs. Option C (Hybrid) fixes it."',
        'd. iterative\n\nAnswer: C\n\nExplanation: Keywords: unstable requirements, organizational change, correct final results, hybrid approach. The project faces unstable requirements due to anticipated CEO-driven organizational changes while also requiring absolutely correct final results with no need for intermediate outputs — conditions that point to a hybrid approach. Hybrid methodology allows the team to adapt requirements iteratively as the organization evolves while ensuring the final product meets the hard correctness criterion demanded by the customer. (PMBOK Guide) – Seventh Edition, 2021, p. 40, \'Tailor Based on Context\'"'
    ),
    (
        'Explanation: Need: keep plans flexible. Option B (Facilitate sprint planning sessions with a focus on defining the minimum viable product (MVP)) fixes it."',
        'Explanation: Keywords: incremental feature release, sprint planning, minimum viable product, product owner delivery priority. When a product owner explicitly values incremental feature delivery during development rather than a single large release at the end, sprint planning sessions focused on defining and delivering the MVP ensure each iteration produces a usable, valuable increment. The MVP focus aligns team sprint commitments with the product owner\'s delivery preference, enabling early and continuous value realization throughout the project. (PMBOK Guide) – Seventh Edition, 2021, p. 32, \'Focus on Value\'"'
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
