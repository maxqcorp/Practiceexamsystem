MD_FILE = './src/imports/project-management-questions-1.md'

with open(MD_FILE, 'r', encoding='utf-8') as f:
    content = f.read()

replacements = [
    # Q1593
    (
        "Explanation: Need: listen to people needs. Option C (Informal verbal communication, such as a conversation) fixes it.\"",
        "Explanation: Keywords: end of first sprint, junior team member not performing, form of communication. Performance conversations with individual team members should begin informally — a private, conversational approach creates psychological safety that enables honest dialogue. Informal verbal communication is the most appropriate first step when addressing individual performance concerns because it is personal, immediate, and respectful, preserving the team member's dignity while setting the foundation for improvement. (PMBOK Guide) – Seventh Edition, 2021, p. 36, 'Demonstrate Leadership Behaviors'\""
    ),
    # Q1594
    (
        "Explanation: Need: listen to people needs. Option A (Stakeholder engagement plan) fixes it.\"",
        "Explanation: Keywords: energy plant completed, local community protests, prior consultation not done, what to verify first. When stakeholders take action after a project is completed because they were not consulted, the project manager should first verify the stakeholder engagement plan. This document should have identified the local community as a stakeholder and defined how they would be engaged — its absence or inadequacy would explain why the required consultation was never conducted. (PMBOK Guide) – Seventh Edition, 2021, p. 30, 'Effectively Engage with Stakeholders'\""
    ),
    # Q1595
    (
        "Explanation: Need: guide and calm the team. Option D (Recommend a different estimation method in the retrospective.) fixes it.\"",
        "Explanation: Keywords: new agile team, high velocity variation, every sprint delivers less than committed, estimation accuracy. When velocity is highly variable and consistently below commitment, the estimation method itself is likely the root cause. The retrospective is the appropriate venue to surface this pattern and propose a different approach — whether story points, t-shirt sizing, or mob estimation — since it is the ceremony designed for reflective process improvement with full team participation. (PMBOK Guide) – Seventh Edition, 2021, p. 40, 'Tailor Based on Context'\""
    ),
    # Q1596
    (
        "Explanation: Need: guide and calm the team. Option B (Contact the senior manager and discuss their needs.) fixes it.\"",
        "Explanation: Keywords: sprint review planning, senior manager requests different template than PMO, kanban board in use. Before modifying any reporting approach, the project manager should understand what the senior manager actually needs — the specific information, frequency, or format that they require. Contacting the manager directly surfaces the real need, which may be addressable through existing tools like the kanban board without creating a new reporting burden. (PMBOK Guide) – Seventh Edition, 2021, p. 30, 'Effectively Engage with Stakeholders'\""
    ),
    # Q1597
    (
        "Explanation: Need: listen to people needs. Option C (Organize more frequent sprint reviews with a broader audience.) fixes it.\"",
        "Explanation: Keywords: agile organization, increments must meet end users' quality requirements, more efficient approach. End-user quality requirements are most accurately captured through direct feedback loops with actual users. Organizing more frequent sprint reviews with a broader audience — including end users — provides real-time quality validation at each increment, reducing the risk of discovering misalignment late and enabling continuous refinement of quality expectations throughout delivery. (PMBOK Guide) – Seventh Edition, 2021, p. 42, 'Build Quality into Processes and Deliverables'\""
    ),
    # Q1598
    (
        "Explanation: Need: listen to people needs. Option C (Meet with the project sponsor and key stakeholders to assess each deliverable's value to the organization and set execution priorities.) fixes it.\"",
        "Explanation: Keywords: two major deliverables same priority, team asking which to deliver first. When two deliverables have equal stated priority, the project manager cannot arbitrarily sequence them — the prioritization decision requires organizational context that only the sponsor and key stakeholders can provide. Meeting with them to assess each deliverable's value and strategic importance enables an informed sequencing decision that reflects the organization's actual priorities. (PMBOK Guide) – Seventh Edition, 2021, p. 32, 'Focus on Value'\""
    ),
    # Q1599
    (
        "Explanation: Need: listen to people needs. Option B (Meet the project team and stakeholders to identify the root cause of the issue and develop a solution.) fixes it.\"",
        "Explanation: Keywords: rescue project, behind schedule, contractual penalty, former PM had conflicts, first action. When assigned to rescue a troubled project, the project manager must first understand the actual situation before taking action. Meeting with the team and stakeholders to identify the root cause of the delays surfaces the real issues — which may be technical, organizational, or interpersonal — and enables development of a solution that addresses the causes rather than just the symptoms. (PMBOK Guide) – Seventh Edition, 2021, p. 30, 'Effectively Engage with Stakeholders'\""
    ),
    # Q1600
    (
        "Explanation: Need: guide and calm the team. Option C (Choose a reward for the team member that aligns with their personal goals.) fixes it.\"",
        "Explanation: Keywords: team member 2 years, consistently high performance, stood out among peers, recognition. Effective recognition is personal, not generic. Choosing a reward that aligns with the team member's personal goals ensures the recognition resonates deeply and reinforces the behavior being acknowledged. Generic rewards — bonuses, public acknowledgment, or promotions — may not be valued equally by all individuals, whereas a personalized reward demonstrates genuine attention to what motivates this specific person. (PMBOK Guide) – Seventh Edition, 2021, p. 36, 'Demonstrate Leadership Behaviors'\""
    ),
    # Q1601
    (
        "Explanation: Need: guide and calm the team. Option D (Discuss this with the team and review the quality process.) fixes it.\"",
        "Explanation: Keywords: high-performing team member concerned about quality feedback mechanism, cannot deliver high-quality output. When a capable team member identifies that the quality feedback mechanism is preventing them from delivering high-quality work, the issue is systemic — the process itself is inadequate. Discussing the concern with the whole team and reviewing the quality process collaboratively identifies the specific gaps and generates solutions that benefit everyone, not just the individual who raised the concern. (PMBOK Guide) – Seventh Edition, 2021, p. 42, 'Build Quality into Processes and Deliverables'\""
    ),
    # Q1602
    (
        "Explanation: Need: guide and calm the team. Option C (Meet with the purchasing manager to find the source of the delays and agree on a purchasing schedule.) fixes it.\"",
        "Explanation: Keywords: functional structure, purchasing department other priorities, service purchases taking too long. In a functional organization, resource departments operate under their own priorities. Rather than escalating or modifying the project schedule unilaterally, the project manager should engage directly with the purchasing manager to understand the source of the delays and negotiate a purchasing schedule that accommodates both the project's needs and the department's workload. (PMBOK Guide) – Seventh Edition, 2021, p. 30, 'Effectively Engage with Stakeholders'\""
    ),
    # Q1603
    (
        "Explanation: Need: listen to people needs. Option B (Update the risk register and discuss it with the project stakeholders.) fixes it.\"",
        "Explanation: Keywords: procurement manager says equipment delivery will be delayed, project manager concerned about schedule. When a potential delay is identified through the procurement channel, the project manager must first formalize it as a risk and communicate it to stakeholders. Updating the risk register creates a documented basis for the subsequent discussion, while engaging stakeholders ensures they are informed, can provide input on impact assessment, and can authorize any required schedule adjustments. (PMBOK Guide) – Seventh Edition, 2021, p. 46, 'Optimize Risk Responses'\""
    ),
    # Q1604
    (
        "Explanation: Need: guide and calm the team. Option B (Organize a team meeting to discuss the changes and their importance for the company.) fixes it.\"",
        "Explanation: Keywords: structural changes, some positions made redundant, team unhappy and confused, project on track. When organizational changes create uncertainty and anxiety among team members, the project manager must address the human dimension rather than directing the team to ignore it. A team meeting that openly discusses the changes and explains their organizational context provides the transparency and respect that team members need to process the situation and refocus on their work. (PMBOK Guide) – Seventh Edition, 2021, p. 36, 'Demonstrate Leadership Behaviors'\""
    ),
    # Q1605
    (
        "Explanation: Need: guide and calm the team. Option B (Discuss the situation with the team member's functional manager to see if the schedule can be adjusted.) fixes it.\"",
        "Explanation: Keywords: experienced team member, conflicting operational schedule, cannot attend all project activities. In a matrix organization, team members have dual reporting obligations. When an operational schedule conflicts with project activities, the resolution requires engagement with the functional manager — who controls the operational schedule — to explore whether flexibility exists. This approach respects the organizational structure and avoids placing the team member in an impossible dual-commitment situation. (PMBOK Guide) – Seventh Edition, 2021, p. 30, 'Effectively Engage with Stakeholders'\""
    ),
    # Q1606
    (
        "Explanation: Need: guide and calm the team. Option A (Talk to the team member to determine why their performance changed.) fixes it.\"",
        "Explanation: Keywords: formerly high performer, now not completing work on time, review meeting, what to do. When a previously high-performing team member's performance declines, the cause is almost always contextual — a personal issue, a change in work conditions, or an unmet need. Talking directly to the team member to understand what changed demonstrates respect, surfaces the real reason, and opens the possibility of addressing it — rather than immediately escalating to HR or management based on incomplete information. (PMBOK Guide) – Seventh Edition, 2021, p. 36, 'Demonstrate Leadership Behaviors'\""
    ),
    # Q1607
    (
        "Explanation: Need: keep plans flexible. Option B (Inform the neighbor that all of the project documentation has been approved.) fixes it.\"",
        "Explanation: Keywords: construction project, neighboring business complains about building height, first action. When an external party raises an objection to a project activity, the project manager's first response is to establish the factual basis of the situation. Informing the neighbor that all project documentation — including height specifications — has been formally approved provides the objective reference point that either resolves the concern or establishes the starting point for any further discussion. (PMBOK Guide) – Seventh Edition, 2021, p. 25, 'Be a Diligent, Respectful, and Caring Steward'\""
    ),
    # Q1608
    (
        "Explanation: Need: guide and calm the team. Option B (Agreed-upon key performance indicators (KPIs)) fixes it.\"",
        "Explanation: Keywords: end of project, performance rating of team members, what to reference mainly. Performance evaluations must be grounded in objective, pre-agreed criteria to be fair and credible. The agreed-upon KPIs established at the beginning of the project provide the authoritative benchmark for assessment — ensuring that team members are evaluated against the standards they understood and accepted rather than subjective impressions formed during the project. (PMBOK Guide) – Seventh Edition, 2021, p. 36, 'Demonstrate Leadership Behaviors'\""
    ),
    # Q1609
    (
        "Explanation: Need: guide and calm the team. Option A (Explain to the team that open discussions are needed but remind the team to follow the ground rules.) fixes it.\"",
        "Explanation: Keywords: team member extends discussion topics beyond time, others feel inconsiderate. When one team member consistently over-extends discussions, the project manager should address the behavior in a way that balances openness with discipline. Reinforcing the value of open discussion while reminding everyone of the ground rules addresses the behavior indirectly and constructively — preserving the culture of contribution while establishing that time boundaries serve the entire team. (PMBOK Guide) – Seventh Edition, 2021, p. 28, 'Create a Collaborative Team Environment'\""
    ),
    # Q1610
    (
        "Explanation: Need: guide and calm the team. Option C (Regulatory compliance issues discussed in the meeting.) fixes it.\"",
        "Explanation: Keywords: daily standup, list of impediments, compliance defects, product owner and developers leaving, contract not renewed, prioritize. Among multiple competing impediments, regulatory compliance defects must always be addressed first. Compliance failures carry legal and operational consequences that no other impediment category can match — product owner transitions, vendor contract renewals, and developer recruitment are all manageable, but unresolved compliance defects create systemic risk to the project and organization. (PMBOK Guide) – Seventh Edition, 2021, p. 25, 'Be a Diligent, Respectful, and Caring Steward'\""
    ),
    # Q1611
    (
        "Explanation: Need: listen to people needs. Option A (Schedule a meeting with the reluctant project stakeholder to obtain their feedback.) fixes it.\"",
        "Explanation: Keywords: post-release evaluation, six stakeholders gave feedback, one has not responded to numerous requests. When a stakeholder is unresponsive to multiple written requests for feedback, shifting to a direct meeting is the most effective escalation. A scheduled meeting creates a specific time commitment that is harder to ignore than emails, and provides the personal engagement context that may be needed to understand and overcome whatever is preventing the stakeholder from responding. (PMBOK Guide) – Seventh Edition, 2021, p. 30, 'Effectively Engage with Stakeholders'\""
    ),
    # Q1612
    (
        "Explanation: Need: guide and calm the team. Option C (Conduct a workshop with both of the teams.) fixes it.\"",
        "Explanation: Keywords: design team, implementation team in different country, how to communicate design. Design handoffs between geographically separated teams are high-risk for misinterpretation. A joint workshop with both teams transforms a one-way information transfer into a two-way collaborative session where the implementation team can ask questions, raise concerns, and confirm their understanding — dramatically reducing the rework risk that arises when a design is simply sent as a document. (PMBOK Guide) – Seventh Edition, 2021, p. 28, 'Create a Collaborative Team Environment'\""
    ),
    # Q1613
    (
        "Explanation: Need: guide and calm the team. Option C (Story points) fixes it.\"",
        "Explanation: Keywords: new project, urgent funding approval, Scrum team worked together 3 years, previous project under budget. When a well-established Scrum team needs to estimate a new project urgently, story points are the most appropriate technique. The team's three years of shared experience — including their established velocity from the previous project — provides the empirical calibration data that makes story point estimation reliable for this team, enabling a meaningful estimate that justifies the funding request. (PMBOK Guide) – Seventh Edition, 2021, p. 44, 'Navigate Complexity'\""
    ),
    # Q1614
    (
        "Explanation: Need: guide and calm the team. Option B (Verify the information needed for steering committee members.) fixes it.\"",
        "Explanation: Keywords: steering committee member complaints about weekly report, too long, unnecessary details, cannot get main message. When a report format fails to serve its audience, the solution is not to change the format arbitrarily — it is to understand what the audience actually needs. Verifying the specific information that steering committee members need enables the project manager to redesign the report around those needs, delivering exactly what they require to take action and nothing more. (PMBOK Guide) – Seventh Edition, 2021, p. 30, 'Effectively Engage with Stakeholders'\""
    ),
    # Q1615
    (
        "Explanation: Need: listen to people needs. Option B (Set up a stakeholder session with all teams to agree and document the benefits and establish ownership.) fixes it.\"",
        "Explanation: Keywords: software frees up staff, multiple business areas want to benefit, project manager action. When multiple business areas claim a shared benefit, ambiguity over ownership can lead to duplication, conflict, or the benefit never being fully realized. Bringing all interested teams together to agree on how the benefit will be distributed and who will own each portion ensures clarity, accountability, and documented commitment — the prerequisites for successful benefits realization. (PMBOK Guide) – Seventh Edition, 2021, p. 32, 'Focus on Value'\""
    ),
    # Q1616
    (
        "Explanation: Need: listen to people needs. Option D (Discuss this with the team so they are able to reprioritize critical tasks and aim for the release deadline.) fixes it.\"",
        "Explanation: Keywords: key team member sick, all team members cross-functional and near full capacity, release deadline at risk. When a team member is unexpectedly absent near a release deadline, the team's cross-functional capability means other members can potentially absorb the work. Discussing the situation with the team allows them to reprioritize collectively — determining which critical tasks must be protected and which can be deferred — enabling a targeted response that maximizes the probability of meeting the release date. (PMBOK Guide) – Seventh Edition, 2021, p. 28, 'Create a Collaborative Team Environment'\""
    ),
    # Q1617
    (
        "Explanation: Need: listen to people needs. Option C (Suggest that the sponsor conduct a cost-benefit analysis to determine feasibility.) fixes it.\"",
        "Explanation: Keywords: sponsor wants new deliverable within 2 months, advice on most efficient approach. When a sponsor requests advice on a potential scope addition, the project manager's role is to help them make an informed decision. Suggesting a cost-benefit analysis gives the sponsor the analytical tool to objectively compare the value of the deliverable against its cost — which is especially important when the 2-month timeline creates scheduling pressure that may inflate the true cost of delivery. (PMBOK Guide) – Seventh Edition, 2021, p. 32, 'Focus on Value'\""
    ),
    # Q1618
    (
        "Explanation: Need: listen to people needs. Option B (Create the project management plans with the project team and share the documents with the stakeholders.) fixes it.\"",
        "Explanation: Keywords: newly assigned project manager, project management plans and documents missing, what to do. The absence of project management plans is a fundamental gap that must be addressed before the project can proceed in a controlled manner. Creating the plans collaboratively with the project team ensures they reflect the team's actual working context and builds ownership, while sharing them with stakeholders aligns all parties on the project's approach, roles, and governance. (PMBOK Guide) – Seventh Edition, 2021, p. 28, 'Create a Collaborative Team Environment'\""
    ),
    # Q1619
    (
        "Explanation: Need: listen to people needs. Option A (Perform a root cause analysis (RCA) of the existing communication approach.) fixes it.\"",
        "Explanation: Keywords: stakeholders complaining about poor communication, communications management plan was followed, what to do. When stakeholder complaints persist despite adherence to the communications management plan, the plan itself is the problem — not its execution. A root cause analysis of the communication approach identifies the specific gaps between what the plan prescribes and what stakeholders actually need, providing the basis for a targeted improvement rather than incremental adjustments that address symptoms. (PMBOK Guide) – Seventh Edition, 2021, p. 30, 'Effectively Engage with Stakeholders'\""
    ),
    # Q1620
    (
        "Explanation: Need: guide and calm the team. Option C (Validate that the software is compliant with standards and regulations.) fixes it.\"",
        "Explanation: Keywords: aviation software, regulatory requirements must be met, development and testing completed. When aviation software development and testing are complete, the final obligation before the project can be considered done is formal validation of regulatory compliance. Validating that the software meets all applicable standards and regulations provides the evidence required for the regulatory approval process and is the non-negotiable prerequisite for any operational deployment. (PMBOK Guide) – Seventh Edition, 2021, p. 25, 'Be a Diligent, Respectful, and Caring Steward'\""
    ),
    # Q1621
    (
        "Explanation: Need: listen to people needs. Option C (Work with the product owner to change the priorities in the sprint backlog.) fixes it.\"",
        "Explanation: Keywords: developer taking unexpected leave, backlog item prerequisite for next sprint review feature. When a key backlog item cannot be completed due to a resource absence, the product owner must be involved in deciding how to handle the sprint backlog. Working with the product owner to reprioritize ensures that the decision reflects business priorities — either by shifting other items to cover the dependency or by adjusting the sprint review expectations — rather than being made unilaterally by the project manager. (PMBOK Guide) – Seventh Edition, 2021, p. 32, 'Focus on Value'\""
    ),
    # Q1622
    (
        "Explanation: Need: listen to people needs. Option D (Ensure that knowledge is transferred to the operations team.) fixes it.\"",
        "Explanation: Keywords: transition to operations, sponsor wants good support for end users, what to ensure. Effective operational support depends on the operations team having a thorough understanding of how the system works. Ensuring that knowledge is formally transferred to the operations team — through documentation, training sessions, and hands-on walkthroughs — is the project manager's primary contribution to sustainable post-project support and the most direct way to honor the sponsor's requirement. (PMBOK Guide) – Seventh Edition, 2021, p. 28, 'Create a Collaborative Team Environment'\""
    ),
    # Q1623
    (
        "Explanation: Need: listen to people needs. Option D (Newspapers) fixes it.\"",
        "Explanation: Keywords: construction in remote rural area, project nearing end, share good news with local community. Communication channels must be matched to the audience's actual access and habits. In a remote rural area, newspapers are the most widely accessible and trusted medium for reaching the local community — particularly residents who may not have reliable internet access or mobile connectivity. Choosing the right channel ensures the message reaches the intended audience rather than being lost in a medium they do not use. (PMBOK Guide) – Seventh Edition, 2021, p. 30, 'Effectively Engage with Stakeholders'\""
    ),
    # Q1624
    (
        "Explanation: Need: keep plans flexible. Option B (Target benefits, strategic alignment, time frame for realizing benefits) fixes it.\"",
        "Explanation: Keywords: project benefits management plan, what should be included. A benefits management plan documents how and when project benefits will be realized. The three essential elements are: the specific target benefits the project is expected to deliver, how those benefits align with the organization's strategic objectives, and the time frame within which each benefit will be realized — together providing the framework for tracking and validating benefits realization after the project is complete. (PMBOK Guide) – Seventh Edition, 2021, p. 32, 'Focus on Value'\""
    ),
    # Q1625
    (
        "Explanation: Need: listen to people needs. Option D (Discuss the project objectives with all stakeholders, including the farmers' group, and review their requirements.) fixes it.\"",
        "Explanation: Keywords: community center, farmers' group not consulted, use site for monthly market, how to move forward. When a previously unidentified stakeholder group emerges with legitimate interests in the project site, the project manager must engage them even if approvals have been obtained. Discussing the project objectives with all stakeholders — including the farmers' group — and reviewing their requirements is both an ethical obligation and a risk mitigation measure that can prevent costly conflicts during or after construction. (PMBOK Guide) – Seventh Edition, 2021, p. 30, 'Effectively Engage with Stakeholders'\""
    ),
    # Q1626
    (
        "Explanation: Need: listen to people needs. Option D (Update the communications management plan to fulfill the key stakeholder's expectations about relevant information.) fixes it.\"",
        "Explanation: Keywords: key stakeholder complains about incomplete and late information, beginning to disengage. When a stakeholder is disengaging because their communication needs are not being met, the root cause is a gap in the communications management plan. Updating the plan to explicitly capture and fulfill this stakeholder's expectations — with respect to content, timing, and completeness — addresses the systemic issue rather than making one-off adjustments that will not prevent future gaps. (PMBOK Guide) – Seventh Edition, 2021, p. 30, 'Effectively Engage with Stakeholders'\""
    ),
    # Q1627
    (
        "Explanation: Need: listen to people needs. Option A (Discuss this with the project team and select the appropriate tools.) fixes it.\"",
        "Explanation: Keywords: distributed team, collaboration tools causing communication issues, team wants to change platform. Tool selection for a distributed team should be a collaborative decision that reflects the team's actual working needs. Discussing the situation with the team and selecting appropriate tools together ensures the chosen solution addresses the specific friction points identified, builds collective commitment to the new platform, and avoids the same dissatisfaction that occurred with the current tools. (PMBOK Guide) – Seventh Edition, 2021, p. 28, 'Create a Collaborative Team Environment'\""
    ),
    # Q1628
    (
        "Explanation: Need: listen to people needs. Option B (Host an alignment session with stakeholders to formalize the project requirements.) fixes it.\"",
        "Explanation: Keywords: supplier says no customer testing required, internal project manager wants to confirm with stakeholders. When a supplier makes an assumption about customer involvement that may contradict stakeholder expectations, the project manager must validate this with the relevant parties rather than accepting the supplier's assertion. An alignment session brings stakeholders and the supplier together to formally establish and document the agreed requirements — preventing assumptions from becoming costly misunderstandings later. (PMBOK Guide) – Seventh Edition, 2021, p. 30, 'Effectively Engage with Stakeholders'\""
    ),
    # Q1629
    (
        "Explanation: Need: guide and calm the team. Option C (Determine the possibility for team members to split up the required tasks.) fixes it.\"",
        "Explanation: Keywords: highly critical project, missing professional resources, newly assigned project manager, first action. Before seeking external resources — which takes time and budget — the project manager should first assess whether the existing team can collectively cover the missing expertise by distributing the tasks among themselves. This approach leverages existing team capacity, maintains project velocity, and avoids the onboarding delays associated with hiring external professionals. (PMBOK Guide) – Seventh Edition, 2021, p. 28, 'Create a Collaborative Team Environment'\""
    ),
    # Q1630
    (
        "Explanation: Need: watch risks early. Option D (Assess the possible impact of the raw material shortage on the project.) fixes it.\"",
        "Explanation: Keywords: supplier informs of upcoming raw material shortage due to regulatory change, what to do. When a supplier notifies the project of an anticipated constraint, the first step is to assess what that constraint means for the project specifically. Evaluating the impact of the raw material shortage on schedule, cost, and deliverables establishes the factual basis for determining whether mitigation actions — alternative sourcing, schedule adjustment, or scope change — are warranted and at what urgency. (PMBOK Guide) – Seventh Edition, 2021, p. 46, 'Optimize Risk Responses'\""
    ),
    # Q1631
    (
        "Explanation: Need: listen to people needs. Option B (Analyze both internal and external stakeholders and develop a customized engagement strategy for each stakeholder.) fixes it.\"",
        "Explanation: Keywords: internal and external stakeholders, strategic approach to engagement, different needs and access to information. Effective stakeholder engagement is never one-size-fits-all. Internal and external stakeholders have fundamentally different relationships to the project, different information needs, and different communication preferences. Analyzing each stakeholder individually and developing customized engagement strategies ensures that every interaction is targeted, appropriate, and more likely to result in genuine participation and support. (PMBOK Guide) – Seventh Edition, 2021, p. 30, 'Effectively Engage with Stakeholders'\""
    ),
    # Q1633
    (
        "Explanation: Need: listen to people needs. Option C (Receive an agreement from the product owner and add the new story to the product backlog) fixes it.\"",
        "Explanation: Keywords: customer technical lead discussed new feature, project manager added as high priority to sprint, sprint not completed. When a project manager unilaterally adds stories to the sprint backlog without product owner involvement, it disrupts the sprint and overrides the agreed-upon scope. The appropriate correction is to obtain product owner agreement before adding the story to the product backlog — ensuring the story is properly evaluated, prioritized, and sequenced for a future sprint rather than disrupting the current one. (PMBOK Guide) – Seventh Edition, 2021, p. 32, 'Focus on Value'\""
    ),
    # Q1634
    (
        "Explanation: Need: protect benefits for users. Option D (Identified the regulatory differences among the countries.) fixes it.\"",
        "Explanation: Keywords: global project, definitions from country A, delivery in countries B, C, D, country B discovers unaddressed legal requirement. When a project is deployed across multiple regulatory jurisdictions, each country's specific legal requirements must be identified and addressed during planning. Proactively identifying regulatory differences among the target countries would have ensured that country B's specific legal requirement was incorporated into the design from the beginning, preventing the costly mid-project discovery. (PMBOK Guide) – Seventh Edition, 2021, p. 25, 'Be a Diligent, Respectful, and Caring Steward'\""
    ),
    # Q1635
    (
        "Explanation: Need: protect value and acceptance. Option D (Rank the requirements with the highest benefit-cost ratio as more important.) fixes it.\"",
        "Explanation: Keywords: database migration, many disagreements on scope and timelines, how to prioritize requirements impartially. Prioritizing requirements by benefit-cost ratio provides an objective, business-grounded method that is independent of departmental politics or individual influence. Requirements with the highest return per unit of investment deliver the most value to the organization, making this the most defensible and impartial basis for resolving disagreements among competing department leaders. (PMBOK Guide) – Seventh Edition, 2021, p. 32, 'Focus on Value'\""
    ),
    # Q1636
    (
        "Explanation: Need: guide and calm the team. Option C (Schedule a meeting with the new team member to learn about the new method of testing.) fixes it.\"",
        "Explanation: Keywords: new team member proposes new testing method, established team resistant. When a new team member brings a different methodology, the project manager should explore it rather than defaulting to the existing approach. Scheduling a meeting to learn about the new method demonstrates openness to improvement, gives the suggestion a fair hearing, and creates the foundation for an evidence-based decision about whether to adopt, adapt, or set aside the proposal. (PMBOK Guide) – Seventh Edition, 2021, p. 28, 'Create a Collaborative Team Environment'\""
    ),
    # Q1637
    (
        "Explanation: Need: guide and calm the team. Option D (Meet with the project scheduler to rebaseline the project using a more realistic schedule.) fixes it.\"",
        "Explanation: Keywords: declining SPI for 4 consecutive reviews, no corrective action in development, team not concerned. When the SPI has declined consistently for four review periods without a corrective response, the schedule baseline is no longer a realistic reflection of the project's actual performance capacity. Rebaselining with a realistic schedule establishes a new, credible reference point for measurement and performance management — enabling meaningful corrective action against a schedule the team can actually meet. (PMBOK Guide) – Seventh Edition, 2021, p. 46, 'Optimize Risk Responses'\""
    ),
    # Q1639
    (
        "Explanation: Need: listen to people needs. Option A (Make arrangements for the stakeholder to join the kick-off meeting virtually.) fixes it.\"",
        "Explanation: Keywords: kick-off meeting, key stakeholder at another location for the month, stakeholder declines. A kick-off meeting is a critical alignment event that should include all key stakeholders. When a stakeholder cannot attend in person, the project manager's obligation is to ensure their participation through alternative means. Making virtual arrangements is both straightforward and inclusive — it preserves the stakeholder's engagement without delaying the project or requiring everyone else to reschedule. (PMBOK Guide) – Seventh Edition, 2021, p. 30, 'Effectively Engage with Stakeholders'\""
    ),
    # Q1640
    (
        "Explanation: Need: listen to people needs. Option B (Schedule a meeting with the project team and the key stakeholder as soon as possible to discuss and agree on an approach.) fixes it.\"",
        "Explanation: Keywords: key stakeholder refusing to participate, disagrees with team approach, team morale affected. When a key stakeholder's disengagement is affecting team morale, the situation needs to be addressed urgently through direct dialogue. Bringing the project team and the stakeholder together in a joint meeting creates the space for both sides to present their perspectives, find common ground, and agree on an approach — resolving both the substantive disagreement and the morale issue simultaneously. (PMBOK Guide) – Seventh Edition, 2021, p. 30, 'Effectively Engage with Stakeholders'\""
    ),
    # Q1641
    (
        "Explanation: Need: guide and calm the team. Option B (Include the dependent activity in the current iteration for team B.) fixes it.\"",
        "Explanation: Keywords: iteration two, team A needs results from team B in iteration four, team B activity not yet prioritized. Managing cross-team dependencies in an agile environment requires proactive sequencing. Including the dependent team B activity in the current iteration — two iterations before team A needs it — provides sufficient lead time for completion without creating an emergency. Waiting until iteration three would leave no buffer for delays, while pushing it further back would guarantee team A is blocked in iteration four. (PMBOK Guide) – Seventh Edition, 2021, p. 34, 'Recognize, Evaluate, and Respond to System Interactions'\""
    ),
    # Q1642
    (
        "Explanation: Need: guide and calm the team. Option D (Encourage the team to hold a knowledge-sharing session in each iteration.) fixes it.\"",
        "Explanation: Keywords: agile team, new content management system, some members struggling to deliver features. When team members lack familiarity with the system they are working on, embedded knowledge sharing within the iteration cadence is the most efficient way to close skill gaps without disrupting delivery. Holding knowledge-sharing sessions every iteration ensures that learning is continuous, contextual, and immediately applicable to the work in progress — faster than training programs and more sustainable than leaving members to struggle independently. (PMBOK Guide) – Seventh Edition, 2021, p. 28, 'Create a Collaborative Team Environment'\""
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
