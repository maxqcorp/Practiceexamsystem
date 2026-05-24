MD_FILE = './src/imports/project-management-questions-1.md'

with open(MD_FILE, 'r', encoding='utf-8') as f:
    content = f.read()

replacements = [
    (
        'Explanation: Need: listen to people needs. Option A (Analyze the stakeholder\'s expectations and emphasize the topics of interest that may influence the project\'s success) fixes it."',
        'Explanation: Keywords: disengaged stakeholder, expectations analysis, topics of interest, project success influence. When a key stakeholder lacks engagement and interest in project status, the project manager should analyze that stakeholder\'s expectations and emphasize the topics most relevant to their interests. Tailoring engagement to what the stakeholder actually values — rather than pushing generic status information — is the most effective way to re-engage a disinterested stakeholder and maintain project alignment. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option D (Meet with the project stakeholders to explain the need to comply with the PMO standards and update the status report format accordingly) fixes it."',
        'Explanation: Keywords: PMO reporting standards, custom status reports, stakeholder information needs, compliance. When stakeholders prefer a non-standard reporting format and the PMO has organizational standards, the project manager should meet with stakeholders to explain the need for compliance while updating the status report format to address their informational needs. This approach balances organizational governance compliance with stakeholder satisfaction by adapting the standard format collaboratively. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option D (Kept documentation in the project management information system (PMIS) and shared it with appropriate stakeholders) fixes it."',
        'Explanation: Keywords: documentation audit, outdated project schedule, PMIS, authorized version control. Project documentation should be stored in the Project Management Information System (PMIS) and shared with appropriate stakeholders, ensuring the most current versions are always available in a centrally accessible, authorized location. Storing documentation in the PMIS — rather than distributing it informally — ensures that stakeholders and auditors can always access the latest approved version. (PMBOK Guide) – Seventh Edition, 2021, p. 25, \'Be a Diligent, Respectful, and Caring Steward\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option D (When the work is progressing well through the team) fixes it."',
        'Explanation: Keywords: first retrospective timing, agile team, continuous improvement, team progress. In agile, the first retrospective should occur when work is progressing well through the team — not only at formal milestones, major releases, or after a predetermined duration. Holding the first retrospective when conditions are constructive ensures the team\'s initial improvement experience is positive and productive, establishing a healthy continuous improvement culture from the outset. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option A (Meet with the stakeholder to discuss the impact of the deliverable) fixes it."',
        'Explanation: Keywords: charter drafting, resistant stakeholder, resource provision, deliverable impact discussion. When a required stakeholder refuses involvement because they perceive no benefit in the project deliverable, the project manager should meet directly with them to discuss the deliverable\'s impact and value from the stakeholder\'s perspective. A direct, value-focused conversation addresses the stakeholder\'s core objection and is the most likely path to gaining their engagement and the resource contributions the project needs. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option C (Use regular feedback loops through daily standups iteration demos and retrospectives) fixes it."',
        'Explanation: Keywords: first agile project, risk management in agile, feedback loops, daily standups retrospectives. In agile projects, risks are assessed and managed continuously through regular feedback loops — daily standups identify emerging impediments, iteration demos surface quality and scope risks, and retrospectives capture process and team risks. These built-in agile ceremonies provide the ongoing risk visibility the manager is seeking without requiring a separate formal risk management overlay. (PMBOK Guide) – Seventh Edition, 2021, p. 46, \'Optimize Risk Responses\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option B (Perform iterative planning with the team to use the prototype) fixes it."',
        'Explanation: Keywords: supply delay, 6-month import delay, prototype workaround, iterative planning. When a critical supply is delayed by 6 months, the project manager should perform iterative planning with the team to explore using the available prototype as a potential workaround. Iterative planning enables the team to adapt progressively to new constraints — evaluating the prototype\'s viability, integrating it into the delivery plan, and adjusting as the situation evolves. (PMBOK Guide) – Seventh Edition, 2021, p. 48, \'Embrace Adaptability and Resiliency\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option C (Conduct a kick-off meeting and communicate the goals and objectives of the project) fixes it."',
        'Explanation: Keywords: multicontinental agile team, scrum knowledge gaps, project goals, kick-off meeting. When gaps in understanding about project goals and objectives emerge during daily scrums, the root cause is likely the absence of a structured kick-off meeting that would have established shared clarity upfront. Conducting a formal kick-off meeting with all team members communicates goals and objectives explicitly, ensuring all members — regardless of continent or background — begin with a common understanding. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option C (Submit a change request to analyze a new set of quality tests) fixes it."',
        'Explanation: Keywords: quality management plan gap, user perception tests, change request, formal process. When the quality management plan fails to address how end users will perceive the product\'s benefits, the project manager should submit a change request to add a new set of quality tests that capture user perception and benefit metrics. Formal change control ensures this addition to the quality plan is properly authorized rather than informally appended, maintaining the integrity of the plan. (PMBOK Guide) – Seventh Edition, 2021, p. 42, \'Build Quality into Processes and Deliverables\'"'
    ),
    (
        'Explanation: Need: keep plans flexible. Option A (Schedule crashing) fixes it."',
        'Explanation: Keywords: SPI CPI payment threshold, 0.95 compliance, schedule crashing, iterative project. When a project\'s SPI and CPI must stay above 0.95 to authorize payment, and the metrics are falling below threshold, schedule crashing — adding resources to critical path activities — is the most direct way to recover schedule performance within the current delivery framework. Crashing accelerates specific activities to bring the schedule performance index back into compliance while keeping the project within its authorized scope and budget. (PMBOK Guide) – Seventh Edition, 2021, p. 40, \'Tailor Based on Context\'"'
    ),
    (
        'Explanation: Need: keep plans flexible. Option A (Follow the risk response plan) fixes it."',
        'Explanation: Keywords: critical path delay, anticipated event, risk response plan execution, proactive risk management. When a delay on a critical path activity is caused by an anticipated event — meaning it was an identified risk — the project manager should follow the established risk response plan rather than improvising a new response. The risk response plan was developed specifically for this scenario; following it demonstrates disciplined, pre-planned risk management rather than reactive decision-making under pressure. (PMBOK Guide) – Seventh Edition, 2021, p. 46, \'Optimize Risk Responses\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option B (Review the quality management plan) fixes it."',
        'Explanation: Keywords: deliverable not functioning as expected, stakeholder approval withheld, quality management plan, end-of-project. When a key stakeholder withholds approval because deliverables are not functioning as expected, the project manager should review the quality management plan to identify what standards were not met and what corrective actions are defined. The quality management plan is the governing reference for understanding and addressing quality performance gaps in delivered work. (PMBOK Guide) – Seventh Edition, 2021, p. 42, \'Build Quality into Processes and Deliverables\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option A (An agreed-upon work method and tools that should fit the business need and project constraints) fixes it."',
        'Explanation: Keywords: work methods and tools discussion, team decision, business need fit, project constraints. When a project team discusses which work methods and tools to use for building a deliverable, the result should be an agreed-upon set of methods and tools that fit the specific business need and project constraints. There is no universally correct methodology or toolset — the team must collaboratively select the approach best suited to their project\'s unique characteristics and organizational context. (PMBOK Guide) – Seventh Edition, 2021, p. 40, \'Tailor Based on Context\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option C (Make sure all stakeholders have access to the system and know where to find project artifacts) fixes it."',
        'Explanation: Keywords: PMIS access issues, stakeholders unable to find artifacts, access and navigation, project schedule. When stakeholders report they cannot find project artifacts in the PMIS, the project manager should ensure all stakeholders have access to the system and know where to find the relevant artifacts. This direct resolution addresses both potential barriers — access rights and navigation knowledge — ensuring stakeholders can independently retrieve the information they need. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option B (Identify the issues between the team members and guide them toward a resolution) fixes it."',
        'Explanation: Keywords: two team members misunderstanding, persistent conflict, issue identification, resolution guidance. When two team members consistently have misunderstandings and struggle to work together, the project manager should identify the specific issues between them and guide them toward a resolution through a structured problem-solving approach. Removing one member, issuing warnings, or providing generic training would all address symptoms rather than the actual interpersonal dynamic causing the persistent conflict. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option A (Request a reserve analysis and update the risk management plan) fixes it."',
        'Explanation: Keywords: next phase critical element, reserve analysis needed, risk management plan update, contingency. When reviewing solved issues and the lead risk analyst identifies a critical element requiring reserves in the next phase, the project manager should request a reserve analysis and update the risk management plan accordingly. A reserve analysis determines the appropriate contingency level needed for the critical risk, and updating the risk management plan ensures the reserve is formally authorized and monitored. (PMBOK Guide) – Seventh Edition, 2021, p. 46, \'Optimize Risk Responses\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option B (Document who will be tracking benefits realization what will be tracked and when it will be tracked in the project closure report) fixes it."',
        'Explanation: Keywords: project closure, post-project benefits realization, closure report documentation, benefits tracking handoff. When some project benefits will not be realized until after project completion, the project manager should document in the project closure report who will track benefits realization, what will be tracked, and when — creating a formal handoff for post-project benefit monitoring. This ensures accountability for benefits realization is clearly assigned and does not fall through the cracks after the project team disbands. (PMBOK Guide) – Seventh Edition, 2021, p. 32, \'Focus on Value\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option D (Force/direct) fixes it."',
        'Explanation: Keywords: consistently late team member, team norms, force and direct, conflict resolution style. When a project manager directly tells a team member to align with the team\'s principles and arrive on time — without exploring the reason or seeking consensus — this represents the force/direct conflict resolution style, which imposes a solution based on authority and rules. Force/direct is appropriate when compliance with established team standards is non-negotiable and the project manager acts with authority to protect the functioning and morale of the broader team. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option B (Implement retrospectives with the vendor to gather the required knowledge) fixes it."',
        'Explanation: Keywords: vendor-produced deliverables, agile project, knowledge transfer, vendor retrospectives. Implementing retrospectives with the vendor creates a structured, recurring forum for the project team to gather knowledge from the vendor about how deliverables were produced. Retrospectives facilitate continuous knowledge transfer, building the team\'s capability to maintain and extend the deliverables after the vendor engagement ends — more effective than one-time manuals or formal training sessions. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option D (Look to see if the deliverable is described in the statement of work (SOW)) fixes it."',
        'Explanation: Keywords: disputed deliverable, cost-reimbursable contract, statement of work, contract investigation. When a deliverable is disputed as being outside the contract, the project manager should first look in the statement of work (SOW) to determine whether the deliverable was described there. The SOW is a key contractual document that captures negotiated scope details and often resolves disputes without requiring contract amendments or escalation to termination. (PMBOK Guide) – Seventh Edition, 2021, p. 25, \'Be a Diligent, Respectful, and Caring Steward\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option A (Estimate user story points and forecast a budget for that deliverable) fixes it."',
        'Explanation: Keywords: MVP cost estimation, board approval required, user story points, budget forecasting. To estimate the cost of the minimum viable product (MVP) for formal board approval, the project manager should estimate the user story points associated with those features and forecast a budget based on team velocity and cost data. This agile estimation approach provides a credible cost forecast grounded in the specific scope and complexity of the MVP rather than top-down financial assumptions. (PMBOK Guide) – Seventh Edition, 2021, p. 32, \'Focus on Value\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option B (Have the team create a minimum viable product (MVP).) fixes it."',
        'Explanation: Keywords: new product feasibility, customer requirements validation, MVP, real customer feedback. To validate customer requirements and gain real feedback on a new product concept, the team should create a minimum viable product (MVP) — a working, testable product with just enough features to enable meaningful customer evaluation. An MVP delivers actual user experience rather than survey responses or documentation, providing the highest-quality validation signal for product-market fit. (PMBOK Guide) – Seventh Edition, 2021, p. 32, \'Focus on Value\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option C (Meet with the sales and marketing teams to identify the requirements that were collected during the interview sessions with potential customers) fixes it."',
        'Explanation: Keywords: missing test cases, no acceptance criteria, customer requirements, sales and marketing. When a project team in the design phase has no test cases or acceptance criteria, the most direct source of product requirements is the sales and marketing teams who captured them from potential customers during interview sessions. Meeting with them to retrieve and formalize those requirements provides the foundation for developing the acceptance criteria and test cases the project needs to proceed. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option A (Become a servant leader by supporting team collaboration and removing impediments) fixes it."',
        'Explanation: Keywords: hybrid approach transition, servant leader, team collaboration support, impediment removal. When transitioning from a predictive to a hybrid approach, the project manager should shift to servant leadership — supporting team collaboration, removing impediments, and empowering the team rather than directing all activities. This behavioral shift is essential for a hybrid approach to succeed, as the agile component depends on team autonomy enabled by a supportive, facilitative leader. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option D (Share the lessons learned from the previous project with the team member) fixes it."',
        'Explanation: Keywords: known technical issue, previous project solution, lessons learned, organizational knowledge sharing. When a team member encounters a technical issue that was already solved in a previous project, the project manager should share the lessons learned from that project rather than allowing independent rediscovery. Leveraging existing organizational knowledge accelerates resolution, avoids wasted effort, and fulfills the project manager\'s stewardship responsibility to preserve and propagate knowledge across projects. (PMBOK Guide) – Seventh Edition, 2021, p. 25, \'Be a Diligent, Respectful, and Caring Steward\'"'
    ),
    (
        'Explanation: Need: protect value and acceptance. Option B (Break down the deliverable by using the work breakdown structure (WBS) process to make it more manageable for task assignment) fixes it."',
        'Explanation: Keywords: large complex deliverable, multiple developers needed, WBS decomposition, task assignment. When a deliverable is too large and complex to assign to a single person, the project manager should first use the Work Breakdown Structure (WBS) process to decompose it into manageable, assignable tasks. The WBS provides a structured framework for breaking down complexity, ensuring all work is identified, appropriately scoped, and assigned to specific resources with clear accountability. (PMBOK Guide) – Seventh Edition, 2021, p. 32, \'Focus on Value\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option B (Create a log to track risks assumptions issues and dependencies and establish a periodic review with the stakeholders) fixes it."',
        'Explanation: Keywords: dependencies and risks raised, RAID log, periodic stakeholder review, execution phase. When team members are surfacing dependencies, risks, and open questions during execution, the project manager should create a RAID log (Risks, Assumptions, Issues, Dependencies) to formally track these items and establish a periodic review with stakeholders. Systematic tracking and regular structured review ensures these factors are actively monitored rather than lost in informal meeting discussions. (PMBOK Guide) – Seventh Edition, 2021, p. 34, \'Recognize, Evaluate, and Respond to System Interactions\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option D (Start the project plan for the scope and quality and identify options to deliver and meet stakeholders expectations) fixes it."',
        'Explanation: Keywords: 2-month start delay, fixed budget deadline, project planning, delivery options identification. When a project is delayed at start with a fixed budget, deadline, and specifications, the project manager should start the project plan for scope and quality and identify options to deliver while meeting stakeholder expectations. Proactive planning focuses on finding creative delivery solutions within the given constraints rather than immediately seeking to renegotiate the baselines or accept degraded quality. (PMBOK Guide) – Seventh Edition, 2021, p. 40, \'Tailor Based on Context\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option C (Call for an open dialogue which the team will arrive at through consensus) fixes it."',
        'Explanation: Keywords: technology dispute, time-critical iteration, consensus, open dialogue. When team members are arguing about which technology to use on a time-critical iteration, the project manager should call for an open dialogue through which the team arrives at consensus — ensuring the decision is team-owned, technically sound, and made in time to keep the iteration on track. Consensus-based dialogue is more sustainable and effective than the project manager imposing a solution or leaving the team in an unresolved impasse. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    (
        'Explanation: Need: protect benefits for users. Option A (Refer to the project charter) fixes it."',
        'Explanation: Keywords: new project manager, delegated authority, project charter, role clarity. The project charter is the document that formally authorizes the project and defines the project manager\'s delegated authority — making it the first reference for any new project manager seeking to understand the scope of their decision-making power. Referring to the charter ensures the new project manager acts within their sanctioned boundaries from day one without relying on informal assumptions or verbal briefings. (PMBOK Guide) – Seventh Edition, 2021, p. 25, \'Be a Diligent, Respectful, and Caring Steward\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option B (Review the ground rules for collaboration within the team) fixes it."',
        'Explanation: Keywords: team conflict, talking over others, not listening, ground rules for collaboration. When two team members are in ongoing conflict over communication behavior — one consistently talking over the other — the project manager should review the team\'s ground rules for collaboration. Ground rules define expected behavioral standards for team interactions; revisiting them reminds all members of the agreed norms and provides a structured, non-punitive framework for resolving behavioral conflicts. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option B (Work with the IT team to prioritize the validation and release of the new features) fixes it."',
        'Explanation: Keywords: IT team validation delays, other priorities, feature release dependency, collaborative prioritization. When an external IT team\'s other priorities are delaying product validation and release, the project manager should work collaboratively with the IT team to prioritize the validation and release of the new features. A collaborative prioritization conversation demonstrates respect for the IT team\'s workload while advocating for the project\'s delivery needs within the system of interdependencies. (PMBOK Guide) – Seventh Edition, 2021, p. 34, \'Recognize, Evaluate, and Respond to System Interactions\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option D (During each iteration and review) fixes it."',
        'Explanation: Keywords: hybrid project, risk alignment gap, risk and mitigation review frequency, each iteration. To maintain ongoing alignment between the project team and stakeholders on risks and mitigation strategies, risks should be reviewed during each iteration and review cycle rather than only at formal milestones or steering committee meetings. This cadence ensures risk alignment is continuously refreshed as the project evolves, preventing the misalignment that occurs when risk reviews happen too infrequently. (PMBOK Guide) – Seventh Edition, 2021, p. 46, \'Optimize Risk Responses\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option D (Meet with the project team to find another solution) fixes it."',
        'Explanation: Keywords: insufficient risk response, issue still unresolved, team engagement, alternative solution. When a response action for an identified issue proves insufficient, the project manager should meet with the project team to collectively identify and evaluate alternative solutions. The team brings the most relevant technical and contextual knowledge to develop an effective replacement response — whereas individual actions like logging the failure or informing stakeholders alone do not address the unresolved problem. (PMBOK Guide) – Seventh Edition, 2021, p. 34, \'Recognize, Evaluate, and Respond to System Interactions\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option D (Empower the team to self-organize and make their own decisions) fixes it."',
        'Explanation: Keywords: stories awaiting project manager approval, hybrid retrospective, self-organizing team, empowerment. When stories are blocked because they are waiting for the project manager\'s approval — a bottleneck surfaced in the retrospective — the project manager should empower the team to self-organize and advance stories through their own decisions. Empowering the team removes the approval bottleneck and enables the faster, continuous delivery flow that hybrid agile methodology requires. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option B (Agile tools and techniques used in the defined hybrid methodology for consistent application by all team members) fixes it."',
        'Explanation: Keywords: hybrid approach adoption, varied agile knowledge, consistent application of tools, distributed team. When a distributed team has varied agile knowledge during a transition to hybrid delivery, the project manager should ensure agile tools and techniques defined in the hybrid methodology are applied consistently by all team members — not revert to predictive for some members. Consistent application of the defined hybrid practices ensures a common delivery standard and allows the team to build shared competency progressively. (PMBOK Guide) – Seventh Edition, 2021, p. 40, \'Tailor Based on Context\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option C (Provide proper training sessions to the stakeholders so they understand the purpose of the change) fixes it."',
        'Explanation: Keywords: conservative organizational culture, digital transformation, resistance to change, stakeholder training. When organizational culture is conservative and resistant to transformation, the first critical step is providing proper training sessions to stakeholders so they understand the purpose and benefits of the change. Building stakeholder understanding through education addresses the root cause of cultural resistance — people resist what they don\'t understand — creating the foundation for the transformation to succeed. (PMBOK Guide) – Seventh Edition, 2021, p. 50, \'Enable Change to Achieve the Envisioned Future State\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option A (Present brainstorming topics a day before the session so the team can reflect and contribute more fully during the session) fixes it."',
        'Explanation: Keywords: introverted team members, brainstorming sessions, advance topic preparation, contribution quality. When more than half the team are introverts, the project manager should present brainstorming topics a day in advance so team members can reflect before the session. Introverts typically do their best thinking in quiet, preparatory contexts rather than in spontaneous social settings — providing advance notice enables them to contribute more fully and confidently during collaborative team discussions. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option B (Create a problem-solving team from quality assurance subject matter experts (SMEs) experienced in this type of analysis) fixes it."',
        'Explanation: Keywords: high prototype defect rate, cause-and-effect analysis, quality SMEs, problem-solving team. When the quality management plan calls for a cause-and-effect analysis and prototypes show an unacceptably high defect rate, the project manager should create a problem-solving team from quality assurance SMEs experienced in this type of analysis. Selecting quality experts for this team ensures the analysis is conducted with the expertise needed to accurately identify root causes and develop effective corrective actions. (PMBOK Guide) – Seventh Edition, 2021, p. 42, \'Build Quality into Processes and Deliverables\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Options A and B (Strive toward continuous improvement; Work together daily as a team) work together."',
        'Explanation: Keywords: agile transition, third sprint, team cohesion, continuous improvement and daily collaboration. For a team that is not functioning as a cohesive unit during their third sprint, the two most foundational agile rules to instill are striving for continuous improvement and working together daily as a team. Continuous improvement builds the team\'s capacity to learn and adapt together, while daily collaboration creates the recurring interactions and shared accountability that transform a group of individuals into a cohesive, high-performing agile team. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option C (Assist by connecting the product owner with the team member to discuss what problem is to be solved) fixes it."',
        'Explanation: Keywords: servant leader, team member struggling with requirement, product owner connection, problem clarity. As a servant leader, the project manager should assist by connecting the product owner with the team member so they can discuss directly what problem the requirement is meant to solve. The product owner is the authoritative source on requirement meaning and business value — facilitating this conversation is the servant leader\'s role in removing knowledge barriers between the team and the clarity they need. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option B (Meet with the team member privately to discuss the problem and work together to find a solution) fixes it."',
        'Explanation: Keywords: underperforming team member, status meeting concern, private meeting, collaborative solution. When a team member raises concerns about an underperforming resource during a status meeting, the project manager should first meet with the affected team member privately to discuss the problem and work together to find a solution. A private, constructive meeting demonstrates respect, creates a safe space to understand the root cause, and jointly develops an improvement plan — more effective than replacing, escalating, or delegating the issue back to the team. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option A (Work more closely with the agile team to eliminate the need for progress reports) fixes it."',
        'Explanation: Keywords: agile team behind schedule, progress reports resource, direct team engagement, eliminate reporting. When an agile team is running late and a resource is spending time producing progress reports rather than contributing to delivery, the project manager should work more closely with the agile team directly to eliminate the need for separate reports — since close direct collaboration makes formal reporting redundant. Freeing the resource from reporting duties allows them to apply their skills toward accelerating the team\'s delayed tasks. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
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
