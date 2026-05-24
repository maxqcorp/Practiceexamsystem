MD_FILE = './src/imports/project-management-questions-1.md'

with open(MD_FILE, 'r', encoding='utf-8') as f:
    content = f.read()

replacements = [
    (
        'Explanation: Need: guide and calm the team. Option C (Train the marketing team and keep their director informed.) fixes it."',
        'Explanation: Keywords: hybrid adoption, marketing team training, resistant director, team preparation. When a director does not support a new delivery approach, the most practical strategy is to build capability within the team while keeping the director informed of progress — this allows the project to move forward without waiting for leadership buy-in that may develop gradually. Training the team creates the competency needed for successful hybrid delivery while the director\'s familiarity with the approach grows over time. (PMBOK Guide) – Seventh Edition, 2021, p. 40, \'Tailor Based on Context\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Options B and E (Retrospective; Backlog refinement) work together."',
        'Explanation: Keywords: knowledge gaps, no SME, retrospective, backlog refinement. Without a continuously available SME, knowledge gaps will surface during backlog refinement — when the team discovers they cannot estimate or understand work items — and during retrospectives — when the team reflects on what blocked their progress. These two events provide the visibility into knowledge-driven impediments that enables the project manager to take corrective action before the gaps cause delivery failures. (PMBOK Guide) – Seventh Edition, 2021, p. 40, \'Tailor Based on Context\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option A (Request expert advice from the compliance leader to confirm if there are any compliance requirements for the project.) fixes it."',
        'Explanation: Keywords: sensitive data, compliance requirements, compliance expert, verification. When a project will handle sensitive data for millions of users, compliance requirements cannot be dismissed based solely on the sponsor\'s informal recollection — the stakes of non-compliance are too high. Consulting the compliance leader provides authoritative expert confirmation that goes beyond the sponsor\'s general knowledge and ensures the project does not inadvertently violate regulatory obligations. (PMBOK Guide) – Seventh Edition, 2021, p. 25, \'Be a Diligent, Respectful, and Caring Steward\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option B (Plan to implement team-building strategies throughout the project.) fixes it."',
        'Explanation: Keywords: team motivation, lessons learned, team-building strategies, proactive planning. When lessons learned from a similar project identify team motivation as the primary challenge, the project manager must plan motivation-building interventions from the outset rather than waiting for morale problems to emerge. Embedding team-building strategies throughout the project plan treats motivation as a proactive investment rather than a reactive response to visible performance issues. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option C (Propose a session for essential agile knowledge transfer for the client team to align with the daily meeting goals) fixes it."',
        'Explanation: Keywords: client agile knowledge, knowledge transfer, daily meetings, client representation. When a client project manager has no agile experience but needs to participate meaningfully in daily meetings, a targeted knowledge transfer session on the essential concepts and daily meeting goals equips them to contribute effectively without requiring comprehensive agile training. This tailored approach ensures the client can engage productively in the specific ceremonies they will attend. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option C (Inform management of the new law as an opportunity to expand market share and share the proposed products) fixes it."',
        'Explanation: Keywords: regulatory opportunity, new products, management communication, market expansion. When a project manager has proactively monitored a regulatory change and identified new products that could benefit from it, the next action is to present this as a strategic business opportunity to management rather than simply noting the regulatory change. Informing management with proposed products demonstrates foresight and enables the organization to move quickly to capture market share ahead of competitors. (PMBOK Guide) – Seventh Edition, 2021, p. 50, \'Enable Change to Achieve the Envisioned Future State\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option A (Provide a software for instant messaging.) fixes it."',
        'Explanation: Keywords: virtual team, real-time collaboration, instant messaging, cultural diversity. Open real-time collaboration across a culturally and geographically diverse virtual team requires a tool that enables immediate, informal communication — instant messaging provides the real-time channel that allows team members to ask quick questions, share updates, and maintain the informal connection that email and scheduled meetings cannot provide. This promotes the open collaboration needed for effective distributed teamwork. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option D (Include the team member in the stakeholder register and update the communications management plan.) fixes it."',
        'Explanation: Keywords: remote team member, stakeholder register, communications management plan, engagement preferences. When a new team member with specific remote-working characteristics and communication preferences joins the project, the project manager must formally document them in the stakeholder register and update the communications management plan to account for their working style. This ensures face-to-face communication opportunities are created for the situations where this team member engages best. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    (
        'Explanation: Need: watch risks early. Option D (Determine if business value will be delivered without this feature. and try to fix the defects after the go-live milestone.) fixes it."',
        'Explanation: Keywords: feature defects, go-live milestone, business value assessment, post-go-live resolution. When a feature defect cannot be resolved before the go-live date, the project manager must determine whether sufficient business value can still be delivered without that feature to justify proceeding. If the go-live can deliver value without the defective feature, proceeding on schedule and fixing the defect post-launch is preferable to delaying the entire release. (PMBOK Guide) – Seventh Edition, 2021, p. 32, \'Focus on Value\'"'
    ),
    (
        'Explanation: Need: keep plans flexible. Option A (Issue log) fixes it."',
        'Explanation: Keywords: vendor delay, issue log, project risk, vendor management. When a vendor awarded a contract is revealed to be running behind schedule on a separate project, this represents an active threat to the project\'s timeline that must be immediately logged as a current issue. The issue log is the correct first update because the delay is a known, materializing problem — not merely a potential future risk — that requires active tracking and response. (PMBOK Guide) – Seventh Edition, 2021, p. 46, \'Optimize Risk Responses\'"'
    ),
    (
        'Explanation: Need: protect value and acceptance. Option D (Reevaluated the new product owner',
        'Explanation: Keywords: new product owner, disengaged stakeholder, needs reevaluation, sprint approval delay. When a new product owner is disengaged and delays sprint approvals, the root cause is typically unaddressed engagement needs that differ from those of the previous product owner. Reevaluating the new product owner\'s specific needs and motivations enables the project manager to develop a tailored engagement approach that secures the active participation necessary for timely sprint approvals. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option D (Modeling servant leadership) fixes it."',
        'Explanation: Keywords: servant leadership, no hierarchy, engaged team lead, leadership style. Operating without a chain of command or formal authority levels while remaining highly engaged and focused on the team\'s needs is the defining characteristic of servant leadership. A team lead who prioritizes enabling the team rather than asserting authority is demonstrating servant leadership in practice. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option A (Document the issue in the issue log and escalate to the project sponsor) fixes it."',
        'Explanation: Keywords: competitor announcement, first-to-market goal, issue log, sponsor escalation. When a competitor announces a product that directly undermines a key project goal — being first to market with a specific innovation — this is a significant project issue that must be formally documented and escalated to the sponsor for a strategic decision. The project manager cannot unilaterally decide whether to proceed, pivot, or cancel; the sponsor must be engaged with all relevant information to determine the appropriate response. (PMBOK Guide) – Seventh Edition, 2021, p. 34, \'Recognize, Evaluate, and Respond to System Interactions\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option D (Set clear meeting expectations by sharing agendas in advance) fixes it."',
        'Explanation: Keywords: meeting attendance, stakeholder participation, advance agenda, clear expectations. When key stakeholders consistently fail to attend project meetings, the problem is often that they do not see sufficient value in participating — sharing clear agendas in advance communicates the meeting\'s purpose and specific decisions required from each attendee. Setting explicit expectations with a structured agenda gives stakeholders the context they need to prioritize attendance and come prepared to contribute. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option C (Extract this from the project risk register tracking tool and issues log.) fixes it."',
        'Explanation: Keywords: risk trend analysis, risk register, issues log, historical risk data. The risk register tracking tool and issues log are the authoritative sources for historical risk data — they contain the documented record of all risks identified, monitored, and resolved over the project\'s lifecycle. Extracting this data provides the sponsor with an accurate, complete trend analysis that reflects the actual risk evolution of the project over the past 12 months. (PMBOK Guide) – Seventh Edition, 2021, p. 46, \'Optimize Risk Responses\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option D (Review the communications management plan and verify whether the stakeholder\'s needs are captured in the project management plan.) fixes it."',
        'Explanation: Keywords: stakeholder unaware, communications management plan, project management plan, needs verification. When a stakeholder is uninformed about project deliverables during a status review, the project manager must first check whether that stakeholder\'s communication needs are even captured in the plan before taking corrective action. Reviewing the communications management plan verifies whether the gap is a plan deficiency or an execution failure, which determines the appropriate remedy. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option A (Analyze the bounds of the negotiation for agreement with both parties.) fixes it."',
        'Explanation: Keywords: cost reduction request, negotiation bounds, both parties, consensus. When a customer requests a reduced cost at project completion that affects the internal sales department\'s budget, the project manager must identify the acceptable range for both parties before attempting any negotiation. Analyzing the negotiation bounds establishes what each party needs and can concede, creating the foundation for a mutually acceptable resolution that achieves project closure without damaging the commercial relationship. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option B (Share the project schedule, milestones, and meeting agendas with the stakeholdersahead of time.) fixes it."',
        'Explanation: Keywords: stakeholder availability, advance notice, project schedule, meeting agendas. For a project that demands significant stakeholder time for business decisions, proactively sharing the schedule, milestones, and meeting agendas allows stakeholders to plan their availability around key decision points in advance. This reduces last-minute conflicts and ensures stakeholders arrive prepared, which is far more effective than scheduling meetings reactively when decisions are urgently needed. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option A (Implement daily standups where the team can share their impediments, risks, andissues.) fixes it."',
        'Explanation: Keywords: servant leadership, team feedback, daily standups, impediment sharing. A servant leader who is not receiving impediment and risk feedback from the team cannot effectively remove blockers — the team needs a structured, safe forum for sharing these items. Implementing daily standups creates the regular touchpoint where team members are specifically invited to surface impediments and issues, enabling the project manager to act on them promptly. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    (
        'Explanation: Need: protect benefits for users. Option C (Workstream leader and functional manager) fixes it."',
        'Explanation: Keywords: workstream deadline, functional manager, accountability, performance improvement. When a workstream repeatedly misses deadlines, addressing only the workstream leader may be insufficient — if the root cause involves resource constraints or competing priorities managed by the functional manager, their involvement is essential to prevent recurrence. Engaging both the workstream leader and the functional manager creates shared accountability and access to the organizational levers needed to resolve the underlying performance issue. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option C (Archive all the project documents following the organization\'s accepted practices sothe documents can be used in other future projects.) fixes it."',
        'Explanation: Keywords: project closure, document archiving, organizational practices, knowledge preservation. When pressure to close quickly tempts shortcuts in project closure, the project manager must ensure that document archiving is completed according to organizational standards — archived project documents are organizational assets that future project managers will depend on for lessons learned, templates, and historical data. Proper archiving preserves institutional knowledge that would otherwise be permanently lost. (PMBOK Guide) – Seventh Edition, 2021, p. 25, \'Be a Diligent, Respectful, and Caring Steward\'"'
    ),
    (
        'Explanation: Need: protect value and acceptance. Option A (Identify how the proposed changes will benefit the project in relation to the businesscase.) fixes it."',
        'Explanation: Keywords: poorly defined project, change requests, business case alignment, change evaluation. On a poorly defined project receiving multiple change requests from senior management, the project manager must evaluate each proposed change against the original business case to determine whether it actually serves the project\'s purpose. Identifying how changes connect to the business case prevents scope creep driven by organizational politics while ensuring legitimate value-adding changes receive appropriate priority. (PMBOK Guide) – Seventh Edition, 2021, p. 32, \'Focus on Value\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option C (Reschedule the meeting to ensure the majority of stakeholders are present for theproduct backlog discussions.) fixes it."',
        'Explanation: Keywords: backlog planning, stakeholder participation, meeting rescheduling, incomplete attendance. A product backlog meeting that proceeds with only one attendee out of the intended group will produce priorities that do not reflect the full range of end-user needs — this defeats the purpose of the collaborative session. Rescheduling ensures the backlog is built with the representative input needed to make valid prioritization decisions. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option B (Identify virtual communication methods and arrange for regular team meetingsaccordingly.) fixes it."',
        'Explanation: Keywords: time zone difference, virtual communication, regular team meetings, distributed team. A 12-hour time difference makes synchronous in-person collaboration impractical — the project manager must identify the virtual tools and meeting windows that can bridge the geographic gap and enable effective regular interaction. Arranging structured virtual meetings with appropriate tools creates the consistent connection needed for a distributed team to collaborate productively across such a significant time difference. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option A (Encourage the team members to make decisions.) fixes it."',
        'Explanation: Keywords: team autonomy, agile self-direction, decision-making, empowerment. In an agile team, members requesting more autonomy are demonstrating the self-organizing mindset that effective agile delivery requires — encouraging them to make decisions aligns with agile principles and builds the team\'s capacity for independent problem-solving. A project manager who supports rather than suppresses this initiative creates a more engaged, capable team. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option C (Assess the training requirements and ensure time for professional developmenttraining by senior members.) fixes it."',
        'Explanation: Keywords: inexperienced team members, training requirements, professional development, senior mentoring. When team members are new to their roles, the project plan must explicitly account for the time and resources needed to develop their capabilities rather than assuming they will learn on the job without impact on delivery. Assessing training requirements and planning mentoring by senior members builds team competency in a structured way while protecting delivery timelines. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option B (Prepare a weekly status report and share it with executive management every week.) fixes it."',
        'Explanation: Keywords: executive management updates, weekly status report, agile project, communication frequency. When executive management requires more frequent updates than the current sprint demo cadence provides, the project manager should fulfill this need with a weekly status report rather than changing the agile delivery process or redirecting executives to customer-facing ceremonies. A tailored report for executives addresses their governance needs without disrupting the team\'s agile workflow. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option A (Advise the customer to discuss changes with the product owner.) fixes it."',
        'Explanation: Keywords: direct customer requests, Scrum team, product owner authority, change channeling. When a customer bypasses the product owner and requests priority changes directly from the Scrum team, it creates confusion and undermines the team\'s sprint planning stability. Advising the customer to channel all change requests through the product owner restores the proper authority structure that protects the team\'s focus while ensuring customer needs are properly evaluated and prioritized. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    (
        'Explanation: Need: secure people or vendors. Option A (Work on resolving the differences with the key resource and building a good working relationship to ensure project success.) fixes it."',
        'Explanation: Keywords: prior conflict, key resource, relationship building, project success. When a project manager must work with a key resource they have previously had conflict with, the professional obligation is to set past differences aside and focus on building a productive working relationship for the project\'s benefit. Proactively resolving the interpersonal dynamic ensures the essential resource can contribute fully without the previous tension undermining collaboration or project outcomes. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    (
        'Explanation: Need: learn from data and lessons. Option D (Review the lessons learned registers from the previous projects.) fixes it."',
        'Explanation: Keywords: lessons learned, failed similar projects, government software, risk prevention. When similar projects in the same organization have previously failed, the lessons learned registers from those projects contain the documented root causes and mitigation recommendations that can directly inform the current project\'s risk planning. Reviewing this organizational knowledge is the most targeted approach for understanding what went wrong and how to avoid repeating the same patterns. (PMBOK Guide) – Seventh Edition, 2021, p. 46, \'Optimize Risk Responses\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option B (Find the root cause of the issue and discuss the customer\'s current engagement.) fixes it."',
        'Explanation: Keywords: customer non-participation, clearance blockage, root cause analysis, engagement discussion. When a customer stops participating in scheduled calls and project approvals stall, the project manager must investigate why rather than simply increasing pressure for responses. Understanding the root cause of the customer\'s disengagement enables a targeted response that addresses the actual barrier to their participation and restores the collaborative relationship needed to clear the remaining packages. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option B (Set up review sessions with each of the team members to identify the root cause ofdelays.) fixes it."',
        'Explanation: Keywords: remote team, task delays, individual review sessions, root cause identification. When remote team members consistently miss task deadlines despite reminders, the project manager must investigate the individual-level reasons rather than repeating the same team-wide reminder. One-on-one review sessions allow the project manager to understand each team member\'s specific challenges — whether technical, capacity-related, or motivational — and address them with targeted support. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    (
        'Explanation: Need: watch risks early. Option A (Update the issue log.) fixes it."',
        'Explanation: Keywords: regulatory change, environmental regulations, issue log, project delay risk. When a government regulatory change materializes and could delay a project, this is an active issue that must be immediately logged in the issue log for tracking and response. Recording it as an issue — rather than a risk — reflects its current, known status and triggers the appropriate issue management response to assess and mitigate the impact. (PMBOK Guide) – Seventh Edition, 2021, p. 44, \'Navigate Complexity\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option C (Deliver the information to the stakeholders with the project management office\'s (PMO)assistance.) fixes it."',
        'Explanation: Keywords: bad news communication, delayed project, farmers impacted, PMO assistance. When delivering difficult news about a significant project delay to affected community stakeholders, the project manager should not communicate alone — partnering with the PMO provides institutional credibility, communication expertise, and shared accountability for the message. The PMO\'s involvement also signals organizational-level recognition of the impact and demonstrates a commitment to managing the situation responsibly. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option C (Meet with the team and agree on expectations from team members.) fixes it."',
        'Explanation: Keywords: interpersonal differences, colocated team, agreed expectations, work style conflict. When personal differences and varying work styles between technical and business unit members are affecting a colocated project negatively, the resolution lies in establishing agreed-upon behavioral expectations that all team members commit to. A team meeting to define shared norms creates explicit standards for how members will interact and resolve differences, reducing friction without requiring anyone to fundamentally change their personality. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option B (The project did not identify and engage the correct stakeholders.) fixes it."',
        'Explanation: Keywords: unauthorized project execution, political stakeholders, local government, stakeholder identification. When local municipal governments block a project\'s activities in their jurisdiction, it reveals that these authorities were not identified as stakeholders and engaged during planning — their authorization is a prerequisite for project execution in their territory. Failing to identify political and governmental stakeholders at project initiation leads to the exact type of implementation obstruction that is occurring. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option D (Meet with the project sponsors to align expectations) fixes it."',
        'Explanation: Keywords: multiple sponsors, first-time project, expectation alignment, sponsor meeting. With three first-time sponsors from different business units on a long-delayed project, the risk of misaligned expectations is high — each sponsor may have a different vision of success, priorities, and acceptable tradeoffs. Meeting with all sponsors together to align expectations establishes a shared understanding of project goals and decision-making protocols that prevents future conflicts between sponsors derailing the project. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option B (Ensured the project team applied a long-term solution for the issue) fixes it."',
        'Explanation: Keywords: issue recurrence, long-term solution, post-go-live, temporary fix. When an issue recurs after go-live despite having been "resolved" during the project, it indicates that only a temporary or symptomatic fix was applied rather than addressing the underlying root cause. Ensuring a long-term, root-cause solution was implemented during the project would have prevented the issue from recurring in the operational environment. (PMBOK Guide) – Seventh Edition, 2021, p. 42, \'Build Quality into Processes and Deliverables\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option D (Consider organizing paired work sessions for the junior and senior economists.) fixes it."',
        'Explanation: Keywords: intimidated team member, paired work, junior-senior collaboration, performance support. When a junior team member is falling behind because they are intimidated by working alongside a prominent expert, paired work sessions address both the performance gap and the psychological barrier simultaneously. Working directly alongside the senior expert in a structured pairing context normalizes the interaction, builds the junior member\'s confidence, and provides direct knowledge transfer that accelerates their progress. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option A (Reinforce the value of documenting and approving all change requests and ask thecustomer to issue these through the agreed channels.) fixes it."',
        'Explanation: Keywords: unauthorized changes, live environment, change control process, agreed channels. When a customer is requesting live environment changes directly from a team member without formal documentation, the project manager must reinforce the change control process with both the customer and the team. Explaining the value of proper documentation and directing the customer to use agreed channels protects the project from undocumented changes that create risk, confusion, and accountability gaps. (PMBOK Guide) – Seventh Edition, 2021, p. 50, \'Enable Change to Achieve the Envisioned Future State\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option B (Engage with the team member and draw up a development plan.) fixes it."',
        'Explanation: Keywords: declining performance, development plan, team member engagement, long-standing team. When a team member\'s performance declines after years with the team, the root cause is likely personal, motivational, or skill-related rather than simply behavioral — a development plan addresses the underlying issue constructively. Engaging directly with the team member and creating a structured development plan demonstrates investment in their recovery rather than immediately seeking replacement. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option D (Discuss communication needs with the key stakeholder.) fixes it."',
        'Explanation: Keywords: absent stakeholder, false information, communication needs, direct engagement. When a key stakeholder is absent from meetings and spreading inaccurate information about project delivery, both problems likely stem from insufficient or poorly suited communication — the stakeholder is not receiving the information they need in a way that works for them. Discussing their communication needs directly identifies how to keep them accurately informed and eliminates the information vacuum that is generating the misinformation. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    (
        'Explanation: Need: control changes and baselines. Option C (Meet with the operations manager to explain the background for the change andunderstand the operation manager\'s concerns about the change.) fixes it."',
        'Explanation: Keywords: post-approval concern, CCB decision, operations manager, change impact discussion. When an operations manager discovers a CCB-approved change that will disrupt their production line, the project manager must engage them directly to explain the decision rationale and fully understand their concerns before determining the path forward. This dialogue respects the CCB\'s authority while acknowledging that implementation impacts on operations may require additional coordination or mitigations not considered during the approval process. (PMBOK Guide) – Seventh Edition, 2021, p. 50, \'Enable Change to Achieve the Envisioned Future State\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option A (Provide mentoring for the key team members on agile practices and support the teamwith training and encouragement.) fixes it."',
        'Explanation: Keywords: digital transformation, knowledge gaps, agile mentoring, training support. In a digital transformation, knowledge gaps among key team members are the most direct risk to successful culture change — the project manager must invest in closing those gaps through targeted mentoring and training rather than replacing or directing people without developing their understanding. Providing agile mentoring and encouragement builds the genuine capability and mindset needed to sustain the transformation beyond the project. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option D (Review the terms and conditions of the contract.) fixes it."',
        'Explanation: Keywords: missing deliverable, maintenance manual, contract terms, contractual obligation. When a customer claims a deliverable — such as a maintenance manual — was not included with the final delivery, the project manager must first review the contract terms and conditions to determine whether it was a contractual requirement. The contract is the authoritative reference for what was agreed, preventing disputes from being resolved based on assumptions or verbal understanding. (PMBOK Guide) – Seventh Edition, 2021, p. 25, \'Be a Diligent, Respectful, and Caring Steward\'"'
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
