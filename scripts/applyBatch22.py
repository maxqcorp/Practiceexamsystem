MD_FILE = './src/imports/project-management-questions-1.md'

with open(MD_FILE, 'r', encoding='utf-8') as f:
    content = f.read()

replacements = [
    # Q1040 multi-select A,B,C
    (
        'Explanation: Need: listen to people needs. Options A, B, and C (Prioritize stakeholders based on the project phase and need.; Develop a stakeholder impact influence matrix to determine the level of engagement; Perform a stakeholder assessment to align with the project objectives.) work together."',
        'Explanation: Keywords: multiyear project, new stakeholders joining, stakeholder engagement planning, impact-influence analysis. As new stakeholders express interest in a long-running project, the project manager must prioritize them by phase and need, map their impact and influence to determine appropriate engagement levels, and conduct a stakeholder assessment to align their involvement with project objectives. Together these three actions create a structured and strategic approach to expanding stakeholder engagement without overwhelming the project with undifferentiated involvement. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    # Q1041
    (
        'Explanation: Need: guide and calm the team. Option B (Assess the impact of a possible delay to the project and encourage the team to take the work if the impact is tolerable.) fixes it."',
        'Explanation: Keywords: specialized work outside team competence, agile team, impact assessment, acceptable risk tolerance. When a team is willing to take on specialized work outside their core expertise, the project manager should assess the potential delay impact rather than immediately routing to another team. If the impact is within tolerable limits, empowering the team to attempt the work builds capability and avoids the coordination overhead of cross-team handoffs. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    # Q1042
    (
        'Explanation: Need: listen to people needs. Option B (The project is under budget and on schedule.) fixes it."',
        'Explanation: Keywords: agile EVM, story points delivered, planned versus actual cost, earned value analysis. With 50 of 100 user stories delivered (50% complete) at a cost of US$2,000, and each story worth US$50 (total project value US$5,000), the earned value is US$2,500. Since actual cost (US$2,000) is less than earned value (US$2,500), the project is under budget, and since 50 stories are planned to be complete at this point and 50 are delivered, the project is on schedule. (PMBOK Guide) – Seventh Edition, 2021, p. 32, \'Focus on Value\'"'
    ),
    # Q1043
    (
        'Explanation: Need: guide and calm the team. Option D (Add construction productivity to the risk register and develop a mitigation strategy for site execution) fixes it."',
        'Explanation: Keywords: lessons learned, low construction productivity risk, risk register entry, proactive mitigation. When lessons learned from a related project identify low construction productivity as a potential delay risk, the project manager must formally register this as a risk and develop a mitigation strategy during initiation — before it can impact project execution. Proactive risk registration translates organizational knowledge into protective action. (PMBOK Guide) – Seventh Edition, 2021, p. 46, \'Optimize Risk Responses\'"'
    ),
    # Q1044 multi-select C,E
    (
        'Explanation: Need: guide and calm the team. Options C and E (Analyze the business benefits criteria and assumptions; Schedule a project review meeting to analyze the root cause) work together."',
        'Explanation: Keywords: post-delivery revenue shortfall, business case gap, benefits criteria analysis, root cause review. When a delivered product fails to meet the incremental revenue targets defined in the business case, the project manager must analyze the benefits criteria and underlying assumptions to understand where the gap originated, and then convene a review meeting to diagnose the root cause. Together these actions produce the evidence needed to inform a corrective strategy without premature escalation. (PMBOK Guide) – Seventh Edition, 2021, p. 32, \'Focus on Value\'"'
    ),
    # Q1045
    (
        'Explanation: Need: listen to people needs. Option D (Collaborate with the team to assess the impact of the change on the project and recommend an updated project plan) fixes it."',
        'Explanation: Keywords: new sponsor budget cuts, servant leader, team collaboration, updated project plan. As a servant leader responding to budget reductions, the project manager should engage the team collaboratively to assess the full impact before making any recommendations. This participatory approach produces an honest and comprehensive impact assessment while respecting the team\'s ownership of their work and building commitment to the revised plan. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    # Q1047 (Q1046 missing)
    (
        'Explanation: Need: keep plans flexible. Option B (Reevaluate the backlog priority with the product owner since the velocity has been impacted) fixes it."',
        'Explanation: Keywords: resource loss, new backlog requirements, velocity impact, backlog reprioritization. When both a resource is lost and new requirements are added simultaneously, the net effect is reduced team capacity against an expanded backlog. The project manager must work with the product owner to re-prioritize the backlog based on the new velocity reality so that the highest-value items are delivered first within the adjusted capacity. (PMBOK Guide) – Seventh Edition, 2021, p. 32, \'Focus on Value\'"'
    ),
    # Q1048
    (
        'Explanation: Need: guide and calm the team. Option C (Log the situation in the issue log.) fixes it."',
        'Explanation: Keywords: team member emergency, no coverage available, issue log, tracking. When a team member is unexpectedly unavailable and no immediate substitute exists, logging the situation in the issue log formally records the active problem and ensures it receives ongoing tracking and visibility. This documentation enables a structured resolution process rather than an ad hoc response that might be forgotten or poorly coordinated. (PMBOK Guide) – Seventh Edition, 2021, p. 34, \'Recognize, Evaluate, and Respond to System Interactions\'"'
    ),
    # Q1050 (Q1049 missing)
    (
        'Explanation: Need: listen to people needs. Option B (Present the project to the stakeholder) fixes it."',
        'Explanation: Keywords: new board director, mid-execution project impact, stakeholder onboarding, project presentation. When a new influential stakeholder joins mid-project and begins affecting decisions without project context, the first action must be to present the project to that stakeholder. Ensuring they understand the project\'s current state, objectives, and constraints enables their influence to become constructive rather than disruptive. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    # Q1051 (Q1052 missing)
    (
        'Explanation: Need: listen to people needs. Option B (Invite the project sponsor to the sprint review meeting and have a Q&A session about the concept and expected performance of the equipment) fixes it."',
        'Explanation: Keywords: major investor concerns, sprint review, concept doubts, project sponsor involvement. When a major investor raises technical doubts about the product concept in a sprint review, the project manager should bring in the project sponsor to address those concerns in a structured Q&A. The sponsor has the organizational authority and strategic context to respond to investor-level concerns in a way that builds confidence and prevents the doubt from escalating into resistance. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    # Q1053 (Q1052, Q1054 missing)
    (
        'Explanation: Need: guide and calm the team. Option A (Follow the Perform integrated Change Control process and submit a change request) fixes it."',
        'Explanation: Keywords: unexpected remote work, operational expenditure reimbursement, change control, cost baseline impact. When unforeseen circumstances force a team to work remotely and incur additional operational costs, these expenses represent a scope and cost change that must flow through the integrated change control process. Submitting a change request ensures the additional costs are formally evaluated, approved, and incorporated into the project cost baseline with proper documentation. (PMBOK Guide) – Seventh Edition, 2021, p. 50, \'Enable Change to Achieve the Envisioned Future State\'"'
    ),
    # Q1055 (Q1054 missing)
    (
        'Explanation: Need: listen to people needs. Option A (Analyse the team members\' influence levels and schedule a training on the importance of daily standups and the time-bound feature of the meetings.) fixes it."',
        'Explanation: Keywords: daily standup resistance, sponsor-required daily updates, team member influence, standup training. When team members resist daily meetings requested by the sponsor, the project manager must first understand their influence dynamics before applying a solution, and then use targeted training to address the resistance by helping team members understand the value and brevity of effective standups. This approach secures participation through understanding rather than mandate. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    # Q1056
    (
        'Explanation: Need: listen to people needs. Option A (Ensure that the project artifacts are kept up-to-date and shared with the stakeholders.) fixes it."',
        'Explanation: Keywords: complex project artifacts, stakeholder access issues, artifact currency, proactive sharing. When stakeholders have trouble accessing project artifacts, the root cause is typically that documents are outdated or not proactively distributed. Keeping artifacts current and actively sharing them with stakeholders removes access friction and ensures stakeholders always have the information they need to stay engaged with the project. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    # Q1057
    (
        'Explanation: Need: listen to people needs. Option A (Look at the stakeholder assessment matrix to find stakeholders\' interests and make updates if necessary.) fixes it."',
        'Explanation: Keywords: varied stakeholder interest levels, execution phase, stakeholder assessment matrix, engagement updates. When stakeholders show varying levels of interest during execution, the project manager should consult the stakeholder assessment matrix to understand where each stakeholder currently stands and update it to reflect any changes. This evidence-based approach allows the project manager to target engagement strategies to those who need more or different attention. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    # Q1058
    (
        'Explanation: Need: protect value and acceptance. Option B (The contractual deliverables of the project have been accepted.) fixes it."',
        'Explanation: Keywords: project closure initiation, contractual deliverables, formal acceptance, closure prerequisites. Before formally closing a project, the project manager must confirm that all contractual deliverables have been accepted by the client or sponsor. Acceptance is the definitive evidence that the project has fulfilled its obligations and that closure activities can proceed — without it, the project has not technically completed its purpose. (PMBOK Guide) – Seventh Edition, 2021, p. 32, \'Focus on Value\'"'
    ),
    # Q1059
    (
        'Explanation: Need: keep plans flexible. Option A (30/40) fixes it."',
        'Explanation: Keywords: agile SPI calculation, story points, planned versus delivered, schedule performance index. The schedule performance index is calculated as earned value divided by planned value. In agile terms, the team earned 30 story points but planned to complete 40, giving an SPI of 30/40 = 0.75. An SPI below 1.0 indicates the team is behind the planned delivery pace. (PMBOK Guide) – Seventh Edition, 2021, p. 32, \'Focus on Value\'"'
    ),
    # Q1060
    (
        'Explanation: Need: control changes and baselines. Option B (Keep the focus on the priority items while the change goes through the change control process.) fixes it."',
        'Explanation: Keywords: cross-portfolio change request, tactical change, change control process, team focus protection. When an external project proposes a tactical change that affects another project, the receiving project manager must channel it through the change control process and protect the team\'s focus on current priority items in the meantime. Implementing changes before they are approved disrupts the baseline and bypasses governance. (PMBOK Guide) – Seventh Edition, 2021, p. 50, \'Enable Change to Achieve the Envisioned Future State\'"'
    ),
    # Q1061
    (
        'Explanation: Need: guide and calm the team. Option B (Identify the impediment and associated risks at the daily standup.) fixes it."',
        'Explanation: Keywords: team member struggling with impediment, schedule risk, daily standup, impediment visibility. When a team member\'s impediment is blocking progress and creating delivery risk, the daily standup is the correct agile forum to surface it, making it visible to the whole team and enabling collective problem-solving. Raising it in a broader forum prematurely escalates an issue that should first be addressed at the team level. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    # Q1062
    (
        'Explanation: Need: guide and calm the team. Option C (Work with the project management office (PMO) manager to generate an onboarding plan for the new product owner.) fixes it."',
        'Explanation: Keywords: new product owner, knowledge gap, team confidence, PMO onboarding plan. When a new product owner lacks the product knowledge needed to earn the team\'s confidence, a structured onboarding plan developed with the PMO provides a systematic approach to building their credibility. This is more effective than the project manager assuming the product owner role — which conflates two distinct accountabilities — or team-building activities that do not address the knowledge gap directly. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    # Q1063
    (
        'Explanation: Need: listen to people needs. Option B (Raise a change request to the change control board (CCB) and inform the project sponsor about the change.) fixes it."',
        'Explanation: Keywords: 90% complete project, late scope addition, CCB submission, project sponsor notification. A scope addition at 90% project completion must follow the formal change control process regardless of how late in the project it arrives. Raising a change request to the CCB and notifying the sponsor ensures the addition is evaluated on its merits, approved by appropriate governance, and incorporated into the project with full visibility to leadership. (PMBOK Guide) – Seventh Edition, 2021, p. 50, \'Enable Change to Achieve the Envisioned Future State\'"'
    ),
    # Q1064
    (
        'Explanation: Need: listen to people needs. Option B (Review the definition of done (DoD) with the product owner.) fixes it."',
        'Explanation: Keywords: sprint goals not met, no defects reported, DoD misalignment, product owner alignment. When the team is confused about unmet sprint goals despite having no defects and no new requirements, the issue is likely a misaligned definition of done between the team and the product owner. Reviewing the DoD together ensures both parties share the same criteria for what constitutes a completed and acceptable sprint deliverable. (PMBOK Guide) – Seventh Edition, 2021, p. 42, \'Build Quality into Processes and Deliverables\'"'
    ),
    # Q1065
    (
        'Explanation: Need: listen to people needs. Option C (Start the process to include the new features of the product on the next iteration.) fixes it."',
        'Explanation: Keywords: competitive advantage features, post-consensus request, next iteration, change process initiation. When a new feature request arrives after design consensus is reached, the project manager should begin the formal process to include it in the next iteration rather than inserting it into the current work or bypassing change control. This approach accommodates valuable scope additions without disrupting the current iteration\'s commitments. (PMBOK Guide) – Seventh Edition, 2021, p. 50, \'Enable Change to Achieve the Envisioned Future State\'"'
    ),
    # Q1066
    (
        'Explanation: Need: guide and calm the team. Option B (Propose a governance model that empowers the teams while providing the necessary oversight to the executive leadership team.) fixes it."',
        'Explanation: Keywords: agile transformation, executive scope control concern, governance model, empowerment with oversight. When executives fear losing control during an agile transformation, the project manager should propose a governance model that explicitly provides oversight visibility while empowering teams to work autonomously within defined boundaries. This balanced approach addresses the concern without reverting to heavy-handed approval gates that would undermine the agile intent. (PMBOK Guide) – Seventh Edition, 2021, p. 50, \'Enable Change to Achieve the Envisioned Future State\'"'
    ),
    # Q1067
    (
        'Explanation: Need: listen to people needs. Option C (Consider the view of each team member about the issue in order to reach consensus.) fixes it."',
        'Explanation: Keywords: team disagreement, training approach conflict, consensus building, facilitation. When two team members cannot resolve a planning disagreement independently, the project manager must facilitate a process that gives each perspective equal consideration in order to reach a collaborative consensus. Imposing a solution based on expert judgment alone bypasses team ownership and may cause resentment that persists beyond the specific decision. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    # Q1068
    (
        'Explanation: Need: guide and calm the team. Option A (Help the team create the definition of done (DoD) to improve delivery quality.) fixes it."',
        'Explanation: Keywords: degrading code quality, retrospective feedback, rework accumulation, definition of done. When retrospective feedback reveals declining code quality, the root cause is typically the absence of clear and enforced quality standards for what constitutes a complete increment. Helping the team establish a definition of done that includes quality criteria creates an objective bar that prevents the progressive quality erosion that leads to unmanageable rework. (PMBOK Guide) – Seventh Edition, 2021, p. 42, \'Build Quality into Processes and Deliverables\'"'
    ),
    # Q1069
    (
        'Explanation: Need: listen to people needs. Option D (Understand the scope complexity and project magnitude prior to determining which approach to use.) fixes it."',
        'Explanation: Keywords: mixed stakeholder experience, methodology selection, scope complexity assessment, project magnitude. The project manager\'s decision about which approach to use — predictive, agile, or hybrid — must be based on the nature of the project rather than the team\'s prior exposure or the simplest path. Understanding the scope complexity and project magnitude first ensures the selected methodology is fit for purpose regardless of stakeholder familiarity. (PMBOK Guide) – Seventh Edition, 2021, p. 40, \'Tailor Based on Context\'"'
    ),
    # Q1070
    (
        'Explanation: Need: guide and calm the team. Option C (At the end of each and every iteration) fixes it."',
        'Explanation: Keywords: iterative delivery, incremental value demonstration, sprint review timing, agile cadence. In an iterative project, value is demonstrated at the end of each and every iteration to enable continuous stakeholder feedback and course correction. Waiting for a major feature or full development completion contradicts the agile principle of frequent inspection and adaptation through working increments. (PMBOK Guide) – Seventh Edition, 2021, p. 32, \'Focus on Value\'"'
    ),
    # Q1071
    (
        'Explanation: Need: listen to people needs. Option C (Review and amend the processes to ensure only value-adding activities are present.) fixes it."',
        'Explanation: Keywords: process-following team, recurring roadblocks, similar previous project, non-value-adding activities. When a team is following processes exactly but still running behind schedule with recognizable roadblocks from previous projects, the processes themselves are the problem. The project manager must review and amend the processes to eliminate activities that do not add value, as strict adherence to flawed processes perpetuates the same delays. (PMBOK Guide) – Seventh Edition, 2021, p. 48, \'Embrace Adaptability and Resiliency\'"'
    ),
    # Q1072
    (
        'Explanation: Need: guide and calm the team. Option A (Evaluate the issue with the team to determine if they have the necessary skills to perform assignments.) fixes it."',
        'Explanation: Keywords: consistently behind schedule, recurring rework, international team, skills assessment. When a geographically distributed team consistently underperforms with frequent rework, the root cause may be a skill gap rather than effort or motivation. Evaluating the issue directly with the team surfaces the actual capability gaps and allows the project manager to target the right intervention — training, support, or scope reallocation. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    # Q1073 multi-select A,E
    (
        'Explanation: Need: listen to people needs. Options A and E (Update the project stakeholder analysis and methods to satisfy the stakeholders\' requirements.; Engage all stakeholders in the project including the unsupportive stakeholders.) work together."',
        'Explanation: Keywords: stakeholders working against project, tight budget, unsupportive stakeholders, inclusive engagement. When stakeholders actively resist a project, excluding them escalates opposition while ignoring legitimate concerns. The project manager must update the stakeholder analysis to understand what is driving resistance and then engage all stakeholders — including the unsupportive ones — to address concerns and build alignment. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    # Q1074
    (
        'Explanation: Need: guide and calm the team. Option B (Develop relationship skills as a leader and also develop the teams\' emotional intelligence skills.) fixes it."',
        'Explanation: Keywords: high turnover, relationship management gaps, emotional intelligence, leadership development. When exit interviews consistently cite the project manager\'s poor relationship management as the reason for departures, the project manager must invest in developing their own interpersonal and emotional intelligence skills. Building these capabilities in the team as well creates a more emotionally resilient environment that reduces the relational friction driving turnover. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    # Q1075
    (
        'Explanation: Need: guide and calm the team. Option D (Speak with the experienced team member to discuss the issues in a supportive way.) fixes it."',
        'Explanation: Keywords: deflecting behavior, experienced team member, supportive conversation, team dynamics. When an experienced team member consistently criticizes others in meetings while avoiding their own issues, a private, supportive conversation is the most effective first response. This approach preserves the relationship, gives the team member an opportunity to reflect without public embarrassment, and addresses the behavior at its source. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    # Q1076
    (
        'Explanation: Need: keep plans flexible. Option B (Address the issue during the next sprint planning meeting.) fixes it."',
        'Explanation: Keywords: quality rework causing delays, hybrid project, sprint planning meeting, process improvement. When recurring quality issues are causing rework and feature delivery slowdowns, the sprint planning meeting is the appropriate agile forum to address the root cause and adjust the approach. This keeps the quality problem visible and actionable within the team\'s existing governance cadence rather than requiring escalation or a schedule change request. (PMBOK Guide) – Seventh Edition, 2021, p. 42, \'Build Quality into Processes and Deliverables\'"'
    ),
    # Q1077
    (
        'Explanation: Need: guide and calm the team. Option A (Help all team members learn to deal with their emotions by building a culture of empathy.) fixes it."',
        'Explanation: Keywords: personal issues affecting performance, team contagion, empathy culture, emotional resilience. When one team member\'s emotional situation spreads to affect the whole team\'s performance, the project manager must respond by building a culture of empathy that helps all members develop emotional resilience. This systemic approach addresses the team-level impact rather than isolating the individual, and creates a lasting protective culture for future challenges. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    # Q1078
    (
        'Explanation: Need: listen to people needs. Option B (Propose that the well-defined scope items be delivered using a predictive approach and use an agile approach to deal with the complex items.) fixes it."',
        'Explanation: Keywords: partial scope definition, complex undefinable items, hybrid approach, scope clarity. When some scope items are well-defined and others are too complex to specify upfront, a hybrid approach applies the right methodology to each category. Predictive planning suits the defined scope, while an agile approach allows the complex items to be explored, refined, and delivered incrementally — starting the project without waiting for full scope definition. (PMBOK Guide) – Seventh Edition, 2021, p. 40, \'Tailor Based on Context\'"'
    ),
    # Q1079
    (
        'Explanation: Need: guide and calm the team. Option B (Ask the team member to provide details to address the issue with the vendor.) fixes it."',
        'Explanation: Keywords: vendor delay reported at standup, sprint progress impact, team member details, vendor issue resolution. When a vendor delay is flagged in a standup, the project manager should gather the specific details from the team member before taking action with the vendor. Understanding the precise nature of the delay enables a targeted and effective resolution approach rather than a generic escalation that may not address the actual problem. (PMBOK Guide) – Seventh Edition, 2021, p. 34, \'Recognize, Evaluate, and Respond to System Interactions\'"'
    ),
    # Q1080
    (
        'Explanation: Need: guide and calm the team. Option D (Ask the team to monitor the risk and provide an alert if it becomes an issue.) fixes it."',
        'Explanation: Keywords: high-probability risk, risk monitoring, team alerting, active risk watch. When a high-probability risk has been identified, the project manager should assign the team to actively monitor it and trigger an alert the moment it escalates to an active issue. This watch-and-respond approach ensures the risk is not forgotten while avoiding premature or costly actions that may not be needed if the risk does not materialize. (PMBOK Guide) – Seventh Edition, 2021, p. 46, \'Optimize Risk Responses\'"'
    ),
    # Q1081
    (
        'Explanation: Need: listen to people needs. Option C (Communicate the results and negotiate the needed resources and time with the stakeholder.) fixes it."',
        'Explanation: Keywords: sponsor feature addition, significant cost and schedule impact, negotiation, resource and time request. When a sponsor requests a major addition that will significantly impact the schedule and budget, the project manager must communicate the impact transparently and negotiate with the stakeholder for the additional resources and time needed to accommodate it. This collaborative approach ensures the sponsor makes an informed decision and that any accommodation is properly resourced. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    # Q1082
    (
        'Explanation: Need: keep plans flexible. Option B (Obtain management approval prior to implementing the new risk response.) fixes it."',
        'Explanation: Keywords: escalated risk, new response plan deviation, management approval, governance protocol. When a risk escalates beyond its original response plan and the project manager develops a different mitigation approach, management approval must be obtained before implementing it. Deviating from an approved plan — even for good reasons — without authorization bypasses governance and creates accountability gaps if the new approach also fails. (PMBOK Guide) – Seventh Edition, 2021, p. 46, \'Optimize Risk Responses\'"'
    ),
    # Q1083
    (
        'Explanation: Need: listen to people needs. Option B (Share the existing technical architect so they can be allocated to the current project and other projects.) fixes it."',
        'Explanation: Keywords: existing technical architect, portfolio-level allocation, shared resource model, moderate time requirement. When a highly knowledgeable technical architect already exists at the portfolio level and the project only needs them for a moderate amount of time, sharing the resource across projects is the most efficient use of that expertise. Hiring a new architect would duplicate capacity unnecessarily when the existing resource can serve the need within a shared model. (PMBOK Guide) – Seventh Edition, 2021, p. 34, \'Recognize, Evaluate, and Respond to System Interactions\'"'
    ),
    # Q1084
    (
        'Explanation: Need: guide and calm the team. Option B (Refer to the project\'s resource management plan.) fixes it."',
        'Explanation: Keywords: deploying manager availability refusal, new project manager, resource management plan, escalation prevention. When a deploying manager declines to confirm resource availability, the first step for a newly appointed project manager is to consult the resource management plan, which documents how resources are to be acquired and managed. The plan may address this exact scenario with escalation paths or alternative arrangements that the new project manager should follow before taking other action. (PMBOK Guide) – Seventh Edition, 2021, p. 34, \'Recognize, Evaluate, and Respond to System Interactions\'"'
    ),
    # Q1085
    (
        'Explanation: Need: guide and calm the team. Option D (Enroll team members in training on the tool.) fixes it."',
        'Explanation: Keywords: testing backlog bottleneck, team-identified tool solution, training investment, hybrid project. When the team has already identified a tool that could resolve a testing bottleneck, the project manager should enable them to use it by enrolling them in training. Empowering the team to act on their own solution builds ownership and addresses the bottleneck with the option most likely to succeed because the team already believes in it. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    # Q1086
    (
        'Explanation: Need: keep plans flexible. Option A (Plan for continuous validation of the product.) fixes it."',
        'Explanation: Keywords: post-delivery rework, quality issues, new feature delays, continuous validation. When major quality issues surface at delivery and cause rework that delays subsequent feature development, the project manager must institute continuous product validation throughout development rather than relying on end-of-cycle testing. Building validation into every phase catches defects earlier when they are less costly to fix. (PMBOK Guide) – Seventh Edition, 2021, p. 42, \'Build Quality into Processes and Deliverables\'"'
    ),
    # Q1087
    (
        'Explanation: Need: guide and calm the team. Option B (Ensure that the team assesses opportunities to deliver the highest business value items incrementally.) fixes it."',
        'Explanation: Keywords: competing backlog prioritization schemes, engineering versus quality versus compliance, business value, incremental delivery. When steering committee members advocate for different prioritization frameworks, the project manager must refocus the discussion on the foundational agile principle of delivering the highest business value first. Assessing incremental business value provides an objective criterion that resolves the competing preferences by grounding prioritization in what matters most to the organization. (PMBOK Guide) – Seventh Edition, 2021, p. 32, \'Focus on Value\'"'
    ),
    # Q1088
    (
        'Explanation: Need: listen to people needs. Option C (Build trust with the stakeholder by keeping project commitments and use demo sessions to gather feedback and realign goals.) fixes it."',
        'Explanation: Keywords: disengaged stakeholder, transparency frustration, trust building, demo sessions. When a stakeholder refuses to participate due to past transparency failures, plans and presentations are insufficient to re-engage them — only demonstrated reliability can rebuild trust. Consistently keeping commitments and using demo sessions to show real working product creates the evidence-based trust that reopens the stakeholder\'s willingness to engage. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    # Q1089
    (
        'Explanation: Need: guide and calm the team. Option A (Ask one of the more experienced team members to support the team member with the task.) fixes it."',
        'Explanation: Keywords: struggling team member, experienced colleagues identified, peer support, task completion. When a team member struggles with a task and the project manager identifies more experienced members who can help, the appropriate first response is to arrange peer support rather than reassigning the task. This approach keeps the original team member engaged and learning while leveraging available expertise within the team. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    # Q1090 multi-select A,C
    (
        'Explanation: Need: listen to people needs. Options A and C (Schedule weekly progress meetings with all three teams and have them take turns as key players.; Update the communications management plan and encourage the teams to review it promptly and proactively.) work together."',
        'Explanation: Keywords: time zone isolation, team left out, information delays, preferential treatment. When one virtual team consistently receives information late and feels deprioritized, the project manager must create structured parity through rotating key player roles in shared meetings and update the communications management plan to formalize equitable information flow. Together these two actions address both the structural and behavioral causes of the team\'s exclusion. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    # Q1091
    (
        'Explanation: Need: control changes and baselines. Option B (Request management to update the project requirements accordingly.) fixes it."',
        'Explanation: Keywords: external business influence, changed business parameters, requirements update, management authorization. When the external business conditions that justified the project have changed, the project requirements must be updated to reflect the new reality rather than proceeding on outdated assumptions. The project manager should request management authorization for the requirement updates, since these changes affect the project\'s strategic basis and require proper governance approval. (PMBOK Guide) – Seventh Edition, 2021, p. 50, \'Enable Change to Achieve the Envisioned Future State\'"'
    ),
    # Q1092
    (
        'Explanation: Need: guide and calm the team. Option C (Assist the team in defining a minimum viable product (MVP) by the launch date.) fixes it."',
        'Explanation: Keywords: fixed launch date, insufficient capacity for full backlog, MVP definition, competitive product. When the team determines that all features cannot be delivered by a fixed public launch date, the project manager must help define a minimum viable product that delivers the core value needed for a successful launch. An MVP strategy protects the launch date while ensuring the product meets the threshold of customer usefulness. (PMBOK Guide) – Seventh Edition, 2021, p. 32, \'Focus on Value\'"'
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
