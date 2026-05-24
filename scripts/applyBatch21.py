MD_FILE = './src/imports/project-management-questions-1.md'

with open(MD_FILE, 'r', encoding='utf-8') as f:
    content = f.read()

replacements = [
    # Q1011
    (
        'Explanation: Need: protect value and acceptance. Option A (The functionality is delivered early; therefore, more value is delivered.) fixes it."',
        'Explanation: Keywords: agile delivery benefit, early functionality, value realization, project evaluation. The primary advantage of agile delivery from an evaluation perspective is that working functionality is delivered and available earlier than in a predictive approach. Early delivery of usable features means the organization begins realizing value sooner, improving the overall return on investment of the project. (PMBOK Guide) – Seventh Edition, 2021, p. 32, \'Focus on Value\'"'
    ),
    # Q1012
    (
        'Explanation: Need: listen to people needs. Option B (Determine if the feature is within the scope.) fixes it."',
        'Explanation: Keywords: team-requested feature, scope verification, gold plating risk, near-complete project. Before accepting any new feature addition, the project manager must first verify whether it falls within the approved project scope. If it is out of scope, the formal change control process must be followed — under budget and ahead of schedule do not give the team license to add unauthorized features. (PMBOK Guide) – Seventh Edition, 2021, p. 42, \'Build Quality into Processes and Deliverables\'"'
    ),
    # Q1013
    (
        'Explanation: Need: watch risks early. Option C (Start executing the project as the scope will be defined and redefined throughout the project.) fixes it."',
        'Explanation: Keywords: agile scope definition, uncertainty tolerance, progressive elaboration, experienced PM adaptation. In an agile project, attempting to fully define scope before execution contradicts the methodology\'s core principle that scope will emerge and evolve throughout delivery. The project manager should begin execution with the available information, trusting that scope will be progressively refined through iterations and customer feedback. (PMBOK Guide) – Seventh Edition, 2021, p. 48, \'Embrace Adaptability and Resiliency\'"'
    ),
    # Q1014
    (
        'Explanation: Need: listen to people needs. Option D (Review the communications management plan and communicate which technology is to be used to develop, transmit, and store project artifacts,) fixes it."',
        'Explanation: Keywords: unauthorized project management software, artifact storage, communications management plan, technology standardization. When a team member uses an unsanctioned tool to report and store project artifacts, the project manager must reference the communications management plan to clarify the approved technologies and communicate this standard to all team members. Standardizing on planned tools ensures information is findable, retrievable, and consistent across the project. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    # Q1015
    (
        'Explanation: Need: keep plans flexible. Option B (Identify an alternative component in case of incompatibility.) fixes it."',
        'Explanation: Keywords: new technology component, incompatibility risk, contingency component, risk response planning. When a risk of technology incompatibility is identified during planning, the appropriate proactive response is to identify an alternative component that could be substituted if the primary component fails to integrate. This contingency plan preserves the project\'s schedule and avoids being unprepared when the risk materializes. (PMBOK Guide) – Seventh Edition, 2021, p. 46, \'Optimize Risk Responses\'"'
    ),
    # Q1016
    (
        'Explanation: Need: protect benefits for users. Option A (Explore the minimum requirements of the product and their feasibility.) fixes it."',
        'Explanation: Keywords: conceptual product, uncertain marketability, 3-month deadline, MVP feasibility. When a product is still in conceptual stages with unclear marketability and a tight delivery timeline, the project manager must first explore what minimum requirements the product must satisfy and whether those are achievable within the constraints. This feasibility assessment grounds the project in what is actually deliverable before committing to a development approach. (PMBOK Guide) – Seventh Edition, 2021, p. 32, \'Focus on Value\'"'
    ),
    # Q1017
    (
        'Explanation: Need: guide and calm the team. Option B (Coach the team to solve the problem independently,) fixes it."',
        'Explanation: Keywords: self-organizing team, servant leader, coaching autonomy, problem-solving independence. When a self-organizing team brings an internal problem to the project manager, a servant leader\'s role is to coach the team through solving it themselves rather than providing a direct solution. This approach builds the team\'s self-sufficiency and preserves the self-organizing dynamic that is essential for agile performance. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    # Q1018
    (
        'Explanation: Need: guide and calm the team. Option A (Prioritized blockers on the critical path) fixes it."',
        'Explanation: Keywords: daily standup blockers, schedule deviation, critical path, impediment prioritization. Removing 75% of reported blockers but still seeing schedule deviation indicates that the project manager was resolving obstacles in the wrong order. Prioritizing blockers that affect the critical path over non-critical ones ensures that the activities directly determining project completion date are kept moving. (PMBOK Guide) – Seventh Edition, 2021, p. 44, \'Navigate Complexity\'"'
    ),
    # Q1019
    (
        'Explanation: Need: protect value and acceptance. Option B (Propose an approach based on value measurement, such as the use of objectives and key results.) fixes it."',
        'Explanation: Keywords: digital transformation, agile performance measurement, OKRs, value-based metrics. As an organization transitions to agile delivery, traditional scope/cost/schedule performance indicators become insufficient because they measure efficiency rather than value creation. Proposing an OKR-based or value measurement framework aligns the performance system with the agile emphasis on outcomes and business results rather than plan adherence. (PMBOK Guide) – Seventh Edition, 2021, p. 32, \'Focus on Value\'"'
    ),
    # Q1020
    (
        'Explanation: Need: listen to people needs. Option B (The product owner and the stakeholders—to prioritize the requirements in the product backlog.) fixes it."',
        'Explanation: Keywords: 2-month versus 4-month delivery gap, backlog prioritization, product owner and stakeholders, MVP acceleration. When a full delivery cannot fit within the required timeline, the solution is not to increase team velocity artificially but to work with the product owner and stakeholders to prioritize the most valuable requirements in the backlog for early delivery. This value-first reprioritization allows the most critical requirements to be delivered within the constraint. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    # Q1021
    (
        'Explanation: Need: guide and calm the team. Option D (Set up a weekly video conference to monitor the progress of the team member\'s work.) fixes it."',
        'Explanation: Keywords: key team member relocation, virtual collaboration, regular check-in, remote team management. When a critical team member relocates, the project manager should adapt to the new reality by establishing a regular video conference cadence to maintain oversight and collaboration rather than requiring physical presence or replacing the member. This pragmatic approach retains a valuable resource while accommodating their changed circumstances. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    # Q1022
    (
        'Explanation: Need: guide and calm the team. Option C (Add this item to the issue log and explore possible resolution options with the team.) fixes it."',
        'Explanation: Keywords: proof of concept failure, technology incompatibility, issue log, team resolution exploration. When a proof of concept reveals that current technology cannot support the solution, this active problem must be recorded in the issue log and explored collaboratively with the team. Logging the issue ensures it receives visibility and tracking, while team exploration leverages collective expertise to identify viable alternative approaches. (PMBOK Guide) – Seventh Edition, 2021, p. 34, \'Recognize, Evaluate, and Respond to System Interactions\'"'
    ),
    # Q1023
    (
        'Explanation: Need: keep plans flexible. Option A (The project is currently behind schedule with a corresponding lower cost, and every effort is being made to expedite the delayed activities.) fixes it."',
        'Explanation: Keywords: SPI below 1, cost savings with schedule lag, steering committee report, corrective action commitment. When actual progress is below planned progress but actual cost is also below budgeted cost, the project is behind schedule with a proportionate cost reduction — not a true savings. The steering committee report must accurately convey the schedule slippage and the corrective actions being taken to recover. (PMBOK Guide) – Seventh Edition, 2021, p. 25, \'Be a Diligent, Respectful, and Caring Steward\'"'
    ),
    # Q1024
    (
        'Explanation: Need: keep plans flexible. Option C (Create a draft schedule based on the activity list and the historical data from the closed project.) fixes it."',
        'Explanation: Keywords: activity list, no schedule baseline, historical project data, analogous estimating. When a project has an activity list but no baseline schedule, and a similar project was recently completed, the project manager should use both the activity list and historical duration data to create a draft schedule. This analogous estimating approach provides a reasonable starting point that can be refined as more project-specific information becomes available. (PMBOK Guide) – Seventh Edition, 2021, p. 40, \'Tailor Based on Context\'"'
    ),
    # Q1025
    (
        'Explanation: Need: guide and calm the team. Option B (Coach the project owner about the implications of unplanned meetings.) fixes it."',
        'Explanation: Keywords: ad hoc meetings, agile project, team disruption, product owner coaching. Repeated unplanned meetings called by the product owner disrupt the team\'s sprint focus and undermine the structured agile cadence. The project manager should coach the product owner about how ad hoc interruptions reduce team velocity and what the proper channels are for communicating outside planned ceremonies. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    # Q1026
    (
        'Explanation: Need: guide and calm the team. Option D (Help the teams in establishing and adhering to their ground rules and revisit after regular intervals.) fixes it."',
        'Explanation: Keywords: self-organizing teams, ground rules facilitation, servant leader empowerment, regular review. To create a positive environment for self-organizing teams, the project manager should help teams establish their own ground rules rather than imposing external ones — and then revisit those rules regularly to ensure they continue to serve the team\'s evolving needs. This collaborative facilitation approach supports autonomy while maintaining behavioral structure. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    # Q1027
    (
        'Explanation: Need: keep plans flexible. Option A (Perform tests and routinely track results as per the quality management plan.) fixes it."',
        'Explanation: Keywords: high risk of failing acceptance criteria, historical data, quality management plan, routine testing. When historical data signals a high risk of failing acceptance criteria, the appropriate response is disciplined execution of the quality management plan — performing tests early and tracking results routinely. This systematic approach detects compliance gaps early enough to correct them before final delivery. (PMBOK Guide) – Seventh Edition, 2021, p. 42, \'Build Quality into Processes and Deliverables\'"'
    ),
    # Q1028
    (
        'Explanation: Need: guide and calm the team. Option D (Listen to the concerns and suggest that the lead developer and the team be empowered to recommend the best approach.) fixes it."',
        'Explanation: Keywords: technology selection uncertainty, lead developer seeking direction, servant leadership, team empowerment. When a lead developer seeks direction on a complex technical decision, the project manager acting as servant leader should listen carefully and then empower the technical team to evaluate and recommend the best approach rather than directing the decision. Those closest to the technical problem are best positioned to make the optimal technology choice. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    # Q1029
    (
        'Explanation: Need: listen to people needs. Option C (Work with the organization\'s legal department to identify local regulations to ensure project compliance.) fixes it."',
        'Explanation: Keywords: international expansion, local government risk, legal compliance, regulatory identification. When opening operations in a new country, the project manager must work with the legal department to identify and integrate all applicable local regulations before any site or staffing decisions are made. Legal compliance is a non-negotiable constraint that must be understood up front to prevent the project from creating regulatory exposure for the organization. (PMBOK Guide) – Seventh Edition, 2021, p. 25, \'Be a Diligent, Respectful, and Caring Steward\'"'
    ),
    # Q1030
    (
        'Explanation: Need: guide and calm the team. Option C (Continue iterating and monitoring quality aspects sprint by sprint.) fixes it."',
        'Explanation: Keywords: incomplete product details, sponsor quality concern, servant leader, iterative quality monitoring. When product appearance details are still being finalized by other areas and the sponsor raises quality concerns, the servant leader should continue iterating while maintaining sprint-by-sprint quality monitoring rather than halting progress. Agile\'s iterative approach is designed to converge on quality progressively — not to require completeness before starting. (PMBOK Guide) – Seventh Edition, 2021, p. 42, \'Build Quality into Processes and Deliverables\'"'
    ),
    # Q1031
    (
        'Explanation: Need: listen to people needs. Option C (Connect with every location and check their preferred methods of communication.) fixes it."',
        'Explanation: Keywords: global project team, multiple continents, communication preferences, cultural alignment. Before establishing any communication framework for a globally distributed team, the project manager must connect with each location to understand their preferred methods of communication. Imposing a single approach without consulting regional preferences creates friction and reduces engagement among those whose preferences are not reflected. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    # Q1032
    (
        'Explanation: Need: guide and calm the team. Option B (Review the project charter to determine if the training is in scope and, if not, put in a change request.) fixes it."',
        'Explanation: Keywords: team training questions, project charter scope check, change request, training in scope. When stakeholders raise training needs and it is unclear whether training is within project scope, the project manager must first consult the project charter as the authoritative scope definition document. If training is not included, a change request is the correct mechanism to formally evaluate and approve its addition. (PMBOK Guide) – Seventh Edition, 2021, p. 50, \'Enable Change to Achieve the Envisioned Future State\'"'
    ),
    # Q1033
    (
        'Explanation: Need: guide and calm the team. Option C (Provide the team with virtual collaboration software and training on the software to minimize disruption,) fixes it."',
        'Explanation: Keywords: colocated performing team forced virtual, unforeseen dispersion, virtual tools, disruption minimization. When a high-performing colocated team is suddenly forced to work virtually, the project manager must equip them with virtual collaboration software and training to replicate as much of the colocated dynamic as possible. Providing the tools and the knowledge to use them effectively minimizes the performance disruption caused by the transition. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    # Q1034
    (
        'Explanation: Need: guide and calm the team. Option C (Storming) fixes it."',
        'Explanation: Keywords: Tuckman model, task discomfort, schedule challenges, storming phase. When team members are uncomfortable with their assignments and challenge scheduling decisions after initial task allocation, they are exhibiting the conflict and resistance that characterizes the storming phase of the Tuckman team development model. Recognizing this phase allows the project manager to apply appropriate leadership behaviors to help the team progress toward norming. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    # Q1035
    (
        'Explanation: Need: guide and calm the team. Option C (Mentor and coach the team to meet the project needs.) fixes it."',
        'Explanation: Keywords: retrospective reveals knowledge gap, iterative principles, third-party training insufficient, coaching intervention. When retrospective findings reveal that a recently completed training has left the team with gaps in iterative development knowledge, the project manager must supplement with direct mentoring and coaching tailored to the team\'s specific needs. Third-party training provides general knowledge; project-specific coaching bridges the gap between theory and actual project application. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    # Q1036
    (
        'Explanation: Need: guide and calm the team. Option B (Ensure the junior engineers make decisions within a certain responsibility level and commit to it,) fixes it."',
        'Explanation: Keywords: junior engineers deferring to seniors, decision avoidance, responsibility level empowerment, progress slowdown. When junior engineers consistently defer minor decisions to senior colleagues despite being capable, the project manager must empower them to own decisions within a defined responsibility boundary. Establishing clear decision-making authority removes the uncertainty that causes deferral and the slowdowns it creates. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    # Q1037
    (
        'Explanation: Need: guide and calm the team. Option A (Determined the appropriate type of incentive for key team members) fixes it."',
        'Explanation: Keywords: financial incentive ineffective, team still underperforming, motivation type mismatch, tailored incentive design. When financial rewards fail to improve team performance, it indicates the incentive type was not aligned with what actually motivates the team members. The project manager should have determined the appropriate form of recognition for each individual before distributing rewards, as one-size-fits-all incentives fail when team members are motivated by different factors. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    # Q1038 multi-select A,D
    (
        'Explanation: Need: listen to people needs. Options A and D (Schedule regular meetings with the key stakeholder to provide updates and receive feedback,; Promote an adaptive and transparent environment where the team can easily communicate with the stakeholders.) work together."',
        'Explanation: Keywords: stakeholder escalating directly to sponsor, bypassing project manager, engagement strategy, transparent communication environment. When a key stakeholder routes all communication through the sponsor rather than the project manager or team, the response must restore direct engagement through regular meetings and create an open environment where the team and stakeholder can interact naturally. Together these actions rebuild the stakeholder relationship and reduce the need for escalation. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    # Q1039 multi-select A,D
    (
        'Explanation: Need: listen to people needs. Options A and D (Keep the team engaged and focused on the project\'s direction.; Set a clear vision for the project and ensure it is visible to all stakeholders.) work together."',
        'Explanation: Keywords: past direction failures, team concern, project vision, sustained engagement. A team that previously experienced lack of direction needs both a clearly articulated vision and active efforts to keep them engaged and focused on that direction throughout execution. A visible vision alone is not sufficient — the project manager must also continuously reinforce it and monitor that the team remains aligned with the project\'s purpose. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
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
