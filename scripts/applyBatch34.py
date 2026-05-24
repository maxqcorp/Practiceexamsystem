MD_FILE = './src/imports/project-management-questions-1.md'

with open(MD_FILE, 'r', encoding='utf-8') as f:
    content = f.read()

replacements = [
    # Q1643
    (
        'Explanation: Need: guide and calm the team. Option D (Discuss growth and development needs with the team member and provide learning opportunities accordingly.) fixes it."',
        'Explanation: Keywords: less engaged in meetings, delivers promptly, lack of skills, new tasks. The servant leader recognizes that demotivation stemming from skill gaps requires targeted development support, not reassignment. By discussing growth needs directly with the team member and tailoring learning opportunities, the project manager addresses the root cause of disengagement while investing in long-term team capability. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    # Q1644
    (
        'Explanation: Need: guide and calm the team. Option C (Praise the team for self-organizing and growing, then work one-on-one with the facilitators, as needed.) fixes it."',
        'Explanation: Keywords: rotating facilitators, daily scrum, some run inefficient, agile team self-organizing. A servant leader acknowledges team growth and supports rather than reverting to top-down control. Praising self-organization reinforces positive behavior, while targeted one-on-one coaching addresses specific facilitation gaps without undermining the team\'s autonomy. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    # Q1645
    (
        'Explanation: Need: guide and calm the team. Option D (Understand the team member\'s personal issue and offer them support.) fixes it."',
        'Explanation: Keywords: incomplete tasks, no impediments, personal issue, daily standup. Servant leadership means removing barriers to performance, which includes personal challenges affecting a team member\'s contribution. Taking time to understand the personal issue demonstrates empathy and trust, enabling the project manager to offer appropriate support and help the team member return to effectiveness. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    # Q1646
    (
        'Explanation: Need: listen to people needs. Option B (Allocate resources to provide training about the new technology to the stakeholders.) fixes it."',
        'Explanation: Keywords: complex and innovative project, new technology, stakeholders unfamiliar, servant leader. A servant leader\'s role includes enabling stakeholders to understand and engage effectively with the project. Allocating resources for technology training ensures stakeholders can make informed decisions and provide meaningful input, reducing misunderstandings that arise from unfamiliarity. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    # Q1647
    (
        'Explanation: Need: guide and calm the team. Option A (Help engineer A to become familiar with this new role and ensure engineer B stays motivated.) fixes it."',
        'Explanation: Keywords: team lead left, management promotes engineer A, project manager prefers engineer B, decision unchanged. Once management\'s decision is final, a servant leader accepts it and focuses on making the best of the situation. Helping engineer A succeed in the new role while keeping engineer B motivated protects team cohesion and project continuity regardless of the initial disagreement. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    # Q1648
    (
        'Explanation: Need: guide and calm the team. Option A (Use a servant leader approach.) fixes it."',
        'Explanation: Keywords: challenging project, empower team members, remove organizational impediments, facilitate collaboration. The servant leader model is defined by placing the team\'s needs first — removing obstacles, facilitating collaboration, and empowering team members to deliver. This approach directly addresses the challenge described and creates the conditions for high performance. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    # Q1649
    (
        'Explanation: Need: listen to people needs. Option C (Plan the delivery of a minimum viable feature in 2 weeks to enable early showcasing of business value.) fixes it."',
        'Explanation: Keywords: urgent new feature in 2 weeks, company B needs 4 weeks, minimum viable feature, early business value. Delivering a minimum viable feature in 2 weeks allows early business value realization while company B completes the full back end. This incremental approach balances marketing\'s urgency with technical realities, enabling early showcasing to stakeholders without blocking either company\'s work. (PMBOK Guide) – Seventh Edition, 2021, p. 32, \'Focus on Value\'"'
    ),
    # Q1650
    (
        'Explanation: Need: listen to people needs. Option C (Review the communications management plan.) fixes it."',
        'Explanation: Keywords: distributed team, important release delayed, developer missed email, communications management plan. A failed communication that caused a release delay signals a gap in the communications management plan — the channel did not reliably reach all team members. Reviewing and updating this plan to use more reliable delivery methods prevents similar failures and ensures critical information reaches every team member. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    # Q1651
    (
        'Explanation: Need: listen to people needs. Option C (Analyzed stakeholders) fixes it."',
        'Explanation: Keywords: project charter approval, key stakeholder questioned project value, delay in approval. A key stakeholder who questions value at the charter stage should have been identified and engaged earlier through stakeholder analysis. Understanding their interests, concerns, and influence before presenting the charter would have allowed the project manager to proactively address value concerns and secure support. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    # Q1652
    (
        'Explanation: Need: listen to people needs. Option A (Adjust the communications management plan to gain stakeholder trust.) fixes it."',
        'Explanation: Keywords: transferred to another country, emails perceived as harsh, cultural differences, communications management plan. Cultural differences in communication style can erode stakeholder trust even when messages are technically accurate. Adjusting the communications management plan to reflect cultural norms and stakeholder preferences rebuilds trust and ensures messages are received as intended rather than as offensive. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    # Q1653
    (
        'Explanation: Need: guide and calm the team. Option C (Review organizational process assets (OPAs) and perform analogous estimating.) fixes it."',
        'Explanation: Keywords: regulatory project, tight deadline, similar project completed previously for another country, organizational process assets. Tailoring the approach based on available context means leveraging prior experience from a similar project through organizational process assets. Analogous estimating using the previous project\'s data provides a realistic baseline quickly, which is critical when team members have not yet been assigned. (PMBOK Guide) – Seventh Edition, 2021, p. 40, \'Tailor Based on Context\'"'
    ),
    # Q1654
    (
        'Explanation: Need: listen to people needs. Option D (Review the requirements traceability matrix and conduct inspections.) fixes it."',
        'Explanation: Keywords: quality specifications formally accepted, key stakeholder dissatisfied, requirements traceability matrix, inspections. When a stakeholder claims deliverables do not meet accepted quality specifications, the correct response is to verify compliance objectively rather than dispute the claim. Reviewing the requirements traceability matrix and conducting inspections provides evidence-based resolution aligned with quality management principles. (PMBOK Guide) – Seventh Edition, 2021, p. 42, \'Build Quality into Processes and Deliverables\'"'
    ),
    # Q1655
    (
        'Explanation: Need: listen to people needs. Option A (Segment the types of communications to be delivered to different stakeholders.) fixes it."',
        'Explanation: Keywords: multiple reporting formats, same project updates, multiple stakeholders, time spent on reporting. Delivering different reporting formats to multiple stakeholders represents an inefficiency caused by a one-size-fits-all approach. Segmenting communications so each stakeholder receives only the information relevant to them reduces redundant effort while maintaining effective engagement. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    # Q1656
    (
        'Explanation: Need: listen to people needs. Option C (Create a decision tree.) fixes it."',
        'Explanation: Keywords: purchase expensive application vs less expensive option, deadline at risk, cost impact, decision tree. When faced with competing options that carry cost and schedule trade-offs, a decision tree quantifies the expected value of each alternative objectively. This gives the sponsor and project manager a structured basis for choosing between the expensive application, the less expensive alternative, and the status quo. (PMBOK Guide) – Seventh Edition, 2021, p. 32, \'Focus on Value\'"'
    ),
    # Q1657
    (
        'Explanation: Need: keep plans flexible. Option A (Consult the risk response plan.) fixes it."',
        'Explanation: Keywords: lead design programmer accepted competitor offer, milestone upcoming, risk response plan. The departure of a key resource is a risk event — one that a well-maintained risk response plan should have anticipated. Consulting the plan provides pre-defined response options that can be activated immediately without improvising under pressure. (PMBOK Guide) – Seventh Edition, 2021, p. 46, \'Optimize Risk Responses\'"'
    ),
    # Q1658
    (
        'Explanation: Need: listen to people needs. Option B (Review the completion costs of similar projects.) fixes it."',
        'Explanation: Keywords: agile project, sponsor needs cost estimation for business case, completion costs of similar projects. In agile environments, precise upfront cost estimation is difficult; the most reliable source is analogous data from similar projects. Reviewing completion costs of comparable agile projects provides the sponsor with a credible estimate to support the business case without requiring detailed scope definition at this early stage. (PMBOK Guide) – Seventh Edition, 2021, p. 40, \'Tailor Based on Context\'"'
    ),
    # Q1659
    (
        'Explanation: Need: control changes and baselines. Option B (Meet with the operations manager to explain the background for the change and understand the operation manager\'s concerns about the change.) fixes it."',
        'Explanation: Keywords: CCB-approved change, operations manager not consulted, disruption to production line, meet with operations manager. An affected stakeholder who was not included in the change approval process has legitimate concerns that must be addressed. Meeting with the operations manager first — to explain the rationale and understand the concerns — opens dialogue and may surface solutions that reduce production disruption without reversing the approved change. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    # Q1660
    (
        'Explanation: Need: listen to people needs. Option C (Allow the team to focus and complete the complex work because it will reduce the risk of finding issues later in the project.) fixes it."',
        'Explanation: Keywords: technical complex requirement, no visual deliverable, customer cannot see progress, risk of late issues. When a complex requirement has no tangible deliverable to show, the risk of late discovery of issues is high. Allowing the team to focus and complete the complex work early reduces technical risk, even if this temporarily reduces visible output — addressing complexity before it compounds is sound project leadership. (PMBOK Guide) – Seventh Edition, 2021, p. 44, \'Navigate Complexity\'"'
    ),
    # Q1661
    (
        'Explanation: Need: listen to people needs. Option D (Gather enough requirements to produce a minimum viable product (MVP) with which to evaluate customer acceptance.) fixes it."',
        'Explanation: Keywords: product requirements not fully met, uncertainties about customer acceptance, minimum viable product. When requirements are uncertain, attempting to define all requirements upfront risks delivering work that does not meet actual customer needs. Producing an MVP enables early customer feedback and validation, reducing waste and allowing the team to iteratively refine requirements based on real acceptance signals. (PMBOK Guide) – Seventh Edition, 2021, p. 32, \'Focus on Value\'"'
    ),
    # Q1662
    (
        'Explanation: Need: listen to people needs. Option D (Escalate the issue to the project sponsor and seek their guidance.) fixes it."',
        'Explanation: Keywords: several organizations, unique corporate cultures, diverse expectations, conflicts requiring project manager involvement. Cross-organizational cultural conflicts that affect project expectations are a governance-level challenge. Escalating to the project sponsor is the appropriate first step to obtain the authority and guidance needed to define how cultural differences will be managed across organizations. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    # Q1663
    (
        "Explanation: Need: listen to people needs. Option D (Clarify the project roles and responsibilities, and share the purpose to gain the stakeholder's buyin.) fixes it.\"",
        "Explanation: Keywords: influential stakeholder, does not believe project management processes bring business value, clarify roles and share purpose. Engaging an influential stakeholder who lacks confidence in the project management approach requires transparent communication about the value of those processes. Clarifying roles and responsibilities and sharing the project's purpose addresses the stakeholder's skepticism by connecting project management activities directly to outcomes the stakeholder cares about. (PMBOK Guide) – Seventh Edition, 2021, p. 30, 'Effectively Engage with Stakeholders'\""
    ),
    # Q1664
    (
        'Explanation: Need: protect value and acceptance. Option B (Coordinate with the benefit owner to track and collect the missing data and build the KPIs.) fixes it."',
        'Explanation: Keywords: track project benefits, KPIs not yet defined, missing data, benefit owner. The benefit owner is accountable for tracking and realizing the project\'s intended benefits. Coordinating with them to build missing KPIs ensures accountability is placed correctly and that benefit tracking is aligned with the strategic outcomes the project is meant to deliver. (PMBOK Guide) – Seventh Edition, 2021, p. 32, \'Focus on Value\'"'
    ),
    # Q1665
    (
        'Explanation: Need: guide and calm the team. Option B (Meet with the team to discuss alternatives.) fixes it."',
        'Explanation: Keywords: key project deliverable not budgeted, discovered during implementation, team discuss alternatives. When an unbudgeted deliverable is discovered mid-project, the team is best positioned to identify creative alternatives — such as scope adjustments, resource reallocation, or phased delivery — that address the gap. Meeting with the team first gathers the necessary technical input before escalating or making decisions unilaterally. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    # Q1666
    (
        'Explanation: Need: keep plans flexible. Option C (Risk analysis) fixes it."',
        'Explanation: Keywords: product features at risk of cancellation, high operational costs at launch, iteration review, risk analysis. The risk of high operational costs upon launch is a project risk that should have been identified and analyzed during the project lifecycle. Conducting risk analysis — specifically evaluating cost implications in the production environment — would have surfaced this issue before it threatened feature viability. (PMBOK Guide) – Seventh Edition, 2021, p. 46, \'Optimize Risk Responses\'"'
    ),
    # Q1667
    (
        'Explanation: Need: listen to people needs. Option C (Analyze the interests and influence of stakeholders and evaluate their requirements.) fixes it."',
        'Explanation: Keywords: large public project, high impact on town citizens, define requirements, interests and influence of stakeholders. A project with broad public impact involves diverse stakeholders with differing priorities. Analyzing their interests and influence ensures requirements are gathered systematically and weighted by stakeholder importance, producing a balanced scope that reflects the needs of those most affected. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    # Q1668
    (
        'Explanation: Need: listen to people needs. Option A (Perform an impact analysis, readjust the schedule as needed, and communicate the changes to the customer.) fixes it."',
        'Explanation: Keywords: developer must take 4-week leave, no replacement, agile team, significant impact on deliverable. When a resource constraint materially impacts the delivery schedule, transparent communication with the customer — after performing a thorough impact analysis — is essential. Readjusting the schedule realistically and communicating the changes proactively preserves trust and allows the customer to plan accordingly. (PMBOK Guide) – Seventh Edition, 2021, p. 34, \'Recognize, Evaluate, and Respond to System Interactions\'"'
    ),
    # Q1669
    (
        'Explanation: Need: listen to people needs. Option C (Review the critical path with the stakeholders to define next steps.) fixes it."',
        'Explanation: Keywords: schedule delays from supplier issues, some tasks on critical path, review critical path with stakeholders. When supplier delays threaten critical path tasks, stakeholders need to be involved in defining next steps because the resolution may require scope, schedule, or resource trade-offs beyond the project manager\'s authority alone. Reviewing the critical path together enables collaborative, informed decision-making. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    # Q1670
    (
        'Explanation: Need: keep plans flexible. Option D (Assess and evaluate the certification process and understand the best and worst case scenarios.) fixes it."',
        'Explanation: Keywords: certification process needs 6 months, mass production scheduled in 3 months, assess best and worst case scenarios. Before escalating or committing to a solution, the project manager should thoroughly understand the certification process constraints. Assessing best and worst case scenarios provides the data needed to make an informed recommendation about schedule compression, scope changes, or timeline extension. (PMBOK Guide) – Seventh Edition, 2021, p. 46, \'Optimize Risk Responses\'"'
    ),
    # Q1671
    (
        'Explanation: Need: keep plans flexible. Option D (Identify the risks in implementing the new technology.) fixes it."',
        'Explanation: Keywords: new technology project, approval required, identify risks in implementing new technology. Before committing to a new technology project, identifying the associated risks is essential to building a credible business case and approval request. Understanding key risks allows decision-makers to evaluate the project\'s viability and assign appropriate contingencies. (PMBOK Guide) – Seventh Edition, 2021, p. 46, \'Optimize Risk Responses\'"'
    ),
    # Q1672
    (
        'Explanation: Need: guide and calm the team. Option A (Clear responsible, accountable, consult, and inform (RACI) matrix) fixes it."',
        'Explanation: Keywords: governance issue, team member receiving assignments from multiple people, not working effectively, RACI matrix. A team member receiving conflicting assignments from multiple sources signals an unclear accountability structure. Establishing a clear RACI matrix defines who is Responsible, Accountable, Consulted, and Informed for each task, eliminating ambiguity about who directs the team member\'s work and restoring effectiveness. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    # Q1673
    (
        'Explanation: Need: guide and calm the team. Option B (Support a voting exercise so all team members can express their opinion and the reason behind their vote.) fixes it."',
        'Explanation: Keywords: sprint planning, product owner wants high business value, team concerned about technical debt and infrastructure dependencies. When the product owner\'s priorities conflict with the team\'s technical concerns, a voting exercise creates a safe space for all voices to be heard. This collaborative decision-making surfaces the rationale behind both positions, enabling the team to reach a balanced prioritization that accounts for both value delivery and technical health. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    # Q1674
    (
        'Explanation: Need: listen to people needs. Option C (Inform the subcontractor that they must send the schedule.) fixes it."',
        'Explanation: Keywords: milestone payment conditioned on updated schedule, subcontractor claims agreement already made, must send schedule. A contract condition is binding regardless of informal agreements between the subcontractor and the client. Informing the subcontractor clearly and directly that the schedule must be submitted upholds the contractual terms and the project manager\'s stewardship responsibility to protect the project\'s interests. (PMBOK Guide) – Seventh Edition, 2021, p. 25, \'Be a Diligent, Respectful, and Caring Steward\'"'
    ),
    # Q1675
    (
        'Explanation: Need: listen to people needs. Option B (Analyze the impact against the release plan if the blocker is not addressed.) fixes it."',
        'Explanation: Keywords: subcontractor cash flow problem, may not provide same resources for next iterations, release plan impacted. When an external dependency is threatened, the first step is to quantify the impact on the project\'s plans before deciding on a response. Analyzing the impact against the release plan provides the data needed to assess severity and decide whether to escalate or restructure the delivery approach. (PMBOK Guide) – Seventh Edition, 2021, p. 34, \'Recognize, Evaluate, and Respond to System Interactions\'"'
    ),
    # Q1676
    (
        'Explanation: Need: protect benefits for users. Option D (Negotiate special arrangements for an agile pilot project.) fixes it."',
        'Explanation: Keywords: organization beginning agile delivery, lack of support from business units, lack of trust in agile, negotiate agile pilot. Organizational resistance to agile adoption is best addressed through demonstrated results rather than mandates. A pilot project negotiated with skeptical business units provides a low-risk, evidence-based path to building trust in agile delivery, enabling change through participation rather than imposition. (PMBOK Guide) – Seventh Edition, 2021, p. 50, \'Enable Change to Achieve the Envisioned Future State\'"'
    ),
    # Q1677
    (
        'Explanation: Need: guide and calm the team. Option A (Empower the team members to conduct their job activities and hold each person accountable to improve the schedule.) fixes it."',
        'Explanation: Keywords: servant leader, critical roadway construction, low-performing team, falling behind schedule. A servant leader\'s response to underperformance is to empower team members and establish clear accountability, not to impose direct control or threaten consequences. Empowering the team to take ownership of their work and holding each person accountable creates a performance culture that can sustain schedule recovery without undermining morale. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    # Q1678
    (
        'Explanation: Need: keep plans flexible. Option A (Assess the schedule impact and evaluate the most feasible solution to keep the project on track.) fixes it."',
        'Explanation: Keywords: factory acceptance test, deficiencies identified, product on critical path, assess schedule impact. When a quality issue threatens a critical path item, the first step is to assess the schedule impact quantitatively before choosing a resolution strategy. Understanding the full range of feasible options allows the project manager to choose the solution that best balances cost, time, and quality. (PMBOK Guide) – Seventh Edition, 2021, p. 46, \'Optimize Risk Responses\'"'
    ),
    # Q1679 — curly apostrophe U+2019 in "team members'"
    (
        'Explanation: Need: guide and calm the team. Option B (Review the list of team members’ skills and understand how they will work together to deliver the project outcomes.) fixes it."',
        'Explanation: Keywords: service integration project, team from two companies, different technology backgrounds, different work approaches. Building a cohesive team across organizations requires understanding what each member brings and how their skills complement each other. Reviewing skills and understanding how team members will collaborate enables the project manager to design a working structure that leverages diverse capabilities effectively. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    # Q1680 — multi-select A,C,E
    (
        'Explanation: Need: guide and calm the team. Options A, C, and E (Arrange and conduct team-building sessions to improve team effectiveness.; Get feedback from other team members to understand what led to this situation.; Obtain feedback from the isolated team member to understand the situation.) work together."',
        'Explanation: Keywords: team member isolated by others, time-bound quality improvement project, team-building sessions, feedback from all sides. When a team member is isolated, effective intervention requires understanding the situation from all perspectives. Gathering feedback from both the isolated team member and colleagues, combined with structured team-building, addresses both the symptom and the underlying interpersonal friction. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    # Q1681
    (
        'Explanation: Need: guide and calm the team. Option C (Mentor the team member on a regular basis.) fixes it."',
        'Explanation: Keywords: team member asking for directions on many tasks, performing slowly, mentor on regular basis. A team member who consistently seeks direction may lack confidence or clarity rather than capability. Regular mentoring builds the team member\'s judgment and decision-making skills over time, gradually reducing dependency on the project manager while improving performance and engagement. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    # Q1682
    (
        'Explanation: Need: guide and calm the team. Option B (Adjust the project manager\'s management style to better fit senior team members.) fixes it."',
        'Explanation: Keywords: experienced team members feel micromanaged, complaints about project manager, adjust management style. Effective leadership requires adapting one\'s style to the experience level and maturity of the team. Senior team members need autonomy and trust, not close supervision; adjusting the management style demonstrates servant leadership and removes the barrier to their effective contribution. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    # Q1683
    (
        "Explanation: Need: listen to people needs. Option C (Meet with the project team to discuss the concerns and determine how to ensure the project's deliverable can compete with the competitor's.) fixes it.\"",
        "Explanation: Keywords: competitor releasing similar product with newer technology, project manager fears competitor's offering is better, meet with project team. When a competitive threat is identified, the project team has the collective knowledge to assess the threat and identify improvement opportunities across technical, scope, and strategic dimensions. Meeting with the full project team ensures all perspectives are considered in the competitive response. (PMBOK Guide) – Seventh Edition, 2021, p. 46, 'Optimize Risk Responses'\""
    ),
    # Q1684
    (
        'Explanation: Need: guide and calm the team. Option B (Create the epics at a high level for the requirements and begin grooming sessions.) fixes it."',
        'Explanation: Keywords: agile team, mandatory government project, 6 months, create epics at high level and begin grooming sessions. For a mandate-driven agile project, starting with high-level epics allows the team to capture the required scope broadly before diving into detailed stories. Beginning grooming sessions immediately creates a structured, collaborative process for refining requirements incrementally as clarity emerges. (PMBOK Guide) – Seventh Edition, 2021, p. 40, \'Tailor Based on Context\'"'
    ),
    # Q1685
    (
        'Explanation: Need: listen to people needs. Option A (Ask the sponsor for an experienced team member in the company to help the project team.) fixes it."',
        'Explanation: Keywords: agile environment, 4th of 6 iterations, team member leaves with no replacement, ask sponsor for experienced team member. When a key team member departs mid-project with no replacement available through normal channels, the sponsor is the appropriate escalation path for securing experienced internal resources quickly. This preserves project momentum without compromising the team\'s ability to meet iteration commitments. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    # Q1686
    (
        'Explanation: Need: guide and calm the team. Option C (Ask the team to propose a minimum viable product (MVP) to meet the date.) fixes it."',
        'Explanation: Keywords: critical project, strict deadline, too many requirements to deliver on time, ask team to propose MVP. When requirements exceed delivery capacity, an MVP approach ensures the most valuable functionality is delivered by the deadline. Asking the team to propose the MVP engages their technical expertise in defining what is achievable, building ownership of the solution and increasing commitment to meeting the date. (PMBOK Guide) – Seventh Edition, 2021, p. 32, \'Focus on Value\'"'
    ),
    # Q1687
    (
        'Explanation: Need: listen to people needs. Option C (Review the additional changes and perform integrated change control.) fixes it."',
        'Explanation: Keywords: customer requests changes 1 day before planned change date, review changes, integrated change control. Change requests — regardless of timing — must follow the integrated change control process to assess impacts on scope, schedule, cost, and quality before approval. Skipping this process because the lead time is short would undermine the project\'s control mechanisms and risk unintended consequences. (PMBOK Guide) – Seventh Edition, 2021, p. 44, \'Navigate Complexity\'"'
    ),
    # Q1688
    (
        'Explanation: Need: listen to people needs. Option C (Risk register) fixes it."',
        'Explanation: Keywords: new office overseas, delays due to legal permits, CCB approved additional time, update risk register. When a change is approved specifically to address an identified risk (longer permit timeline), the risk register must be updated first to document the change, its associated risk event, and the approved response. This ensures the project\'s risk management records accurately reflect the current risk posture. (PMBOK Guide) – Seventh Edition, 2021, p. 46, \'Optimize Risk Responses\'"'
    ),
    # Q1689
    (
        'Explanation: Need: listen to people needs. Option A (Propose to close the project because it no longer fits the business values of the organization.) fixes it."',
        'Explanation: Keywords: environmentally sustainable organization, stakeholders oppose project, land erosion concerns, project viability questioned. When a project fundamentally conflicts with the organization\'s values and faces stakeholder opposition on ethical grounds, continuing it would damage organizational integrity and stakeholder trust. Proposing to close the project demonstrates stewardship by protecting the organization\'s values and reputation over short-term delivery. (PMBOK Guide) – Seventh Edition, 2021, p. 25, \'Be a Diligent, Respectful, and Caring Steward\'"'
    ),
    # Q1690
    (
        'Explanation: Need: listen to people needs. Option C (Push back on the feature because it is not an immediate priority.) fixes it."',
        'Explanation: Keywords: feature prioritized over critical security patches, iteration backlog, sponsor override, push back. Security patches that protect the product from critical vulnerabilities represent higher value than new features. Pushing back on the sponsor\'s feature request — citing the relative priority of security — demonstrates the project manager\'s responsibility to protect the integrity and reliability of the product. (PMBOK Guide) – Seventh Edition, 2021, p. 32, \'Focus on Value\'"'
    ),
    # Q1691 — multi-select C,D
    (
        'Explanation: Need: listen to people needs. Options C and D (Reduce the scope items of the final deliverable.; Discuss and review this external risk with the project sponsor.) work together."',
        'Explanation: Keywords: competitor releasing similar deliverable in 8 months with fewer features, design phase not yet started, reduce scope, discuss risk with sponsor. A competitive release timeline is both a market risk and a scope decision trigger. Discussing the risk with the sponsor ensures informed decision-making at the appropriate level, while reducing scope targets delivery of a competitive subset before the competitor\'s release — together these actions address both strategic and operational dimensions of the threat. (PMBOK Guide) – Seventh Edition, 2021, p. 48, \'Embrace Adaptability and Resiliency\'"'
    ),
    # Q1692
    (
        'Explanation: Need: listen to people needs. Option D (Define a product scope and ask the stakeholders to not deviate from it.) fixes it."',
        'Explanation: Keywords: constant complaints about functionalities delivered but not required, project resources not used effectively, define product scope. When teams repeatedly deliver work that stakeholders did not need, the root cause is typically insufficient scope definition. Defining a clear product scope and establishing boundaries prevents scope creep and ensures resources are directed only toward deliverables that genuinely add business value. (PMBOK Guide) – Seventh Edition, 2021, p. 32, \'Focus on Value\'"'
    ),
    # Q1693
    (
        'Explanation: Need: listen to people needs. Option B (Share the project schedule, milestones, and meeting agendas with the stakeholders ahead of time.) fixes it."',
        'Explanation: Keywords: integration project, stakeholders require significant time for decisions, critical and time-bound, share schedule and agendas ahead of time. Providing stakeholders with advance notice of decision points — through the schedule, milestones, and meeting agendas — allows them to prepare and reserve time appropriately. This proactive communication ensures key stakeholders can engage meaningfully without disrupting their other commitments. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    # Q1694
    (
        'Explanation: Need: listen to people needs. Option B (User stories) fixes it."',
        'Explanation: Keywords: new agile project, confirm scope to address stakeholder concern, user stories. User stories are the natural vehicle in agile for expressing scope in terms of user needs and business outcomes. Using user stories to explain the project scope aligns communication with the agile framework and makes scope tangible and understandable to stakeholders who may not be familiar with traditional documentation. (PMBOK Guide) – Seventh Edition, 2021, p. 40, \'Tailor Based on Context\'"'
    ),
    # Q1695
    (
        'Explanation: Need: listen to people needs. Option B (Discuss reducing interruptions with the sponsor.) fixes it."',
        'Explanation: Keywords: sponsor micromanaging, requesting iterations affecting team effectiveness, scope not affected, discuss reducing interruptions. When a sponsor\'s involvement — even well-intentioned — disrupts team effectiveness, it is the project manager\'s responsibility to address it constructively. Discussing reducing interruptions with the sponsor directly maintains the working relationship while protecting the team\'s ability to perform. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    # Q1696
    (
        'Explanation: Need: listen to people needs. Option A (Identified the vice president as a stakeholder) fixes it."',
        'Explanation: Keywords: vice president valid concern brought late in project, not identified as stakeholder earlier, release delayed. Stakeholder identification is a critical early-project activity precisely because overlooked stakeholders introduce risks at the worst possible times. If the vice president had been identified as a stakeholder during planning, their concerns could have been captured and addressed early rather than surfacing as a last-minute change. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    # Q1697
    (
        'Explanation: Need: listen to people needs. Option B (Perform integrated change control.) fixes it."',
        'Explanation: Keywords: quality audit failed, multiple action items, new stakeholders identified, new audit resources, integrated change control. When audit results require adding new stakeholders, resources, and actions to the project, these represent changes to the project baseline that must be processed through integrated change control. This ensures the changes are formally evaluated, approved, and incorporated into the project management plan in a controlled manner. (PMBOK Guide) – Seventh Edition, 2021, p. 44, \'Navigate Complexity\'"'
    ),
    # Q1698
    (
        'Explanation: Need: listen to people needs. Option B (Set up a meeting with key stakeholders to clarify requirements.) fixes it."',
        'Explanation: Keywords: development team in another country, different interpretations of client needs, rework causing delays, clarify requirements. When rework results from divergent requirement interpretations, bringing key stakeholders together to clarify expectations directly is the most effective fix. A structured clarification meeting aligns the development team, the client, and the project manager on the correct requirements, preventing further rework. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    # Q1699
    (
        'Explanation: Need: listen to people needs. Option D (Estimate the impact and consult with the product owner.) fixes it."',
        'Explanation: Keywords: 5th of 6 iterations, customer adds regulatory feature exceeding remaining capacity, estimate impact, consult product owner. A regulatory feature added late in the project requires assessing its impact on scope, timeline, and remaining iterations before committing to any course of action. Consulting the product owner ensures that prioritization decisions reflect the correct business and compliance priorities. (PMBOK Guide) – Seventh Edition, 2021, p. 32, \'Focus on Value\'"'
    ),
    # Q1700
    (
        'Explanation: Need: watch risks early. Option D (Assess the situation as a risk and reach out to the contractor to check the origin of this resistance.) fixes it."',
        'Explanation: Keywords: contractor stops attending meetings and submitting reports, claims consuming too much time, assess as risk. When a contractor withdraws from agreed activities, this behavior signals an underlying issue — potential dissatisfaction, resource constraints, or misaligned expectations — that could escalate into a more serious project risk. Assessing the situation as a risk and proactively reaching out identifies the root cause before it affects deliverables. (PMBOK Guide) – Seventh Edition, 2021, p. 46, \'Optimize Risk Responses\'"'
    ),
    # Q1701
    (
        'Explanation: Need: guide and calm the team. Option C (Share the project team ground rules with the subcontractors.) fixes it."',
        'Explanation: Keywords: subcontracted resources from sister company, smooth inclusion, share project team ground rules. The most direct way to integrate subcontracted resources into the team environment is to share the established ground rules. This sets clear expectations about how the team operates, communicates, and makes decisions, enabling subcontractors to integrate quickly without disrupting existing team norms. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    # Q1702
    (
        'Explanation: Need: listen to people needs. Option B (Reviewed the compliance requirements with stakeholders) fixes it."',
        'Explanation: Keywords: government-owned company, iterative approach, first useful release, security team declined deployment. Compliance requirements — particularly security requirements enforced by a government security team — must be identified and incorporated from the start. Reviewing compliance requirements with all relevant stakeholders, including the security team, during iteration planning would have surfaced the deployment constraints before the code was written. (PMBOK Guide) – Seventh Edition, 2021, p. 25, \'Be a Diligent, Respectful, and Caring Steward\'"'
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
