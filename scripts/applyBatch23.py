MD_FILE = './src/imports/project-management-questions-1.md'

with open(MD_FILE, 'r', encoding='utf-8') as f:
    content = f.read()

replacements = [
    # Q1093
    (
        'Explanation: Need: guide and calm the team. Option C (Evaluate the fallback plan proposed by the team and submit a change request, if required.) fixes it."',
        'Explanation: Keywords: critical path delay, team fallback plan, additional cost, change request evaluation. When a team proposes a fallback plan that requires additional cost on a tight budget, the project manager must evaluate the plan\'s feasibility and submit a change request if the added cost exceeds approved contingency. This ensures the fallback option is formally reviewed and authorized before committing resources that could further strain the budget. (PMBOK Guide) – Seventh Edition, 2021, p. 50, \'Enable Change to Achieve the Envisioned Future State\'"'
    ),
    # Q1094
    (
        'Explanation: Need: listen to people needs. Option D (Develop and define a communication strategy for stakeholders.) fixes it."',
        'Explanation: Keywords: stakeholder groups, communication strategy, tailored approach, influence levels. After categorizing stakeholders into groups, the project manager must develop a distinct communication strategy that addresses the needs, interests, and influence levels of each group. A uniform approach fails to account for the different information requirements and engagement expectations that distinguish each stakeholder category. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    # Q1095
    (
        'Explanation: Need: listen to people needs. Option B (Invite the stakeholders to the sprint review meetings.) fixes it."',
        'Explanation: Keywords: stakeholder progress visibility, biweekly meeting request, sprint review, agile cadence. In an agile project, the sprint review is specifically designed to demonstrate progress and gather stakeholder feedback at the end of each sprint. Inviting stakeholders to this existing ceremony meets their biweekly visibility need without creating a redundant meeting, while keeping them engaged through the working product demonstrations that sprint reviews provide. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    # Q1096
    (
        'Explanation: Need: keep plans flexible. Option B (Start project planning and develop the project management plan.) fixes it."',
        'Explanation: Keywords: urgent humanitarian project, well construction, project management plan, planning discipline. Urgency does not justify bypassing planning — even for humanitarian projects with critical need. Starting project planning and developing a project management plan ensures the 100-well initiative has the structure, resource allocation, and governance needed to execute reliably and sustainably. (PMBOK Guide) – Seventh Edition, 2021, p. 25, \'Be a Diligent, Respectful, and Caring Steward\'"'
    ),
    # Q1097
    (
        'Explanation: Need: listen to people needs. Option C (Promote, inspire, and follow the stakeholder engagement process.) fixes it."',
        'Explanation: Keywords: politicized environment, conflicting stakeholder interests, collective goal alignment, stakeholder engagement. In a highly political environment where stakeholders prioritize their own operational goals, the project manager must actively promote and inspire alignment toward the shared project purpose through structured stakeholder engagement. Following the stakeholder engagement process provides the systematic framework for building this collective commitment. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    # Q1098
    (
        'Explanation: Need: listen to people needs. Option D (Evaluate the consequences of noncompliance with relevant stakeholders and update the risk register with agreed actions.) fixes it."',
        'Explanation: Keywords: new legal requirements, uncertain compliance, mid-project, noncompliance consequences. When new legal requirements emerge mid-project and compliance is uncertain, the project manager must evaluate the specific consequences of noncompliance with relevant stakeholders and formally register the risk with agreed response actions. This collaborative assessment prevents both premature project stoppage and unacknowledged legal exposure. (PMBOK Guide) – Seventh Edition, 2021, p. 46, \'Optimize Risk Responses\'"'
    ),
    # Q1099
    (
        'Explanation: Need: listen to people needs. Option A (Organize a meeting with relevant stakeholders explaining the benefits of agile and the practices relevant for the project.) fixes it."',
        'Explanation: Keywords: agile adoption in construction, stakeholder buy-in, benefits explanation, relevant practices. Gaining stakeholder buy-in for a new approach requires educating them about its specific benefits for their context rather than assuming they will accept the change without understanding it. A direct meeting that explains both the advantages of agile and how specific practices apply to this project creates informed support and reduces resistance grounded in unfamiliarity. (PMBOK Guide) – Seventh Edition, 2021, p. 50, \'Enable Change to Achieve the Envisioned Future State\'"'
    ),
    # Q1100
    (
        'Explanation: Need: keep plans flexible. Option C (Include the dependency in the project schedule.) fixes it."',
        'Explanation: Keywords: external IT dependency, activity constraint, schedule dependency, planning integration. When an external dependency is identified during planning — such as requiring another department to implement a system before a project activity can start — that dependency must be formally incorporated into the project schedule. Documenting it creates visibility, enables realistic sequencing, and prevents the project from being unexpectedly delayed when the dependency manifests. (PMBOK Guide) – Seventh Edition, 2021, p. 40, \'Tailor Based on Context\'"'
    ),
    # Q1101
    (
        'Explanation: Need: listen to people needs. Option C (Coordinate with the team and the project stakeholders to collect the knowledge.) fixes it."',
        'Explanation: Keywords: client without knowledge management system, project knowledge collection, team and stakeholder coordination. When the client has no knowledge management system, the project manager must coordinate with both the team and stakeholders to collectively capture the project knowledge in a structured way. This collaborative approach ensures comprehensive coverage and stakeholder buy-in for whatever knowledge repository solution is established. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    # Q1102
    (
        'Explanation: Need: guide and calm the team. Option D (Train the three team leads to conduct a local meeting, then run an overall status meeting.) fixes it."',
        'Explanation: Keywords: three-country scrum team, language barriers, 45-minute standup, tiered meeting structure. When language barriers in a distributed daily standup cause misunderstandings and extend meetings beyond the timebox, a tiered approach solves both problems. Training team leads to run local meetings in their own language first, then consolidating key updates in an overall meeting, improves communication accuracy while keeping the cross-team session focused and time-efficient. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    # Q1103
    (
        'Explanation: Need: guide and calm the team. Option B (Set up a daily virtual meeting with the development team.) fixes it."',
        'Explanation: Keywords: virtual development teams, insufficient communication, misalignment on tasks, daily standup. When distributed development teams are not communicating enough and lack alignment on tasks and impediments, introducing a daily virtual standup creates the regular touchpoint needed for coordination. This structured daily meeting surfaces blockers early and ensures the team maintains a shared understanding of progress and priorities. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    # Q1104
    (
        'Explanation: Need: listen to people needs. Option B (Call a technical meeting with the customer to agree on a specification for the component and document it in the quality management plan.) fixes it."',
        'Explanation: Keywords: deficient component, quality plan gap, customer specification, technical alignment. When a customer identifies a quality failure for a component with no current quality specification, the project manager must convene a technical meeting with the customer to jointly define the specification and then document it in the quality management plan. This collaborative approach ensures the standard reflects both technical requirements and customer expectations, and formalizes it for ongoing quality assurance. (PMBOK Guide) – Seventh Edition, 2021, p. 42, \'Build Quality into Processes and Deliverables\'"'
    ),
    # Q1105
    (
        'Explanation: Need: listen to people needs. Option A (Plan the project with a predictive approach with a work breakdown structure (WBS) and then execute it using an agile approach to delivervalue incrementally.) fixes it."',
        'Explanation: Keywords: long-term complex scope, high-level plan required, incremental value delivery, hybrid planning and execution. When a client needs both a long-term predictive plan and incremental value delivery throughout the project, a hybrid model that uses WBS-based planning for structure and agile execution for delivery is the optimal approach. This satisfies the sponsor\'s need for comprehensive planning visibility while delivering progressive value that the client can react to. (PMBOK Guide) – Seventh Edition, 2021, p. 40, \'Tailor Based on Context\'"'
    ),
    # Q1106
    (
        'Explanation: Need: protect benefits for users. Option C (Milestones status report) fixes it."',
        'Explanation: Keywords: senior management decision-making, broader project view, milestone reporting, executive communication. Senior management needs high-level project status that enables strategic decision-making without operational detail overload. A milestones status report provides the executive view they need — showing progress against major project deliverables and timelines — without the granularity that is appropriate for the project team but counterproductive for leadership analysis. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    # Q1107
    (
        'Explanation: Need: listen to people needs. Option D (Update the stakeholder engagement plan for the stakeholder.) fixes it."',
        'Explanation: Keywords: difficult stakeholder, feedback not received, healthcare IT project, engagement plan update. When an approach to engaging a specific stakeholder is not working, the project manager must update the stakeholder engagement plan to define a more effective strategy for that individual. A revised engagement plan formalizes the new approach and ensures it is consistently applied rather than improvised each time feedback is needed. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    # Q1108 - Note: file may use curly apostrophe in "stakeholders" - use double quotes
    (
        "Explanation: Need: listen to people needs. Option B (Recognize the stakeholders skills are important for the project and evaluate the possibility of the stakeholder supporting the project team.) fixes it.\"",
        "Explanation: Keywords: lessons learned, expert stakeholder identified, tax project, stakeholder support evaluation. When lessons learned from a previous project reveal an expert stakeholder who is willing to help, the project manager should formally evaluate how that stakeholder can support the current project team rather than leaving the connection informal. This evidence-based approach leverages organizational knowledge while ensuring the stakeholder's involvement is structured and purposeful. (PMBOK Guide) – Seventh Edition, 2021, p. 30, 'Effectively Engage with Stakeholders'\""
    ),
    # Q1109
    (
        'Explanation: Need: guide and calm the team. Option D (Speak with the team member directly to reinforce the ground rules.) fixes it."',
        'Explanation: Keywords: recurring tardiness, daily standup, direct conversation, ground rules reinforcement. When a team member is repeatedly late to standups, the project manager should address the issue directly and privately with that individual rather than reinforcing ground rules to the entire team. A one-on-one conversation respects the member\'s dignity, avoids creating a group dynamic of blame, and is more likely to produce behavioral change through genuine understanding. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    # Q1110
    (
        'Explanation: Need: listen to people needs. Option D (Set expectations for contributions ahead of the meeting) fixes it."',
        'Explanation: Keywords: ground rules discussion, unequal participation, dominant voices, pre-meeting expectations. When only a few team members contribute to a ground rules discussion, the result favors those voices and excludes others. Setting contribution expectations ahead of the meeting — for example, asking all members to prepare ideas in advance — creates equal preparedness and reduces the dominance of the most vocal participants. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    # Q1111
    (
        'Explanation: Need: listen to people needs. Option C (Assessed the situation with the project stakeholders first and communicated the impact to the customer) fixes it."',
        'Explanation: Keywords: abrupt office closure, premature delay communication, stakeholder assessment first, customer impact. Before communicating a delay to the customer, the project manager should first assess the actual impact with the project team and stakeholders to understand whether a delay is truly unavoidable and how significant it will be. Communicating immediately without this assessment risks overstating the problem and creating customer concern that a careful assessment might have prevented. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    # Q1112
    (
        'Explanation: Need: listen to people needs. Option B (Archive the survey responses with project artifacts for future projects.) fixes it."',
        'Explanation: Keywords: cancelled project, stakeholder survey, lessons learned, organizational process assets. Survey responses from a cancelled project represent valuable institutional knowledge that must be preserved as organizational process assets for future reference. Archiving them with the project artifacts ensures future project managers can access these insights when initiating similar work, turning the cancelled project\'s experience into a learning benefit for the organization. (PMBOK Guide) – Seventh Edition, 2021, p. 25, \'Be a Diligent, Respectful, and Caring Steward\'"'
    ),
    # Q1113
    (
        'Explanation: Need: listen to people needs. Option D (Use iterative life cycles involving stakeholders to enable the team to improve the product end result through successive prototypes.) fixes it."',
        'Explanation: Keywords: rapidly changing environment, hybrid project, stakeholder needs, iterative prototypes. In a dynamic business environment, stakeholder needs evolve continuously and cannot be fully captured upfront. Using iterative life cycles with stakeholder involvement at each prototype stage allows the team to continuously incorporate feedback and adapt the product end result — ensuring delivered value remains aligned with evolving needs throughout the project. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    # Q1114
    (
        'Explanation: Need: secure people or vendors. Option B (Invite the vendor to a meeting to discuss the concerns.) fixes it."',
        'Explanation: Keywords: unresponsive vendor, mid-project, direct meeting, vendor relationship management. When a vendor is not responding through normal channels, the project manager should invite them to a direct meeting to surface and address the underlying concerns. A face-to-face or virtual discussion is more effective than continuing to use the same channels that are failing and creates the opportunity to uncover reasons for the lack of responsiveness that email alone cannot reveal. (PMBOK Guide) – Seventh Edition, 2021, p. 34, \'Recognize, Evaluate, and Respond to System Interactions\'"'
    ),
    # Q1115
    (
        'Explanation: Need: listen to people needs. Option B (The daily standup meetings were not consistently attended.) fixes it."',
        'Explanation: Keywords: siloed team members, knowledge gaps, agile communication breakdown, standup attendance. In an agile project, the daily standup is the primary mechanism for team members to synchronize on work, surface blockers, and understand what others are doing. When standups are not consistently attended, team members lose visibility into each other\'s work — directly causing the silos and knowledge gaps the question describes. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    # Q1116
    (
        'Explanation: Need: listen to people needs. Option A (Investigate the reasons for the disagreement to understand the gap among the stakeholders and search for consensus.) fixes it."',
        'Explanation: Keywords: adaptive tool disagreement, stakeholder gap, consensus building, root cause investigation. Before attempting to resolve stakeholder disagreement about new tools, the project manager must understand the reasons behind the resistance. Investigating the specific concerns reveals whether the gap is technical, cultural, or related to past experience — information that is essential for building genuine consensus rather than just overcoming surface objections. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    # Q1117
    (
        'Explanation: Need: listen to people needs. Option C (Analyze the stakeholders.) fixes it."',
        'Explanation: Keywords: stakeholder identification, stakeholder analysis sequence, next step, engagement planning. After identifying stakeholders, the project manager\'s next step is to analyze them to understand their interests, influence, impact, and engagement requirements. Analysis transforms a list of names into an actionable understanding of how each stakeholder relates to the project — the essential foundation for planning effective engagement. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    # Q1118
    (
        'Explanation: Need: guide and calm the team. Option B (Risk occurred) fixes it."',
        'Explanation: Keywords: risk register, issue log, risk materialization, transfer point. The transfer from risk register to issue log happens at the moment a risk materializes — when it actually occurs and becomes an active problem requiring immediate management. Before occurrence it remains a risk; after occurrence it becomes an issue that must be tracked through the issue management process. (PMBOK Guide) – Seventh Edition, 2021, p. 34, \'Recognize, Evaluate, and Respond to System Interactions\'"'
    ),
    # Q1119
    (
        'Explanation: Need: listen to people needs. Option C (Set up an intranet site and allow stakeholders to access the relevant project information.) fixes it."',
        'Explanation: Keywords: 1000 stakeholders, matrix organization, pull communication, intranet access. When a project has over 1,000 stakeholders who need project awareness, a pull communication approach through an intranet site is far more scalable than push communication methods like individual emails. Stakeholders can access current, relevant project information on demand, reducing the project team\'s communication overhead while ensuring consistent information availability. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    # Q1120
    (
        'Explanation: Need: guide and calm the team. Option C (Develop the team member\'s capacities through mentoring and training.) fixes it."',
        'Explanation: Keywords: expert unavailable on another project, hybrid project, team member development, government regulator compliance. When an external expert needed to resolve an impediment is assigned elsewhere, the project manager should invest in developing the existing team member\'s capabilities through mentoring and training rather than competing for the shared resource. Building internal capacity creates a sustainable solution that reduces future dependency on the external expert. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    # Q1121
    (
        "Explanation: Need: guide and calm the team. Option D (Focus on the team's engagement during the next retrospective meeting.) fixes it.\"",
        "Explanation: Keywords: product complexity, maximizing delivery, collaboration approach, retrospective engagement. When a team wants to maximize delivery on a complex product, improving collaboration is best addressed through the retrospective — the dedicated forum for inspecting how the team is working and adapting their approach. Focusing the retrospective on team engagement enables a structured, team-owned discussion about what collaboration improvements will most increase throughput. (PMBOK Guide) – Seventh Edition, 2021, p. 28, 'Create a Collaborative Team Environment'\""
    ),
    # Q1122 multi-select C,D,E
    (
        'Explanation: Need: listen to people needs. Options C, D, and E (Review the communications strategy with the team regularly with a view for continuous improvement.; Send out a survey to review the preferred method, time frequency for communications.; Compile a communications management plan with input from all stakeholders and distribute for review and approval.) work together."',
        'Explanation: Keywords: globally distributed team, time zones, communications management plan, collaborative strategy. Effective global team communication requires an inclusive approach: surveying team members for their preferred methods and frequencies, compiling that input into a comprehensive communications management plan, and regularly reviewing the strategy for continuous improvement. Together these three actions create a communication framework that is built on actual team needs and remains adaptive as those needs evolve. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    # Q1123
    (
        'Explanation: Need: guide and calm the team. Option D (Engage the remote team member, empathize with them, and let them know their contribution is appreciated regardless of their remote work status.) fixes it."',
        'Explanation: Keywords: remote team member, recognition gap, empathy, contribution acknowledgment. When a remote team member feels underrecognized, the project manager must respond with direct, empathetic engagement that explicitly acknowledges the value of their contribution. Remote workers are particularly vulnerable to feeling overlooked in distributed teams, and personalized recognition from the project manager is a key factor in retaining their engagement and commitment. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    # Q1124
    (
        'Explanation: Need: guide and calm the team. Option A (Allow the team to reevaluate the tasks and determine how they should be allocated.) fixes it."',
        'Explanation: Keywords: new team member different skill set, task reallocation, team self-organization, hybrid project. When a replacement team member has a different skill profile than their predecessor, the project manager should allow the team to collectively reevaluate and reallocate tasks to match the new capability mix. This team-led approach leverages the members\' knowledge of the work and each other, producing a more accurate allocation than a top-down reassignment decision. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    # Q1125
    (
        'Explanation: Need: listen to people needs. Option A (Organize the project into multiple subsets based on business functions and deliver each subset as a component of the final product.) fixes it."',
        'Explanation: Keywords: multiyear ERP project, incremental value demonstration, final product integrity, business function subsets. To balance the sponsor\'s need to demonstrate value throughout a long ERP project with the requirement to maintain final product integrity, the project manager should structure delivery around business function subsets. Each subset provides a working increment of value while contributing to the coherent whole, satisfying both the progressive demonstration and integration requirements. (PMBOK Guide) – Seventh Edition, 2021, p. 32, \'Focus on Value\'"'
    ),
    # Q1126
    (
        'Explanation: Need: keep plans flexible. Option C (Issue a change order to the change control board (CCB) and rebaseline the schedule.) fixes it."',
        'Explanation: Keywords: behind schedule project, new project manager, CCB change order, schedule rebaselining. When a newly assigned project manager discovers the project is running behind schedule, the appropriate response is to formalize the schedule recovery or revised timeline through a change order to the CCB and rebaseline accordingly. Ad hoc resource additions or informal plan modifications bypass the governance process that ensures all changes are properly evaluated and authorized. (PMBOK Guide) – Seventh Edition, 2021, p. 50, \'Enable Change to Achieve the Envisioned Future State\'"'
    ),
    # Q1127
    (
        'Explanation: Need: watch risks early. Option D (Perform an impact analysis to see the effect on the project.) fixes it."',
        'Explanation: Keywords: resource reallocation to another project, product upgrade, impact analysis, schedule and scope assessment. When promised resources are redirected to a higher-priority project mid-execution, the project manager must first conduct an impact analysis to understand how the resource loss will affect scope, schedule, and budget. Only with this quantified impact can the project manager make informed decisions about how to respond or negotiate. (PMBOK Guide) – Seventh Edition, 2021, p. 46, \'Optimize Risk Responses\'"'
    ),
    # Q1128
    (
        'Explanation: Need: listen to people needs. Option C (Schedule a session with stakeholders to understand the impact.) fixes it."',
        'Explanation: Keywords: operating system termination, thousands of machines impacted, mid-iteration discovery, stakeholder impact session. When a major system change with broad organizational impact is discovered mid-iteration, the project manager must convene stakeholders to understand the full scope of the impact before taking any technical action. Stakeholders have the authority, context, and information needed to define the appropriate response to a change affecting thousands of machines. (PMBOK Guide) – Seventh Edition, 2021, p. 34, \'Recognize, Evaluate, and Respond to System Interactions\'"'
    ),
    # Q1129
    (
        'Explanation: Need: listen to people needs. Option D (Work with and assist the project sponsor in building and prioritizing the product backlog.) fixes it."',
        'Explanation: Keywords: CFO as project sponsor, inexperienced product owner, backlog building, agile mentoring. When the project sponsor is committed to agile but lacks product owner experience, the project manager should work alongside them to build and prioritize the backlog, transferring knowledge through collaborative practice. This approach develops the sponsor\'s product ownership capability gradually while ensuring the backlog is properly structured from the start. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    # Q1130
    (
        'Explanation: Need: listen to people needs. Option D (Define the project scope with the stakeholders and determine how formal acceptance will be obtained.) fixes it."',
        'Explanation: Keywords: mobile app project, vague competitive objective, stakeholder scope definition, formal acceptance criteria. Before building a team or beginning any development, the project manager must establish a defined scope and formal acceptance criteria with stakeholders. A goal like \'better than the competitor\' is not actionable without specific, measurable requirements that define what success looks like and how it will be validated. (PMBOK Guide) – Seventh Edition, 2021, p. 42, \'Build Quality into Processes and Deliverables\'"'
    ),
    # Q1131
    (
        'Explanation: Need: guide and calm the team. Option A (Plan a training session for the new team members not familiar with the system.) fixes it."',
        'Explanation: Keywords: new team members unfamiliar with system, evaluation criteria, training session, knowledge gap. When new team members lack the knowledge needed to perform their project role effectively, a planned training session provides the structured knowledge transfer needed to close the gap. This proactive investment in the team\'s capability prevents errors and delays that would otherwise occur as team members learn through trial and error. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    # Q1132
    (
        'Explanation: Need: listen to people needs. Option A (Ensure the content of the project report is clearly understood and request any necessary feedback.) fixes it."',
        'Explanation: Keywords: steering committee confusion, agile incremental releases, report misunderstanding, feedback solicitation. When stakeholders misinterpret project status reports about an agile project with multiple releases, the project manager must proactively verify that reports are clearly understood and invite feedback to identify and correct comprehension gaps. Steering committee confusion about project status is a communication problem that must be resolved at the reporting level rather than through changes to the delivery approach. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    # Q1133
    (
        'Explanation: Need: listen to people needs. Option D (Review and validate the scope management plan.) fixes it."',
        'Explanation: Keywords: near-complete project, late feature request, scope management plan, scope validation. When a stakeholder proposes adding features near project completion, the first step is to review and validate the scope management plan to understand the process for evaluating and deciding on scope changes at this stage. The scope management plan defines the change control procedures that must be followed before any new features can be considered. (PMBOK Guide) – Seventh Edition, 2021, p. 42, \'Build Quality into Processes and Deliverables\'"'
    ),
    # Q1134
    (
        'Explanation: Need: guide and calm the team. Option D (Request management for a high-performing team.) fixes it."',
        'Explanation: Keywords: overloaded team, low quality delivery, work-life balance culture, high-performing team request. When a team is consistently overloaded and delivering poor quality in an organization that values work-life balance, requesting a better-resourced high-performing team from management is the appropriate escalation. Asking the same overloaded team to work more undermines the organizational culture and does not address the root cause — insufficient team capacity. (PMBOK Guide) – Seventh Edition, 2021, p. 25, \'Be a Diligent, Respectful, and Caring Steward\'"'
    ),
    # Q1135
    (
        'Explanation: Need: listen to people needs. Option B (Meet with the project sponsor to better understand the strategic benefits of the project.) fixes it."',
        'Explanation: Keywords: business strategy alignment uncertainty, project charter approved, strategic benefits clarification, sponsor meeting. When the project manager is unclear whether the project\'s intended benefits align with business strategy despite an approved charter and business case, the most direct path to clarity is a conversation with the project sponsor. The sponsor is the authoritative source on the strategic context and can clarify the connection between the project\'s objectives and organizational strategy. (PMBOK Guide) – Seventh Edition, 2021, p. 32, \'Focus on Value\'"'
    ),
    # Q1136
    (
        'Explanation: Need: listen to people needs. Option D (Use the next retrospective to understand the root cause of the quality issues and have the team come up with an action plan.) fixes it."',
        'Explanation: Keywords: production defects, agile team quality issues, retrospective root cause, team-owned action plan. When recurring quality defects prevent customers from properly using delivered solutions, the retrospective is the appropriate agile forum to investigate root causes and develop a team-owned action plan. Having the team diagnose and solve their own quality problem produces more effective and sustainable improvements than solutions imposed from outside. (PMBOK Guide) – Seventh Edition, 2021, p. 42, \'Build Quality into Processes and Deliverables\'"'
    ),
    # Q1137
    (
        'Explanation: Need: keep plans flexible. Option B (Consider using digital or virtual tools to conduct the kick-off meeting to minimize geographic boundaries.) fixes it."',
        'Explanation: Keywords: multinational digital transformation, five phases, global team, virtual kickoff. For a company-wide digital transformation spanning multiple regions, requiring all participants to travel for a kickoff meeting is cost-prohibitive and logistically complex. Digital or virtual tools enable full global participation at a fraction of the cost and time, demonstrating the organization\'s commitment to the digital approach it is adopting. (PMBOK Guide) – Seventh Edition, 2021, p. 40, \'Tailor Based on Context\'"'
    ),
    # Q1138
    (
        'Explanation: Need: listen to people needs. Option A (Review the benefits realization plan with the stakeholder.) fixes it."',
        'Explanation: Keywords: new stakeholder, deliverable benefits concern, benefits realization plan, post-planning onboarding. When a new stakeholder has concerns about the benefits of specific deliverables after the planning phase, the project manager should review the benefits realization plan with them directly. This plan documents the expected benefits and how they will be realized — sharing it addresses the stakeholder\'s concern with evidence and integrates them into the existing planning work. (PMBOK Guide) – Seventh Edition, 2021, p. 32, \'Focus on Value\'"'
    ),
    # Q1139
    (
        'Explanation: Need: listen to people needs. Option C (Perform lessons learned to ensure the issue does not happen again.) fixes it."',
        'Explanation: Keywords: quality issues resolved, project back on track, lessons learned, recurrence prevention. After a quality problem has been identified and resolved, performing lessons learned captures the root cause and corrective actions while they are fresh, creating organizational knowledge that prevents recurrence in this project and future ones. Skipping this step when the project is back on track wastes the learning opportunity the quality incident provides. (PMBOK Guide) – Seventh Edition, 2021, p. 48, \'Embrace Adaptability and Resiliency\'"'
    ),
    # Q1140
    (
        'Explanation: Need: listen to people needs. Option D (Use a hybrid model to combine predictive and adaptive life cycles.) fixes it."',
        'Explanation: Keywords: three-phase construction project, structured phases, adaptive flexibility, hybrid model. When a project has well-defined phases requiring predictive planning but also needs to accommodate new data and customer input as it progresses, a hybrid model is the appropriate choice. It provides the structured baseline each phase needs while incorporating the adaptive flexibility to respond to new information throughout the project lifecycle. (PMBOK Guide) – Seventh Edition, 2021, p. 40, \'Tailor Based on Context\'"'
    ),
    # Q1141
    (
        'Explanation: Need: listen to people needs. Option B (Assist the team with identifying the minimum viable product (MVP) to validate assumptions.) fixes it."',
        'Explanation: Keywords: new technology, uncertain marketability, team unfamiliarity, MVP assumption validation. When both the team and the customer are uncertain about a new technology product\'s reception and approach, an MVP allows the critical assumptions driving the project to be tested quickly with real users. Identifying the MVP first focuses limited resources on the highest-value learning rather than committing to full development before key uncertainties are resolved. (PMBOK Guide) – Seventh Edition, 2021, p. 32, \'Focus on Value\'"'
    ),
    # Q1142
    (
        'Explanation: Need: guide and calm the team. Option A (Inform the functional manager that self-organization includes task allocation.) fixes it."',
        'Explanation: Keywords: functional manager interference, self-organizing team, task allocation authority, team autonomy. When a functional manager attempts to control how a self-organizing agile team allocates tasks, the project manager must clearly explain that self-organization includes responsibility for task allocation. Protecting the team\'s autonomy over how they divide and assign work is essential for maintaining the accountability and collaborative dynamic that make self-organizing teams effective. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
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
