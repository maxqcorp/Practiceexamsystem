MD_FILE = './src/imports/project-management-questions-1.md'

with open(MD_FILE, 'r', encoding='utf-8') as f:
    content = f.read()

replacements = [
    # Q951
    (
        'Explanation: Need: protect benefits for users. Option D (Begin discussions with other functional managers and meet with the accounting manager later.) fixes it."',
        'Explanation: Keywords: sequential dependency, accounting manager unavailability, schedule optimization, parallel planning. When a key resource is temporarily unavailable but not the only input required, the project manager should advance parallel planning activities and incorporate the missing input when it becomes available. Starting discussions with other functional managers keeps momentum and avoids a full stop that would compress the overall schedule. (PMBOK Guide) – Seventh Edition, 2021, p. 32, \'Focus on Value\'"'
    ),
    # Q952
    (
        'Explanation: Need: guide and calm the team. Option A (The project manager must ensure that the knowledge transfer occurred and that this is also included in the organizational process assets (OPAs),) fixes it."',
        'Explanation: Keywords: project closure, knowledge transfer, organizational process assets, institutional memory. The project manager is responsible for ensuring all project knowledge is transferred and captured in organizational process assets before experienced team members depart. This stewardship responsibility protects the organization\'s ability to sustain the delivered product and leverage lessons learned in future projects. (PMBOK Guide) – Seventh Edition, 2021, p. 25, \'Be a Diligent, Respectful, and Caring Steward\'"'
    ),
    # Q953
    (
        'Explanation: Need: guide and calm the team. Option C (Work with the team to determine appropriate project methods and practices and implement them.) fixes it."',
        'Explanation: Keywords: predictive team, agile tools needed, methodology flexibility, tailored approach. When a predictive team encounters a situation that would benefit from agile tools, the project manager should work collaboratively with the team to select and implement appropriate methods rather than rigidly adhering to processes that do not serve the project\'s current needs. This adaptive tailoring respects both team expertise and project context. (PMBOK Guide) – Seventh Edition, 2021, p. 40, \'Tailor Based on Context\'"'
    ),
    # Q954
    (
        'Explanation: Need: guide and calm the team. Option C (Have a discussion with the team on the approach and come to a decision on when the daily standups should be.) fixes it."',
        'Explanation: Keywords: timezone conflict, daily standup scheduling, team consensus, distributed agile team. When a timezone difference creates a scheduling conflict for agile ceremonies, the project manager should facilitate a team discussion to reach a consensus on a time that balances participation across all locations. Imposing a single time without input from the affected team members violates the collaborative spirit of agile practice. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    # Q955
    (
        'Explanation: Need: guide and calm the team. Option A (Apply a root-cause analysis on the data breaches.) fixes it."',
        'Explanation: Keywords: recurring data breaches, mandatory training completed, root cause analysis, compliance gap. When security breaches persist despite mandatory training, the training itself is not the root cause — a deeper systemic issue exists. Root cause analysis identifies the actual driver of the breach so the project manager can implement a targeted and effective corrective action rather than repeating ineffective interventions. (PMBOK Guide) – Seventh Edition, 2021, p. 34, \'Recognize, Evaluate, and Respond to System Interactions\'"'
    ),
    # Q956
    (
        'Explanation: Need: guide and calm the team. Option D (Find ways to reduce the tension, increase cooperation, and understand the emotions of all team members involved.) fixes it."',
        'Explanation: Keywords: recurring conflict, procurement team lead, emotional intelligence, cooperation building. When a team lead repeatedly causes conflict and team members question their suitability, the project manager must address the emotional and relational dynamics holistically rather than assigning blame or issuing warnings. Understanding the emotions of all involved parties and working to reduce tension and build cooperation creates a sustainable resolution rather than a punitive one. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    # Q957
    (
        'Explanation: Need: listen to people needs. Option D (Analyze the impact of this change and present the options to the senior manager.) fixes it."',
        'Explanation: Keywords: sponsor scope addition, predictive government project, impact analysis, options presentation. When a significant new feature is requested mid-project in a predictive environment, the project manager must analyze the full impact on scope, schedule, cost, and risk, then present the sponsor with clear options rather than accepting or refusing unilaterally. This enables an informed decision by the authority responsible for the project\'s strategic direction. (PMBOK Guide) – Seventh Edition, 2021, p. 50, \'Enable Change to Achieve the Envisioned Future State\'"'
    ),
    # Q958
    (
        'Explanation: Need: listen to people needs. Option D (Allocate time to mentor the stakeholder in the selected project approach.) fixes it."',
        'Explanation: Keywords: predictive-only experience, hybrid project, stakeholder mentoring, methodology onboarding. A stakeholder who is highly competent in their domain but unfamiliar with the selected hybrid approach needs tailored mentoring rather than being expected to adapt independently. Investing time to mentor this stakeholder protects project collaboration quality and ensures their contributions are aligned with the methodology being used. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    # Q959
    (
        'Explanation: Need: guide and calm the team. Option C (Invest in coaching and training for all project team members.) fixes it."',
        'Explanation: Keywords: low team competence, performance risk, coaching investment, capability development. When widespread competence gaps are creating issues that risk project performance and viability, the project manager must invest in coaching and training to elevate the team\'s capability across the board. Targeted capability building is more sustainable than escalation and addresses the root cause rather than the symptoms. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    # Q960
    (
        'Explanation: Need: listen to people needs. Option B (Use a password-enabled audio/video product,) fixes it."',
        'Explanation: Keywords: confidential patient data, virtual meetings, secure communication tool, data protection. When meetings will include confidential patient information, the project manager must select a communication tool that provides authenticated access controls such as password protection. This protects sensitive data from unauthorized access during transmission while enabling effective virtual collaboration. (PMBOK Guide) – Seventh Edition, 2021, p. 25, \'Be a Diligent, Respectful, and Caring Steward\'"'
    ),
    # Q961
    (
        'Explanation: Need: guide and calm the team. Option B (Review this method with the team.) fixes it."',
        'Explanation: Keywords: estimation change suggestion, feature-based estimation, team decision, agile planning. When a team member proposes a different estimation approach, the project manager should facilitate a team review of the suggestion rather than accepting or rejecting it unilaterally. The team\'s collective evaluation produces the best-informed decision about whether the proposed method improves their planning accuracy. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    # Q962
    (
        'Explanation: Need: listen to people needs. Option D (A hybrid approach will work, using agile for software development and a predictive approach for the hardware deliveries.) fixes it."',
        'Explanation: Keywords: dual deliverables, hardware fixed specifications, software high uncertainty, hybrid approach. When a project has two fundamentally different types of deliverables — one well-defined and one uncertain — a hybrid approach that applies the right methodology to each is the appropriate choice. Predictive planning suits the hardware with fixed specs, while agile suits the software requiring user experience iteration. (PMBOK Guide) – Seventh Edition, 2021, p. 40, \'Tailor Based on Context\'"'
    ),
    # Q963
    (
        'Explanation: Need: guide and calm the team. Option D (Include buffer time in the schedule to absorb future delays.) fixes it."',
        'Explanation: Keywords: inexperienced team, repeated deadline extension requests, schedule buffer, contingency planning. When an inexperienced team has already requested deadline extensions, the project manager must proactively add buffer time to the schedule to account for the team\'s demonstrated need for extra time on increments. This realistic adjustment prevents repeated rescheduling and sets sustainable expectations for delivery. (PMBOK Guide) – Seventh Edition, 2021, p. 46, \'Optimize Risk Responses\'"'
    ),
    # Q964
    (
        'Explanation: Need: listen to people needs. Option D (Agree up front on a minimum viable product (MVP), establish deadlines for review, and run the project with a backlog and weekly sprints.) fixes it."',
        'Explanation: Keywords: unclear requirements, no product owner, fixed budget and deadline, MVP agreement. When requirements are unclear and the client cannot commit a product owner, the project manager must establish a structured agile framework with a defined MVP and regular review deadlines so that value can be demonstrated incrementally and client feedback is captured systematically. This adapts the approach to the client\'s constraints without abandoning agile practices. (PMBOK Guide) – Seventh Edition, 2021, p. 32, \'Focus on Value\'"'
    ),
    # Q965
    (
        'Explanation: Need: guide and calm the team. Option A (Recommend that the product owner reviews the backlog refinement processes.) fixes it."',
        'Explanation: Keywords: unclear requirements, stalled iterations, backlog refinement, product owner responsibility. When a team cannot complete iterations due to unclear requirements over multiple cycles, the root cause is typically inadequate backlog refinement. The project leader should recommend that the product owner review and improve the refinement process so that stories entering each iteration are sufficiently detailed for the team to execute. (PMBOK Guide) – Seventh Edition, 2021, p. 42, \'Build Quality into Processes and Deliverables\'"'
    ),
    # Q966
    (
        'Explanation: Need: guide and calm the team. Option D (Determine what the problem is and develop an action plan.) fixes it."',
        'Explanation: Keywords: connectivity issues, virtual team, root cause investigation, action plan. When virtual team members experience recurring connectivity problems, the project manager must investigate the actual root cause before implementing any solution. Understanding the specific nature of the problem allows for a targeted action plan that addresses the real issue rather than applying generic workarounds that may not resolve it. (PMBOK Guide) – Seventh Edition, 2021, p. 34, \'Recognize, Evaluate, and Respond to System Interactions\'"'
    ),
    # Q967
    (
        'Explanation: Need: guide and calm the team. Option B (Reassess the team\'s hours collaboratively so that the team is not impeded by the issue.) fixes it."',
        'Explanation: Keywords: personal commitments, previously agreed hours, collaborative rescheduling, team accommodation. When a team member\'s personal circumstances change and the original agreed hours are no longer workable, the project manager should reassess working hours collaboratively with the team. This respectful, adaptive approach maintains the team member\'s contribution while minimizing the schedule impact on others. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    # Q968
    (
        'Explanation: Need: listen to people needs. Option B (Include the use of tools and monitoring of their benefits in regular status reports and the communications management plan.) fixes it."',
        'Explanation: Keywords: adaptive tools rollout, low stakeholder awareness, change management, benefits communication. When implementing new adaptive tools in an organization with low awareness, the project manager should embed tool usage and benefits monitoring in routine status reporting and the communications management plan. This ensures stakeholders receive regular, transparent updates on the transition without requiring a separate change initiative. (PMBOK Guide) – Seventh Edition, 2021, p. 50, \'Enable Change to Achieve the Envisioned Future State\'"'
    ),
    # Q969
    (
        'Explanation: Need: guide and calm the team. Option D (Conduct an alternative analysis to decide whether to hire people directly or contract with a company to do the job.) fixes it."',
        'Explanation: Keywords: call center staffing, build versus buy decision, alternative analysis, resource strategy. Before deciding how to staff a call center, the project manager must conduct an alternative analysis comparing the costs, risks, and benefits of direct hiring versus contracting. This systematic evaluation prevents premature commitment to either option and ensures the selected approach is the most appropriate for the project\'s needs. (PMBOK Guide) – Seventh Edition, 2021, p. 40, \'Tailor Based on Context\'"'
    ),
    # Q970
    (
        'Explanation: Need: guide and calm the team. Option B (Meet with the designer to share the current status and develop a solution to complete the task.) fixes it."',
        'Explanation: Keywords: release deadline, designer blocker, direct engagement, collaborative solution. When a critical release is blocked by a specific designer\'s pending task, the project manager should meet directly with that designer to share the urgency and jointly develop a solution. This targeted, collaborative approach is more effective than escalating to the team manager, which adds an unnecessary layer and may not resolve the problem as quickly. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    # Q971
    (
        'Explanation: Need: guide and calm the team. Option A (Maintain a central repository of artifacts with a version control system.) fixes it."',
        'Explanation: Keywords: distributed team, version tracking difficulty, central repository, artifact management. When a geographically distributed team struggles to track changes and progress despite regular communication, the root cause is the absence of a centralized, version-controlled repository. A single source of truth with version control eliminates the confusion of conflicting document versions and ensures all team members work from the same current information. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    # Q972
    (
        'Explanation: Need: keep plans flexible. Option B (Have a direct talk with the functional manager to understand the reasons behind their attitude.) fixes it."',
        'Explanation: Keywords: functional manager resistance, staff assignment delays, direct conversation, root cause understanding. When a functional manager consistently withholds requested staff without explanation, the project manager must have a direct conversation to understand the underlying reasons. Escalating without first seeking to understand the manager\'s perspective misses the opportunity to resolve a potentially legitimate concern and unnecessarily adversarializes the relationship. (PMBOK Guide) – Seventh Edition, 2021, p. 34, \'Recognize, Evaluate, and Respond to System Interactions\'"'
    ),
    # Q973
    (
        'Explanation: Need: guide and calm the team. Option B (Have the team meet on a regular basis and share their experiences, challenges, and lessons learned.) fixes it."',
        'Explanation: Keywords: tacit knowledge transfer, outgoing team member, experiential learning, knowledge sharing sessions. Tacit knowledge — the kind embedded in experience and intuition rather than documentation — cannot be transferred through written materials alone. Regular team meetings where experiences and challenges are openly discussed create the social learning environment in which tacit knowledge naturally passes from experienced to new members. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    # Q974
    (
        'Explanation: Need: listen to people needs. Option A (Acknowledge the stakeholders\' concerns with open dialogues and realign the project with stakeholder requirements and past lessons learned.) fixes it."',
        'Explanation: Keywords: remodeling project, missing original documentation, stakeholder skepticism, open dialogue. When stakeholders are hesitant due to an absence of original design records, the project manager must acknowledge their concerns genuinely and facilitate open dialogue about requirements and relevant lessons learned from comparable work. This transparent engagement builds the confidence needed to secure stakeholder support for a project that carries inherent uncertainty. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    # Q975
    (
        'Explanation: Need: protect value and acceptance. Option A (Monitored progress in achieving the business value throughout the project) fixes it."',
        'Explanation: Keywords: brand image improvement, business value gap, monitoring throughout project, value realization. When a project goal is to improve company reputation, the project manager must continuously monitor whether the project activities are actually producing the intended business value rather than waiting until closure to assess outcomes. Ongoing business value monitoring allows timely course corrections before it is too late to influence results. (PMBOK Guide) – Seventh Edition, 2021, p. 32, \'Focus on Value\'"'
    ),
    # Q976
    (
        'Explanation: Need: keep plans flexible. Option D (Meet privately with the risk owners and work with them to address any impediments to the risk responses.) fixes it."',
        'Explanation: Keywords: risk response non-implementation, risk owner accountability, private coaching, impediment removal. When risk owners have not implemented agreed-upon risk responses, the project manager must first understand why through a private discussion rather than reporting them or reassigning their tasks. The reasons may reveal legitimate impediments that the project manager can help remove, turning the situation into a coaching opportunity rather than a disciplinary one. (PMBOK Guide) – Seventh Edition, 2021, p. 46, \'Optimize Risk Responses\'"'
    ),
    # Q977
    (
        'Explanation: Need: guide and calm the team. Option D (Recommend the option to the product owner for consideration.) fixes it."',
        'Explanation: Keywords: low-cost software alternative, scope reduction opportunity, product owner authority, backlog decision. When a team discovers a commercial product that could significantly reduce development scope, the project manager should channel this through the product owner who has authority to evaluate and decide on backlog items. The product owner is the appropriate decision-maker for what to build versus buy, and the project manager\'s role is to ensure the option is properly considered. (PMBOK Guide) – Seventh Edition, 2021, p. 32, \'Focus on Value\'"'
    ),
    # Q978
    (
        'Explanation: Need: listen to people needs. Option D (Confirm the definition of done (DoD) has been met.) fixes it."',
        'Explanation: Keywords: project nearing completion, sponsor assignment pressure, definition of done, proper closure. Before transitioning to a new project, the project manager must verify that all project deliverables satisfy the agreed definition of done. Confirming DoD completion ensures the project is genuinely finished — not just apparently done — before resources and attention shift to a new initiative. (PMBOK Guide) – Seventh Edition, 2021, p. 42, \'Build Quality into Processes and Deliverables\'"'
    ),
    # Q979
    (
        'Explanation: Need: listen to people needs. Option B (Review the communications management plan.) fixes it."',
        'Explanation: Keywords: CEO communication overload, irrelevant content, report frequency, communications management plan review. When a senior stakeholder receives too many reports with irrelevant content, the root cause is a communications management plan that was not tailored to their actual information needs. Reviewing and updating the plan — rather than making ad hoc changes to report format — produces a sustainable fix that serves all stakeholders appropriately. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    # Q980
    (
        'Explanation: Need: listen to people needs. Option D (Negotiate with the project sponsor to develop a mutually beneficial solution.) fixes it."',
        'Explanation: Keywords: sponsor disagreement, implementation conflict, negotiation, mutually beneficial solution. When the project manager and sponsor disagree on how to implement a key technology, negotiation to find a jointly acceptable solution is the appropriate first response. This preserves the relationship, respects the sponsor\'s authority, and produces a solution with organizational backing rather than a unilaterally imposed approach that may lack support. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    # Q981
    (
        'Explanation: Need: guide and calm the team. Option A (Coordinate with team members to define and communicate ways of working, roles and responsibilities, scheduling, time zone, and culturalobservance information.) fixes it."',
        'Explanation: Keywords: virtual global team, SMEs from different divisions, ways of working, cultural observance. A virtual team spanning multiple countries and divisions needs explicit, co-created agreements on how they will work together before collaboration can be effective. Coordinating to define and communicate working norms, time zones, and cultural observances prevents the misunderstandings that arise when diverse teams operate under different unstated assumptions. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    # Q982
    (
        'Explanation: Need: listen to people needs. Option B (Engage the project stakeholders.) fixes it."',
        'Explanation: Keywords: quality assurance vendor, rate over budget, stakeholder engagement, procurement decision. When a preferred vendor\'s rates exceed the project budget, the project manager should engage stakeholders rather than unilaterally resolving the issue, because stakeholders may have budget flexibility, alternative vendor knowledge, or approval authority that the project manager lacks. Stakeholder engagement ensures the decision is made with appropriate organizational input. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    # Q983
    (
        'Explanation: Need: guide and calm the team. Option D (Ensure that coaching meetings are in place for this team member within the project timeline.) fixes it."',
        'Explanation: Keywords: inexperienced new team member, coaching plan, ongoing support, skill development. When the only available resource lacks required experience, the project manager must embed structured coaching sessions within the project timeline rather than leaving the member to learn through trial and error. Scheduled coaching provides consistent guidance, reduces error risk, and builds the member\'s capability progressively throughout the project. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    # Q984
    (
        'Explanation: Need: listen to people needs. Option D (Explain that more features can be planned in upcoming Iterations and begin building the product.) fixes it."',
        'Explanation: Keywords: planning phase extension, client feature creep, agile iteration, progressive elaboration. When stakeholders keep requesting planning meetings to add features, the project manager should redirect them to the iterative process and begin building with what is clear and agreed. Features not yet detailed can be addressed in future iterations, preventing planning paralysis while still leaving the door open to future refinement. (PMBOK Guide) – Seventh Edition, 2021, p. 48, \'Embrace Adaptability and Resiliency\'"'
    ),
    # Q985
    (
        'Explanation: Need: guide and calm the team. Option A (Include this restriction as a ground rule and ensure all team members are familiar with it by reviewing the ground rules at the end of everyiteration.) fixes it."',
        'Explanation: Keywords: confidentiality risk, agile project, ground rules, iterative reinforcement. Addressing information disclosure risk through a team ground rule that is reviewed at the end of every iteration ensures the restriction is embedded into the team\'s operating norms rather than being a one-time reminder that gets forgotten. Regular reinforcement of the ground rule keeps confidentiality expectations visible and maintained throughout the project. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    # Q986
    (
        'Explanation: Need: guide and calm the team. Option A (Meet with each team member separately and apply an appropriate approach with each one.) fixes it."',
        'Explanation: Keywords: lack of discipline, individualized leadership, motivational barriers, tailored approach. When team members show varying levels of discipline and focus, a blanket response will not be effective because the underlying causes differ by individual. Meeting separately with each member allows the project manager to understand their specific barriers and apply a tailored motivational approach that addresses each person\'s actual situation. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    # Q987
    (
        'Explanation: Need: guide and calm the team. Option A (Develop the team members to work as a cross-functional team.) fixes it."',
        'Explanation: Keywords: lessons learned review, knowledge gaps, cross-functional development, team capability. When lessons learned reveal that a team lacks the cross-functional knowledge needed for a new project, investing in developing those capabilities within the existing team is more effective than seeking replacement members. Cross-functional development builds team resilience and reduces dependence on specific specialists for future challenges. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    # Q988
    (
        'Explanation: Need: control changes and baselines. Option C (Discuss the proposed changes with the PMO.) fixes it."',
        'Explanation: Keywords: governance deviation, PMO policy conflict, project-specific needs, collaborative discussion. When a project manager believes project-specific governance requirements justify departing from PMO policies, the appropriate path is to discuss the proposed changes with the PMO rather than implementing them unilaterally. This collaborative approach may gain formal approval for the deviation while maintaining organizational alignment. (PMBOK Guide) – Seventh Edition, 2021, p. 50, \'Enable Change to Achieve the Envisioned Future State\'"'
    ),
    # Q989
    (
        'Explanation: Need: listen to people needs. Option D (Keep project artifacts up-to-date and accessible to all stakeholders.) fixes it."',
        'Explanation: Keywords: performance data as reference, future projects, artifact accessibility, knowledge preservation. For project data to serve as a reference for future projects, it must be stored in a form that is current, complete, and readily accessible to those who will need it. Keeping artifacts updated and accessible throughout the project lifecycle ensures the knowledge is available when future teams need it — not just at project close. (PMBOK Guide) – Seventh Edition, 2021, p. 25, \'Be a Diligent, Respectful, and Caring Steward\'"'
    ),
    # Q990
    (
        'Explanation: Need: guide and calm the team. Option B (Complying with new regulations) fixes it."',
        'Explanation: Keywords: regulatory compliance, program requirements prioritization, fine avoidance, legal obligation. When a program must prioritize among multiple requirement types, compliance with applicable regulations takes precedence because failure to comply carries legal and financial penalties that other requirement types do not. Non-compliance risks including fines are non-negotiable constraints that must be addressed before pursuing discretionary improvements. (PMBOK Guide) – Seventh Edition, 2021, p. 25, \'Be a Diligent, Respectful, and Caring Steward\'"'
    ),
    # Q991
    (
        'Explanation: Need: guide and calm the team. Option B (Set up a meeting with the team member to review the team charter.) fixes it."',
        'Explanation: Keywords: team charter violation, post-merger team, direct conversation, behavioral alignment. When a team member consistently ignores a specific team charter rule, a direct one-on-one meeting is the most appropriate first response. This private discussion allows the project manager to understand whether the behavior stems from unawareness, disagreement, or other reasons, and to reinforce the expectation without public embarrassment. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    # Q992
    (
        'Explanation: Need: listen to people needs. Option A (Facilitate a meeting with the stakeholders and product owner to clarify the new need,) fixes it."',
        'Explanation: Keywords: stakeholder disagreement, new agile requirement, product owner involvement, facilitated clarification. When two key stakeholders disagree about a major new requirement, the project manager must bring them together with the product owner to clarify the need and reach a shared understanding. The product owner\'s presence is essential because they are responsible for making the final backlog prioritization decision and can arbitrate competing stakeholder preferences. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    # Q993
    (
        'Explanation: Need: listen to people needs. Option D (Work with the team and the product owner to define the next steps.) fixes it."',
        'Explanation: Keywords: product delivery delay, client complaints, inventory issue, product owner collaboration. When a confirmed delivery delay is linked to an inventory and availability problem, the project manager should work with both the team and the product owner to define the next steps. The product owner has the stakeholder relationships and product knowledge to help shape the response, while the team has the operational knowledge to execute it. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    # Q994
    (
        'Explanation: Need: listen to people needs. Option A (Have a high-level plan for incremental deliveries and get the customer\'s feedback as early as possible.) fixes it."',
        'Explanation: Keywords: quick public deployment, experienced team, stakeholder support, incremental delivery strategy. When a solution needs to reach the public quickly with strong stakeholder support, an incremental delivery strategy that gets early customer feedback is the most effective approach. High-level planning with frequent feedback loops allows the team to validate direction early and adapt before investment grows too large. (PMBOK Guide) – Seventh Edition, 2021, p. 32, \'Focus on Value\'"'
    ),
    # Q995
    (
        'Explanation: Need: guide and calm the team. Option B (Determine the appropriate approach) fixes it."',
        'Explanation: Keywords: performance evaluation, no existing metrics, appropriate approach selection, 360-degree input. When performance metrics do not exist and additional input is needed from the team, the project manager must first determine the most appropriate approach for gathering and applying that input before proceeding. Jumping to evaluation without a defensible approach risks producing results that are inconsistent or unfair. (PMBOK Guide) – Seventh Edition, 2021, p. 40, \'Tailor Based on Context\'"'
    ),
    # Q996
    (
        'Explanation: Need: secure people or vendors. Option B (Evaluate the procurement contract to determine the agreed-upon specifications.) fixes it."',
        'Explanation: Keywords: measurement dispute, cross-country supplier, contract specifications, procurement review. When a supplier insists their delivery meets specifications but the recipient disagrees, the project manager must reference the procurement contract as the authoritative document defining what was actually agreed. This objective review resolves the dispute based on documented commitments rather than competing interpretations. (PMBOK Guide) – Seventh Edition, 2021, p. 34, \'Recognize, Evaluate, and Respond to System Interactions\'"'
    ),
    # Q997
    (
        'Explanation: Need: keep plans flexible. Option C (Plan the task delivery with the contractor or vendor, highlighting the criticality of the current situation,) fixes it."',
        'Explanation: Keywords: contractor delivery uncertainty, hybrid project, schedule criticality communication, collaborative planning. When a contractor has not confirmed they can meet the schedule, the project manager should engage them directly in delivery planning and clearly communicate the criticality of the timeline. This collaborative approach aligns the contractor with project priorities and creates shared accountability for the schedule outcome. (PMBOK Guide) – Seventh Edition, 2021, p. 34, \'Recognize, Evaluate, and Respond to System Interactions\'"'
    ),
    # Q998
    (
        'Explanation: Need: watch risks early. Option C (Issue log) fixes it."',
        'Explanation: Keywords: operations concern, hatchery project, active problem, issue log documentation. A concern raised by the operations group about a current situation that could not be addressed represents an active issue requiring ongoing tracking rather than a future risk. The issue log is the correct document for recording problems that are currently present and require management attention and resolution. (PMBOK Guide) – Seventh Edition, 2021, p. 34, \'Recognize, Evaluate, and Respond to System Interactions\'"'
    ),
    # Q999
    (
        'Explanation: Need: guide and calm the team. Option A (Ask the team to focus on and deliver only the agreed-upon features.) fixes it."',
        'Explanation: Keywords: scope creep, gold plating, EV cost variance, agreed features only. When a team adds features not included in requirements, they create cost overruns and delivery risk without explicit stakeholder approval — a classic scope creep pattern called gold plating. The project manager must redirect the team to deliver only what was agreed upon, protecting the cost baseline while respecting the change control process. (PMBOK Guide) – Seventh Edition, 2021, p. 42, \'Build Quality into Processes and Deliverables\'"'
    ),
    # Q1000
    (
        'Explanation: Need: guide and calm the team. Option A (Support the team member by removing the blockers and impediments.) fixes it."',
        'Explanation: Keywords: daily standup, blockers and impediments, servant leadership, impediment removal. When a team member surfaces blockers in a standup, the project lead\'s primary responsibility is to actively support them by removing those impediments. This servant leadership action clears the path for the team member to continue their work and demonstrates the project manager\'s commitment to enabling team productivity. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    # Q1001
    (
        'Explanation: Need: listen to people needs. Option C (Coordinate with the stakeholders to ensure the benefits management plan is in alignment with the goals.) fixes it."',
        'Explanation: Keywords: benefits management plan, stakeholder misalignment, value understanding, goal alignment. When stakeholders do not understand how a project delivers value, the project manager should coordinate with them to verify that the benefits management plan reflects their goals and that they understand how the identified benefits connect to organizational objectives. This alignment conversation resolves misunderstanding before the system goes live. (PMBOK Guide) – Seventh Edition, 2021, p. 32, \'Focus on Value\'"'
    ),
    # Q1002
    (
        'Explanation: Need: guide and calm the team. Option A (Engage with the functional manager to discuss details to obtain the required support.) fixes it."',
        'Explanation: Keywords: testing resources unavailable, matrix organization, functional manager engagement, resource negotiation. In a matrix organization, the functional manager controls resource availability and must be engaged directly to negotiate and secure the testing support the project needs. Bypassing the functional manager by going to the sponsor or procurement without first attempting this conversation is premature and may unnecessarily escalate the situation. (PMBOK Guide) – Seventh Edition, 2021, p. 34, \'Recognize, Evaluate, and Respond to System Interactions\'"'
    ),
    # Q1003
    (
        'Explanation: Need: guide and calm the team. Option D (Schedule crashing) fixes it."',
        'Explanation: Keywords: delayed project, extra resources added, overtime approved, schedule crashing technique. Adding extra resources to activities and approving overtime are the defining characteristics of schedule crashing — a compression technique that reduces duration by increasing cost. This is distinct from fast tracking, which compresses the schedule by overlapping activities rather than adding resources. (PMBOK Guide) – Seventh Edition, 2021, p. 40, \'Tailor Based on Context\'"'
    ),
    # Q1004
    (
        'Explanation: Need: guide and calm the team. Option C (Videoconferencing) fixes it."',
        'Explanation: Keywords: global distributed teams, team interactions, rich communication medium, kickoff meeting. For a global program involving distributed teams, videoconferencing provides the richest communication medium by combining audio and visual cues, enabling more effective team interaction than text-based or audio-only alternatives. This supports the relationship-building that is critical at program kickoff when team dynamics and collaborative norms are being established. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    # Q1005
    (
        'Explanation: Need: listen to people needs. Option A (Ask the client how the project will affect the client\'s organization and recommend that all impacted parties be involved.) fixes it."',
        'Explanation: Keywords: enterprise-wide software, executive-only planning, impacted stakeholders, inclusive engagement recommendation. When a software project will be deployed across all levels of an organization but the client only wants executive involvement in planning, the project manager must recommend including all impacted parties. Excluding operational stakeholders from planning creates the risk of delivering a solution that executives approved but frontline users cannot effectively adopt. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    # Q1006
    (
        'Explanation: Need: listen to people needs. Option C (Leverage hybrid methods as the project has a blend of work that needs to bring in both agile and predictive methods,) fixes it."',
        'Explanation: Keywords: new technology service, business process reengineering, hybrid methodology, blended project work. When a project involves both novel software development and business process reengineering across operations teams, a hybrid approach is most appropriate because the two workstreams have fundamentally different levels of certainty and collaboration requirements. Leveraging both agile and predictive methods allows each workstream to be managed with the approach best suited to its nature. (PMBOK Guide) – Seventh Edition, 2021, p. 40, \'Tailor Based on Context\'"'
    ),
    # Q1007
    (
        'Explanation: Need: guide and calm the team. Option D (Open up to the team to work collaboratively to achieve the outcomes.) fixes it."',
        'Explanation: Keywords: information hoarding, agile project, transparent collaboration, project lead behavior. In an agile environment built on transparency and collaboration, a project lead withholding vital product information from the team creates silos that directly undermine the approach and introduce risk. Opening up and sharing information collaboratively is not just a preference — it is a prerequisite for agile execution to function as intended. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    # Q1008
    (
        'Explanation: Need: guide and calm the team. Option D (Support the outcome of the architects\' agreement.) fixes it."',
        'Explanation: Keywords: architect disagreement resolved, module ownership agreement, team consensus, project manager support. When team members who are best positioned to make a technical decision reach their own resolution and the team supports it, the project manager should respect and support that outcome rather than reopening the discussion. Overriding a self-organized resolution undermines team autonomy and the servant leadership model. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    # Q1009
    (
        'Explanation: Need: listen to people needs. Option B (Ask the customer to discuss these changes with the product owner.) fixes it."',
        'Explanation: Keywords: customer priority changes, direct team access, product owner role, change management. When a customer is bypassing the product owner by directly changing priorities with team members, the project manager must redirect that communication through the product owner. The product owner is the single authority for managing scope and priorities, and direct customer-to-team interactions undermine this governance structure and disrupt team focus. (PMBOK Guide) – Seventh Edition, 2021, p. 34, \'Recognize, Evaluate, and Respond to System Interactions\'"'
    ),
    # Q1010
    (
        'Explanation: Need: listen to people needs. Option D (Encourage the whole team to be empowered and accountable for the decisions made according to their roles,) fixes it."',
        'Explanation: Keywords: acceptance criteria failures, backlog item sizing, servant leader, team empowerment and accountability. When recurring sprint failures stem from both the development team and the product owner operating outside their proper roles, the servant leader must reinforce the empowerment and accountability that each role carries. Encouraging the team to own their decisions according to defined roles — rather than extending sprints or overriding process — produces the structural fix that prevents recurrence. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
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
