MD_FILE = './src/imports/project-management-questions-1.md'

with open(MD_FILE, 'r', encoding='utf-8') as f:
    content = f.read()

replacements = [
    # Q1143
    (
        'Explanation: Need: guide and calm the team. Option B (Share project updates through regular community meetings.) fixes it."',
        'Explanation: Keywords: community health project, stakeholder updates, regular meetings, progress sharing. When managing a community-oriented project, stakeholders must receive regular, accessible updates to remain engaged and informed. Scheduling consistent community meetings ensures project progress is shared proactively, builds trust, and allows community members to raise concerns early. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    # Q1144 - ASCII apostrophe in stakeholder's
    (
        'Explanation: Need: listen to people needs. Option D (Review this stakeholder\'s communication requirements.) fixes it."',
        'Explanation: Keywords: stakeholder bypass, team distraction, communication requirements, status requests. When a stakeholder repeatedly contacts team members directly for updates, the root cause is typically a gap in the communications management plan that fails to meet their information needs. The project manager should review that stakeholder\'s communication requirements and update the plan so their needs are addressed through proper channels. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    # Q1145
    (
        'Explanation: Need: listen to people needs. Option B (Implement short cycles for inspection and provide feedback.) fixes it."',
        'Explanation: Keywords: stakeholder hesitancy, servant leader, uncertainty, short cycles, feedback loops. Even when no current issues or risks are evident, stakeholder hesitancy signals that trust needs to be built through demonstrated progress. Implementing short inspection cycles with regular feedback creates visible checkpoints that reassure the stakeholder and surface any emerging concerns before they escalate. (PMBOK Guide) – Seventh Edition, 2021, p. 48, \'Embrace Adaptability and Resiliency\'"'
    ),
    # Q1146
    (
        'Explanation: Need: keep plans flexible. Option D (Behind schedule) fixes it."',
        'Explanation: Keywords: schedule variance, negative SV, earned value management, project status. In earned value management, a negative schedule variance indicates the project has accomplished less work than planned by this point in time, meaning it is behind schedule. This status holds true regardless of cost performance or quality outcomes — the schedule metric stands independently. (PMBOK Guide) – Seventh Edition, 2021, p. 34, \'Recognize, Evaluate, and Respond to System Interactions\'"'
    ),
    # Q1147
    (
        'Explanation: Need: listen to people needs. Option B (Add collaboration tools to the communications management plan.) fixes it."',
        'Explanation: Keywords: distributed team, virtual communication, health protocol changes, collaboration tools. When a team shifts to a new communication mode due to external circumstances, the communications management plan must be updated to reflect the tools and methods that support the new reality. Adding collaboration tools ensures that both colocated and remote team members can maintain effective communication and shared understanding. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    # Q1148
    (
        'Explanation: Need: listen to people needs. Option C (Draft a contract change with the desired scope changes and send it to the client for approval.) fixes it."',
        'Explanation: Keywords: T&M contract, client dissatisfaction, scope change, hybrid approach, contract amendment. In a time and materials engagement, when client requirements change significantly, the appropriate response is to formalize those changes through a contract amendment. Drafting a contract change with the newly desired scope and sending it for client approval ensures both parties have a mutual understanding and that changes are legally and commercially protected. (PMBOK Guide) – Seventh Edition, 2021, p. 50, \'Enable Change to Achieve the Envisioned Future State\'"'
    ),
    # Q1149
    (
        'Explanation: Need: listen to people needs. Option C (Negotiate a mutually agreeable feedback cycle with acceptable timelines.) fixes it."',
        'Explanation: Keywords: communication overload, multi-channel demands, peer relationship, feedback cycle negotiation. When peers have conflicting expectations around communication frequency and responsiveness, the most productive path is direct negotiation to establish a mutually acceptable feedback cycle. This preserves the working relationship while setting clear boundaries that protect productivity on both sides. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    # Q1150
    (
        'Explanation: Need: watch risks early. Option D (Review the procurement contract and ask the supplier to negotiate a solution.) fixes it."',
        'Explanation: Keywords: supplier defect, contract dispute, procurement management, negotiation. Before escalating or canceling a contract, the project manager should review the actual procurement terms to clarify what was agreed and then engage the supplier in a solution-focused negotiation. This approach protects the project\'s interest while preserving the supplier relationship and avoiding the delays that contract cancellation would create. (PMBOK Guide) – Seventh Edition, 2021, p. 34, \'Recognize, Evaluate, and Respond to System Interactions\'"'
    ),
    # Q1151
    (
        'Explanation: Need: watch risks early. Option B (Discuss the issue with the engineer and determine how to prevent another problem.) fixes it."',
        'Explanation: Keywords: redo loop, documentation gap, vendor clarity, root cause, quality prevention. When a redo loop occurs due to an unclear document, the priority is to close the immediate gap and prevent recurrence. The project manager should discuss the issue with the responsible engineer to understand what was missed and determine preventive measures for future similar tasks. (PMBOK Guide) – Seventh Edition, 2021, p. 42, \'Build Quality into Processes and Deliverables\'"'
    ),
    # Q1152
    (
        'Explanation: Need: guide and calm the team. Option C (Observed and assessed the competencies and skills of the team members and analyzed the training material beforehand) fixes it."',
        'Explanation: Keywords: training mismatch, competency assessment, training planning, skills gap. Effective training requires understanding both the current competency level of team members and the difficulty of the training material before enrollment. The project manager should have assessed team members\' skills and reviewed the course content to ensure alignment, preventing the mismatch that led to frustration and wasted effort. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    # Q1153
    (
        'Explanation: Need: guide and calm the team. Option D (Let the new team member know that even if they know the answer, it is better to give the team a chance to solve their own problems) fixes it."',
        'Explanation: Keywords: SME integration, team self-organization, servant leadership, agile empowerment. In an agile environment, the team\'s ability to self-organize and solve problems is a core strength that builds capability and morale over time. Even when a team member knows the answer, encouraging the team to work through challenges themselves fosters independence, shared ownership, and continuous learning. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    # Q1154
    (
        'Explanation: Need: listen to people needs. Option C (Check the organizational process assets (OPAs).) fixes it."',
        'Explanation: Keywords: newly assigned PM, defect resolution, organizational process assets, lessons learned. When a project encounters a recurring defect and the team that built the original system is no longer available, organizational process assets — including historical records, lessons learned, and documented solutions from similar projects — are the first source of institutional knowledge to consult. (PMBOK Guide) – Seventh Edition, 2021, p. 48, \'Embrace Adaptability and Resiliency\'"'
    ),
    # Q1155
    (
        'Explanation: Need: guide and calm the team. Option D (Use a formal approach using procurement policies, procedures, forms, and work instructions.) fixes it."',
        'Explanation: Keywords: vendor engagement, Scrum, procurement process, organizational policies. Even in an agile environment, engaging a new vendor requires following the organization\'s established procurement policies, procedures, and documentation to ensure compliance, fair selection, and contractual protection. The PMO\'s support for agile does not override the need for proper procurement governance when selecting external suppliers. (PMBOK Guide) – Seventh Edition, 2021, p. 25, \'Be a Diligent, Respectful, and Caring Steward\'"'
    ),
    # Q1156
    (
        'Explanation: Need: listen to people needs. Option C (Include stakeholders in the weekly status meetings with the team.) fixes it."',
        'Explanation: Keywords: communications gap, stakeholder inclusion, status meetings, information delivery. When stakeholders confirm they are not receiving updates despite regular reports being sent, the delivery method is clearly not reaching them effectively. Including stakeholders directly in weekly status meetings ensures they receive information in real time through an interactive format that promotes understanding and engagement. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    # Q1157
    (
        'Explanation: Need: guide and calm the team. Option D (Allocate time within the iterations to mentor the new team member.) fixes it."',
        'Explanation: Keywords: new team member onboarding, schedule impact, mentoring, iterative delivery. When a new team member lacks familiarity with team processes and is disrupting delivery, the most constructive response is to invest in their integration through dedicated mentoring time within the iteration. This protects long-term team performance while building the new member\'s capabilities in context. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    # Q1158
    (
        'Explanation: Need: listen to people needs. Option C (Hold a brainstorming session to identify the root cause of the complaints.) fixes it."',
        'Explanation: Keywords: customer complaints, stability issues, root cause analysis, gap between perception and reality. When the customer\'s experience contradicts the team\'s assessment of stability, there is a gap that must be investigated rather than dismissed. A brainstorming session allows the team to collectively examine both the technical and communication dimensions driving the customer\'s concerns. (PMBOK Guide) – Seventh Edition, 2021, p. 42, \'Build Quality into Processes and Deliverables\'"'
    ),
    # Q1159
    (
        'Explanation: Need: guide and calm the team. Option C (Understand what the team member wants and find possible opportunities to address it.) fixes it."',
        'Explanation: Keywords: team conflict, defiance, experienced member, servant leadership, root cause. When an experienced, high-performing team member consistently challenges the project manager\'s decisions, addressing the surface behavior alone is unlikely to resolve the underlying tension. The project manager should seek to understand the team member\'s perspective and motivations to find opportunities that address their legitimate concerns and rebuild alignment. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    # Q1160 multi-select
    (
        'Explanation: Need: keep plans flexible. Options B and E (The junior project manager can discuss certain problems with their mentor without fear of retribution.; The mentor can provide past project documentation with early warning indicators that potential problems could occur.) work together."',
        'Explanation: Keywords: mentoring relationship, junior project manager, safe space, organizational knowledge. A mentoring relationship creates a confidential space where the junior project manager can surface concerns and challenges without fear of formal consequences, which is critical for learning. Additionally, a mentor\'s access to historical project documentation and early warning patterns provides the junior PM with evidence-based foresight that cannot be replicated from a classroom alone. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    # Q1161
    (
        'Explanation: Need: watch risks early. Option A (Organize a sprint retrospective and discuss the issues and how they can be avoided in the next sprint.) fixes it."',
        'Explanation: Keywords: agile transition, sprint review failure, product owner rejection, retrospective. When a product owner does not accept the sprint results, a retrospective is the appropriate forum to examine what went wrong and how the team can adjust for the next sprint. This process of inspect-and-adapt is fundamental to agile improvement and prevents the same issues from recurring across subsequent iterations. (PMBOK Guide) – Seventh Edition, 2021, p. 48, \'Embrace Adaptability and Resiliency\'"'
    ),
    # Q1162
    (
        'Explanation: Need: guide and calm the team. Option D (Meet with the development team to review and assess the requirements specifications.) fixes it."',
        'Explanation: Keywords: missing requirements, prototype review, design phase, requirements assessment. When requirements specifications are found to be missing mid-project, the project manager must first understand the scope and impact of the gap before taking corrective action. Meeting with the development team to review and assess the missing specifications ensures the response is proportionate, informed, and aligned with project objectives. (PMBOK Guide) – Seventh Edition, 2021, p. 42, \'Build Quality into Processes and Deliverables\'"'
    ),
    # Q1163
    (
        'Explanation: Need: listen to people needs. Option D (Develop a standard for document quality control.) fixes it."',
        'Explanation: Keywords: documentation error, quality standards, technical writing, quality control process. A single occurrence of erroneous references in project documentation signals the absence of a systematic quality control process for deliverables. Developing a standard for document quality control creates a repeatable mechanism that prevents similar errors across all future project documents. (PMBOK Guide) – Seventh Edition, 2021, p. 42, \'Build Quality into Processes and Deliverables\'"'
    ),
    # Q1164
    (
        'Explanation: Need: listen to people needs. Option D (Request that the project team develop a release plan and roadmap for the project.) fixes it."',
        'Explanation: Keywords: large-scale innovation, stakeholder expectations, release planning, roadmap. Before a large and complex project begins, stakeholders need a structured view of how value will be delivered incrementally and what the path to the final product looks like. Developing a release plan and roadmap provides this clarity, aligning business expectations with the delivery approach from the outset. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    # Q1165
    (
        'Explanation: Need: listen to people needs. Option B (Defined the appropriate recipients for the report in the communications management plan) fixes it."',
        'Explanation: Keywords: data privacy, communications management, sensitive report, recipient definition. A well-designed communications management plan explicitly defines which stakeholders receive which types of reports, preventing sensitive information from reaching unintended audiences. The project manager should have identified the appropriate recipients for each report type — especially confidential HR data — as part of the communications planning process. (PMBOK Guide) – Seventh Edition, 2021, p. 25, \'Be a Diligent, Respectful, and Caring Steward\'"'
    ),
    # Q1166
    (
        'Explanation: Need: guide and calm the team. Option C (Update the issue log with the status and priority.) fixes it."',
        'Explanation: Keywords: technical impediment, issue escalation, issue log, status tracking. When a technical issue persists beyond initial resolution efforts and is impacting deliverables, the project manager must ensure it is properly documented in the issue log with its current status and priority to maintain visibility and drive accountability. This positions the issue for appropriate escalation if it remains unresolved. (PMBOK Guide) – Seventh Edition, 2021, p. 34, \'Recognize, Evaluate, and Respond to System Interactions\'"'
    ),
    # Q1167
    (
        "Explanation: Need: keep plans flexible. Option C (Capture the risk in the risk register and monitor it to prevent it from becoming an issue by taking the proper response action.) fixes it.\"",
        "Explanation: Keywords: schedule risk, risk register, risk response, go-live delay. When a project faces a potential schedule delay, the appropriate risk management response is to formally document the risk in the risk register and initiate monitoring with a planned response action. This ensures the threat is tracked and addressed proactively before it becomes an issue that forces a reactive schedule change. (PMBOK Guide) – Seventh Edition, 2021, p. 46, 'Optimize Risk Responses'\""
    ),
    # Q1168
    (
        'Explanation: Need: keep plans flexible. Option A (Prioritize which backlog activities should be kept.) fixes it."',
        'Explanation: Keywords: backlog overload, fixed budget, aggressive timeline, backlog prioritization. With an aggressive timeline and a fixed budget, completing all backlog items is not feasible and the team must focus on items that deliver the most value within constraints. Prioritizing which backlog activities to retain ensures that limited capacity is directed toward the highest-impact work. (PMBOK Guide) – Seventh Edition, 2021, p. 32, \'Focus on Value\'"'
    ),
    # Q1169
    (
        'Explanation: Need: listen to people needs. Option A (Review the requirements of the report with the team member to redefine its purpose.) fixes it."',
        'Explanation: Keywords: reporting resistance, report purpose, team engagement, communication planning. When a team member pushes back on a reporting requirement, dismissing or escalating the concern bypasses a legitimate opportunity to improve the communication process. Reviewing the report\'s purpose and requirements collaboratively with the team member may produce a more effective, better-targeted report that they are willing to prepare. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    # Q1170
    (
        'Explanation: Need: guide and calm the team. Option A (Study and determine the appropriate leadership style suitable for the team.) fixes it."',
        'Explanation: Keywords: new project manager, underperformance, leadership style, team assessment. Different teams require different leadership approaches depending on their maturity, motivation, and context. Before making changes, the project manager should study and determine the leadership style most appropriate for this team — adapting their approach rather than imposing a default style is the foundation for improving performance and engagement. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    # Q1171
    (
        'Explanation: Need: listen to people needs. Option C (Make documentation a standard part of the definition of done (DoD).) fixes it."',
        'Explanation: Keywords: documentation gap, agile, definition of done, quality standard. In an agile environment, the definition of done is the team\'s quality contract for each deliverable. Making documentation a standard component of the DoD ensures it is completed with each increment rather than deferred, embedding quality into the delivery process rather than treating it as an afterthought. (PMBOK Guide) – Seventh Edition, 2021, p. 42, \'Build Quality into Processes and Deliverables\'"'
    ),
    # Q1172
    (
        'Explanation: Need: listen to people needs. Option B (Work with the project team to evaluate the potential delay.) fixes it."',
        'Explanation: Keywords: potential delay, client communication, team assessment, proactive communication. Before communicating a potential delay to a client, the project manager must first work with the team to evaluate the actual extent and likelihood of the delay. Sharing unverified concerns could alarm the client unnecessarily, while a clear assessment with proposed solutions enables a more credible and constructive conversation. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    # Q1173
    (
        'Explanation: Need: protect value and acceptance. Option D (Assess the influence and power of the employee to see if the employee will add value.) fixes it."',
        'Explanation: Keywords: stakeholder analysis, employee influence, salience, power-interest assessment. A newly identified stakeholder whose role and influence on the project are unclear requires a structured assessment before their request is acted upon. By assessing the employee\'s influence and power, the project manager can determine whether engaging them will add value to the project or introduce unnecessary scope and governance complexity. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    # Q1174
    (
        'Explanation: Need: listen to people needs. Option C (Monitor Risks, to install system performance monitoring tools and update the risk register) fixes it."',
        'Explanation: Keywords: UAT defect, system performance risk, risk monitoring, risk register update. When a known risk materializes into an actual defect during testing, the project manager should shift to the Monitor Risks process to track the evolving situation, implement performance monitoring mechanisms, and update the risk register to reflect the current state and any revised response plan. (PMBOK Guide) – Seventh Edition, 2021, p. 46, \'Optimize Risk Responses\'"'
    ),
    # Q1175
    (
        'Explanation: Need: listen to people needs. Option C (Complete development for the must-have functionalities only prior to demonstration in order to fail fast and get early feedback.) fixes it."',
        'Explanation: Keywords: hybrid project, market uncertainty, MVP, fail fast, incremental delivery. When a product\'s market acceptance is uncertain, delivering all functionalities before testing the market is a costly gamble. Completing only the must-have functionalities and demonstrating them early allows the team to gather real feedback quickly, enabling pivots before significant investment is sunk into features that may not resonate. (PMBOK Guide) – Seventh Edition, 2021, p. 32, \'Focus on Value\'"'
    ),
    # Q1176
    (
        'Explanation: Need: guide and calm the team. Option B (Meet with the project team to collaboratively determine how the project manager can ensure the needed testing assistance is obtained.) fixes it."',
        'Explanation: Keywords: resource constraint, testing support, matrix organization, collaborative problem-solving. When a key functional resource is unavailable and testing support is uncertain, the project manager should involve the project team in collaboratively identifying how to secure the needed assistance. The team closest to the work often has the best insight into alternative approaches, and involving them builds shared ownership of the solution. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    # Q1177
    (
        'Explanation: Need: listen to people needs. Option D (Schedule a meeting to discuss the different perspectives and agree on a decision.) fixes it."',
        'Explanation: Keywords: role clarification, program management, expectations alignment, collaborative resolution. When two parties have differing interpretations of roles and responsibilities, unilateral decisions or written responses are rarely effective. Scheduling a meeting to discuss both perspectives and reach a shared agreement ensures clarity, preserves the working relationship, and establishes a clear operating model going forward. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    # Q1178
    (
        'Explanation: Need: keep plans flexible. Option B (Assign the unallocated tasks to the functional role and then reallocate when the resources are available.) fixes it."',
        'Explanation: Keywords: resource assignment, hybrid project, functional role placeholder, WBS. When specific resources cannot be immediately assigned to project tasks, using functional roles as placeholders maintains schedule integrity and allows planning to progress without delay. Resources can be reallocated to named individuals when they become available, preserving the project plan\'s structure in the interim. (PMBOK Guide) – Seventh Edition, 2021, p. 40, \'Tailor Based on Context\'"'
    ),
    # Q1179
    (
        'Explanation: Need: listen to people needs. Option B (Meet with these stakeholders to review the project charter.) fixes it."',
        'Explanation: Keywords: stakeholder awareness gap, deliverable clarity, project charter, senior manager alignment. When senior stakeholders claim ignorance of a key deliverable, the project manager should meet with them directly to review the project charter, which serves as the foundational agreement about project scope and deliverables. This meeting will either clarify a misunderstanding or reveal a charter gap that needs to be addressed. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    # Q1180
    (
        'Explanation: Need: guide and calm the team. Option B (Create a new item in the sprint backlog to determine the appropriate algorithm.) fixes it."',
        'Explanation: Keywords: technical uncertainty, sprint planning, spike, algorithm selection, backlog item. When the team cannot determine the most efficient algorithm without investigative work, the appropriate agile response is to create a dedicated backlog item — often called a spike — to conduct the research. This keeps the sprint focused and ensures the decision is made with evidence rather than assumptions. (PMBOK Guide) – Seventh Edition, 2021, p. 40, \'Tailor Based on Context\'"'
    ),
    # Q1181
    (
        'Explanation: Need: guide and calm the team. Option A (Set up a proper governance structure to ensure functional managers\' requests are processed correctly.) fixes it."',
        'Explanation: Keywords: scope creep, governance, change control, functional manager interference. When functional managers add requirements outside the formal change process and team members accommodate them directly, the project\'s scope baseline is at risk. Establishing a proper governance structure ensures all requests are routed through the change control process, protecting the schedule and cost baselines while maintaining transparency. (PMBOK Guide) – Seventh Edition, 2021, p. 50, \'Enable Change to Achieve the Envisioned Future State\'"'
    ),
    # Q1182
    (
        'Explanation: Need: listen to people needs. Option A (Provide an overview of the completed functionalities and release plan, and capture expectations for future stakeholder involvement.) fixes it."',
        'Explanation: Keywords: stakeholder interest, product owner support, release plan overview, expectation capture. When stakeholders express interest in the project and the product owner seeks guidance, the project manager should recommend providing a structured overview of completed functionalities and the release plan. This gives stakeholders meaningful context while capturing their expectations, which feeds back into the engagement strategy. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    # Q1183
    (
        'Explanation: Need: listen to people needs. Option B (Include project stakeholder expectations and needs while creating project acceptance criteria.) fixes it."',
        'Explanation: Keywords: acceptance criteria, stakeholder expectations, requirements alignment, deliverable quality. Acceptance criteria disconnected from stakeholder needs create the risk of producing technically correct deliverables that stakeholders will not accept. Including stakeholder expectations and needs when defining acceptance criteria ensures that both the project team and stakeholders share a common definition of success for each deliverable. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    # Q1184 - ASCII apostrophe in technology's
    (
        'Explanation: Need: guide and calm the team. Option A (Use retrospectives to better understand the new technology\'s impact on the schedule, map the skill gaps, and adjust the team accordingly.) fixes it."',
        'Explanation: Keywords: velocity decrease, new technology, skill gap, retrospective, team adaptation. When a team\'s velocity drops due to unfamiliar technology, the retrospective is the right forum to understand the full schedule impact, identify specific knowledge gaps, and agree on adjustments such as training or pairing. This data-driven approach allows the team to recover deliberately rather than through trial and error. (PMBOK Guide) – Seventh Edition, 2021, p. 48, \'Embrace Adaptability and Resiliency\'"'
    ),
    # Q1185
    (
        'Explanation: Need: listen to people needs. Option C (Ask the customer to work with the product owner to prioritize all requests.) fixes it."',
        'Explanation: Keywords: customer pressure, backlog management, product owner role, prioritization. In an agile project, the product owner is responsible for managing and prioritizing the backlog to reflect value and constraints. Directing the customer to work with the product owner ensures that new requests are properly evaluated and sequenced rather than being injected directly by the customer. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    # Q1186
    (
        'Explanation: Need: guide and calm the team. Option C (Have a meeting with the resource to understand the issue.) fixes it."',
        'Explanation: Keywords: team retention, last iteration, key resource, understanding root cause. When a key team member signals their intention to leave at a critical stage of the project, the project manager\'s first step is to understand the underlying reason through a direct conversation. Without knowing the root cause, any response — whether reassignment, incentives, or requesting a replacement — risks being misdirected. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    # Q1187
    (
        'Explanation: Need: guide and calm the team. Option B (Hold virtual daily standups each workday morning and use collaboration tools to manage project updates.) fixes it."',
        'Explanation: Keywords: remote work, virtual standup, daily meetings, collaboration tools, communication continuity. When in-person meetings are no longer possible, the project manager must adapt the communication approach rather than abandon the meeting cadence. Holding virtual daily standups using collaboration tools maintains the team\'s shared awareness and coordination while complying with management\'s directive. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    # Q1188
    (
        'Explanation: Need: guide and calm the team. Option B (Organize knowledge-sharing workshops and ask one of the senior team members to facilitate them.) fixes it."',
        'Explanation: Keywords: knowledge transfer, distributed team, skills sharing, retrospective action. When new team members raise knowledge transfer gaps in a retrospective, the team has collectively identified an impediment that requires a structured response. Organizing knowledge-sharing workshops led by experienced team members addresses the root cause, builds shared understanding, and reduces the team\'s dependence on individual expertise. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    # Q1189
    (
        'Explanation: Need: keep plans flexible. Option C (Start the organization\'s change control process via a change request.) fixes it."',
        'Explanation: Keywords: scope change, regulatory requirement, permit, change control, change request. When a regulatory authority introduces a requirement not included in the current project scope, the project manager cannot simply add it to the plan without formal evaluation. Initiating the change control process ensures the new work is assessed for impact on schedule, cost, and risk, and that stakeholders approve the scope change through proper governance. (PMBOK Guide) – Seventh Edition, 2021, p. 50, \'Enable Change to Achieve the Envisioned Future State\'"'
    ),
    # Q1190
    (
        'Explanation: Need: listen to people needs. Option C (Consult the communications management plan.) fixes it."',
        'Explanation: Keywords: mid-project assignment, dependency management, communications plan, stakeholder information. When a newly assigned project manager observes that the team is not being kept informed of changes that affect them, the first step is to consult the existing communications management plan. This reveals what communication commitments exist and where current practice is falling short, informing targeted corrective action. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    # Q1191
    (
        'Explanation: Need: listen to people needs. Option B (Recommend the team member for effective communication training and support their career development interests.) fixes it."',
        'Explanation: Keywords: career development, communication skills gap, leadership aspiration, coaching. A project manager who observes a gap between a team member\'s aspirations and their current capabilities has an opportunity to invest in that team member\'s growth. Recommending targeted communication training while supporting their career interest demonstrates servant leadership and helps the team member build the skills needed to succeed in their desired role. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    # Q1192
    (
        'Explanation: Need: listen to people needs. Option A (Arrange a meeting with the project team member and project sponsor to discuss the change and obtain consensus.) fixes it."',
        'Explanation: Keywords: governance conflict, sponsor challenge, three-way alignment, change management. When a governance change creates conflict that reaches the project sponsor through a team member\'s complaint, the project manager must address it inclusively rather than defensively. Arranging a meeting with both the team member and the sponsor creates a space where the rationale for the change can be explained, concerns can be heard, and consensus can be built. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
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
