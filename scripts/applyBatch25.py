MD_FILE = './src/imports/project-management-questions-1.md'

with open(MD_FILE, 'r', encoding='utf-8') as f:
    content = f.read()

replacements = [
    # Q1193
    (
        'Explanation: Need: control changes and baselines. Option B (Review the new requirements with the compliance department to determine if a change request is needed.) fixes it."',
        'Explanation: Keywords: regulatory compliance, mandatory changes, change request, compliance review. When a regulatory authority introduces mandatory requirements during project execution, the project manager cannot simply incorporate them without formal evaluation. Reviewing the new requirements with the compliance department and determining whether a change request is needed ensures that scope, schedule, and budget impacts are properly assessed and approved. (PMBOK Guide) – Seventh Edition, 2021, p. 50, \'Enable Change to Achieve the Envisioned Future State\'"'
    ),
    # Q1194
    (
        'Explanation: Need: listen to people needs. Option A (Discuss the issue with the virtual team members and revise the communications management plan.) fixes it."',
        'Explanation: Keywords: global project, virtual team, meeting attendance, communications management plan. When virtual team members cannot attend regular project update meetings, the communications management plan must be revised to find approaches that accommodate their constraints while maintaining adequate information flow. Discussing the issue directly with the affected team members identifies the root cause and ensures the revised plan is practical and actionable. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    # Q1195
    (
        'Explanation: Need: guide and calm the team. Option C (Communicate the project\'s impact and plans to engage the project team throughout the project.) fixes it."',
        'Explanation: Keywords: team pessimism, organizational change, project rationale, stakeholder engagement. When team members are pessimistic about a project because they lack context or are concerned about its broader impact, the project manager must proactively communicate the project\'s purpose, expected impact, and the plan for engaging the team throughout execution. Transparent leadership communication builds understanding and replaces uncertainty with a shared sense of direction. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    # Q1196
    (
        'Explanation: Need: listen to people needs. Option A (Update the communications matrix to ensure that client team member is included.) fixes it."',
        'Explanation: Keywords: communications matrix, missing stakeholder, client team member, recurring delays. When a stakeholder not listed in the communications plan is repeatedly causing delays due to a lack of understanding, the root cause is a gap in the communications management plan. Updating the communications matrix to include that stakeholder ensures they receive the appropriate information through proper channels, removing the recurring bottleneck. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    # Q1197
    (
        'Explanation: Need: listen to people needs. Option A (Talk to the customer and project team member separately to assess the issue and decide on the next steps.) fixes it."',
        'Explanation: Keywords: stakeholder conflict, team member, customer relationship, root cause assessment. When a customer requests the removal of a team member without explanation, the project manager must first understand the situation before taking action, particularly when the team member is critical to a key deliverable. Speaking separately with both the customer and the team member allows the project manager to assess the issue objectively and determine appropriate next steps. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    # Q1198
    (
        'Explanation: Need: protect benefits for users. Option C (Make the decision on which project approach to use that would best fit the project.) fixes it."',
        'Explanation: Keywords: hybrid delivery, PMO directive, functional manager concern, approach tailoring. When there is tension between organizational directives and functional manager preferences about delivery approach, the project manager must exercise judgment and select the approach that best fits the specific project. The project manager is ultimately responsible for project success and must tailor the approach based on context rather than defaulting to either stakeholder\'s preference. (PMBOK Guide) – Seventh Edition, 2021, p. 40, \'Tailor Based on Context\'"'
    ),
    # Q1199
    (
        'Explanation: Need: guide and calm the team. Option B (Implement a requirements traceability matrix.) fixes it."',
        'Explanation: Keywords: requirements traceability, business objectives, large project, value alignment. A requirements traceability matrix explicitly links each project requirement to the business and project objectives it supports, enabling the project manager to verify that all work being done is justified by a specific benefit. Implementing this matrix ensures transparency, prevents scope creep, and makes it clear when a requirement is not tied to any meaningful outcome. (PMBOK Guide) – Seventh Edition, 2021, p. 32, \'Focus on Value\'"'
    ),
    # Q1200
    (
        'Explanation: Need: guide and calm the team. Option A (Meet with the project team to develop a proper resolution to the issue.) fixes it."',
        'Explanation: Keywords: iteration delay, story completion, sprint planning, collaborative resolution. When an iteration is nearing its end and the team cannot complete all planned stories, the project manager\'s first step is to convene the team to collectively assess the situation and determine the most appropriate response. Team involvement ensures the solution is realistic, maintains morale, and aligns with the project\'s delivery commitments. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    # Q1201
    (
        'Explanation: Need: keep plans flexible. Option D (Submit the request to the project director for interim approval and include this approval for discussion at the next investment committee meeting.) fixes it."',
        'Explanation: Keywords: funding authorization, expedited schedule, interim approval, governance escalation. When formal committee approval cycles are too slow for an expedited project schedule, the project manager should seek interim authorization from the next level of governance to allow critical work to proceed. Including this approval for discussion at the next investment committee meeting ensures full transparency and governance compliance. (PMBOK Guide) – Seventh Edition, 2021, p. 50, \'Enable Change to Achieve the Envisioned Future State\'"'
    ),
    # Q1202
    (
        'Explanation: Need: listen to people needs. Option D (Determine the root cause of the misunderstandings, get all parties to reach a consensus, and help to implement the outcome.) fixes it."',
        'Explanation: Keywords: stakeholder conflict, construction project, root cause analysis, consensus building. When reemerging conflicts among stakeholders are stalling a project, the project manager must address the underlying causes rather than working around them. Determining the root cause of misunderstandings, facilitating stakeholder consensus, and helping implement the agreed outcome resolves the conflict at its source and enables the project to proceed with aligned parties. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    # Q1203
    (
        'Explanation: Need: guide and calm the team. Option B (Assess a mechanism for knowledge transfer among the team members.) fixes it."',
        'Explanation: Keywords: knowledge concentration, team member departure, knowledge transfer, project vulnerability. When a single team member holds most of the critical project knowledge and is leaving, the risk is not just losing a person but losing irreplaceable institutional knowledge. Assessing a knowledge transfer mechanism ensures that critical information is distributed across the team before the departure, reducing the project\'s vulnerability to key-person risk. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    # Q1204
    (
        'Explanation: Need: listen to people needs. Option A (Ensured that communications were sent to all stakeholders when requirements change) fixes it."',
        'Explanation: Keywords: requirements change, procurement mismatch, communication failure, stakeholder expectations. When project requirements change during execution, all relevant stakeholders — including the procurement team — must be informed promptly to prevent misalignment between what was originally ordered and what is now needed. The project manager should have ensured communications were sent to all stakeholders whenever requirements changed. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    # Q1205
    (
        'Explanation: Need: listen to people needs. Option B (Request a meeting with the stakeholder.) fixes it."',
        'Explanation: Keywords: stakeholder engagement, informal information flow, attendance gap, direct outreach. When a stakeholder is obtaining project information through informal channels rather than attending scheduled meetings, the project manager must address this by reaching out directly to the stakeholder. Requesting a meeting allows the project manager to understand constraints, introduce proper communication channels, and establish the engagement expected of them. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    # Q1206
    (
        'Explanation: Need: guide and calm the team. Option D (Prioritize the actions with the team, assign individuals who will be responsible for completion, and monitor progress.) fixes it."',
        'Explanation: Keywords: action items, workshop follow-up, accountability, task assignment. When a workshop generates follow-up action items, they must be systematically managed to ensure timely completion and project accountability. Prioritizing the actions with the team, assigning responsible individuals, and monitoring progress transforms workshop outputs into executed commitments rather than forgotten notes. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    # Q1207
    (
        'Explanation: Need: guide and calm the team. Option B (Collaborate with the team to arrive at team ground rules and publish the rules to the team.) fixes it."',
        'Explanation: Keywords: team forming stage, disruptive behavior, ground rules, team norming. Disruptive behavior during the forming stage is expected as team members test boundaries and establish norms. The most effective response is to collaboratively establish and publish team ground rules, creating shared expectations for conduct and giving the team a common framework for self-governance going forward. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    # Q1208
    (
        'Explanation: Need: listen to people needs. Option B (Request help from the project sponsor to get support from the sales agents.) fixes it."',
        'Explanation: Keywords: organizational change, resistance, sales agents, sponsor engagement. When end users resist a significant operational change, the project manager alone often lacks the organizational authority to overcome that resistance. Requesting support from the project sponsor — who has executive standing and relationships with the affected groups — is the most effective way to gain buy-in from stakeholders outside the project team\'s direct sphere of influence. (PMBOK Guide) – Seventh Edition, 2021, p. 50, \'Enable Change to Achieve the Envisioned Future State\'"'
    ),
    # Q1209
    (
        'Explanation: Need: listen to people needs. Option C (Request a new resource to execute the activities.) fixes it."',
        'Explanation: Keywords: performance management, repeated intervention, resource replacement, escalation exhausted. When multiple rounds of feedback, escalation, and formal support have failed to improve a team member\'s performance, continuing the same approach without result serves neither the project nor the team. Requesting a replacement resource is the appropriate action after all reasonable corrective measures have been exhausted. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    # Q1210
    (
        'Explanation: Need: listen to people needs. Option C (Ensure the team demonstrates product features to this customer regularly to collect feedback and improve as needed.) fixes it."',
        'Explanation: Keywords: agile quality, customer concern, feature demonstrations, iterative feedback. A customer unfamiliar with agile may equate its flexibility with a lack of quality control. Ensuring the team demonstrates product features regularly for the customer to review and provide feedback creates visible quality checkpoints, builds confidence, and incorporates customer input continuously throughout development. (PMBOK Guide) – Seventh Edition, 2021, p. 42, \'Build Quality into Processes and Deliverables\'"'
    ),
    # Q1211
    (
        'Explanation: Need: listen to people needs. Option C (Explore ways to share the project vision and outcome with the new sponsor.) fixes it."',
        'Explanation: Keywords: new sponsor, project continuity, vision sharing, stakeholder alignment. When a new project sponsor lacks enthusiasm for a project they have inherited, the project manager must proactively engage them by sharing the project\'s vision, benefits, and strategic value. Building the sponsor\'s understanding and conviction is essential for securing continued support and advocacy throughout the project. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    # Q1212
    (
        'Explanation: Need: listen to people needs. Option A (Personas) fixes it."',
        'Explanation: Keywords: user analysis, stakeholder types, personas, requirement elicitation. Personas are a structured technique for representing distinct user types based on shared characteristics, behaviors, and needs, making abstract user groups concrete and actionable. Using personas after an initial design workshop helps the team empathize with and design for the specific behaviors and expectations of each type of likely user. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    # Q1213
    (
        'Explanation: Need: listen to people needs. Option C (Explore if the materials could be supplied locally and obtained on time.) fixes it."',
        'Explanation: Keywords: supply chain disruption, global shipping delays, local sourcing, delivery risk. When a global supply chain disruption threatens the project timeline, the project manager must identify alternative pathways to obtain the required materials. Exploring whether the materials can be sourced locally and obtained within the needed timeframe is a pragmatic risk response that preserves delivery schedules without escalation or delay. (PMBOK Guide) – Seventh Edition, 2021, p. 34, \'Recognize, Evaluate, and Respond to System Interactions\'"'
    ),
    # Q1214
    (
        'Explanation: Need: listen to people needs. Option A (Assess the impact of the stakeholder and engage properly.) fixes it."',
        'Explanation: Keywords: resistant stakeholder, legacy ties, stakeholder analysis, proactive engagement. When a stakeholder with strong legacy ties objects to a project that affects their area, dismissing or avoiding them increases opposition and risk. Assessing the stakeholder\'s level of impact and engaging them appropriately addresses the resistance through the right channels and at the right intensity. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    # Q1215
    (
        'Explanation: Need: guide and calm the team. Option D (Coach the team member to pick up the challenging tasks.) fixes it."',
        'Explanation: Keywords: team member initiative, challenging tasks, servant leadership, coaching. Rather than simply assigning challenging tasks to the team member, a servant leader helps the team member develop the agency to select and claim those tasks themselves. Coaching the team member on how to identify and pick up challenging tasks builds self-confidence, initiative, and long-term professional growth. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    # Q1216
    (
        'Explanation: Need: watch risks early. Option C (Monitor the budget for the project continually and anticipate any issues if possible.) fixes it."',
        'Explanation: Keywords: tight budget, cost monitoring, budget risk, proactive management. When a project operates with a very tight budget and no room for cost overruns, the project manager must monitor the budget continuously to detect variances early before they become unrecoverable. Anticipating potential issues in advance allows corrective action to be taken while options still exist. (PMBOK Guide) – Seventh Edition, 2021, p. 46, \'Optimize Risk Responses\'"'
    ),
    # Q1217 multi-select
    (
        'Explanation: Need: guide and calm the team. Options B and D (Analyze the impact of the issue and submit a change request to update the project schedule.; Extend the project deadline and update the project schedule to reflect the delay.) work together."',
        'Explanation: Keywords: risk materialization, power outage, schedule delay, change request, formal documentation. When a risk materializes and causes a significant schedule delay, the project manager must both formally document the impact through a change request and update the project schedule to reflect the new reality. Both actions together ensure proper stakeholder approval, transparency, and an accurate baseline for future monitoring. (PMBOK Guide) – Seventh Edition, 2021, p. 34, \'Recognize, Evaluate, and Respond to System Interactions\'"'
    ),
    # Q1218
    (
        'Explanation: Need: guide and calm the team. Option A (Focus the discussion on recovery and ways to get back on track.) fixes it."',
        'Explanation: Keywords: bad news delivery, team morale, recovery focus, leadership response. When a team member raises difficult news about project performance, punishing or dismissing the messenger creates a culture of silence that harms the project. The project manager should acknowledge the information and immediately redirect the discussion toward recovery options, signaling that transparency is valued and problems are solvable. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    # Q1219
    (
        'Explanation: Need: listen to people needs. Option C (The product owner has evaluated the product against the definition of done (DoD).) fixes it."',
        'Explanation: Keywords: sprint review, product owner acceptance, definition of done, increment delivery. When a product owner declares an increment ready for delivery at a sprint review, this means they have evaluated the product against the agreed definition of done. The DoD is the team\'s shared quality standard, and the product owner\'s acceptance confirms that all criteria within it have been satisfied. (PMBOK Guide) – Seventh Edition, 2021, p. 42, \'Build Quality into Processes and Deliverables\'"'
    ),
    # Q1220
    (
        'Explanation: Need: listen to people needs. Option B (Meet with the stakeholder to understand what is causing the delays.) fixes it."',
        'Explanation: Keywords: stakeholder approval delay, new stakeholder, deliverable bottleneck, root cause. When a newly engaged stakeholder is holding up approvals without explanation, a direct conversation is required to understand the specific concerns or constraints driving the delays. Understanding the reason enables the project manager to address it effectively rather than escalating or bypassing the stakeholder. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    # Q1221
    (
        'Explanation: Need: listen to people needs. Option D (Negotiate a common agreement with the involved stakeholders regarding the requirements.) fixes it."',
        'Explanation: Keywords: conflicting requirements, stakeholder priorities, negotiation, consensus building. When stakeholders have requirements that directly conflict with each other, the project manager must bring the involved parties together to negotiate a common agreement rather than making a unilateral prioritization decision. A negotiated resolution builds joint ownership of the outcome and reduces the risk of future objections. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    # Q1222
    (
        'Explanation: Need: listen to people needs. Option C (Schedule regular project audits.) fixes it."',
        'Explanation: Keywords: cybersecurity compliance, regulatory adherence, project audits, compliance monitoring. Compliance with mandatory requirements cannot be verified retrospectively at project closeout. Scheduling regular project audits creates systematic checkpoints throughout execution that confirm adherence to cybersecurity requirements, enabling early detection and correction of deviations before they escalate into major violations. (PMBOK Guide) – Seventh Edition, 2021, p. 42, \'Build Quality into Processes and Deliverables\'"'
    ),
    # Q1223
    (
        'Explanation: Need: guide and calm the team. Option B (Create a risk register to identify, capture, review, and manage risks using a risk management process.) fixes it."',
        'Explanation: Keywords: agile risk management, risk register, risk identification, structured process. Even in an agile context, risks must be formally identified, captured, and managed throughout the project lifecycle. Creating a risk register and implementing a structured risk management process — regardless of the team\'s subjective risk assessment — provides a traceable, governed approach that can be reviewed and updated as the project evolves. (PMBOK Guide) – Seventh Edition, 2021, p. 46, \'Optimize Risk Responses\'"'
    ),
    # Q1224
    (
        'Explanation: Need: guide and calm the team. Option A (Foster knowledge sharing and coaching among team members.) fixes it."',
        'Explanation: Keywords: productivity gap, root cause analysis, knowledge sharing, coaching, internal learning. When a root cause analysis reveals that a knowledge gap in a specific framework is driving reduced productivity, the most targeted response is to facilitate knowledge sharing and coaching among team members with complementary expertise. This approach builds internal capability without external training costs and immediately begins closing the performance gap. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    # Q1225
    (
        'Explanation: Need: listen to people needs. Option C (Meet with the project sponsor to obtain more information.) fixes it."',
        'Explanation: Keywords: benefits management plan, organizational alignment, strategic vision, sponsor clarification. When it is unclear how a project\'s benefits align with the organization\'s strategic vision, the project sponsor — as the primary link between the project and organizational strategy — is the appropriate source of clarification. Meeting with the sponsor first ensures the benefits management plan is anchored in the correct strategic context before further planning proceeds. (PMBOK Guide) – Seventh Edition, 2021, p. 32, \'Focus on Value\'"'
    ),
    # Q1226
    (
        'Explanation: Need: guide and calm the team. Option B (Suggest that the team member facilitate an upcoming iteration and review the outcomes in the iteration retrospective.) fixes it."',
        'Explanation: Keywords: professional development, facilitation skills, servant leadership, experiential learning. A servant leader actively supports team members\' growth aspirations rather than deferring or redirecting them. Suggesting the team member facilitate an upcoming iteration provides a real, hands-on learning opportunity, and reviewing the outcomes in the retrospective creates a structured feedback loop for continuous improvement. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    # Q1227
    (
        'Explanation: Need: guide and calm the team. Option C (Set short-term goals in order to create a winning culture internally and praise team members for achieving them.) fixes it."',
        'Explanation: Keywords: new project manager, team direction, short-term goals, winning culture. When a team has been without a project manager and feels lost, the priority is to restore direction and confidence quickly. Setting short-term achievable goals creates early wins, demonstrates forward momentum, and rebuilds the team\'s sense of purpose and shared capability. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    # Q1228
    (
        'Explanation: Need: listen to people needs. Option D (Facilitate a stakeholder alignment session so that the team and project sponsor are in agreement with the deliverables.) fixes it."',
        'Explanation: Keywords: scope misalignment, sponsor understanding, stakeholder alignment, shared vision. When the project sponsor and team are operating with different interpretations of the project scope, a facilitated alignment session is required to surface and resolve the divergence directly. Bringing both parties to a shared understanding of deliverables prevents the misalignment from compounding as execution progresses. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    # Q1229
    (
        'Explanation: Need: listen to people needs. Option B (Listen carefully and show understanding of the growing needs of the functional manager.) fixes it."',
        'Explanation: Keywords: stakeholder dissatisfaction, active listening, emotional intelligence, escalating concern. When a functional manager who is also a key stakeholder expresses dissatisfaction during a status meeting, a defensive response is unlikely to resolve the underlying concern. The project manager should listen carefully and demonstrate understanding of the functional manager\'s growing needs, which creates space for constructive dialogue rather than conflict. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    # Q1230
    (
        'Explanation: Need: guide and calm the team. Option B (Encourage both team members to meet as soon as possible and resolve the problem) fixes it."',
        'Explanation: Keywords: team conflict, interpersonal friction, direct resolution, collaborative environment. When two team members are in conflict, the most effective resolution approach is direct dialogue between the parties involved. Encouraging them to meet and resolve the issue themselves respects their agency as professionals and is more likely to produce a durable resolution than escalation or avoidance. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    # Q1231
    (
        'Explanation: Need: listen to people needs. Option B (Specify the scope and features to be deployed in the contract clearly.) fixes it."',
        'Explanation: Keywords: customer expectations, contract clarity, scope definition, third-party management. When a customer is known to make frequent, specific requests and the project involves third parties, the most effective way to manage expectations is to define the scope and features to be delivered precisely in the contract from the outset. Clear contractual boundaries give all parties a shared reference point for evaluating and responding to requests. (PMBOK Guide) – Seventh Edition, 2021, p. 42, \'Build Quality into Processes and Deliverables\'"'
    ),
    # Q1232
    (
        'Explanation: Need: guide and calm the team. Option B (Establish the project scope and set clear team objectives.) fixes it."',
        'Explanation: Keywords: team formation, project scope, clear objectives, high-performing team. Before assembling and motivating a high-performing team, the project manager must establish a clear project scope and define what success looks like through specific team objectives. Without clear direction, even a capable team will lack the shared purpose and alignment needed to perform at their best. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    # Q1233
    (
        'Explanation: Need: listen to people needs. Option B (Foster an environment of open communication where all parties can discuss issues and agree on objectives.) fixes it."',
        'Explanation: Keywords: agile accountability, executive concern, open communication, stakeholder education. When a new executive stakeholder is concerned that agile lacks accountability, a collaborative approach to building understanding is more effective than prescribing formal approvals. Fostering an environment of open communication where all parties can discuss issues and agree on objectives demonstrates accountability through transparency rather than bureaucratic control. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    # Q1234
    (
        'Explanation: Need: listen to people needs. Option D (Encourage collaboration on a daily basis, facilitating different communication channels.) fixes it."',
        'Explanation: Keywords: hybrid project, daily collaboration, multiple communication channels, team awareness. In a hybrid project environment, ensuring all team members are informed about ongoing changes requires active facilitation of collaboration rather than passive distribution of information. Encouraging daily collaboration through multiple communication channels creates an environment where information flows naturally and changes are understood in real time. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    # Q1235
    (
        'Explanation: Need: guide and calm the team. Option B (Used bottom-up estimating) fixes it."',
        'Explanation: Keywords: cost performance, analogous estimating, bottom-up estimating, estimate accuracy. A CPI of 0.65 indicates significant cost overrun, often resulting from estimates that were too high-level to capture the detailed complexity of the work. Bottom-up estimating — which builds the estimate from individual work components upward — would have provided a more accurate and comprehensive cost baseline by accounting for specific resource needs at the task level. (PMBOK Guide) – Seventh Edition, 2021, p. 40, \'Tailor Based on Context\'"'
    ),
    # Q1236
    (
        'Explanation: Need: keep plans flexible. Option A (Speak directly with the resource.) fixes it."',
        'Explanation: Keywords: plan approval, resource resistance, direct communication, root cause. When a key resource refuses to approve the project plan without explanation, the most direct and respectful approach is to speak with them personally to understand the specific concerns driving the refusal. This conversation often reveals actionable feedback that can be addressed rather than a fundamental disagreement. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    # Q1237
    (
        'Explanation: Need: listen to people needs. Option A (Plan the project to deliver value incrementally with regular releases.) fixes it."',
        'Explanation: Keywords: incremental delivery, digital product, regular releases, agile value delivery. When a digital product requires ongoing customer feedback to refine features, the project must be structured to deliver value incrementally through regular releases rather than in a single final delivery. This approach accelerates value realization, creates feedback loops, and reduces the risk of building features that miss the mark. (PMBOK Guide) – Seventh Edition, 2021, p. 32, \'Focus on Value\'"'
    ),
    # Q1238
    (
        'Explanation: Need: guide and calm the team. Option B (Add an experienced professional to the team to reinforce knowledge sharing and help grow team expertise in the new product) fixes it."',
        'Explanation: Keywords: skill gap, robotic interfaces, knowledge sharing, team capability building. When a team lacks expertise in a critical technology and is motivated to learn, adding an experienced professional creates a knowledge-sharing environment that grows internal capability over time. This approach avoids the risks of outsourcing the work entirely while building expertise that benefits the team beyond the current project. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    # Q1239
    (
        'Explanation: Need: listen to people needs. Option A (Ensure the change management plan highlights this requirement to prevent future issues.) fixes it."',
        'Explanation: Keywords: lessons learned, client change review, change management plan, stakeholder requirement. When historical lessons learned reveal that a specific stakeholder consistently demands involvement in all changes — even those outside the contract — the project manager should document this as a requirement in the change management plan for future projects. Proactively incorporating this expectation prevents conflicts from arising during execution. (PMBOK Guide) – Seventh Edition, 2021, p. 50, \'Enable Change to Achieve the Envisioned Future State\'"'
    ),
    # Q1240
    (
        'Explanation: Need: listen to people needs. Option D (Reassess continually to remove blockers for the team.) fixes it."',
        'Explanation: Keywords: contractor constraint, virtual team, communication gap, continuous reassessment. When unforeseen constraints force a virtual approach and communication gaps begin affecting performance, the project manager must continuously reassess the situation to identify and remove barriers that are impeding the team. This adaptive approach acknowledges that the operating environment is dynamic and requires ongoing intervention rather than a single corrective action. (PMBOK Guide) – Seventh Edition, 2021, p. 44, \'Navigate Complexity\'"'
    ),
    # Q1241
    (
        'Explanation: Need: guide and calm the team. Option B (Explain that the team is fully dedicated to the current sprint activities and negotiate a mutually agreeable time.) fixes it."',
        'Explanation: Keywords: sprint commitment, quality workshops, negotiation, functional manager request. When a functional manager makes an urgent request that conflicts with the team\'s current sprint commitments, the project manager must protect the team\'s focus while honoring the legitimate need. Explaining the current sprint commitment and negotiating a mutually agreeable time demonstrates respect for both the sprint process and the functional manager\'s concern. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    # Q1242
    (
        'Explanation: Need: guide and calm the team. Option D (Assess the team member\'s commitment to the master\'s program and its impact on project performance.) fixes it."',
        'Explanation: Keywords: team member development, master\'s program, project impact assessment, timing conflict. When a key team member\'s enrollment in an educational program overlaps with a critical project phase, the project manager must understand the specific implications for project performance before responding. Assessing the team member\'s commitment level and the realistic impact on their work provides the information needed to make an informed decision about adjustments. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
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
