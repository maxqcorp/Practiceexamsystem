MD_FILE = './src/imports/project-management-questions-1.md'

with open(MD_FILE, 'r', encoding='utf-8') as f:
    content = f.read()

replacements = [
    (
        'Explanation: Need: guide and calm the team. Option D (A team whose members have more general aptitudes and can collaborate on different tasks) fixes it."',
        'Explanation: Keywords: agile team, general aptitudes, collaboration, cross-functional tasks. Effective agile teams thrive not because they have the most specialized experts, but because members with general aptitudes can flex across tasks, support each other, and adapt to evolving needs. This cross-functional collaboration is the foundation of the high-performing team environment that PMBOK 7th Edition emphasizes as central to project success. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    (
        'Explanation: Need: keep plans flexible. Option C (The project manager is obligated to comply with the project location’s regulatoryrequirements.) fixes it."',
        'Explanation: Keywords: health and safety requirements, regulatory compliance, project location, legal obligation. Health and safety regulations are non-negotiable legal requirements that the project manager is obligated to address regardless of project complexity or schedule pressure. As a steward of organizational and public interests, the project manager must identify and integrate all regulatory requirements of the project location into the project plan. (PMBOK Guide) – Seventh Edition, 2021, p. 25, \'Be a Diligent, Respectful, and Caring Steward\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option B (Put the new requirements in the backlog and submit a formal change request forapproval.) fixes it."',
        'Explanation: Keywords: new stakeholder, scope change request, product backlog, formal approval. When a new stakeholder requests scope changes, the project manager must capture those requirements in the backlog and route them through the integrated change control process for proper evaluation and authorization. Acting on stakeholder requests without formal approval creates uncontrolled scope changes that can undermine the project baseline and destabilize delivery commitments. (PMBOK Guide) – Seventh Edition, 2021, p. 34, \'Recognize, Evaluate, and Respond to System Interactions\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option B (Conduct a customer demonstration at the end of each build cycle.) fixes it."',
        'Explanation: Keywords: customer value demonstration, agile build cycle, product demo, conceptual product. When technical requirements are vague, the most effective way to demonstrate value is through live product demonstrations at the end of each build cycle. Working demos provide tangible, visible evidence of progress and allow the customer to provide feedback that ensures the evolving product aligns with their actual needs — directly fulfilling the focus-on-value principle. (PMBOK Guide) – Seventh Edition, 2021, p. 32, \'Focus on Value\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option D (Treat it as a change request and assess the effect on the project’s goals.) fixes it."',
        'Explanation: Keywords: missing feature claim, change request, international client, scope impact assessment. When a stakeholder claims a feature discussed at initiation was not implemented, the project manager must treat it as a change request and assess its full impact on project goals before taking any action. Implementing unvetted claims as immediate work items bypasses change control and risks disrupting the scope, schedule, and cost baselines. (PMBOK Guide) – Seventh Edition, 2021, p. 34, \'Recognize, Evaluate, and Respond to System Interactions\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option C (Refer to the communications management plan.) fixes it."',
        'Explanation: Keywords: hybrid project, stakeholder time zones, feedback collection, communications management plan. The communications management plan defines approved channels, methods, and timing for stakeholder interactions — including how to address geographic and time zone differences in feedback collection. When a hybrid project faces communication challenges with globally distributed stakeholders, this plan is the authoritative reference the project manager should consult first. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option A (Assessed the technical and organizational readiness for the project and identified risksat the beginning of the first iteration) fixes it."',
        'Explanation: Keywords: agile transition, technical capability gap, organizational readiness, risk identification. Before beginning sprint iterations, the project manager must assess both technical and organizational readiness and identify risks at the outset — not after costly rework has already occurred. Failing to evaluate capability gaps before the first iteration leaves hidden blockers undiscovered until they surface as expensive, schedule-threatening issues mid-project. (PMBOK Guide) – Seventh Edition, 2021, p. 46, \'Optimize Risk Responses\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option B (Talk with project B’s leader to discuss possible impacts to both projects.) fixes it."',
        'Explanation: Keywords: cross-project resource sharing, competing demands, impact on both projects, leader dialogue. When a team member is consistently being pulled into another project, the project manager must proactively engage with that project\'s leader to understand and address the potential impact on both initiatives. This leader-to-leader conversation demonstrates accountability, prevents silent resource conflicts from escalating, and enables a coordinated solution serving both projects\' needs. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option A (Emphasize the ground rules and then focus on today’s activities and impediments.) fixes it."',
        'Explanation: Keywords: standup meeting, open criticism, psychological safety, ground rules. During a standup meeting, publicly criticizing a team member disrupts psychological safety and derails the meeting from its intended purpose. The agile coach should immediately reinforce ground rules to restore a respectful environment, then redirect the team to focus on impediments and activities as the meeting structure requires. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option D (Raise a new issue in the issue log and convene subject matter experts (SMEs) and relevant stakeholders to identify alternatives to address the problem.) fixes it."',
        'Explanation: Keywords: subcontractor supply failure, issue log, SME consultation, stakeholder alternatives. When a subcontractor is unable to supply a key component, this is a realized problem — not a future risk — and should be formally logged as an issue and resolved by convening subject matter experts and relevant stakeholders to identify viable alternatives. This structured approach ensures transparency, leverages collective expertise, and maintains project momentum in the face of the supply disruption. (PMBOK Guide) – Seventh Edition, 2021, p. 34, \'Recognize, Evaluate, and Respond to System Interactions\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option A (Revisit the communication process control.) fixes it."',
        'Explanation: Keywords: different document versions, communication process failure, version control, stakeholder alignment. When stakeholders arrive at a meeting holding different draft versions of a key document, the underlying problem is a broken communication process — not just an isolated version control lapse. Revisiting the communication process control addresses the root cause systematically, ensuring proper document distribution and version management practices are in place for all future project communications. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option D (Work with the team to analyze which processes are suitable to use and define them in the ground rules.) fixes it."',
        'Explanation: Keywords: company merger, process conflict, ground rules, shared ownership. After a merger, process conflicts arise because different organizational cultures carry different expectations about how work should be done. Working collaboratively with the team to analyze applicable processes and formalize them in ground rules builds shared ownership of the new norms and ensures the combined team operates from a mutually agreed framework. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    (
        'Explanation: Need: keep plans flexible. Option A (Plan to execute the procurement tasks in a virtual environment.) fixes it."',
        'Explanation: Keywords: local vendors unavailable, virtual procurement, overseas alternatives, adaptive planning. When an unexpected event prevents local vendors from operating, the project manager must tailor the procurement approach by executing tasks in a virtual environment to engage qualified overseas companies. Adapting the procurement process to the changed context — rather than delaying or reducing scope — allows the project to continue delivering value despite the disruption. (PMBOK Guide) – Seventh Edition, 2021, p. 40, \'Tailor Based on Context\'"'
    ),
    (
        'Explanation: Need: keep plans flexible. Option A (Update the risk register.) fixes it."',
        'Explanation: Keywords: low availability testing facility, schedule dependency, risk identification, risk register. A known dependency on a testing facility with low availability represents an identified threat to the project schedule that has not yet materialized — making it a risk, not a current issue. Updating the risk register to formally capture, analyze, and plan a response for this potential impact is the appropriate first action before any schedule disruption occurs. (PMBOK Guide) – Seventh Edition, 2021, p. 46, \'Optimize Risk Responses\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option C (Agree on the criteria to prioritize risks.) fixes it."',
        'Explanation: Keywords: risk response planning, prioritization criteria, probability and impact, risk management. Before developing risk response strategies, the team must first agree on the criteria used to prioritize identified risks — such as probability, impact, and urgency thresholds. Without consensus on prioritization criteria, the team cannot consistently rank risks or allocate limited response resources to the threats and opportunities that matter most to project objectives. (PMBOK Guide) – Seventh Edition, 2021, p. 46, \'Optimize Risk Responses\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option C (Facilitate communication promoting a Scrum of Scrums so the different teams areaware of the dependencies and progress.) fixes it."',
        'Explanation: Keywords: digital transformation, hybrid project, inter-team dependencies, Scrum of Scrums. In a hybrid project with multiple interdependent teams working across different delivery streams, a Scrum of Scrums provides a structured mechanism for dependency management and cross-team progress visibility. This coordination practice enables teams to identify and resolve dependencies proactively rather than discovering integration conflicts late in the project lifecycle. (PMBOK Guide) – Seventh Edition, 2021, p. 34, \'Recognize, Evaluate, and Respond to System Interactions\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option C (Review the stakeholder engagement plan and inform the stakeholders.) fixes it."',
        'Explanation: Keywords: stakeholders bypassing project manager, direct team access, engagement plan, communication channels. When stakeholders consistently contact team members directly instead of going through the project manager, the project manager should review the stakeholder engagement plan and communicate the proper channels and protocols to all stakeholders. The engagement plan defines how stakeholders should interact with the project team, so reinforcing it restores proper information flow and protects the team from uncontrolled change requests. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option A (Review the established project benefits tracking metrics.) fixes it."',
        'Explanation: Keywords: success criteria concern, benefits tracking metrics, stakeholder concern, project performance. When a stakeholder raises concern that established success criteria are not being met, the project manager must first review the benefits tracking metrics to determine objectively whether the project is on track to deliver its intended value. Without an evidence-based review of the metrics, the project manager cannot assess the validity of the concern or determine what corrective action, if any, is required. (PMBOK Guide) – Seventh Edition, 2021, p. 32, \'Focus on Value\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option D (Facilitate a discussion of the vision for the project.) fixes it."',
        'Explanation: Keywords: team disengagement, project vision, repeated scope changes, leadership alignment. When a long-running team becomes disassociated from the project after multiple product owner changes and significant scope shifts, the most effective realignment comes from reconnecting the team to the project\'s underlying purpose and vision. Facilitating a structured discussion about what the project aims to achieve restores a shared sense of direction and rebuilds the commitment that scope changes had eroded. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option A (Motivate the team and deploy the necessary resources.) fixes it."',
        'Explanation: Keywords: scope expansion, team morale, new agreement, resource deployment. After a difficult negotiation results in an expanded scope commitment, the project manager\'s role is to translate that agreement into action by motivating the team and ensuring adequate resources are deployed to meet the new obligations. Effective leadership means championing the outcome rather than allowing team discontent or resource gaps to undermine the organization\'s negotiated position. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option B (Ensure a review is done with a representative group of users.) fixes it."',
        'Explanation: Keywords: experimental program, public users, benefits validation, representative review. For a program intended for public use, confirming that the desired benefits are actually achieved requires validation with a representative sample of the actual end users — not internal testing alone. A representative user review reveals whether the product delivers real-world value in practice, ensuring the project outcome aligns with its intended purpose for the target audience. (PMBOK Guide) – Seventh Edition, 2021, p. 32, \'Focus on Value\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option C (Mentor the team to explain agile principles and create a shared understanding.) fixes it."',
        'Explanation: Keywords: first agile project, team knowledge gap, agile principles, mentoring. When a team lacks a shared understanding of agile approaches at the start of their first agile project, the project manager must bridge the knowledge gap through mentoring — building common ground in principles and practices before execution begins. A team with a shared agile mindset can self-organize, collaborate effectively, and make sound decisions throughout the project lifecycle. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option D (Recommend to the sponsor to review the results of the team’s supplier evaluation.) fixes it."',
        'Explanation: Keywords: sponsor preferred supplier, unreliable vendor, objective evaluation results, stewardship. A project manager who knows a sponsor-preferred supplier has a track record of non-performance has a professional obligation to present objective evaluation data rather than simply accommodating the preference. Recommending that the sponsor review the team\'s supplier evaluation ensures procurement decisions are grounded in evidence and due diligence, protecting the project\'s quality and schedule integrity. (PMBOK Guide) – Seventh Edition, 2021, p. 25, \'Be a Diligent, Respectful, and Caring Steward\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option C (Mentoring and coaching) fixes it."',
        'Explanation: Keywords: PMO stakeholder training, AI program, difficult situations, mentoring and coaching. When stakeholders need support in navigating difficult situations on a complex program, mentoring and coaching provides the personalized, experiential guidance that builds lasting judgment and capability. As a PMO leader, developing stakeholder competence through direct coaching better serves the program\'s long-term success than one-time transactional training methods. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    (
        'Explanation: Need: control changes and baselines. Option A (Compare the achieved results to the contract requirements.) fixes it."',
        'Explanation: Keywords: project closure, supplier financial difficulty, contract requirements, formal acceptance. Before issuing formal project closure approvals or transferring liability, the project manager must first verify that the supplier\'s delivered results meet the terms agreed in the contract. Comparing achieved results against contractual requirements provides the objective evidence needed to justify final payment and formally close the procurement — protecting the organization\'s interests even when the supplier faces financial pressure. (PMBOK Guide) – Seventh Edition, 2021, p. 25, \'Be a Diligent, Respectful, and Caring Steward\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option A (Clarify expectations by explaining the company culture with the supervisor.) fixes it."',
        'Explanation: Keywords: new supervisor leadership style, company culture conflict, employee complaints, culture alignment. When a new supervisor\'s leadership style conflicts with the organization\'s recently improved culture, the project manager should address this directly by clarifying cultural expectations in a conversation with the supervisor. Proactive culture alignment protects the work environment and preserves the organizational progress achieved through the company\'s recent cultural transformation. (PMBOK Guide) – Seventh Edition, 2021, p. 25, \'Be a Diligent, Respectful, and Caring Steward\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option C (Update the issue log, identify the involved stakeholders, and assign resources to thecorrective actions.) fixes it."',
        'Explanation: Keywords: gate review, deliverable quality deficiency, issue log, corrective action assignment. When a quality deficiency is identified during a gate review, the project manager must formally log the issue, identify all affected stakeholders, and assign resources to execute the corrective actions. Systematic issue tracking with clear accountability ensures quality deficiencies are resolved with urgency and transparency rather than being deferred or informally managed. (PMBOK Guide) – Seventh Edition, 2021, p. 42, \'Build Quality into Processes and Deliverables\'"'
    ),
    (
        'Explanation: Need: keep plans flexible. Option A (Update the schedule to reflect the holidays and share the workload among offices tomitigate schedule slippage.) fixes it."',
        'Explanation: Keywords: international project, holiday scheduling conflicts, schedule update, workload redistribution. When project activities are inadvertently scheduled during local holiday periods in overseas offices, the project manager must update the schedule to reflect those constraints and redistribute the workload across offices to maintain progress. Proactively adapting the schedule to cultural and regional calendar differences prevents predictable delays and demonstrates respect for team members across locations. (PMBOK Guide) – Seventh Edition, 2021, p. 40, \'Tailor Based on Context\'"'
    ),
    (
        'Explanation: Need: protect value and acceptance. Option A (Determine the critical requirements.) fixes it."',
        'Explanation: Keywords: innovative solution, compliance gap, critical requirements, RFP analysis. When reviewing an RFP for a new offering and discovering gaps in both technical and compliance coverage, the project manager must first determine the critical requirements — the must-have conditions the project must satisfy to deliver its expected business value. Without clarity on what is truly critical, no gap can be properly addressed or prioritized for corrective action. (PMBOK Guide) – Seventh Edition, 2021, p. 32, \'Focus on Value\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option D (Suggest to the teams to limit the scope of work per iteration so they will start to delivermore reliably.) fixes it."',
        'Explanation: Keywords: hybrid project, consistently late demos, low morale, limit sprint scope. When self-organizing teams consistently miss sprint demo deadlines, the root cause is typically over-commitment within each iteration. Limiting the scope of work per sprint allows teams to establish a reliable delivery cadence, restore confidence, and begin demonstrating consistent value — directly addressing both team morale and the steering committee\'s concerns about predictability. (PMBOK Guide) – Seventh Edition, 2021, p. 40, \'Tailor Based on Context\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option B (Plan a communication method and allow the project team members to virtually interact.) fixes it."',
        'Explanation: Keywords: geographically dispersed team, virtual interaction, remote collaboration, communication method. When a project team spans multiple countries and members are unlikely to ever meet in person, the project manager must plan a structured virtual communication method that enables meaningful collaboration rather than just information exchange. Planned virtual interaction creates the working relationships and shared context needed to coordinate effectively and maintain team cohesion across distances. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option C (Meet with the SME to discuss the current challenges the team is facing.) fixes it."',
        'Explanation: Keywords: SME limited availability, team challenges, knowledge transfer, targeted consultation. With a senior SME available for only one week, the project manager should maximize impact by meeting directly with the SME to discuss the specific challenges the team is currently facing. A targeted conversation about real project problems ensures the SME\'s expertise is applied precisely where it will have the most impact, rather than being spent on general document reviews. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    (
        'Explanation: Need: watch risks early. Option D (Become aware of any cultural characteristics of the new supplier that could impactnegotiation.) fixes it."',
        'Explanation: Keywords: overseas supplier, cultural characteristics, negotiation preparation, procurement transition. When transitioning to an overseas supplier, cultural characteristics must be understood first because they directly shape how negotiations are conducted, what signals commitment, and what constitutes respectful engagement in that business context. Entering a procurement negotiation without cultural awareness creates misunderstandings that can derail the relationship before the project even benefits from the new supplier. (PMBOK Guide) – Seventh Edition, 2021, p. 44, \'Navigate Complexity\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option D (Update and share the guideline document dealing with team communication.) fixes it."',
        'Explanation: Keywords: virtual team, acquired company integration, new team members, communication guidelines. When new members from a recently acquired company join a virtual team, updating and sharing the communication guideline document ensures all members — existing and new — operate from a common framework that prevents misunderstandings. A refreshed and distributed guideline proactively addresses the cultural and process differences that organizational integration typically introduces into an established team. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option B (Review the open issues with the issue reporter and issue a change request to hire anexternal domain expert.) fixes it."',
        'Explanation: Keywords: high-priority open issues, external domain expertise, change request, issue resolution. When outstanding issues require specialized expertise that is not available within the project team, the project manager must review those issues with their reporters and submit a change request to bring in qualified external domain experts. Closing issues due to a lack of internal knowledge — without seeking the necessary expertise — fails stakeholders and leaves system problems unresolved in the delivered product. (PMBOK Guide) – Seventh Edition, 2021, p. 34, \'Recognize, Evaluate, and Respond to System Interactions\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option A (Work with the team and others in the network to assess and prioritize the obstacles.) fixes it."',
        'Explanation: Keywords: multiple project obstacles, vendor performance, technical issues, prioritization. When multiple obstacles emerge simultaneously — spanning vendor performance, technical concerns, and inter-divisional conflict — the project manager must first work with the team to assess and prioritize them before acting on any individual issue. Prioritization ensures limited project resources are directed at the highest-impact obstacles rather than responding reactively to whichever issue is most immediately visible. (PMBOK Guide) – Seventh Edition, 2021, p. 44, \'Navigate Complexity\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option B (Schedule a meeting to discuss recent observations with the team member.) fixes it."',
        'Explanation: Keywords: team member disengagement, decreased participation, missed deliverables, direct conversation. When a previously engaged team member suddenly reduces their contributions and begins missing deliverables, the project manager should schedule a private meeting to discuss the recent observations and understand what has changed. This respectful, direct conversation demonstrates genuine concern and may reveal personal, workload, or professional challenges the project manager can help address before the situation escalates further. (PMBOK Guide) – Seventh Edition, 2021, p. 36, \'Demonstrate Leadership Behaviors\'"'
    ),
    (
        'Explanation: Need: keep plans flexible. Option C (US$547,500) fixes it."',
        'Explanation: Keywords: expected monetary value, vendor bid evaluation, probability-weighted outcomes, risk quantification. The expected monetary value (EMV) of the vendor bid is calculated as: $500,000 + (0.65 × $100,000) – (0.35 × $50,000) = $500,000 + $65,000 – $17,500 = $547,500. This quantitative risk analysis technique integrates both the overrun and savings scenarios into a single risk-adjusted procurement cost estimate. (PMBOK Guide) – Seventh Edition, 2021, p. 46, \'Optimize Risk Responses\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option A (Approach the stakeholder to address the concerns.) fixes it."',
        'Explanation: Keywords: stakeholder withdrawal threat, transparency concern, accountability, direct engagement. When a key stakeholder threatens to withdraw support citing a lack of transparency and accountability, the project manager must approach that stakeholder directly to listen, understand their specific concerns, and address them with factual information. Direct engagement demonstrates respect and commitment to transparency, providing the best opportunity to rebuild trust before the stakeholder\'s opposition becomes irreversible. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    (
        'Explanation: Need: protect value and acceptance. Option A (Increase resources on the technical design to enable a decision to proceed as this is aquick return project.) fixes it."',
        'Explanation: Keywords: energy reduction project, 3-year payback, quick return on investment, technical design acceleration. With a confirmed 3-year payback period indicating strong return on investment, the project manager should accelerate the technical design phase by increasing resources to move confidently to an implementation decision as quickly as possible. Front-loading technical design investment shortens the path to implementation and the time to capture the financial benefits. (PMBOK Guide) – Seventh Edition, 2021, p. 32, \'Focus on Value\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option D (Meet with the sponsor to review the business case.) fixes it."',
        'Explanation: Keywords: business value opportunities, customer inquiry, business case review, sponsor alignment. Before responding to a customer\'s inquiry about value creation opportunities, the project manager must first meet with the sponsor to review the business case — the foundational document that defines expected benefits, value justification, and strategic alignment. Without this baseline understanding, any response about value opportunities would be speculative or misaligned with organizational goals. (PMBOK Guide) – Seventh Edition, 2021, p. 32, \'Focus on Value\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option B (Run a root cause analysis to identify the quality breach and update the qualitymanagement plan.) fixes it."',
        'Explanation: Keywords: product discrepancy, quality breach, root cause analysis, quality management plan update. When a product is found to have discrepancies with customer requirements during a quality review, the first step is to perform a root cause analysis to identify why the breach occurred before determining any corrective action. Without understanding the root cause, any fix applied risks treating symptoms rather than the underlying process failure, allowing the same issue to recur in future deliverables. (PMBOK Guide) – Seventh Edition, 2021, p. 42, \'Build Quality into Processes and Deliverables\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option D (Document the client’s responsibility for the integration with the security subsystem.) fixes it."',
        'Explanation: Keywords: external dependency, client team integration, security subsystem, documented responsibility. When a client insists their own team must perform a specific integration, the project manager must formally document this as the client\'s responsibility — not simply accept it verbally or resist it. Clear documentation protects the project team from being blamed for delays caused by the client\'s integration work and ensures all parties understand where accountability lies for that deliverable. (PMBOK Guide) – Seventh Edition, 2021, p. 34, \'Recognize, Evaluate, and Respond to System Interactions\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option A (Invite the product owner to attend daily standup meetings so they can assessprogress.) fixes it."',
        'Explanation: Keywords: product owner micromanagement, daily standup, constant disruptions, structured visibility. Inviting the product owner to attend daily standup meetings provides structured, time-boxed access to team progress — satisfying their need for information without allowing constant unscheduled disruptions throughout the day. This approach harnesses the standup\'s built-in transparency mechanism to engage the product owner appropriately while protecting the team\'s focus and flow. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    (
        'Explanation: Need: listen to people needs. Option D (Send out documentation to align stakeholder expectations and project objectives.) fixes it."',
        'Explanation: Keywords: compliance disagreement, stakeholder alignment, project objectives, written documentation. When stakeholders hold conflicting views about the priority of regulatory compliance, the project manager should send documentation that aligns stakeholder expectations with the project\'s established objectives and legal requirements. Written documentation creates a shared reference that establishes compliance as a project-level obligation — removing it from the realm of personal opinion and ensuring all stakeholders operate from the same understanding. (PMBOK Guide) – Seventh Edition, 2021, p. 30, \'Effectively Engage with Stakeholders\'"'
    ),
    (
        'Explanation: Need: guide and calm the team. Option D (Facilitate the discussion so that the team members can reach a consensus.) fixes it."',
        'Explanation: Keywords: sprint planning, backlog estimation disagreement, team consensus, agile facilitation. When team members disagree about the comparative size and feasibility of backlog items during sprint planning, the project manager should facilitate the discussion until the team reaches consensus — not make the decision on their behalf or remove items prematurely. Team consensus on estimates builds shared commitment to the sprint and reflects the collaborative decision-making essential to effective agile delivery. (PMBOK Guide) – Seventh Edition, 2021, p. 28, \'Create a Collaborative Team Environment\'"'
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
