import sys

MD_FILE = './src/imports/project-management-questions-1.md'

with open(MD_FILE, 'r', encoding='utf-8') as f:
    content = f.read()

replacements = [
    (
        'Explanation: Need: listen to people needs. Options A and B (Introduce a recognition program to motivate and reward resource performance; Enhance the competencies of the project team through training, mentoring and coaching.) work together."',
        'Explanation: Keywords: multi-year project, staff turnover risk, retention, competency development. Retaining permanent staff over a long project requires both motivation and growth. A recognition program gives team members reasons to stay, while training, mentoring, and coaching build the skills that keep them engaged and valuable — addressing turnover risk at its two core causes simultaneously. (PMBOK Guide) – Seventh Edition, 2021, p. 28, p. 29, \'Create a Collaborative Team Environment\'"'
    ),
    (
        'Explanation: Need: keep plans flexible. Option B (Evaluate the situation and identify ways to compress the schedule without impacting baselines) fixes it."',
        'Explanation: Keywords: first module delay, schedule slippage, compression options, baseline integrity. A 29% overrun on the first module signals a systemic estimation or execution issue. Before acting, the PM must evaluate what caused the delay and identify compression strategies — such as fast-tracking or crashing — that can recover time without breaching the approved baseline. (PMBOK Guide) – Seventh Edition, 2021, p. 44, \'Navigate Complexity\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Options A and C (Revisit the team\'s discussion on team behaviors and norms; Coach the new team member to improve engagement with the team.) work together."',
        'Explanation: Keywords: self-organizing team, new member, reluctant participation, team norms. A new member who stays silent in a self-organizing team may not understand what is expected of them. Revisiting team norms creates shared context for the new member, while direct coaching addresses their individual barriers to engagement — together building the inclusion the team needs to function well. (PMBOK Guide) – Seventh Edition, 2021, p. 28, p. 29, \'Create a Collaborative Team Environment\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option C (Deliver business value as soon as possible) fixes it."',
        'Explanation: Keywords: competitive market, prototype, incremental construction, early value delivery. When a project exists to increase competitive positioning, speed of value delivery is the top priority. Delivering business value as soon as possible through incremental releases ensures the company can capitalize on the product before the competitive window closes. (PMBOK Guide) – Seventh Edition, 2021, p. 32, \'Focus on Value\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option D (Ask an experienced team member to coach the new team member) fixes it."',
        'Explanation: Keywords: new team member, daily meetings, performance gap, peer coaching. When a new team member falls behind, peer coaching is more sustainable than direct PM intervention. An experienced team member who understands the work can provide targeted, real-time guidance while building a collaborative dynamic that strengthens the team as a whole. (PMBOK Guide) – Seventh Edition, 2021, p. 28, p. 29, \'Create a Collaborative Team Environment\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option B (Restate to the developers the importance of focusing and meeting the sprint goal.) fixes it."',
        'Explanation: Keywords: sprint goal, unplanned refactoring, developer initiative, sprint commitment. The sprint goal represents the value the team committed to deliver. Allowing unplanned refactoring work to displace it — however well-intentioned — breaks the sprint agreement and undermines predictability. Restating the sprint goal refocuses the team on their commitment without dismissing the quality concern, which can be addressed in the backlog. (PMBOK Guide) – Seventh Edition, 2021, p. 32, \'Focus on Value\'"'
    ),
    (
        'Explanation: Need: protect benefits for users. Option C (Send documentation to the senior manager about the advantages of the new framework) fixes it."',
        'Explanation: Keywords: iterative framework adoption, senior manager concern, organizational change, awareness building. A senior manager who is unfamiliar with a new framework needs information before they can support it. Sending documentation on its advantages directly addresses the knowledge gap and builds an informed foundation for acceptance, which is the first step in gaining buy-in for any organizational change. (PMBOK Guide) – Seventh Edition, 2021, p. 50, \'Enable Change to Achieve the Envisioned Future State\'"'
    ),
    (
        'Explanation: Need: keep plans flexible. Options B and D (Update the procurement management plan and negotiate with the contractor.; Update the procurement strategy and negotiate with the contractor) work together."',
        'Explanation: Keywords: schedule delay, missing materials, contractor offer, procurement negotiation. When a contractor submits costs the PM does not agree with, the PM must update the procurement documents to reflect the current situation and enter negotiation — not accept the offer as-is or escalate prematurely. Updating the plan and strategy together ensures that negotiations are conducted within a properly documented and aligned procurement framework. (PMBOK Guide) – Seventh Edition, 2021, p. 32, \'Focus on Value\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option A (Hold a stakeholder meeting to align timelines and scope expectations.) fixes it."',
        'Explanation: Keywords: schedule compression request, stakeholder meeting, scope-time trade-off, expectation alignment. A request to finish two months earlier is not simply a scheduling adjustment — it has direct implications for scope and cost. A stakeholder meeting surfaces those trade-offs so the people making the request can make an informed decision rather than the PM absorbing the impact unilaterally. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Options B and D (Encourage working in pairs and knowledge sharing; Facilitate a training event with an external trainer) work together."',
        'Explanation: Keywords: single point of knowledge, critical skill gap, upcoming activities, knowledge transfer. Relying on one person for a skill required by multiple upcoming activities is a critical vulnerability. Pair working transfers knowledge organically within the team while external training builds the skill more formally — together eliminating the single point of failure before it disrupts delivery. (PMBOK Guide) – Seventh Edition, 2021, p. 28, p. 29, \'Create a Collaborative Team Environment\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Options A, B, and C (Define team ground rules; Perform a retrospective session; Implement daily team meetings.) work together."',
        'Explanation: Keywords: critical deliverable, stakeholder complaints, team performance, rapid feedback. When stakeholders are already complaining about team performance on a critical deliverable, the PM needs to act on multiple fronts at once. Ground rules set shared expectations, the retrospective surfaces the root causes of performance gaps, and daily meetings create the ongoing visibility needed to detect and correct issues before they compound. (PMBOK Guide) – Seventh Edition, 2021, p. 28, p. 29, \'Create a Collaborative Team Environment\'"'
    ),
    (
        'Explanation: Need: keep plans flexible. Option D (Mitigate the risk by developing alternative plans to make the solution ready and available without full integration capabilities) fixes it."',
        'Explanation: Keywords: digital solution deployment, partner system risk, integration dependency, mitigation plan. When a key integration dependency carries unavailability risk, the project cannot simply wait and hope. Developing an alternative plan to launch the solution without full integration preserves the project\'s ability to deliver value even if the partner system fails, making this the most concrete and actionable risk mitigation available. (PMBOK Guide) – Seventh Edition, 2021, p. 46, \'Optimize Risk Responses\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option A (Conduct a meeting with the project team to discuss and address the sources of disagreement) fixes it."',
        'Explanation: Keywords: team morale, predecessor PM resignation, persistent disagreements, schedule delay. Low morale and persistent disagreements about how to complete tasks are team dysfunction issues that will continue to erode schedule performance until addressed. A direct team meeting surfaces the sources of conflict so the PM can facilitate resolution, which is the prerequisite to any meaningful schedule recovery. (PMBOK Guide) – Seventh Edition, 2021, p. 28, p. 29, \'Create a Collaborative Team Environment\'"'
    ),
    (
        'Explanation: Need: watch risks early. Option C (Expert judgment) fixes it."',
        'Explanation: Keywords: complex financial product, global investors, early risk identification, complex domain. For a high-complexity financial product with investor expectations, standard risk checklists are insufficient. Expert judgment draws on the deep domain knowledge needed to identify the risks that are specific to the product\'s technical and regulatory complexity, ensuring nothing critical is missed at the outset. (PMBOK Guide) – Seventh Edition, 2021, p. 46, \'Optimize Risk Responses\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option C (Start with a pilot project of appropriate complexity and provide agile training to those who are impacted) fixes it."',
        'Explanation: Keywords: agile adoption, buy-in, pilot project, hands-on training. Agile buy-in comes from experience, not from presentations. Starting with a pilot project of the right scope lets the team and stakeholders learn agile by doing it in a real but controlled context, building genuine confidence in the approach before it is scaled more broadly. (PMBOK Guide) – Seventh Edition, 2021, p. 48, \'Embrace Adaptability and Resiliency\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option D (Review and update the stakeholder engagement plan) fixes it."',
        'Explanation: Keywords: new client technical manager, information gap, stakeholder engagement, communication needs. A newly appointed client representative brings different information needs from their predecessor. Reviewing and updating the stakeholder engagement plan ensures the PM identifies what information this stakeholder requires and how often, closing the gap that led to their dissatisfaction. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option B (Define a user focus group as external stakeholders with a high influence on outcomes) fixes it."',
        'Explanation: Keywords: historical lessons, user experience degradation, product improvement, user focus group. Historical data showing that a similar project worsened user experience reveals that user needs were not adequately represented. Establishing a user focus group as high-influence external stakeholders gives real users a structured role in shaping the product, making it far less likely the same outcome is repeated. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option A (Prepare a detailed presentation for stakeholders on earned value including how it is calculated and the project\'s current earned value results) fixes it."',
        'Explanation: Keywords: SPI below 1, CPI above 1, status reporting, earned value transparency. When a project is behind schedule but under budget, a simple summary risks alarming or misleading stakeholders. A detailed earned value presentation gives stakeholders the full analytical picture — how the metrics are derived and what they actually mean — so they can form an accurate view of whether the project is genuinely under control. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option A (Share the customer feedback with the project team) fixes it."',
        'Explanation: Keywords: customer recognition, on-schedule performance, team meeting, positive feedback. The team delivered the performance that earned the customer\'s recognition, so they should hear it directly. Sharing the feedback in the team meeting connects the customer\'s acknowledgment to the people whose work created it, which is one of the most genuine forms of recognition a PM can provide. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option D (Submit a change request to increase the budget and buy new equipment) fixes it."',
        'Explanation: Keywords: retrospective finding, obsolete equipment, next iteration risk, budget change. Equipment identified in the retrospective as critical to the next iteration represents a scope and budget change. Submitting a change request ensures the additional expenditure receives proper approval and is reflected in the budget baseline rather than being absorbed informally. (PMBOK Guide) – Seventh Edition, 2021, p. 50, \'Enable Change to Achieve the Envisioned Future State\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Options D and E (Product backlog; Sprint goal) work together."',
        'Explanation: Keywords: sprint planning, post-first-sprint, product backlog, sprint goal. Productive sprint planning requires two inputs: the ordered list of available work (product backlog) and clarity on what the team is trying to achieve in the upcoming sprint (sprint goal). Without both, the team cannot make informed decisions about what to commit to next. (PMBOK Guide) – Seventh Edition, 2021, p. 40, \'Tailor Based on Context\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option D (Gather requirements from stakeholders) fixes it."',
        'Explanation: Keywords: CEO directive, AI implementation, new technology, stakeholder requirements. A CEO\'s enthusiasm for a technology is not a requirements document. Before any implementation plan can be formed, the PM must gather requirements from the stakeholders who will use and be affected by the AI solution, ensuring the technology is shaped around real organizational needs rather than conference impressions. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option C (Stakeholder register) fixes it."',
        'Explanation: Keywords: stakeholder role change, promotion, communication accuracy, stakeholder register. When a stakeholder is promoted, their authority, responsibilities, and communication needs all change. Updating the stakeholder register immediately ensures that all project communications going forward are directed to the right role and reflect the stakeholder\'s current position in the organization. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option D (Set up a meeting to discuss accommodations the team will have to make) fixes it."',
        'Explanation: Keywords: team member with limited mobility, team uncertainty, inclusivity, accommodation planning. When team members are uncertain about how a new member\'s mobility needs will change team dynamics, that uncertainty must be addressed openly. A meeting to discuss accommodations ensures practical needs are handled collaboratively and signals to everyone — including the new member — that the team operates as an inclusive environment. (PMBOK Guide) – Seventh Edition, 2021, p. 28, p. 29, \'Create a Collaborative Team Environment\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option C (Promote adoption of the communications management plan with the project team.) fixes it."',
        'Explanation: Keywords: stakeholder bypass, direct contact with technical staff, communications governance, resource management. When stakeholders bypass the PM to contact team members directly, it fragments information flow and undermines the PM\'s ability to manage scope and resources. Promoting the communications management plan re-establishes the agreed channels so the PM can maintain visibility and control over project communications. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    (
        'Explanation: Need: protect benefits for users. Option C (Make work visible using kanban boards.) fixes it."',
        'Explanation: Keywords: hybrid project, agile software component, workflow interruptions, information gaps. Repeated workflow interruptions caused by missing information are a flow problem — the team cannot see where work is blocked. Kanban boards make the workflow visible, exposing exactly where and why interruptions occur so the team can address information gaps before they become recurring impediments. (PMBOK Guide) – Seventh Edition, 2021, p. 44, \'Navigate Complexity\'"'
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
