MD_FILE = './src/imports/project-management-questions-1.md'

with open(MD_FILE, 'r', encoding='utf-8') as f:
    content = f.read()

replacements = [
    (
        'Explanation: Need: listen to people needs. Options A, C, and D (A team member talking about a user story that is not on the Scrum board; A technology that blocks agile capabilities; A lack of team empowerment and an inability to self-organize) work together."',
        'Explanation: Keywords: Scrum master, impediments, agile capability blockers, self-organization. The Scrum master\'s role is to remove impediments to the team\'s delivery. A user story outside the sprint scope signals scope creep, a blocking technology undermines the team\'s agile capability, and lack of empowerment prevents self-organization — all three directly threaten the team\'s ability to deliver on its commitments. (PMBOK Guide) – Seventh Edition, 2021, p. 28, p. 29, \'Create a Collaborative Team Environment\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option D (Create prototypes with the development team to confirm requirements) fixes it."',
        'Explanation: Keywords: international development team, requirement misinterpretation, rework, prototype validation. When different interpretations of requirements are causing rework across geographies, written clarification alone is insufficient — prototypes make the requirement tangible and visible, allowing both teams to validate their shared understanding before more work is built on a flawed foundation. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option A (Create a prioritized backlog and define iteration review sessions with stakeholders) fixes it."',
        'Explanation: Keywords: evolving scope, unclear completion, new stakeholders, business goal misalignment. When scope changes frequently and new stakeholders keep finding gaps, the fix is structure and transparency. A prioritized backlog gives evolving scope a controlled form, while iteration review sessions keep stakeholders continuously aligned — preventing the disconnect between what is delivered and what the business actually needs. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option A (Collaborate with the change control board (CCB) to review the scope and submit any change requests) fixes it."',
        'Explanation: Keywords: schedule delay, scope change concerns, change control board, feasibility study. When a feasibility study confirms the project is behind schedule and scope changes are adding pressure, the PM must route those changes through the CCB rather than absorbing them informally. Formal change control ensures each scope change is evaluated for schedule and cost impact before being approved. (PMBOK Guide) – Seventh Edition, 2021, p. 50, \'Enable Change to Achieve the Envisioned Future State\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option B (A leadership style that coaches people who want help and fosters greater team collaboration) fixes it."',
        'Explanation: Keywords: agile transition, new team, no outcomes after two sprints, coaching leadership. A new agile team that has not yet produced results needs a leader who builds collaboration and supports individuals who are struggling — not one who imposes direction or steps back entirely. A coaching style develops the team\'s agile capability while addressing the pressure from above with steady progress. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option D (Breakdown the situation to identify the root causes for the disagreement and then work with each stakeholder and participating entity on their exact roles and responsibilities) fixes it."',
        'Explanation: Keywords: stakeholder disagreement, project objectives, approach conflict, root cause. Disagreements about objectives and approach typically have different underlying causes for each stakeholder. Breaking down the situation to find those root causes — and then working individually with each party on their specific role — is more effective than trying to resolve everything in a general meeting where the real concerns stay buried. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option C (Ensure the team has a common understanding of agile) fixes it."',
        'Explanation: Keywords: mixed agile backgrounds, different methodologies, shared framework, team alignment. Team members with different agile experiences carry different assumptions about rituals, ceremonies, and roles. Establishing a common understanding before work begins prevents friction that arises when people believe they are working the same way but are applying different practices and using the same words to mean different things. (PMBOK Guide) – Seventh Edition, 2021, p. 28, p. 29, \'Create a Collaborative Team Environment\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option A (Reviewed the communications management plan before inviting an external client representative to the meeting) fixes it."',
        'Explanation: Keywords: budget exposure, external client in meeting, communications management plan, sensitive information. The communications management plan defines what information can be shared with which parties and in which settings. Reviewing it before the meeting would have flagged that budget details are internal and not appropriate to present in front of an external client representative. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    (
        'Explanation: Need: keep plans flexible. Option D (Review and update the issue log and determine if any alternative components can be offered) fixes it."',
        'Explanation: Keywords: vendor delay, core component unavailable, schedule impact, alternative exploration. When a vendor confirms a component cannot arrive on time, the PM\'s first actions are to log the issue formally and explore whether alternative components can fill the gap. Escalating to stakeholders or replacing the vendor before investigating alternatives is premature and may cause unnecessary disruption. (PMBOK Guide) – Seventh Edition, 2021, p. 46, \'Optimize Risk Responses\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option A (Add this risk to the risk register and monitor it according to the risk management plan) fixes it."',
        'Explanation: Keywords: hybrid project, agile-predictive dependency, delivery commitment gap, integration risk. In a hybrid project, an agile team\'s inability to commit to a delivery date that a predictive team depends on is a real integration risk. Registering it formally and monitoring it with a defined response plan ensures the risk is managed proactively rather than becoming a crisis when the hardware team is blocked. (PMBOK Guide) – Seventh Edition, 2021, p. 46, \'Optimize Risk Responses\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option A (Persuade this stakeholder using emotional intelligence skills to obtain acceptance.) fixes it."',
        'Explanation: Keywords: acceptance refusal, outside acceptance criteria, stakeholder concern, emotional intelligence. When a stakeholder withholds acceptance for reasons that fall outside the formal criteria, the underlying issue is relational or perceptual rather than technical. Applying emotional intelligence — active listening, empathy, and interpersonal awareness — allows the PM to understand and address the real concern driving the refusal. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    (
        'Explanation: Need: keep plans flexible. Option B (Identify the goal of each work product) fixes it."',
        'Explanation: Keywords: project management plan, continual benefit delivery, work product purpose, value alignment. When every work product has a clearly defined goal, delivery remains connected to the benefits the project was chartered to produce. This traceability between individual outputs and intended outcomes is what allows the PM to confirm that the plan is continually moving toward expected benefits rather than just producing deliverables. (PMBOK Guide) – Seventh Edition, 2021, p. 32, \'Focus on Value\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option D (Update the resource calendar for enrolled team members in the resource management plan) fixes it."',
        'Explanation: Keywords: work-from-home policy, team availability change, resource calendar, resource management. When team members shift to a different work arrangement, their availability, working hours, and accessibility change. Updating the resource calendar ensures the project schedule and resource allocation reflect reality rather than assumptions based on the previous on-site arrangement. (PMBOK Guide) – Seventh Edition, 2021, p. 25, \'Be a Diligent, Respectful, and Caring Steward\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Options A and C (Five whys; Ishikawa diagrams) work together."',
        'Explanation: Keywords: stakeholder engagement failure, geographically diverse project, root cause analysis, five whys, Ishikawa. When planned engagement strategies are not producing the expected results across diverse geographies, the PM must diagnose why before changing approach. Five whys drills iteratively into the causal chain while an Ishikawa diagram maps multiple potential contributing factors — together they surface the true root cause of the engagement failure. (PMBOK Guide) – Seventh Edition, 2021, p. 44, \'Navigate Complexity\'"'
    ),
    (
        'Explanation: Need: watch risks early. Option C (Prioritize and estimate the milestones for the high-level requirements based on historical data) fixes it."',
        'Explanation: Keywords: program interdependencies, uncertain requirement priorities, historical data, milestone planning. When priorities are uncertain because of cross-project dependencies, waiting for full clarity before planning is not an option. Using historical data to prioritize and estimate milestones for what is known allows the PM to begin planning proactively while remaining ready to adjust as interdependent project details are confirmed. (PMBOK Guide) – Seventh Edition, 2021, p. 44, \'Navigate Complexity\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option B (Schedule knowledge transfer sessions and assign less complex tasks to the new team member) fixes it."',
        'Explanation: Keywords: team member replacement, agile project, knowledge transfer, gradual ramp-up. Accelerating a new member\'s contribution requires both knowledge and confidence. Structured knowledge transfer sessions connect them to the project\'s accumulated context, while starting with less complex tasks builds their understanding of the codebase and team norms before they take on higher-stakes work. (PMBOK Guide) – Seventh Edition, 2021, p. 28, p. 29, \'Create a Collaborative Team Environment\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option A (Plan to address the issues through backlog grooming and incorporate them into the next sprint) fixes it."',
        'Explanation: Keywords: first sprint demo, product owner issues, backlog grooming, next sprint incorporation. In agile, surfacing issues during a sprint demo is the system working as intended. Incorporating the product owner\'s concerns through backlog grooming and planning them into the next sprint is the designed mechanism for continuous improvement — it keeps delivery moving while systematically addressing what needs to be fixed. (PMBOK Guide) – Seventh Edition, 2021, p. 48, \'Embrace Adaptability and Resiliency\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option A (Develop the resource management plan and ensure adequate training) fixes it."',
        'Explanation: Keywords: skills gap, planning phase, key tasks, training planning. Discovering skills gaps during planning — when they can still be addressed proactively — is the right time to act. Developing the resource management plan formalizes how the team will be built and trained, ensuring the necessary capabilities are in place before the tasks that depend on them begin. (PMBOK Guide) – Seventh Edition, 2021, p. 28, p. 29, \'Create a Collaborative Team Environment\'"'
    ),
    (
        'Explanation: Need: keep plans flexible. Option C (Continually survey the quality of the deliverable) fixes it."',
        'Explanation: Keywords: hybrid project, execution phase, quality compliance, ongoing quality monitoring. During execution of a complex project, quality cannot be managed as a final gate — defects discovered late are far more costly to fix. Continually surveying the quality of deliverables throughout execution ensures nonconformances are identified and corrected while the work is still in progress. (PMBOK Guide) – Seventh Edition, 2021, p. 42, \'Build Quality into Processes and Deliverables\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option B (Conduct stakeholder identification and a project objectives review session) fixes it."',
        'Explanation: Keywords: new stakeholder, unmet business capabilities, objectives review, stakeholder identification. A new stakeholder who is dissatisfied with results signals that their expectations were never captured in the project\'s objectives. Conducting stakeholder identification and reviewing project objectives ensures their needs are surfaced before further iterations are planned on a foundation that may not align with what the business actually requires. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    (
        'Explanation: Need: keep plans flexible. Option B (Determine the most appropriate life cycle approach for the project) fixes it."',
        'Explanation: Keywords: mixed requirement clarity, life cycle selection, predictive versus adaptive. When some requirements are clear and others still need definition, the PM\'s first decision is which life cycle approach best fits the mix. Choosing a methodology before assessing the project\'s characteristics risks forcing the wrong structure onto a project whose nature calls for something different. (PMBOK Guide) – Seventh Edition, 2021, p. 40, \'Tailor Based on Context\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option B (Emotional intelligence) fixes it."',
        'Explanation: Keywords: hearing impairment, team disengagement, private conversation, inclusive adaptation. The PM noticed a team member\'s disengagement, sought to understand it privately rather than publicly, responded with empathy rather than judgment, and adapted the meeting environment to enable full participation. This sequence — self-awareness, empathy, and relationship management in action — is the definition of emotional intelligence applied to leadership. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option B (The attendance list is evidence that risk review meetings were held with the appropriate project team members) fixes it."',
        'Explanation: Keywords: quality audit, attendance records, risk review meetings, compliance evidence. Attendance records are not administrative formalities — they are the documentary proof that risk review meetings occurred and included the right people. Without them, an auditor has no basis to confirm that the risk management process was executed as required by the project\'s quality standards. (PMBOK Guide) – Seventh Edition, 2021, p. 25, \'Be a Diligent, Respectful, and Caring Steward\'"'
    ),
    (
        'Explanation: Need: learn from data and lessons. Option B (Review the lessons learned from the previous project) fixes it."',
        'Explanation: Keywords: product enhancement, existing internal product, lessons learned, project initiation. When initiating an enhancement of an existing product that was built internally, the organization\'s own experience is the most directly applicable input available. Lessons learned from the previous project capture the specific pitfalls, decisions, and insights that are most relevant to the work now beginning. (PMBOK Guide) – Seventh Edition, 2021, p. 25, \'Be a Diligent, Respectful, and Caring Steward\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option B (Hold a meeting with the project team project sponsor and the client to agree to the further work required to close the project and add to lessons learned) fixes it."',
        'Explanation: Keywords: project closure dispute, code inspection records incomplete, client acceptance, documentation gap. Incomplete records create legitimate doubt about whether a contractual obligation was met. The responsible path is to bring all parties together, acknowledge the documentation gap openly, agree on what is needed to satisfy closure, and capture the experience in lessons learned to prevent it from happening again. (PMBOK Guide) – Seventh Edition, 2021, p. 25, \'Be a Diligent, Respectful, and Caring Steward\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option A (Quantify the expected tangible and intangible benefits in the benefits management plan for each phase) fixes it."',
        'Explanation: Keywords: financial threshold not met, intangible benefits, phased implementation, benefits management plan. When a project does not clear the financial hurdle but carries significant strategic value, the benefits management plan must make both tangible and intangible benefits explicit and quantifiable per phase. Without this, the project\'s full value case remains invisible to decision-makers who would otherwise see only the financial shortfall. (PMBOK Guide) – Seventh Edition, 2021, p. 32, \'Focus on Value\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option D (Hold a meeting with the project team and relevant stakeholders to agree on the best way to manage the issue) fixes it."',
        'Explanation: Keywords: unregistered emerging issue, big impact, no planned response, collaborative resolution. When an issue arises that was never in the risk register, there is no pre-planned response to execute. Bringing together the project team and relevant stakeholders to collectively determine the best course of action applies the broadest available knowledge to a situation the planning process did not anticipate. (PMBOK Guide) – Seventh Edition, 2021, p. 46, \'Optimize Risk Responses\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option D (Used the resource management plan to identify the impacts of the other projects) fixes it."',
        'Explanation: Keywords: shared resources, competing project priorities, component delay, resource interdependency. When resources are shared across projects, each project\'s demand on those resources affects the others. The resource management plan is the tool that makes those cross-project interdependencies visible — using it proactively allows the PM to anticipate conflicts and act before shared priorities become schedule failures. (PMBOK Guide) – Seventh Edition, 2021, p. 34, \'Recognize, Evaluate, and Respond to System Interactions\'"'
    ),
    (
        'Explanation: Need: control changes and baselines. Option D (Ensured that all the required approvals were received per the organizational procedures) fixes it."',
        'Explanation: Keywords: post-implementation audit, regulatory penalty, approval process, implementation compliance. Organizational approval procedures exist to ensure that implementations meet all compliance requirements before they go live. Receiving all required approvals per those procedures is the PM\'s responsibility — it is the mechanism that protects the project from exactly the kind of post-implementation liability the audit uncovered. (PMBOK Guide) – Seventh Edition, 2021, p. 25, \'Be a Diligent, Respectful, and Caring Steward\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option C (Gather project artifacts that demonstrate the team member\'s high performance) fixes it."',
        'Explanation: Keywords: PM succession recommendation, high performer, project artifacts, evidence-based promotion. A recommendation to senior management requires objective, documented evidence — not anecdotes or summaries. Project artifacts provide verifiable proof of the team member\'s contributions, decisions, and outcomes, giving senior management the concrete basis they need to evaluate the recommendation with confidence. (PMBOK Guide) – Seventh Edition, 2021, p. 25, \'Be a Diligent, Respectful, and Caring Steward\'"'
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
