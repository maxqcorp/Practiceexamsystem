MD_FILE = './src/imports/project-management-questions-1.md'

with open(MD_FILE, 'r', encoding='utf-8') as f:
    content = f.read()

replacements = [
    (
        'Explanation: Need: listen to people needs. Option A (Discuss the company culture with the supervisor to clarify expectations.) fixes it."',
        'Explanation: Keywords: supervisor leadership style, company culture, worker complaints, expectations discussion. When a supervisor\'s leadership style conflicts with the established company culture and is causing worker complaints, the project manager\'s responsibility is to address this directly with the supervisor by explaining the organizational values and behavioral expectations. A discussion grounded in company culture gives the supervisor the context to align their approach with the organization\'s norms rather than interpreting the feedback as personal criticism. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option A (Determine a leadership style that is suitable for that location.) fixes it."',
        'Explanation: Keywords: international assignment, location-appropriate leadership, cultural context, team collaboration. When a project manager is transferred to lead a team in a different country, the leadership approach that worked in their home environment may not be appropriate for the local culture. Determining a leadership style suited to the local context is the critical first step that enables genuine collaboration and ensures the team responds positively to the project manager\'s direction. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option D (Analyze the impact and inform the stakeholders.) fixes it."',
        'Explanation: Keywords: resource loss, deadline impact, impact analysis, stakeholder communication. When multiple developers resign with insufficient time to find replacements, the project manager must first assess the full impact on the project timeline and deliverables before informing stakeholders. Communicating a clear, analysis-based picture to stakeholders enables them to make informed decisions about schedule adjustments, scope changes, or resource escalation. (PMBOK Guide) – Seventh Edition, 2021, p. 34, \'Recognize, Evaluate, and Respond to System Interactions\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option B (Discuss the issue in the next retrospective.) fixes it."',
        'Explanation: Keywords: productivity decline, hybrid project, retrospective, team discussion. When a team\'s productivity declines after multiple iterations, the retrospective is the structured ceremony designed to surface and address exactly this type of performance issue. Bringing the productivity concern to the retrospective invites the team to collectively identify root causes and own the improvement rather than having solutions imposed by the project manager. (PMBOK Guide) – Seventh Edition, 2021, p. 48, \'Embrace Adaptability and Resiliency\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option B (Embed a feedback form into the system for users to respond.) fixes it."',
        'Explanation: Keywords: usage data, value evaluation, embedded feedback, production monitoring. Collecting usage data directly within the system through an embedded feedback form captures authentic user behavior and satisfaction information at the point of use, which is the most accurate way to evaluate delivered value. This approach provides continuous, real-time insights into how users interact with features without relying on users to seek out separate surveys or interviews. (PMBOK Guide) – Seventh Edition, 2021, p. 32, \'Focus on Value\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option B (Provide an opportunity to one of the existing team members to become an SME.) fixes it."',
        'Explanation: Keywords: SME gap, internal development, future projects, capability building. When a needed SME capability is missing and will be required across multiple future projects, the most sustainable solution is to develop that expertise from within the existing team rather than continuously hiring external contractors. Providing a team member with the opportunity to become an SME builds lasting organizational capability while also increasing that team member\'s engagement and career development. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option B (Meet with the team member\'s functional manager to try to remove the impediment.) fixes it."',
        'Explanation: Keywords: functional manager interference, sprint commitment, impediment removal, servant leadership. When a functional manager\'s request is preventing a team member from completing a sprint commitment, the project manager must act as a servant leader by directly engaging the functional manager to resolve the conflict and protect the team\'s capacity. Removing this impediment at the source is more effective than simply escalating it or adjusting the sprint commitment without addressing the underlying resource conflict. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option B (Use a problem-solving approach and set up a discussion with the team lead and team member.) fixes it."',
        'Explanation: Keywords: favoritism complaint, team lead, problem-solving approach, conflict resolution. When a team member raises a well-documented complaint about favoritism by a team lead, the project manager must address it through a structured problem-solving approach rather than ignoring it or immediately escalating. Setting up a direct discussion between the team lead and the affected team member facilitates a resolution based on the specific facts rather than general guidelines or policy. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option C (Review the key performance indicators (KPIs) for this team member and remind the team member how they are determined.) fixes it."',
        'Explanation: Keywords: performance review, KPIs, team member feedback, performance expectations. When a team member is frustrated by vague performance feedback, the project manager must ensure they understand which KPIs apply to their role and how those indicators are measured and evaluated. Reviewing the KPIs together and explaining the determination process transforms performance conversations from subjective impressions into objective, actionable data that the team member can work to improve. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option B (How the acceptance criteria were met) fixes it."',
        'Explanation: Keywords: closure report, acceptance criteria, client concerns, business needs alignment. When a client is uncertain that project outputs will meet their business needs, the project closure report must directly address how each acceptance criterion was met and how the deliverables connect to the intended business outcomes. Demonstrating acceptance criteria fulfillment provides the objective evidence the client needs to gain confidence in the project\'s business value. (PMBOK Guide) – Seventh Edition, 2021, p. 32, \'Focus on Value\'"'
    ),
    (
        'Explanation: Need: secure people or vendors. Option D (Include projected inflation rates.) fixes it."',
        'Explanation: Keywords: long-term project, budget estimate, inflation rates, multi-year project. A budget estimate for a project spanning several years must account for the erosion of purchasing power over time — failing to include projected inflation rates will systematically understate future costs. Including inflation projections ensures the budget baseline remains realistic across the project\'s full duration and prevents cost overruns driven by predictable macroeconomic factors. (PMBOK Guide) – Seventh Edition, 2021, p. 44, \'Navigate Complexity\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option B (Ensure that the definition of done (DoD) is well defined and complete for future iterations.) fixes it."',
        'Explanation: Keywords: feature rejection, definition of done, customer acceptance, iteration quality. When completed features are rejected by a customer, it indicates that the team\'s internal definition of "done" did not match the customer\'s acceptance expectations. A well-defined and complete DoD that explicitly captures all customer acceptance criteria prevents this misalignment by ensuring the team cannot consider a feature complete until all customer-required conditions are satisfied. (PMBOK Guide) – Seventh Edition, 2021, p. 42, \'Build Quality into Processes and Deliverables\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option B (Set up information review sessions before reconvening another approval session.) fixes it."',
        'Explanation: Keywords: stakeholder engagement, approval meeting, information overload, information review sessions. When stakeholders are rubber-stamping approvals due to information overload, meaningful approval cannot be obtained in the same session — the root problem is that stakeholders lack sufficient understanding to engage critically. Setting up separate information review sessions first ensures stakeholders have the knowledge and preparation needed to participate meaningfully in the subsequent approval meeting. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option A (Understood the customer\'s company culture) fixes it."',
        'Explanation: Keywords: communication frequency, customer culture, email annoyance, cultural understanding. A customer\'s preference for communication frequency and style is shaped by their organizational culture — what one company considers adequate updates may feel like intrusive overcommunication to another. Understanding the customer\'s company culture before designing the communication approach would have enabled the project manager to calibrate the frequency and format of updates to match the customer\'s actual preferences. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option D (Initiate a review of the procedures with the CTO and the team.) fixes it."',
        'Explanation: Keywords: CTO bypassing procedures, startup culture, procedure review, compliance. When a CTO actively encourages the team to skip established procedures in the name of speed, the project manager cannot simply instruct the team to comply without addressing the leadership contradiction. Initiating a procedure review with both the CTO and the team examines which procedures are truly necessary versus unnecessarily burdensome, and builds shared agreement on a compliance standard that the CTO will also support. (PMBOK Guide) – Seventh Edition, 2021, p. 25, \'Be a Diligent, Respectful, and Caring Steward\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option C (Schedule a meeting with both team members to understand the issue and facilitate a solution that satisfies both parties.) fixes it."',
        'Explanation: Keywords: team member conflict, deliverable impact, facilitated meeting, conflict resolution. When interpersonal issues between team members begin affecting deliverables during an active iteration, the project manager must directly facilitate a structured resolution rather than waiting or escalating. Scheduling a joint meeting allows the project manager to understand both perspectives and guide the parties toward a mutually acceptable solution before the conflict causes further schedule impact. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    (
        'Explanation: Need: protect value and acceptance. Option B (Early value can be gained by testing the most important features in the initial stages to fix deviations.) fixes it."',
        'Explanation: Keywords: agile value proposition, early value delivery, iterative testing, deviation correction. In agile development, value is not deferred to final release — testing the most important features first identifies deviations early when they are cheapest to fix, while simultaneously delivering functional capabilities to users. This iterative approach generates business value throughout the project by progressively delivering and validating working features. (PMBOK Guide) – Seventh Edition, 2021, p. 32, \'Focus on Value\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option D (In the planning meeting, focus on releasing a minimum viable product (MVP) quickly and getting feedback from the end users.) fixes it."',
        'Explanation: Keywords: uncertain requirements, MVP approach, early feedback, new product development. When a customer is building a brand new product and is uncertain about requirements and costs, the MVP approach provides a structured way to reduce uncertainty through rapid delivery and end-user feedback. Starting with the smallest viable product generates empirical customer insights that guide subsequent development far more reliably than trying to specify all requirements upfront. (PMBOK Guide) – Seventh Edition, 2021, p. 32, \'Focus on Value\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option C (Explain that the needs will be updated in the stakeholder engagement plan.) fixes it."',
        'Explanation: Keywords: stakeholder withdrawal, engagement plan, meeting attendance, stakeholder re-engagement. When a stakeholder announces they will no longer attend project meetings, the project manager must address this as an engagement plan issue — the stakeholder\'s ongoing participation may be needed at key decision points even if they feel currently well-informed. Explaining that their engagement needs will be formally updated in the stakeholder engagement plan communicates that attendance requirements may change as the project progresses. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    (
        'Explanation: Need: control changes and baselines. Option D (Add contingency into the budget for inflation and other changes.) fixes it."',
        'Explanation: Keywords: budget baseline, contingency reserves, inflation adjustment, WBS costing. Before establishing a budget baseline from WBS-derived estimates, contingency reserves must be added to account for identified risks, inflation, and other foreseeable changes — the baseline without contingency understates the realistic budget needed to deliver the project. Adding contingency ensures the budget baseline represents a defensible funding target that can absorb known uncertainties. (PMBOK Guide) – Seventh Edition, 2021, p. 44, \'Navigate Complexity\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option A (Ensure that relevant stakeholders and expectations are identified and assess the component delay.) fixes it."',
        'Explanation: Keywords: vendor delay, component impact, stakeholder identification, delay assessment. When a vendor announces a delay in a key component, the project manager must first identify all stakeholders who will be affected and understand the expectations around the impacted deliverables before communicating or proposing solutions. Assessing the delay\'s full impact on the project provides the factual basis for informing stakeholders and determining the appropriate response. (PMBOK Guide) – Seventh Edition, 2021, p. 34, \'Recognize, Evaluate, and Respond to System Interactions\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option D (Collect the requirements of the regulation and follow the change control process.) fixes it."',
        'Explanation: Keywords: regulatory requirement, sponsor resistance, change control process, compliance obligation. A new regulation is a mandatory constraint that cannot be waived at the sponsor\'s request — the project manager has an ethical and legal obligation to ensure the software complies. Collecting the regulatory requirements and processing them through the change control system ensures compliance is formally addressed with the documented oversight and approval needed to proceed correctly. (PMBOK Guide) – Seventh Edition, 2021, p. 50, \'Enable Change to Achieve the Envisioned Future State\'"'
    ),
    (
        'Explanation: Need: keep plans flexible. Option B (Refer to the resource management plan.) fixes it."',
        'Explanation: Keywords: SME departure, resource management plan, multiyear project, resource replacement. When a key SME resource leaves a long-running project due to organizational downsizing, the resource management plan provides the pre-established guidance for how to handle resource changes of this type — including replacement procedures, skill requirements, and escalation paths. Consulting the plan ensures the response is aligned with the project\'s documented resource strategy. (PMBOK Guide) – Seventh Edition, 2021, p. 34, \'Recognize, Evaluate, and Respond to System Interactions\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option A (Perform an impact analysis with subject matter experts (SMEs).) fixes it."',
        'Explanation: Keywords: government project interference, network upgrade, impact analysis, SMEs. When an external government project is identified as potentially affecting a network upgrade, the project manager must first perform an impact analysis with SMEs before taking any other action — the nature, extent, and timing of the impact must be understood before scope, schedule, or cost decisions can be made. SME involvement ensures the analysis is technically accurate and comprehensive. (PMBOK Guide) – Seventh Edition, 2021, p. 34, \'Recognize, Evaluate, and Respond to System Interactions\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option B (Ensure the team receives continuous feedback from customers users.) fixes it."',
        'Explanation: Keywords: requirement misinterpretation, hybrid project, continuous feedback, expectation alignment. When different team members interpret requirements differently and deliverables miss expectations, the root cause is insufficient ongoing customer validation throughout the delivery process. Ensuring the team receives continuous feedback from customer users creates a real-time correction mechanism that catches misinterpretations early before they accumulate into significant rework. (PMBOK Guide) – Seventh Edition, 2021, p. 32, \'Focus on Value\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option D (Discard the current categorization of requirements as high, medium, and low and prioritize numerically.) fixes it."',
        'Explanation: Keywords: backlog prioritization, high priority overload, numerical prioritization, team clarity. When too many items are categorized as high priority, the prioritization scheme has lost its ability to guide the team — every item being "equally important" is functionally the same as having no priority. Replacing the ambiguous category system with a numerical ranking forces explicit ordering that tells the team exactly which item to work on next without ambiguity. (PMBOK Guide) – Seventh Edition, 2021, p. 32, \'Focus on Value\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option B (Stakeholder analysis) fixes it."',
        'Explanation: Keywords: stakeholder data, stakeholder analysis, organizational influence, role assessment. Information about stakeholders\' roles, project history, and organizational influence is the core input to stakeholder analysis — the process of systematically identifying, categorizing, and planning engagement strategies for each stakeholder. This analysis produces the stakeholder register and the basis for the stakeholder engagement plan that guides all subsequent communication and involvement decisions. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option A (Communicate the task assignments to the team members in a clear manner.) fixes it."',
        'Explanation: Keywords: task duplication, hybrid project, task assignment clarity, agile phase. When team members unknowingly work on the same task during an agile phase, it signals a breakdown in task assignment transparency and team coordination. Communicating task assignments clearly — such as through a visual board or updated backlog — prevents duplicated effort and ensures every team member knows what work has been claimed and by whom. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option B (Inform the project team and create a spike for the next Iteration.) fixes it."',
        'Explanation: Keywords: privacy law compliance, spike, agile investigation, regulatory requirement. When a new regulatory compliance requirement is identified, the team needs dedicated time to investigate what changes are needed before they can be estimated or committed — a spike provides that structured investigation. Creating a spike for the next iteration allows the team to systematically assess the compliance implications without disrupting the current sprint or making premature implementation commitments. (PMBOK Guide) – Seventh Edition, 2021, p. 46, \'Optimize Risk Responses\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option D (Project managers are expected to become coaches in agile teams.) fixes it."',
        'Explanation: Keywords: agile coaching, PM role in agile, motivation issues, servant leadership. In agile teams, the project manager\'s role shifts from directing and controlling to coaching and enabling — a PM who retains a traditional directive style will struggle to motivate agile staff who expect empowerment and self-direction. The capacity building gap was that PMs were not taught to become coaches, which is the leadership model agile teams require for intrinsic motivation. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option A (Perform collaborative work that is coordinated by the project manager.) fixes it."',
        'Explanation: Keywords: relative weighting, feature prioritization, collaborative assessment, project manager coordination. A relative-weighting approach to feature prioritization requires input from multiple perspectives — technical, business, and customer — to produce valid results. The project manager\'s coordination role ensures the collaborative process is structured, all relevant viewpoints are captured, and the weighting results reflect a genuine consensus rather than a single stakeholder\'s preferences. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Options D and E (Review the customer\'s priorities regarding the desired requirements for the milestones.; Discuss which requirements can be delivered faster with the project team.) work together."',
        'Explanation: Keywords: milestone advancement, customer priorities, fast delivery, requirements review. When a customer requests an earlier milestone, the project manager must first understand which requirements are truly essential for that milestone from the customer\'s perspective and then work with the team to identify what can realistically be accelerated. Reviewing priorities with the customer and discussing acceleration options with the team in parallel produces an achievable plan that serves the customer\'s business need without making unworkable promises. (PMBOK Guide) – Seventh Edition, 2021, p. 32, \'Focus on Value\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option B (Issue a change request to include the additional scope, and track the completion of the work items.) fixes it."',
        'Explanation: Keywords: scope validation, missing requirements, change request, customer acceptance. When missing operational requirements are discovered during scope validation and completing them would increase the likelihood of customer acceptance, the project manager must formally add the scope through the change control process rather than proceeding without it. A change request ensures the additional scope is approved, funded, and tracked to completion through the established governance process. (PMBOK Guide) – Seventh Edition, 2021, p. 50, \'Enable Change to Achieve the Envisioned Future State\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option C (Team charter) fixes it."',
        'Explanation: Keywords: team misunderstandings, team charter, expectations alignment, productivity impact. When different expectations among team members are causing misunderstandings and reducing productivity, the project manager should use the team charter to establish a common set of norms, values, and working agreements. A team charter creates explicit alignment on how the team will work together, resolving the ambiguity that allows conflicting expectations to persist. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option A (Engage the project team In implementing and Improving key aspects of the standup meetings.) fixes it."',
        'Explanation: Keywords: standup meeting resistance, hybrid approach, team engagement, meeting improvement. When a team new to hybrid delivery does not see value in standup meetings, imposing the format will not build genuine adoption — involving the team in designing and improving the meetings creates buy-in and ownership. Engaging the team in implementing and refining the standup format ensures the meetings address their actual coordination needs rather than being a ritual they resent. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    (
        'Explanation: Need: learn from data and lessons. Option D (Reinforce to all engineers the company vision of a safety-first approach to project activities.) fixes it."',
        'Explanation: Keywords: safety concerns, timeline pressure, company vision, engineer empowerment. When engineers are feeling pressure to compromise safety standards in order to meet timelines and do not feel empowered to push back, the project manager must reinforce the organization\'s safety-first vision as the non-negotiable foundation for all project work. Making the company vision explicit empowers engineers to decline unsafe activities with organizational backing rather than feeling they must choose between safety and schedule. (PMBOK Guide) – Seventh Edition, 2021, p. 25, \'Be a Diligent, Respectful, and Caring Steward\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option B (Set up a meeting to perform a root cause analysis.) fixes it."',
        'Explanation: Keywords: globally distributed team, low morale, root cause analysis, schedule recovery. When a distributed team is behind schedule due to low commitment and morale, addressing the symptom — the schedule delay — without understanding its cause will produce temporary fixes that fail to restore sustained performance. A root cause analysis meeting surfaces the specific drivers of low commitment so that targeted, effective interventions can be designed. (PMBOK Guide) – Seventh Edition, 2021, p. 44, \'Navigate Complexity\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option A (Identify the problem\'s root causes and define the ground rules with all project team members to minimize interferences.) fixes it."',
        'Explanation: Keywords: team interruptions, retrospective finding, ground rules, interference minimization. When a retrospective reveals that cross-team interruptions are consistently preventing task completion, the project manager must address both the root causes and the behavioral norms that allow them to continue. Identifying root causes explains why the interruptions are happening, while defining ground rules with all team members establishes the shared agreements that protect the team\'s capacity going forward. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option C (Talk with the team member and explain that once the meeting ended, the agreement must be respected.) fixes it."',
        'Explanation: Keywords: meeting agreement, commitment, team member complaint, agreement enforcement. When a team member who participated in and contributed to a meeting decision later contests the agreement, the project manager must reinforce that meeting commitments are binding once the session concludes. Directly explaining this principle preserves the integrity of the team\'s decision-making process and prevents individual reconsideration from undermining collective agreements. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option B (Reassess the team situation and provide a proper solution.) fixes it."',
        'Explanation: Keywords: recurring team conflict, team-building insufficient, situation reassessment, proper solution. When a team-building intervention fails to produce lasting results and new conflicts continue to cause project delays, the underlying situation has changed or the root cause was never fully addressed. Reassessing the team situation with fresh eyes identifies what is actually driving the conflict now and enables a targeted solution rather than repeating a generic intervention that already proved insufficient. (PMBOK Guide) – Seventh Edition, 2021, p. 44, \'Navigate Complexity\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option A (Analyze the problem with both teams to figure out If pan of the work must be redone.) fixes it."',
        'Explanation: Keywords: standstill, unclear requirements, joint problem analysis, rework assessment. When a Scrum team and the business unit have been at an impasse for days due to unclear product requirements, the project leader must bring both teams together to jointly analyze the problem and determine what, if anything, needs to be revisited or redone. A collaborative analysis session enables both teams to surface their respective misunderstandings and agree on a path forward based on shared facts rather than continuing in stalemate. (PMBOK Guide) – Seventh Edition, 2021, p. 44, \'Navigate Complexity\'"'
    ),
    (
        'Explanation: Need: secure people or vendors. Option D (Lack of a proper legal framework in place) fixes it."',
        'Explanation: Keywords: elected officials, legal framework, contract awarded, political stakeholders. When elected officials block a project that has already been contracted and has community support, the underlying cause is typically the absence of a legal or regulatory framework that would authorize the project to proceed. Securing the proper legal framework through the appropriate governmental approval process is the prerequisite the project cannot bypass regardless of contract status or community backing. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option C (Plan to conduct informal sessions with the stakeholders.) fixes it."',
        'Explanation: Keywords: technical project, stakeholder awareness, informal sessions, objections management. When stakeholders are unfamiliar with complex new technology and formal project meetings are derailed by objections and off-topic questions, the project manager needs a different engagement approach that builds understanding in a lower-pressure environment. Informal sessions allow stakeholders to ask questions, build foundational knowledge, and develop comfort with the technology without the accountability pressure of formal meetings, reducing the disruption in the official project forums. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    (
        'Explanation: Need: keep plans flexible. Option B (Submit a change request through the Integrated change control process.) fixes it."',
        'Explanation: Keywords: new regulation, schedule impact, budget impact, integrated change control. When a new municipal regulation materially affects both the schedule and budget of an ongoing project, it constitutes a scope change that must be processed through integrated change control. Submitting a change request ensures the impact is formally evaluated, approved at the appropriate authority level, and reflected in the updated project baselines. (PMBOK Guide) – Seventh Edition, 2021, p. 34, \'Recognize, Evaluate, and Respond to System Interactions\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option D (Address the issue with the stakeholder and explain the situation.) fixes it."',
        'Explanation: Keywords: stakeholder interruption, standup meetings, direct communication, boundary setting. When a stakeholder is disrupting daily standup meetings with requests and unplanned changes, the project manager must address the behavior directly with the stakeholder rather than escalating or ignoring it. Explaining to the stakeholder how their interruptions are affecting the team and the purpose of the standup creates the opportunity to agree on more appropriate channels for their requests. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    (
        'Explanation: Need: protect value and acceptance. Option B (Projects that maximize the business value) fixes it."',
        'Explanation: Keywords: project selection, business value maximization, portfolio criteria, project prioritization. The primary purpose of project portfolio management is to ensure organizational resources are invested in work that generates the greatest return — projects that maximize business value are the most aligned with this fundamental goal. Selection criteria centered on business value focuses the portfolio on strategic impact rather than on superficial metrics like minimum duration or minimum risk. (PMBOK Guide) – Seventh Edition, 2021, p. 32, \'Focus on Value\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option B (Suggest that the product owner attend a training session about assertive communication.) fixes it."',
        'Explanation: Keywords: product owner development, communication skills, assertive communication training, coaching. When a project manager identifies a skill gap in a team member who has potential, structured training is the most effective development intervention — especially for a specific skill like assertive communication that benefits from professional instruction and practice. Recommending formal training equips the product owner with the communication techniques they need while demonstrating the project manager\'s investment in their professional growth. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
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
