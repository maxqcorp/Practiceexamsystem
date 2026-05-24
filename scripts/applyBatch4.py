MD_FILE = './src/imports/project-management-questions-1.md'

with open(MD_FILE, 'r', encoding='utf-8') as f:
    content = f.read()

replacements = [
    (
        'Explanation: Need: keep plans flexible. Option B (Review the quality management plan) fixes it."',
        'Explanation: Keywords: inspection halt, regulatory labels missing, production phase, quality response. When a regulatory label failure stops production, the quality management plan is the authoritative reference for what should have been controlled and what the response protocol is. Reviewing it identifies the gap in quality controls that allowed the issue to reach inspection. (PMBOK Guide) – Seventh Edition, 2021, p. 42, \'Build Quality into Processes and Deliverables\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option A (Request that the customer reviews and clarifies feature definitions for the current sprint) fixes it."',
        'Explanation: Keywords: missing technical requirements, current sprint, customer clarification, iteration delivery. When critical technical information is absent mid-sprint, the direct source is the customer. Requesting that they review and clarify feature definitions for the current sprint provides the exact information the team needs without disrupting the sprint structure unnecessarily. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    (
        'Explanation: Need: keep plans flexible. Option C (The project will be difficult to complete as planned.) fixes it."',
        'Explanation: Keywords: earned value analysis, CPI below 1, cost overrun, completion forecast. A CPI of 0.933 means the project is getting only 93 cents of value for every dollar spent. Extrapolated across the remaining work, this trend makes it increasingly difficult to complete within the approved budget, which is the correct conclusion to draw from this data. (PMBOK Guide) – Seventh Edition, 2021, p. 32, \'Focus on Value\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option B (Establish dialogue with stakeholders on the project constraints, assumptions, and critical inputs) fixes it."',
        'Explanation: Keywords: high-risk novel project, no historical data, reluctant stakeholders, constraint dialogue. For an unprecedented project where no historical data exists, stakeholder dialogue is the primary tool for surfacing the constraints, assumptions, and critical inputs that replace experience-based knowledge. Establishing this dialogue early also begins building the support that reluctant stakeholders have not yet provided. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option C (A hybrid project as this will mitigate stakeholders\' concerns.) fixes it."',
        'Explanation: Keywords: agile transition, skeptical stakeholders, sponsor quick win, hybrid approach. A hybrid approach directly addresses the competing pressures in this environment: it delivers the iterative increments that give the sponsor an early win while maintaining enough predictive structure to satisfy stakeholders who need upfront planning. Tailoring the approach to the context is more effective than choosing either extreme. (PMBOK Guide) – Seventh Edition, 2021, p. 40, \'Tailor Based on Context\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option D (Work with the product owner to clarify the requirement) fixes it."',
        'Explanation: Keywords: sprint execution, acceptance criteria gap, developer clarification, product owner role. In an agile project, the product owner is the single source of truth for what acceptable delivery looks like. Routing acceptance criteria clarifications through the product owner maintains the correct governance structure and ensures the developer gets authoritative guidance, not an interpretation. (PMBOK Guide) – Seventh Edition, 2021, p. 40, \'Tailor Based on Context\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option B (Identify the root cause of communication issues) fixes it."',
        'Explanation: Keywords: global virtual team, communication breakdown, missed messages, missed deadlines. Communication failures in a virtual team can stem from many causes — tool gaps, time zone conflicts, unclear norms, or interpersonal issues. Acting before identifying the root cause risks applying the wrong solution. Understanding the specific failure first is the prerequisite to any effective fix. (PMBOK Guide) – Seventh Edition, 2021, p. 44, \'Navigate Complexity\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option A (Ensured the team charter was developed by the team members) fixes it."',
        'Explanation: Keywords: ground rules, meeting penalty, team charter ownership, rule enforcement. Ground rules are only effective when the team has genuine ownership of them. When team members participate in developing the charter, they understand and commit to the norms — rules they helped create are far less likely to be disputed than rules imposed on them after the fact. (PMBOK Guide) – Seventh Edition, 2021, p. 28, p. 29, \'Create a Collaborative Team Environment\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Options A and C (Alternatives analysis; Cost-benefit analysis) work together."',
        'Explanation: Keywords: project cancellation risk, client decision, alternatives analysis, cost-benefit evidence. To influence a client who is considering closing a project, the PM needs evidence, not persuasion. An alternatives analysis shows the client what other paths exist, while a cost-benefit analysis makes the value of continuing — versus stopping — concrete and quantifiable. Together they give the client an informed basis for their decision. (PMBOK Guide) – Seventh Edition, 2021, p. 32, \'Focus on Value\'"'
    ),
    (
        'Explanation: Need: keep plans flexible. Option D (Apply fast-tracking techniques to compress the schedule of the critical project) fixes it."',
        'Explanation: Keywords: concurrent projects, schedule compression, resource constraints, fast-tracking. When the schedule must be compressed but additional resources are not available, fast-tracking is the compression technique that re-examines dependencies to identify activities that can run in parallel rather than sequentially, shortening duration without adding cost. (PMBOK Guide) – Seventh Edition, 2021, p. 44, \'Navigate Complexity\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option A (The contract has not been appropriately reviewed by the project team) fixes it."',
        'Explanation: Keywords: annual contract renewal, new law, audit finding, contract review failure. A contract renewed annually must be reviewed against current regulations at each renewal cycle. Renewing without checking for regulatory changes is a stewardship failure — the project team is responsible for ensuring their governing documents remain legally compliant throughout the project\'s life. (PMBOK Guide) – Seventh Edition, 2021, p. 25, \'Be a Diligent, Respectful, and Caring Steward\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option D (Review the adequacy of the project\'s governance and ensure that an appropriate structure is in place) fixes it."',
        'Explanation: Keywords: contradicting senior management views, external stakeholders, decision delays, governance gap. When contradicting views between senior management and external stakeholders paralyze decision-making, the root cause is typically a governance gap — no clear authority structure to resolve the conflict. Reviewing and strengthening governance creates the decision-making framework the project needs to move forward. (PMBOK Guide) – Seventh Edition, 2021, p. 34, \'Recognize, Evaluate, and Respond to System Interactions\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Options B and D (Meet with the entire team to review the ground rules about safe environments; Contact the team member to explain what information can be shared outside the team) work together."',
        'Explanation: Keywords: retrospective confidentiality breach, safe environment, functional manager disclosure. Retrospectives depend on psychological safety — when that safety is violated, future retrospectives become less honest and less useful. Reinforcing safe-space ground rules with the full team restores the shared norm, while addressing the individual team member\'s behaviour directly ensures it does not recur. (PMBOK Guide) – Seventh Edition, 2021, p. 28, p. 29, \'Create a Collaborative Team Environment\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option D (Identify the minimum functionality required for the product) fixes it."',
        'Explanation: Keywords: first iteration, marketing prototype, minimum viable product, customer demonstration. When the first iteration must serve a specific external purpose — presenting a prototype to potential customers — the PM must define the minimum functionality that fulfills that purpose. Building beyond the minimum wastes the iteration\'s capacity on features that the marketing demonstration does not need. (PMBOK Guide) – Seventh Edition, 2021, p. 32, \'Focus on Value\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option B (Speak to the stakeholders to resolve the bottleneck and see how the entire process can be streamlined) fixes it."',
        'Explanation: Keywords: delivery deadline, release management backlog, integration bottleneck, stakeholder engagement. A three-week release management backlog against a two-week delivery deadline is a system-level constraint that the project team cannot resolve on their own. The PM must engage the relevant stakeholders to streamline the broader release process — the bottleneck exists outside the project boundary. (PMBOK Guide) – Seventh Edition, 2021, p. 34, \'Recognize, Evaluate, and Respond to System Interactions\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option C (The project manager should allow the resources to periodically choose on which team they would like to work.) fixes it."',
        'Explanation: Keywords: agile organization, team self-selection, resource preference, team autonomy. In an agile organization, giving team members periodic choice over which team they work on builds engagement and ownership. Self-selected teams often outperform assigned teams because members feel genuine commitment to the group they chose to join. (PMBOK Guide) – Seventh Edition, 2021, p. 28, p. 29, \'Create a Collaborative Team Environment\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option B (Validate acceptance criteria with stakeholders prior to backlog refinement) fixes it."',
        'Explanation: Keywords: stakeholder complaints, iteration demos, features not as requested, acceptance criteria gap. When stakeholders repeatedly say delivered features do not match their expectations, the gap is being created before development starts, not during it. Validating acceptance criteria with stakeholders before backlog refinement aligns understanding at the point where changing requirements is cheapest. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Options C and D (Go back to the development team and discuss which second milestone requirements can be performed in the first quarter.; Ask the customer for their priorities regarding the requirements for the second milestone) work together."',
        'Explanation: Keywords: milestone acceleration, hybrid project, customer priorities, feasibility discussion. Accelerating a milestone requires two conversations simultaneously: asking the development team what is feasible in Q1 establishes the supply side, while asking the customer for their priorities on the second milestone establishes the demand side. Together they create the information needed to negotiate a solution that is both deliverable and valuable. (PMBOK Guide) – Seventh Edition, 2021, p. 32, \'Focus on Value\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option A (Execute it as a Scrum project) fixes it."',
        'Explanation: Keywords: evolving requirements, flexible scope, competitive market, iterative delivery. When requirements are still evolving and the market demands flexibility, Scrum\'s iterative structure is the most appropriate fit. It allows the team to respond to requirement changes between sprints and maintain delivery momentum without locking in a scope that may become outdated as the competitive landscape shifts. (PMBOK Guide) – Seventh Edition, 2021, p. 40, \'Tailor Based on Context\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Options B and D (Review and update dependencies; Conduct a root cause analysis.) work together."',
        'Explanation: Keywords: complex critical task, iteration impact, dependency review, root cause analysis. When a critical task proves more complex than estimated, the PM needs to act on two levels: understanding why the complexity was underestimated (root cause analysis) and assessing how the delay cascades through dependent activities (dependency review). Both are needed to make an informed decision about the iteration. (PMBOK Guide) – Seventh Edition, 2021, p. 44, \'Navigate Complexity\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option C (Prioritize the product backlog looking for high business value and low effort, and adjust the project budget and staffing to account for those items.) fixes it."',
        'Explanation: Keywords: 30% budget cut, resource-constrained project, backlog prioritization, value delivery. When a significant budget reduction forces difficult choices, the PM must concentrate remaining resources on items that deliver the highest value for the least effort. Reprioritizing the backlog with this lens — then adjusting staffing accordingly — ensures the team delivers the most meaningful outcomes with what is available. (PMBOK Guide) – Seventh Edition, 2021, p. 32, \'Focus on Value\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option D (Meet with the stakeholder prior to the meeting to obtain their opinion) fixes it."',
        'Explanation: Keywords: regulatory scope change, critical status meeting, key stakeholder absent, pre-meeting input. A key stakeholder\'s perspective on a regulation that changes scope is too important to exclude from the decision. Meeting with them before the formal meeting ensures their input is heard and incorporated, even though they cannot attend — stakeholder engagement does not stop because someone is unavailable. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option B (Update the communications management plan to include informal requests) fixes it."',
        'Explanation: Keywords: executive informal request, team member bypass, communications gap, dashboard. An executive going directly to a team member for project information reveals a gap in how the communications management plan handles informal channels. Updating the plan to include this pattern ensures it is addressed systematically rather than leaving team members uncertain about how to respond to direct executive requests. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option A (Work with the stakeholders to determine which measurable benefits can be tracked and assign an accountable person to monitor and report them) fixes it."',
        'Explanation: Keywords: hybrid framework, benefit tracking, no defined metrics, stakeholder collaboration. Value can only be managed if it can be measured. Working with stakeholders to define which benefits are measurable and assigning an accountable owner creates the governance structure for tracking whether the hybrid framework is actually delivering the business value it was adopted to produce. (PMBOK Guide) – Seventh Edition, 2021, p. 32, \'Focus on Value\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option D (Follow the project escalation policy and communications management plan) fixes it."',
        'Explanation: Keywords: favorable EEF changes, reduced cost, shortened schedule, escalation protocol. When favorable changes affect the project baseline — even positive ones — the PM is not authorized to unilaterally decide what to do with the freed resources or schedule. The escalation policy and communications management plan define how such significant changes must be reported and decided, ensuring the right people are involved. (PMBOK Guide) – Seventh Edition, 2021, p. 25, \'Be a Diligent, Respectful, and Caring Steward\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option C (Have a confidential discussion with the team member to identify the root cause) fixes it."',
        'Explanation: Keywords: persistent task difficulties, daily meetings, one-on-one, root cause. Repeated difficulty completing tasks signals a root cause that the team setting has not surfaced. A confidential one-on-one conversation gives the team member a safe space to reveal the real issue — whether it is a skills gap, personal circumstance, or unclear expectations — so the PM can respond to what is actually happening. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option D (Offer an opinion about the pros and cons of each idea and try to reach a consensus in a facilitated meeting) fixes it."',
        'Explanation: Keywords: feature disagreement, two-day sprint delay, team consensus, facilitated decision. When a team cannot reach consensus after two days of open debate, the PM needs to facilitate a structured resolution. Offering an informed perspective on each idea and guiding the team toward consensus respects every voice while using the PM\'s position to break the impasse without overriding the team\'s judgment. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Options C and E (Send a questionnaire to the project participants and seek their feedback.; Deliver the project materials to the users and see if they have any comments) work together."',
        'Explanation: Keywords: post-project user satisfaction, multi-country users, feedback collection, project closure. User satisfaction data must come from the users themselves. A structured questionnaire captures consistent, comparable feedback across countries, while delivering project materials creates a natural interaction point where users can raise concerns they may not have articulated in a formal survey. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option D (Review the resource management plan and provide mentoring to the new team member if necessary) fixes it."',
        'Explanation: Keywords: new junior team member, unclear expectations, role confusion, mentoring. When a new team member is confused about their role, the resource management plan defines what is expected of them on the project. Combining a review of that plan with direct mentoring gives the team member both the formal context and the personal guidance needed to become an effective contributor. (PMBOK Guide) – Seventh Edition, 2021, p. 28, p. 29, \'Create a Collaborative Team Environment\'"'
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
