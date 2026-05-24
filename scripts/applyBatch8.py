MD_FILE = './src/imports/project-management-questions-1.md'

with open(MD_FILE, 'r', encoding='utf-8') as f:
    content = f.read()

replacements = [
    (
        'Explanation: Need: listen to people needs. Option D (Kept documentation in the project management information system (PMIS), and shared it with appropriate stakeholders) fixes it."',
        'Explanation: Keywords: documentation audit, PMIS, version control, stakeholder access. A PMIS serves as the single, authoritative location for all project documentation — ensuring that updates are stored in one place, versioned correctly, and accessible to the right stakeholders. Without this, documentation quickly becomes inconsistent across team members, creating exactly the kind of discrepancy an audit surfaces. (PMBOK Guide) – Seventh Edition, 2021, p. 25, \'Be a Diligent, Respectful, and Caring Steward\'"'
    ),
    (
        'Explanation: Need: watch risks early. Option D (Meet with subject matter experts (SMEs) to assess the impact to objectives) fixes it."',
        'Explanation: Keywords: new regulation, iterative project, future phase impact, SME assessment. A regulation that affects a future phase must be understood before it arrives — not when the team is already in that phase. Meeting with SMEs while the project is still in phase 2 provides the expert analysis needed to understand the full impact and decide whether the regulation requires a scope change, a schedule adjustment, or a modified delivery approach. (PMBOK Guide) – Seventh Edition, 2021, p. 46, \'Optimize Risk Responses\'"'
    ),
    (
        'Explanation: Need: keep plans flexible. Option D (Requirement 3. Requirement 1, Risk 3, Requirement 2, Risk 1, Risk 2) fixes it."',
        'Explanation: Keywords: agile backlog prioritization, ROI, risk-adjusted value, priority order. In an agile project, backlog items should be prioritized by their value-to-risk trade-off — high-ROI requirements with manageable risk come first, followed by items where risk mitigation enables subsequent delivery. This ordering maximizes business value delivered early while managing the risks that could derail later items. (PMBOK Guide) – Seventh Edition, 2021, p. 32, \'Focus on Value\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option D (Execute a contingency plan to address the issue with the vendor) fixes it."',
        'Explanation: Keywords: vendor miscommunication, missing deliverable, critical path extension, contingency plan. When a vendor-related miscommunication has already extended the critical path, the PM must activate the response that was planned for exactly this situation. Executing the contingency plan is faster and more effective than investigating, auditing, or analyzing — the project cannot afford additional delay while the team diagnoses a problem that already needs to be resolved. (PMBOK Guide) – Seventh Edition, 2021, p. 46, \'Optimize Risk Responses\'"'
    ),
    (
        "Explanation: Need: listen to people needs. Option C (Manage the project sponsor closely and revise the project's resource management plan to improve indicators) fixes it.\"",
        'Explanation: Keywords: schedule ahead, cost overrun, CPI, sponsor management. A CPI near zero signals a critical cost emergency — the project is getting almost no value for every dollar spent. Managing the project sponsor closely maintains their trust and keeps them from taking drastic action prematurely, while revising the resource management plan addresses the root cause of the cost overrun by optimizing how resources are allocated. (PMBOK Guide) – Seventh Edition, 2021, p. 32, \'Focus on Value\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Options A and C (Ask the team members to analyze the impact of including this regulation; Ask the product owner to include the requirements in the product backlog) work together."',
        'Explanation: Keywords: compliance feedback, mid-iteration, impact analysis, product backlog. Compliance requirements arriving mid-project need two parallel actions: understanding what incorporating them will cost the current plan (impact analysis) and formally capturing them where they can be planned and prioritized (product backlog). Skipping either step risks either disrupting the current iteration unnecessarily or losing the requirement before it is properly addressed. (PMBOK Guide) – Seventh Edition, 2021, p. 32, \'Focus on Value\'"'
    ),
    (
        'Explanation: Need: keep plans flexible. Option A (Perform a risk assessment and define a risk response action plan.) fixes it."',
        'Explanation: Keywords: global crisis, material delays, construction phase, risk response plan. A geopolitical crisis that is already disrupting deliveries represents an active and evolving threat. A risk assessment identifies which aspects of the project are most exposed and how the crisis might develop further, while defining a response action plan ensures the team is not reacting to each disruption individually but working from a coherent strategy. (PMBOK Guide) – Seventh Edition, 2021, p. 46, \'Optimize Risk Responses\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option C (Planned and scheduled tasks and work packages to overcome geographical and time zone challenges) fixes it."',
        'Explanation: Keywords: global team, time zone stalls, task planning, geographical challenges. Work stalling because one office must wait for another to wake up is a scheduling failure, not a communication failure. Planning and scheduling tasks and work packages to account for time zone differences — so that each team can work autonomously without being blocked by others — is the structural solution that prevents these daily delays. (PMBOK Guide) – Seventh Edition, 2021, p. 34, \'Recognize, Evaluate, and Respond to System Interactions\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option D (Conduct a root cause analysis session) fixes it."',
        'Explanation: Keywords: team dysfunction, negative behaviors, low motivation, root cause analysis. Negative group behaviors and loss of motivation are symptoms — they have a cause that must be identified before any meaningful improvement is possible. A root cause analysis session engages the team in diagnosing what is driving the dysfunction, generating both insight and shared ownership of the actions needed to turn performance around. (PMBOK Guide) – Seventh Edition, 2021, p. 44, \'Navigate Complexity\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option D (Risk register) fixes it."',
        'Explanation: Keywords: risk triggers, risk-to-issue threshold, risk register, stakeholder inquiry. The risk register contains the specific conditions, thresholds, and trigger events that indicate when a risk has become — or is about to become — an issue. It is the project artifact where the relationship between a risk and its potential escalation to issue status is formally documented and monitored. (PMBOK Guide) – Seventh Edition, 2021, p. 46, \'Optimize Risk Responses\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option A (Retrospect frequently and suggest improvements.) fixes it."',
        'Explanation: Keywords: persistent iteration delay, retrospective frequency, continuous improvement, agile adaptation. A delay that persists for several weeks without improvement signals that the team\'s current approach is not working and needs to change. Increasing retrospective frequency creates more opportunities to surface what is blocking progress and generate the targeted improvements needed to break the pattern before it consumes the remaining iterations. (PMBOK Guide) – Seventh Edition, 2021, p. 48, \'Embrace Adaptability and Resiliency\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option D (Discuss the options with the client as part of the change control process) fixes it."',
        'Explanation: Keywords: realized risk, client-requested workaround, change control, schedule and cost impact. When a client proposes a workaround that introduces delays and additional budget, it is a scope and constraint change — not simply a risk response. Discussing the options within the change control process ensures the client understands the full impact of their request and that any decision to proceed is formally approved rather than informally absorbed. (PMBOK Guide) – Seventh Edition, 2021, p. 50, \'Enable Change to Achieve the Envisioned Future State\'"'
    ),
    (
        'Explanation: Need: watch risks early. Option B (Collaborative discussions) fixes it."',
        'Explanation: Keywords: unfamiliar domain, agile project, risk identification, collaborative discussions. A PM unfamiliar with the project domain lacks the subject matter knowledge to identify risks independently. Collaborative discussions leverage the team\'s domain expertise, surfacing the risks that only those closest to the work would know — making collective intelligence the most powerful risk identification tool available in this situation. (PMBOK Guide) – Seventh Edition, 2021, p. 46, \'Optimize Risk Responses\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option D (Contact department managers who are identified as stakeholders, solicit concern, and provide updates to the situation) fixes it."',
        'Explanation: Keywords: vendor delivery failure, missing component, stakeholder communication, impact update. A missing critical component with known delay implications must be communicated promptly to the stakeholders most affected. Contacting the relevant department managers directly — soliciting their specific concerns and providing timely updates — ensures those with the most at stake are engaged in shaping the response rather than learning about the problem through indirect channels. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Options B and D (Functional managers; Advisory team panel) work together."',
        'Explanation: Keywords: regulated industry, compliance requirements, functional managers, advisory panel. Compliance requirements in a regulated industry require both operational knowledge and specialized expertise. Functional managers understand how compliance applies to day-to-day processes within the organization, while an advisory team panel provides the technical and regulatory depth needed to interpret and implement the requirements correctly. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option A (Update the communications management plan to include the missed stakeholder, and send the current project status documentation to this stakeholder) fixes it."',
        'Explanation: Keywords: missed stakeholder, communications management plan, status report gap, corrective action. A stakeholder who is registered but excluded from the communications plan represents a planning gap that must be corrected immediately. Updating the plan formalizes the inclusion going forward, while providing the current status documentation ensures the stakeholder is immediately brought up to date on what they have missed. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    (
        'Explanation: Need: secure people or vendors. Option B (Refuse the offer as it is included in the initial project scope) fixes it."',
        'Explanation: Keywords: contractor scope billing, initial scope, vendor negotiation, contract compliance. When a contractor bills for work that is already included in the contract\'s initial scope, accepting the offer would amount to paying twice for the same work. Refusing is the correct response — the contract defines what is already committed, and the project team is not obligated to authorize additional payment for deliverables the vendor was already engaged to produce. (PMBOK Guide) – Seventh Edition, 2021, p. 25, \'Be a Diligent, Respectful, and Caring Steward\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option B (The project scope can be decomposed into smaller parts, the first representing a minimum viable product (MVP).) fixes it."',
        'Explanation: Keywords: agile suitability assessment, scope decomposability, MVP, approach selection. The most critical factor for agile suitability is whether the scope can be meaningfully broken into independently deliverable increments. A scope that can be decomposed into smaller parts — with the first increment representing an MVP — enables the iterative delivery and feedback loops that make agile valuable. (PMBOK Guide) – Seventh Edition, 2021, p. 40, \'Tailor Based on Context\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option B (Allocate time to mentor the team.) fixes it."',
        'Explanation: Keywords: hybrid approach adoption, vendor team, agile PM, mentoring. An experienced agile PM hired to transition a vendor team toward hybrid practices must invest time in mentoring — not just setting expectations. Without structured mentoring, the team will default to what they know, and the hybrid approach will exist on paper without changing how work actually gets done. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option A (Award certificates of appreciation to encourage the team) fixes it."',
        'Explanation: Keywords: tight schedule, team performance maintenance, recognition, motivation. A team performing at an acceptable level under delivery pressure needs recognition to sustain that performance through the final push. Certificates of appreciation acknowledge the team\'s contribution in a tangible way — signaling that their effort is seen and valued, which is a more effective motivator than communicating the pressure from above. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option D (Perform a sprint retrospective with the project team members) fixes it."',
        'Explanation: Keywords: sprint issues, team conflicts, low motivation, sprint retrospective. The sprint retrospective is the designed mechanism for processing what went wrong during a sprint and deciding what to improve. When team members are upset and unmotivated after a difficult sprint, the retrospective creates a structured, safe space to surface those experiences, address the conflicts, and collectively rebuild commitment before the next sprint begins. (PMBOK Guide) – Seventh Edition, 2021, p. 48, \'Embrace Adaptability and Resiliency\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Options A and D (Contingency control in the project and rebaseline; Integrated change control in the project) work together."',
        'Explanation: Keywords: unforeseen risks, budget impact, contingency reserve, integrated change control. When risks that were not anticipated at planning materialize and threaten the budget, the PM must simultaneously use available contingency reserves to absorb the impact and route any budget changes through integrated change control. Together these actions manage the immediate financial pressure while ensuring any adjustments to the baseline are formally authorized. (PMBOK Guide) – Seventh Edition, 2021, p. 46, \'Optimize Risk Responses\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option C (Coordinate a meeting to understand the situation and resolve any conflicts.) fixes it."',
        'Explanation: Keywords: global project, regional team collaboration failure, conflict resolution, planning phase. When team members from different regions resist collaborating, the cause must be understood before any structural changes are made. A meeting focused on understanding the situation and resolving the specific conflicts creates the dialogue that surfaces misalignments — whether rooted in cultural differences, role ambiguity, or competing priorities. (PMBOK Guide) – Seventh Edition, 2021, p. 28, p. 29, \'Create a Collaborative Team Environment\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option D (Meet with the project team to understand the issue and define actions.) fixes it."',
        'Explanation: Keywords: incomplete component, WBS confirmation, team diagnosis, action planning. When a component is confirmed in the WBS but the customer reports it as incomplete, there is a gap between what was planned and what was delivered. Meeting with the project team first — before raising change requests or escalating — establishes why the gap exists and what corrective actions are needed to address it. (PMBOK Guide) – Seventh Edition, 2021, p. 44, \'Navigate Complexity\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option A (Schedule a meeting with the project team to reinforce the ground rules.) fixes it."',
        'Explanation: Keywords: ground rule violations, long-running project, team meeting, rule reinforcement. Ground rules erode over time without active reinforcement — especially after many iterations when early commitments fade. Bringing the full team together to revisit and reinforce the ground rules addresses the drift collectively, reminding everyone of the agreed norms without singling out individuals in a way that creates resentment. (PMBOK Guide) – Seventh Edition, 2021, p. 28, p. 29, \'Create a Collaborative Team Environment\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option C (Use a direct, collaborative approach with the technician and supervisor.) fixes it."',
        'Explanation: Keywords: supervisor-technician conflict, time-critical project, collaborative resolution, direct approach. A conflict between supervisor and technician that has reached the point where one party cannot continue working with the other requires direct, structured engagement from the PM. A collaborative approach brings both parties together to surface the actual issues — the technical performance concerns and the interpersonal friction — and find a resolution that allows the team to function despite time pressure. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    (
        'Explanation: Need: keep plans flexible. Option A (Update the issue log and act to minimize the impact) fixes it."',
        'Explanation: Keywords: supplier bankruptcy, material shortage, issue log, impact minimization. A confirmed supplier failure is no longer a risk — it is an issue requiring active management. Logging it immediately ensures the problem is formally tracked, and taking parallel action to minimize the impact — exploring alternative suppliers, adjusting the schedule — prevents the delay from compounding while waiting for a formal response. (PMBOK Guide) – Seventh Edition, 2021, p. 46, \'Optimize Risk Responses\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option C (Evaluate the change request against the project scope statement) fixes it."',
        'Explanation: Keywords: change request, no remaining budget, scope statement evaluation, IT project. Before seeking funding or approving a change, the PM must determine whether the requested change is within the project\'s defined scope. Evaluating it against the scope statement clarifies whether this is a legitimate scope expansion requiring new funding or a requirement that was already committed and should be delivered within the existing budget. (PMBOK Guide) – Seventh Edition, 2021, p. 50, \'Enable Change to Achieve the Envisioned Future State\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option D (Provide the business analyst with access to the financial and scheduling information) fixes it."',
        'Explanation: Keywords: new team member, financial information access, scheduling access, onboarding. A team member who needs to understand the financial and scheduling aspects of a project needs direct access to that information — not reports designed for someone else or coaching through a proxy. Providing access to the source data is the most direct and respectful way to support their learning. (PMBOK Guide) – Seventh Edition, 2021, p. 25, \'Be a Diligent, Respectful, and Caring Steward\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option A (Schedule a meeting with critical stakeholders to review the issue and decide on the next steps) fixes it."',
        'Explanation: Keywords: patent conflict, agile project, issue escalation, stakeholder decision. A patent conflict that threatens the project\'s deliverable is a high-stakes issue with legal implications that the PM cannot navigate alone. Bringing critical stakeholders together ensures the people with authority, knowledge, and accountability for the outcome are part of the decision — which may range from design change to legal action to project cancellation. (PMBOK Guide) – Seventh Edition, 2021, p. 44, \'Navigate Complexity\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option D (Follow the stakeholder engagement plan) fixes it."',
        'Explanation: Keywords: timeline decision, scope change, decision authority, stakeholder engagement plan. Decisions about scope-related timeline changes must go through the right decision-making authority — not be made in a team meeting by whoever is present. Following the stakeholder engagement plan routes the decision to the person or body with the authority to make it, ensuring legitimacy and preventing decisions from being escalated or reversed later. (PMBOK Guide) – Seventh Edition, 2021, p. 34, \'Recognize, Evaluate, and Respond to System Interactions\'"'
    ),
    (
        "Explanation: Need: guide and calm the team. Option C (Adjust the project manager's management style to better fit senior team members.) fixes it.\"",
        'Explanation: Keywords: micromanagement, senior team members, leadership style adjustment, team performance. Senior team members with experience need autonomy, not oversight. Adjusting the management style to match their capability level — providing direction when needed but removing close supervision — resolves the tension while enabling the team to apply the expertise that makes them effective contributors. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Options A and B (Ask the stakeholders about the priority of this change; Ask the product owner to review the product backlog) work together."',
        'Explanation: Keywords: mid-project stakeholder feedback, product change, priority assessment, backlog review. Stakeholder feedback that could change the product requires two immediate actions: understanding how urgently the stakeholders need the change (priority), and ensuring the product owner has the full picture before deciding how it fits into the backlog. Together these steps ensure the change is neither ignored nor incorporated blindly without considering current commitments. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option D (Discuss project requirements with the new stakeholder, and update the communications management plan.) fixes it."',
        'Explanation: Keywords: stakeholder replacement, merger, information gap, communications plan update. When a new stakeholder arrives mid-project, they bring different context, expectations, and communication needs from their predecessor. Discussing project requirements ensures they understand what has been committed, while updating the communications plan formalizes how they will be kept informed going forward — preventing future information gaps. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option A (Ensure the sprint size is appropriate for the iteration duration.) fixes it."',
        'Explanation: Keywords: missed user stories, sprint sizing, iteration capacity, consistent underdelivery. Consistent failure to complete planned user stories over multiple sprints is a capacity planning problem — the team is committing to more than the iteration duration allows them to deliver. Aligning sprint size with the team\'s actual throughput per iteration eliminates the pattern of missed commitments by grounding planning in realistic capacity. (PMBOK Guide) – Seventh Edition, 2021, p. 40, \'Tailor Based on Context\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option A (Set up a training session for all project team members) fixes it."',
        'Explanation: Keywords: hybrid methodology adoption, slow transition, artifact updates, team training. A team that is slow to adopt a new methodology and consistently fails to update project artifacts lacks understanding of what the methodology requires and why. A training session addresses both gaps at once — building the knowledge needed to use the tools correctly and the context needed to understand why timely updates matter to the overall project. (PMBOK Guide) – Seventh Edition, 2021, p. 48, \'Embrace Adaptability and Resiliency\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option C (Update the communications management plan) fixes it."',
        'Explanation: Keywords: online dashboard, executive reporting, communications management plan, new channel. Adding a new reporting channel — an online dashboard for executive bi-weekly reports — changes how project information flows to stakeholders. The communications management plan must be updated to capture this new channel, its intended audience, the frequency, and what information it will contain. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option B (Rolling wave planning) fixes it."',
        'Explanation: Keywords: functionality compliance failure, predictive approach, schedule compression, rolling wave planning. Rolling wave planning addresses the need to accelerate delivery in a predominantly predictive project by planning the near-term work in detail while leaving later phases at a higher level. It allows the team to begin recovery activities immediately while preserving flexibility for how the remaining work will be structured as understanding of the gap improves. (PMBOK Guide) – Seventh Edition, 2021, p. 44, \'Navigate Complexity\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option D (Ask the team member to use their recently acquired knowledge to develop and provide training to the team) fixes it."',
        'Explanation: Keywords: certification, tool adoption gap, knowledge sharing, peer training. A certified team member who knows a tool the rest of the team is not using represents an untapped internal training resource. Asking them to develop and deliver training to the team leverages their expertise, creates knowledge transfer that benefits the whole project, and gives the certified member a leadership opportunity that validates their investment. (PMBOK Guide) – Seventh Edition, 2021, p. 28, p. 29, \'Create a Collaborative Team Environment\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option A (Arrange a meeting with the managers and try to reach an agreement.) fixes it."',
        'Explanation: Keywords: functional manager conflict, task delays, direct meeting, agreement building. Delays driven by an unresolved conflict between two functional managers will not resolve on their own — the underlying disagreement must be surfaced and settled. Arranging a direct meeting with both managers creates the opportunity to understand each party\'s position and negotiate an agreement that allows the critical work to proceed. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    (
        "Explanation: Need: guide and calm the team. Options A and B (Check the risk register for a prepared response to a resource being suddenly unavailable.; Check if the team member's activities are sufficiently documented to facilitate handover) work together.\"",
        'Explanation: Keywords: sudden resource absence, risk register response, activity documentation, handover planning. When a key resource is suddenly unavailable, the PM\'s first two actions are to use the tools already in place: the risk register may contain a prepared response to exactly this scenario, while documentation quality determines whether the work can be handed over without critical knowledge being lost. Both must be assessed before any reallocation decisions are made. (PMBOK Guide) – Seventh Edition, 2021, p. 46, \'Optimize Risk Responses\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option A (Understand the context and interdependencies of the process from the team members and then define improvements) fixes it."',
        'Explanation: Keywords: phase-gate quality, predictive approach, process improvement, context understanding. Before recommending process changes, the PM must understand why the current process exists and how it connects to other project elements. Team members who live in the process know its real constraints and interdependencies — their input is the prerequisite to designing improvements that will actually work rather than breaking something that has a hidden dependency. (PMBOK Guide) – Seventh Edition, 2021, p. 40, \'Tailor Based on Context\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option B (Ensure that relevant stakeholders and expectations are identified and assess the component delay) fixes it."',
        'Explanation: Keywords: vendor delay, key component, stakeholder identification, delay assessment. A vendor-announced delay on a key component affects different stakeholders in different ways — some depend on that component for subsequent work. Identifying who is affected and assessing the full scope of the delay is the necessary first step before any response action can be designed that addresses all the impacts. (PMBOK Guide) – Seventh Edition, 2021, p. 34, \'Recognize, Evaluate, and Respond to System Interactions\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option B (Update the issue log) fixes it."',
        'Explanation: Keywords: government-owned site, implementation location, issue log, site constraint. Discovering that the planned implementation site is government-owned is an issue that could have significant legal, regulatory, and timeline consequences. Logging it in the issue log immediately ensures the problem is formally tracked, assigned for investigation, and visible to the stakeholders who need to respond — before any site work begins on a location the project may not have authority to use. (PMBOK Guide) – Seventh Edition, 2021, p. 46, \'Optimize Risk Responses\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option D (Evaluate the proposed change with integrated change controls and discuss the change with the project sponsor) fixes it."',
        'Explanation: Keywords: mid-execution change request, new stakeholder, integrated change control, sponsor discussion. Any proposed change to project parameters — regardless of who proposes it — must go through integrated change control to understand its full impact. Discussing it with the project sponsor ensures that the person with authority over the project is engaged before any decision is made about whether to absorb, accept, or reject the change. (PMBOK Guide) – Seventh Edition, 2021, p. 50, \'Enable Change to Achieve the Envisioned Future State\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option C (Met with the team, allowed team members to make decisions about what to do and established performance goals) fixes it."',
        'Explanation: Keywords: hybrid project, agile inexperience, schedule slippage, team empowerment. A team inexperienced with agile needs both structure and autonomy to build capability quickly. Meeting with the team to establish performance goals sets the direction, while giving them decision-making authority over how they meet those goals builds the ownership and accountability that transforms compliance into genuine agile practice. (PMBOK Guide) – Seventh Edition, 2021, p. 28, p. 29, \'Create a Collaborative Team Environment\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option B (Change log) fixes it."',
        'Explanation: Keywords: CCB deferral, change requests, stakeholder communication, change log. The change log is the authoritative record of all change requests and their disposition — including those that were approved, rejected, or deferred. Sharing the change log with stakeholders provides a transparent account of what was requested, what the CCB decided, and why — ensuring stakeholders have an accurate picture of the project\'s change history. (PMBOK Guide) – Seventh Edition, 2021, p. 50, \'Enable Change to Achieve the Envisioned Future State\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option C (Help the team member to perform the quantitative risk analysis through coaching, mentoring and training) fixes it."',
        'Explanation: Keywords: skills gap, quantitative risk analysis, coaching, mentoring. A senior team member who lacks a specific technical skill represents a development opportunity, not just a delivery gap. Coaching, mentoring, and training provides the capability-building support that closes the gap while keeping the team member engaged and developing — a more sustainable solution than reassigning the work or escalating the issue. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option D (Offer cross-training and mentoring to the new team member) fixes it."',
        'Explanation: Keywords: key resource departure, new team member onboarding, cross-training, mentoring. The window between a key resource\'s departure and a new team member becoming fully productive represents the highest risk period for project performance. Cross-training accelerates the knowledge transfer of critical skills, while mentoring provides the contextual guidance that documentation alone cannot convey — together shortening the new member\'s ramp-up time. (PMBOK Guide) – Seventh Edition, 2021, p. 28, p. 29, \'Create a Collaborative Team Environment\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option A (Document the lessons learned and implement improvements in the next sprint) fixes it."',
        'Explanation: Keywords: retrospective improvement idea, lessons learned, next sprint, continuous improvement. The retrospective generates improvement actions — not just reflections. Documenting the lesson learned captures the insight for future projects, while implementing the improvement in the next sprint ensures the retrospective produces tangible change rather than just discussion. This is the agile continuous improvement cycle working as intended. (PMBOK Guide) – Seventh Edition, 2021, p. 48, \'Embrace Adaptability and Resiliency\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option C (Help the team review the project approach to initiate the corrective actions) fixes it."',
        'Explanation: Keywords: contingency reserve depletion, late project risk, corrective action, approach review. With only one iteration remaining and contingency depleted by an unidentified risk, the team cannot continue with the current approach unchanged. Reviewing the project approach with the team identifies what must be adjusted — scope, approach, or priorities — to complete the final iteration within what is now available. (PMBOK Guide) – Seventh Edition, 2021, p. 48, \'Embrace Adaptability and Resiliency\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option B (Set up a meeting with the distracted team member to discuss any issues) fixes it."',
        'Explanation: Keywords: exclusion from team event, distracted team member, one-on-one meeting, team dynamics. Visible distraction in standups signals a personal or interpersonal issue affecting the team member\'s ability to contribute. A private meeting gives them the opportunity to discuss what is affecting them without the pressure of the group setting — allowing the PM to understand and address the root cause rather than managing only the behavioral symptom. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option C (Organization-wide diversity training should have been provided to the workforce) fixes it."',
        'Explanation: Keywords: diversity and inclusion policy, organizational conflict, workforce training, change management. A diversity and inclusion policy that affects the whole organization requires a whole-organization response. Implementing the policy in two teams while leaving the broader workforce unprepared creates the friction and resistance that organization-wide training would have addressed — building shared understanding and common ground rather than isolating the change. (PMBOK Guide) – Seventh Edition, 2021, p. 50, \'Enable Change to Achieve the Envisioned Future State\'"'
    ),
    (
        "Explanation: Need: keep plans flexible. Option D (Worked with the product owner to clarify their role in an agile project and the scope of the agile ceremonies) fixes it.\"",
        'Explanation: Keywords: product owner role confusion, cost focus, agile ceremonies, role clarification. A product owner who focuses on iteration costs rather than product value is not operating within their defined agile role — the product owner\'s primary responsibility is maximizing product value, not managing costs. Clarifying the product owner\'s role and the purpose of agile ceremonies reorients them toward the outcomes their position is designed to drive. (PMBOK Guide) – Seventh Edition, 2021, p. 40, \'Tailor Based on Context\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option B (Coordinate virtual and face-to-face meetings at each site to improve communication) fixes it."',
        'Explanation: Keywords: global implementation, multiple sites, mixed communication, virtual and face-to-face. A global project with different locations and regions requires a communication approach that recognizes both the scale of distribution and the value of personal connection. Coordinating virtual meetings for efficiency and face-to-face meetings at each site for depth and relationship-building ensures that no location is reduced to a passive recipient of remote communication. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    (
        "Explanation: Need: listen to people needs. Option B (Create a benefits management plan mapped to the organization's strategic objectives) fixes it.\"",
        'Explanation: Keywords: failing project, stakeholder awareness, benefits management plan, strategic alignment. Stakeholders who do not know the project\'s status or expected benefits cannot support it or make informed decisions about its continuation. A benefits management plan that maps project outcomes to organizational objectives gives stakeholders a clear, compelling answer to what the project delivers and why it matters — addressing the most critical gap driving the project\'s endangered status. (PMBOK Guide) – Seventh Edition, 2021, p. 32, \'Focus on Value\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option D (The project is under budget and on schedule.) fixes it."',
        'Explanation: Keywords: earned value analysis, user stories, CPI, agile performance measurement. With 50 user stories delivered at a value of $50 each, the earned value is $2,500 — but only $2,000 has been spent, giving a CPI greater than 1 (under budget). The delivery of exactly 50 stories when 50 were planned indicates the project is on schedule. Both metrics confirm the project is under budget and on track. (PMBOK Guide) – Seventh Edition, 2021, p. 32, \'Focus on Value\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option D (Conduct an earned value analysis (EVA)) fixes it."',
        'Explanation: Keywords: conflicting status reports, earned value analysis, cost and schedule variance, objective measurement. When reported status conflicts with what stakeholders observe in the metrics, the PM needs an objective analytical tool to establish the ground truth. Earned value analysis combines cost, schedule, and work completed into a single framework that reveals the actual state of the project — removing the ambiguity that allows conflicting narratives to persist. (PMBOK Guide) – Seventh Edition, 2021, p. 32, \'Focus on Value\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option A (Inform the stakeholder that the correct procedure for new requirements is to provide it directly to the project manager.) fixes it."',
        'Explanation: Keywords: stakeholder direct contact, change request bypass, communications management, team member response. When a stakeholder bypasses the PM to request changes from a team member directly, the team member is not equipped to evaluate or commit to that change. Redirecting the stakeholder to the project manager maintains the correct governance structure and protects the team member from obligations they cannot fulfill without PM oversight. (PMBOK Guide) – Seventh Edition, 2021, p. 34, \'Recognize, Evaluate, and Respond to System Interactions\'"'
    ),
    (
        'Explanation: Need: keep plans flexible. Option C (Clarify the high-level business requirements with the event organizer as a basis for forming the deliverables list.) fixes it."',
        'Explanation: Keywords: project initiation, exhibition project, business requirements, deliverables list. A project management plan without a clear deliverables list is built on assumptions. Clarifying high-level business requirements with the event organizer at the start of initiation ensures the deliverables list is grounded in what the client actually needs — not what the PM assumes based on project type or scope documents alone. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Options C and D (Tier the contract for fixed and agile components; Provide alternatives to scope change at specific project phases within the contract.) work together."',
        'Explanation: Keywords: fixed budget, agile component, contract structure, scope change controls. Protecting profitability in a fixed-budget contract with an evolving agile component requires structural controls at the contract level. Tiering the contract separates the fixed and agile work financially, while built-in scope change alternatives at defined phases give both parties agreed-upon options for managing the uncertain scope — preventing open-ended cost growth from eroding the project\'s margin. (PMBOK Guide) – Seventh Edition, 2021, p. 40, \'Tailor Based on Context\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option C (Point out to the project team and the customer that all information concerning the timeline of the project should be communicated by the project manager.) fixes it."',
        'Explanation: Keywords: informal communication, timeline disclosure, communications governance, PM authority. Project timeline information shared informally by a team member — outside agreed communication channels — undermines the PM\'s ability to control the message and its context. Reinforcing that timeline communications are the PM\'s responsibility protects the customer relationship from receiving incomplete or unanticipated information and restores the communications structure that prevents future incidents. (PMBOK Guide) – Seventh Edition, 2021, p. 34, \'Recognize, Evaluate, and Respond to System Interactions\'"'
    ),
    (
        "Explanation: Need: listen to people needs. Option D (Validate the proposed change's impact on the project.) fixes it.\"",
        'Explanation: Keywords: sponsor-requested enhancement, scope change, impact validation, change control. Even a sponsor-requested change must be evaluated for its impact before being accepted. Validating the change\'s effect on scope, schedule, cost, and quality provides the sponsor with the information they need to make an informed decision — and ensures the PM is not committing to a change whose consequences have not been understood. (PMBOK Guide) – Seventh Edition, 2021, p. 50, \'Enable Change to Achieve the Envisioned Future State\'"'
    ),
    (
        'Explanation: Need: keep plans flexible. Option B (Analyze both projects to determine the most effective use of common resources) fixes it."',
        'Explanation: Keywords: concurrent projects, schedule compression, resource constraint, resource optimization. When fast-tracking is not possible and additional resources are unavailable, the only option is to optimize the use of what exists. Analyzing both projects to find the most effective allocation of common resources identifies where rebalancing can free up capacity for the critical project without undermining the other\'s ability to deliver. (PMBOK Guide) – Seventh Edition, 2021, p. 34, \'Recognize, Evaluate, and Respond to System Interactions\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option B (Perform risk analysis against the issue.) fixes it."',
        'Explanation: Keywords: solution design defect, deployment decision, risk analysis, stakeholder uncertainty. When stakeholders face uncertainty about whether to deploy a system with a known defect, the decision requires a clear understanding of the risk. A risk analysis quantifies the likelihood and potential impact of deploying with the defect versus the cost and delay of fixing it first — giving stakeholders the evidence they need to make an informed deployment decision. (PMBOK Guide) – Seventh Edition, 2021, p. 46, \'Optimize Risk Responses\'"'
    ),
    (
        "Explanation: Need: listen to people needs. Option D (Send a communication to management recognizing the team member's contributions) fixes it.\"",
        'Explanation: Keywords: team member improvement, performance recognition, management communication, documentation. Exceptional performance that has been objectively measured deserves recognition that reaches beyond the project team. A formal communication to management creates a documented record of the team member\'s contribution, provides visibility to decision-makers who may influence their career, and demonstrates the PM\'s commitment to rewarding performance. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option A (Review and prioritize new requirements with stakeholders to determine which change requests are needed.) fixes it."',
        'Explanation: Keywords: stakeholder replacement, new requirements surge, prioritization, change request filtering. When multiple new stakeholders introduce numerous requirements simultaneously, the PM cannot route all of them to the CCB at once — nor dismiss them without evaluation. Reviewing and prioritizing them with the new stakeholders distinguishes requirements that genuinely need change requests from those that fall within existing scope, managing the flood while maintaining control. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    (
        "Explanation: Need: protect value and acceptance. Option B (Review the operations manager's concerns and ensure these concerns are addressed) fixes it.\"",
        'Explanation: Keywords: recurring stakeholder concerns, meeting delays, operational concerns, stakeholder engagement. An operations manager who repeatedly raises concerns at meetings is signaling that something important to them is not being addressed elsewhere. Reviewing their concerns and ensuring they are genuinely resolved — not just acknowledged — removes the source of the disruption and builds the trust needed for this stakeholder to support rather than obstruct the project. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option D (Invite a member of the operations team to be part of the validation and sprint meetings) fixes it."',
        'Explanation: Keywords: operations team complaint, sprint performance, acceptance criteria, cross-team inclusion. The operations team\'s inability to support the product outcome signals that their acceptance criteria were never part of the delivery definition. Inviting an operations team member into sprint meetings and validation sessions creates the ongoing collaboration needed to ensure delivery meets operational requirements — addressing the gap at its source rather than at sprint review. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option D (Split the feature into smaller subfeatures. implement them, and then deliver them incrementally in multiple iterations) fixes it."',
        'Explanation: Keywords: feature decomposition, iteration capacity, incremental delivery, critical priority. A critical feature that cannot be completed in a single iteration is a decomposition problem, not a scope negotiation. Splitting it into smaller subfeatures that can each be independently implemented and delivered across multiple iterations maintains progress toward the customer\'s priority while working within the team\'s realistic capacity per iteration. (PMBOK Guide) – Seventh Edition, 2021, p. 32, \'Focus on Value\'"'
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
