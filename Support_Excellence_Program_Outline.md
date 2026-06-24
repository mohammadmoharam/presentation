# Support Excellence Program – PowerPoint Outline

Generated executive-quality training deck with complete slide content, suggested visuals, and speaker notes.

## Slide 1: Support Excellence Program

**Main slide content**
- Audience: Front-Line Support Team / L1
- Presented By: Development Escalation Team / L2
- Duration: 2.5 – 3 Hours

**Suggested visual:** Professional technology/support visual with workflow steps.

**Speaker notes**

Open the session by positioning this as a practical enablement program, not a theoretical lecture. The purpose is to help L1 Support resolve more issues independently and make the escalations that do reach Development faster to investigate.

Set expectations for participation. Ask attendees to think about recent escalations that took too long, had missing information, or bounced between teams. Explain that the deck will use those real patterns to build a consistent troubleshooting and escalation standard.

Emphasize that Support and Development are on the same side: faster customer resolution. The workflow is not about blocking escalations; it is about making sure every escalation is actionable.

## Slide 2: Training Purpose

**Main slide content**
- Improve support quality through effective troubleshooting, investigation, and escalation readiness.
- Key message: Better investigation leads to faster resolution, fewer delays, and higher customer satisfaction.

**Suggested visual:** Three outcome cards: investigation, resolution, satisfaction.

**Speaker notes**

Explain that this training is designed around day-to-day support behavior: how tickets are classified, how evidence is gathered, how internal expertise is used, and when Development should be engaged.

Use a real-world framing: Development can only move quickly when the issue is scoped, evidence is complete, and the customer scenario is clear. A ticket that says “not working” creates delay even when the underlying issue is important.

Invite the audience to treat each section as a checklist they can apply immediately after the session. The expected outcome is not perfection; it is consistency and fewer avoidable escalations.

## Slide 3: Agenda

**Main slide content**
- Product Release Updates & New Features — 30–45 min
- Troubleshooting & Initial Investigation — 45 min
- Escalation Standards & Required Information — 30 min
- Knowledge Base Usage & Internal Collaboration — 20–30 min
- Q&A Session — 15 min

**Suggested visual:** Numbered agenda timeline with duration badges.

**Speaker notes**

Walk through the agenda and connect each module to the escalation lifecycle. Release awareness helps identify expected behavior. Troubleshooting and investigation establish facts. Escalation standards make the handoff actionable. Knowledge Base and collaboration reduce repeat escalations.

Tell attendees that the timing is flexible depending on discussion. If there are current high-volume issue types, use them as examples during Module 2 and Module 3.

Reinforce that Q&A is intentionally included at the end, but questions during the session are welcome when they clarify a process or checklist.

## Slide 4: Module 1 – Product Release Updates and Feature Changes

**Main slide content**
- Release notes should be grouped by business area, not read item by item.
- Support should connect release changes to customer impact and first checks.

**Suggested visual:** Process flow from release note to escalation decision.

**Speaker notes**

Introduce Module 1 as the foundation for post-release support. Many tickets that look like defects are actually changed behavior, new validations, configuration gaps, or permission changes introduced by a release.

Emphasize that Support does not need to memorize every line of every release note. The practical approach is to group changes by business area and understand which customer workflows may be affected.

Discussion prompt: Ask the group which release changes usually generate the most tickets: reporting, exams, interfaces, filters, or permissions. Use responses to make the module concrete.

## Slide 5: Release Updates by Business Area

**Main slide content**
- Exam Workflow: Deletion audit, soft delete, finalize controls
- Exam List & Filters: Filtering, locations, permissions, dual-screen behavior
- Reporting & Worksheets: Preview, Conclusion Editor, macros, worksheet fixes
- Integrations: HL7, routing, NPI, WADO, DICOM HTTP
- Infrastructure & Security: Documents, cache, hostname, hardening

**Suggested visual:** Five-column icon layout grouped by business area.

**Speaker notes**

Explain the five business areas as the mental model for reviewing a release. Each area maps to common customer symptoms: missing exams, reporting differences, interface failures, performance issues, or access/security changes.

Encourage Support to tag or categorize post-release tickets using these areas. This helps identify whether a spike is isolated, customer-specific, or a broader release adoption issue.

Practical reminder: When a customer reports a new issue after upgrade, capture the business area and version immediately. Those two facts often determine the first troubleshooting path.

## Slide 6: Exam Workflow Updates

**Main slide content**
- Exam deletion audit tracking
- Soft delete enhancements
- Batch finalize current page
- Final exam status restriction
- Verify expected behavior before escalation.

**Suggested visual:** Bullet list with support-impact callout and customer-report table.

**Speaker notes**

Walk through the workflow changes as examples of behavior that may look like a bug to an end user. A missing exam may be related to soft delete or filters. A finalize problem may be related to the current-page batch operation or a status rule.

Emphasize that Support should not assume “worked before” means “bug now.” The correct first question is whether the release intentionally changed what is allowed.

Discussion prompt: Ask attendees what evidence would prove whether an exam is truly missing versus filtered, deleted, or inaccessible because of permissions.

## Slide 7: Exam List & Filters

**Main slide content**
- Enhanced filtering, multi-location support, custom filter permissions, dual-screen next exam behavior.
- Before escalating missing exams: check filters, location access, and user permissions.

**Suggested visual:** Four-step green process flow.

**Speaker notes**

Explain that missing exam reports are high-volume and often caused by visibility conditions rather than data loss. Filters, locations, and permissions should be checked in that order because they are common and quick to validate.

Use an example: one user cannot see an exam but another user can. That points away from Development and toward permissions, filters, or location scope.

Practical reminder: Capture screenshots of the active filters and the user permission/location configuration. These screenshots are often more useful than a verbal description.

## Slide 8: Reporting & Worksheets

**Main slide content**
- Report Preview, Conclusion Editor, macro, worksheet, and Adult Echo fixes.
- Verify saved worksheet, generated report, macro application, and manual edits before escalation.

**Suggested visual:** Checklist cards for reporting verification.

**Speaker notes**

Reporting issues can involve data entry, worksheet state, report generation, macros, templates, and manual edits. Support should separate these layers before escalation.

Use a scenario: the user says a macro is wrong. Support should confirm whether the worksheet value was saved, whether the report was regenerated, whether the macro applied to the correct section, and whether the user edited the generated text afterward.

Practical reminder: For reporting escalations, attach the exam/report identifiers, screenshots before and after generation, and the exact expected text versus actual text.

## Slide 9: Integrations

**Main slide content**
- HL7 Ready / QA controls, location-based routing, NPI mapping, WADO, DICOM HTTP.
- Review configuration, endpoints, and job status before Development.

**Suggested visual:** Horizontal integration troubleshooting process flow.

**Speaker notes**

Integrations require a disciplined investigation because failure can occur outside the application: customer system, network, endpoint, configuration, mapping, or queued jobs.

Emphasize the difference between “message did not process” and “application has a bug.” Support should identify whether the message arrived, whether it matched routing rules, whether the endpoint was reachable, and whether jobs are stuck or failed.

Discussion prompt: Ask what information is often missing from interface tickets. Typical answers include message IDs, timestamps, endpoints, job status, and customer-side confirmation.

## Slide 10: Infrastructure & Security

**Main slide content**
- Document handling, cache, multi-tenant hostname, and security hardening changes.
- Check services, configuration, cache status, and logs before escalation.

**Suggested visual:** Infrastructure checklist cards with icons.

**Speaker notes**

Explain that infrastructure and security changes are not always visible to users as “infrastructure” issues. They may appear as login failures, document problems, stale screens, invalid redirects, or blocked operations.

Support should validate services, configuration, cache, and logs before escalating. This is especially important after upgrades, hostname changes, security hardening, or multi-tenant configuration changes.

Practical reminder: Always collect timestamps and the exact user path that led to an infrastructure or security symptom. Security-related logs often need precise timing to locate the event.

## Slide 11: Module 1 Key Takeaways

**Main slide content**
- Not every behavior change is a bug.
- Post-release issues may be configuration, permissions, or workflow changes.
- Compare reported behavior against latest release functionality.
- Release understanding reduces unnecessary escalations.

**Suggested visual:** Large checkmark takeaway list.

**Speaker notes**

Summarize Module 1 by reinforcing the core mindset: after a release, Support should investigate whether behavior is expected, configuration-dependent, or permission-related before treating it as a defect.

Use examples from earlier slides: missing exams may be filters or permissions; reporting differences may be macro or worksheet flow; integration failures may be endpoint or routing changes.

Transition to Module 2 by explaining that release awareness is only one input. The next module covers the structured troubleshooting method that applies to all issue types.

## Slide 12: Module 2 – Troubleshooting & Initial Investigation

**Main slide content**
- Troubleshooting directly affects resolution speed.
- Structured investigation establishes facts before handoff.

**Suggested visual:** Five-step troubleshooting process.

**Speaker notes**

Introduce troubleshooting as the highest-leverage support skill. A strong L1 investigation can resolve simple issues immediately and make complex issues easier for L2 or Development to act on.

Emphasize that structured troubleshooting protects the customer experience. It avoids random checks, repeated questions, and unnecessary escalation delays.

Discussion prompt: Ask attendees what happens when scope is not established early. Guide them toward common consequences: wrong priority, wrong team, missing logs, and repeated customer follow-up.

## Slide 13: Troubleshooting Mindset

**Main slide content**
- What? What exactly is failing?
- Who? One user or all users?
- When? After upgrade? Always? Intermittent?
- Where? Production? Test? Specific site?
- Scope? One exam? One patient? One modality? All exams?

**Suggested visual:** Visual checklist cards for What/Who/When/Where/Scope.

**Speaker notes**

This slide is the core investigation checklist. Walk through each question and explain that none are optional for a quality escalation.

Use a simple example: “Report not working” becomes actionable only when Support knows which report, which user, when it started, which environment, and whether all reports or only one exam type are affected.

Practical reminder: These questions should be answered in the ticket body, not hidden in chat threads. The ticket should tell the next engineer exactly what is known.

## Slide 14: Troubleshooting Matrix

**Main slide content**
- Login — One user or all users?
- Reporting — One report or all reports?
- HL7 — One message or all messages?
- Viewer — One workstation or all workstations?
- Performance — One user or all users?
- Database — Specific operation or whole system?

**Suggested visual:** Two-column troubleshooting matrix table.

**Speaker notes**

Use the matrix to show how the same investigation principle changes by issue type. The first goal is always to distinguish isolated impact from broad impact.

For each row, ask what evidence would support the answer. Login may need user comparison. HL7 may need message IDs and queue status. Viewer may need workstation and browser details. Database may need operation type and timing.

Practical reminder: The matrix can be used as a triage script. It helps Support ask fewer but better questions during the first customer interaction.

## Slide 15: Initial Checks Before Escalation

**Main slide content**
- Server Health
- Database Health
- Application Health
- Browser-Related Issues

**Suggested visual:** Four icon cards for pre-escalation health checks.

**Speaker notes**

Introduce the four health areas as the standard first-pass checklist before escalation. They cover the most common non-code causes of customer-impacting symptoms.

Explain that the goal is not for L1 to become system administrators or DBAs. The goal is to confirm whether obvious health indicators point to infrastructure, database, application jobs, or browser/client-side causes.

Practical reminder: Record what was checked and the result. “Checked services: all running” is much more useful than leaving the next team to repeat the same checks.

## Slide 16: Server Health Checks

**Main slide content**
- Check CPU usage, memory usage, disk space, and services running.
- Infrastructure health can mimic application defects.

**Suggested visual:** Server health checklist with process flow.

**Speaker notes**

Explain that server health issues often appear as application errors: slow screens, failed report generation, timeouts, or unavailable pages. Support should check basic server indicators before assuming an application defect.

Give examples: disk full can stop logging or job processing; high CPU can cause timeouts; stopped services can break features even though the application code is unchanged.

Practical reminder: Capture screenshots or exact values when possible. “Disk C: has 1% free space” is actionable. “Server looks bad” is not.

## Slide 17: Database Health Checks

**Main slide content**
- SQL service running, database connectivity, blocking sessions, long-running queries.
- Symptoms include slowness, timeouts, and failed operations.

**Suggested visual:** DB symptom-to-check table.

**Speaker notes**

Explain that database health is often invisible to end users. They only see slow or failed application behavior. That is why Support should consider SQL service, connectivity, blocking, and long-running queries when symptoms involve saving, searching, reporting, or batch processing.

Clarify that L1 may not always have permission to perform deep database checks. If so, the ticket should state who checked, what was checked, and what remains unknown.

Practical reminder: Timestamp accuracy matters for database issues. A vague “today” is difficult to correlate with SQL logs or performance events.

## Slide 18: Application Health Checks

**Main slide content**
- Check application services, background jobs, queue processing, scheduled tasks.
- Examples: report generation, interface processing, scheduled cleanup.

**Suggested visual:** Application health table with examples.

**Speaker notes**

Application health checks focus on the moving parts inside the product: services, background jobs, queues, and scheduled tasks. These components often affect specific workflows rather than the whole application.

Use examples from the slide. Report generation depends on background jobs. Interface delivery depends on processing queues. Cleanup or cache tasks can affect stale content or storage behavior.

Practical reminder: Attach job names, queue counts, failed job details, and timestamps. Development can investigate much faster when the failing component is identified.

## Slide 19: Browser-Related Checks

**Main slide content**
- Browser version, cache cleared, incognito/private mode, different browser.
- Browser cache and client-side issues are common causes.

**Suggested visual:** Browser troubleshooting process flow.

**Speaker notes**

Browser checks are quick and often resolve or isolate issues. Cached scripts, stale sessions, extensions, and browser-specific behavior can all create symptoms that look like application defects.

Explain when to collect browser evidence. If the issue continues after cache/private/alternate browser tests, capture console errors and a network trace or HAR file when appropriate.

Practical reminder: Never attach browser logs without context. Include the exact time, user action, and whether the trace contains sensitive customer information that needs handling according to policy.

## Slide 20: Top Recurring Root Causes

**Main slide content**
- Browser cache
- User permissions
- Filters
- Incorrect configuration
- Service stopped
- SQL unavailable
- Disk full
- License expired
- Integration endpoint unavailable
- Wrong customer expectation

**Suggested visual:** Clean numbered two-column root cause list.

**Speaker notes**

Use this slide to reinforce pattern recognition. These recurring root causes should become automatic checks before escalation.

Ask the audience which root causes they see most often. This can identify training gaps, KB gaps, or product areas needing better support documentation.

Practical reminder: When a recurring root cause is confirmed, update the ticket with the resolution and recommend a KB update if one does not already exist.

## Slide 21: Module 3 – Escalation Standards and Required Information

**Main slide content**
- Development needs complete information to investigate effectively.
- High-quality escalation reduces back-and-forth and speeds resolution.

**Suggested visual:** Escalation readiness process flow.

**Speaker notes**

Introduce Module 3 as the standard for Development-ready escalations. The message should be firm but collaborative: Development wants to help, but incomplete tickets slow everyone down.

Explain that a good escalation does not need to prove the root cause. It needs to define the problem, scope, evidence, and prior checks clearly enough for the next team to act.

Transition by telling attendees that the next slides define the required ticket fields and examples of good versus bad escalation quality.

## Slide 22: Escalation Template Overview

**Main slide content**
- Customer information
- Environment information
- Access information
- Upgrade information
- Issue classification
- Scope assessment
- Reproduction steps
- Expected result
- Actual result
- Screenshots
- Required logs
- KB and senior support review status

**Suggested visual:** Checklist grid of required escalation fields.

**Speaker notes**

Position this slide as the Development escalation checklist. Every escalated ticket should contain these fields or explicitly explain why a field does not apply.

Explain that the checklist prevents missing information from being discovered after handoff. The goal is to reduce repeated customer follow-up and internal rework.

Practical reminder: Consider turning this checklist into a ticket template or required macro so Support does not have to rebuild the structure manually each time.

## Slide 23: Customer and Environment Information

**Main slide content**
- Customer name
- Environment: Production or Test
- Version
- Installation Type: PACS Only, All-In-One, Enterprise

**Suggested visual:** Required-detail table plus why-it-matters card.

**Speaker notes**

Customer and environment details seem basic, but missing basics cause major delays. Development must know which customer, environment, version, and installation type are involved before interpreting behavior.

Explain why installation type matters: PACS Only, All-In-One, and Enterprise deployments may differ in routing, services, integrations, and operational ownership.

Practical reminder: Do not rely on assumptions from the ticket title. Put the customer and environment details in the escalation body where they are immediately visible.

## Slide 24: Access and Upgrade Information

**Main slide content**
- Application URL, server access method, VPN required, RDP available.
- Last upgrade date, upgrade version, recent changes.

**Suggested visual:** Two side-by-side required-information tables.

**Speaker notes**

Access and upgrade information removes friction at the start of investigation. If Development cannot access the environment or does not know recent changes, the ticket may pause before technical analysis begins.

Highlight upgrade details because timing matters. Issues that begin immediately after upgrade often relate to release behavior, migration, configuration, cache, or permissions.

Practical reminder: If access is restricted, identify the owner and the process. Do not escalate without telling Development how access will be coordinated.

## Slide 25: Issue Classification

**Main slide content**
- Question: User is asking how functionality works.
- Configuration Request: Expected behavior but setup is needed.
- New Feature Request: Enhancement request.
- Bug/Error: System is not behaving as expected.

**Suggested visual:** Decision-tree visual with four classification cards.

**Speaker notes**

Issue classification is critical because each class has a different next action. Questions need answers or KB articles. Configuration requests need setup guidance. Feature requests need product review. Bugs need evidence and Development investigation.

Walk through the decision tree. If behavior is expected, it is not a bug. If setup is required, it is configuration. If the customer wants new behavior, it is an enhancement. If the system fails against expected behavior, it may be a bug.

Practical reminder: Misclassification creates delays and frustration. A configuration request escalated as a bug may bounce back; a true bug labeled as a question may not receive proper urgency.

## Slide 26: Scope Assessment

**Main slide content**
- Users: one/group/all
- Exams: one/multiple/all
- Exam Type: Echo/Vascular/Cath/Nuclear/All
- Location: one/multiple sites

**Suggested visual:** Scope assessment table.

**Speaker notes**

Scope determines almost everything about the next step: priority, owner, reproduction approach, and likely root cause. A single exam problem is investigated differently from an all-user production outage.

Give examples: one user points to permissions or browser; one exam points to data or workflow; all exams points to service, configuration, or systemic defect; one site points to location routing or infrastructure.

Practical reminder: If scope is unknown, say what has been tested and what still needs confirmation. Unknown scope is acceptable only when the ticket explains the gap and the plan to close it.

## Slide 27: Reproduction Steps

**Main slide content**
- Open exam → Click Reports → Generate report → Error occurs
- Include expected result, actual result, screenshot or recording.

**Suggested visual:** Four-step process flow and required evidence table.

**Speaker notes**

Reproduction steps are one of the most important parts of a Development escalation. They turn a vague symptom into an actionable scenario.

Explain that steps should be written as a sequence of user actions and system responses. Include expected result, actual result, and evidence. If the issue is intermittent, describe frequency and known triggers.

Practical reminder: Use customer-safe screenshots or recordings when available. A short recording can eliminate ambiguity around the exact click path or message shown.

## Slide 28: Required Logs

**Main slide content**
- Application logs: relevant timeframe only, e.g., 10 minutes before/after.
- Browser logs: console errors and HAR when applicable.
- Windows Event Logs for server issues.
- SQL errors for database symptoms.
- Avoid entire large log folders.

**Suggested visual:** Log requirements table with avoid callout.

**Speaker notes**

Logs should be relevant, focused, and tied to the issue timeframe. Large log dumps slow investigation and may create privacy or security concerns.

Explain the 10-minute guidance: collect a window before and after the issue so investigators can see setup, failure, and after-effects. Adjust the window for intermittent or long-running jobs when needed.

Practical reminder: Always include the timezone and exact timestamp of reproduction. A log file without timing context can be difficult to use.

## Slide 29: Priority Classification

**Main slide content**
- P1 — System Down: Critical business impact. No workaround.
- P2 — Major Function Impact: Major functionality affected for multiple users or departments.
- P3 — Limited Functionality: Partial impact with workaround available.
- P4 — Question / Enhancement: How-to request, minor issue, or feature request.

**Suggested visual:** Color-coded priority classification table.

**Speaker notes**

Priority classification must be objective. Frustration is understandable, but priority is based on business impact, scope, and workaround availability.

Discuss examples. A single user with a workaround is usually not P1. A production system unavailable to all users with no workaround is P1. A major function down for a department may be P2.

Practical reminder: State the business impact in the ticket. “All echo reports blocked for production cardiology with no workaround” supports priority much better than “customer is upset.”

## Slide 30: What Not to Escalate

**Main slide content**
- User training issues
- Configuration issues
- Missing permissions
- Known limitations
- Known release changes
- Issues already documented in the Knowledge Base
- Issues resolved by standard troubleshooting

**Suggested visual:** Warning list of non-Development escalation categories.

**Speaker notes**

This slide defines boundaries. Development should not be the default route for training, configuration, permissions, known limitations, documented KB issues, or items resolved by standard troubleshooting.

Be careful with tone: the message is not “do not ask for help.” The message is “use the right path first.” Senior Support and Support Leads are part of that path.

Practical reminder: If a customer insists on escalation for a known limitation or expected behavior, escalate internally through Support leadership or Product process rather than labeling it as a Development bug.

## Slide 31: Bad vs Good Escalation Example

**Main slide content**
- Bad: “Report not working.” Missing customer, version, scope, steps, logs, screenshot, expected/actual.
- Good: ABC Hospital, version 5.22.3, all users affected, after upgrade, one exam type, steps/logs/screenshot attached, KB checked, Senior Support reviewed.

**Suggested visual:** Side-by-side comparison slide.

**Speaker notes**

Use this comparison to make escalation quality tangible. The bad example is common because it feels urgent, but it gives the next team almost nothing to act on.

Walk through the good example line by line. It contains customer, version, impact, timing, scope, evidence, KB check, and senior review. Development can immediately decide how to reproduce or inspect logs.

Discussion prompt: Ask attendees what they would add to the good example for a reporting issue. Expected answers include report ID, exam ID, expected text, actual text, and exact timestamp.

## Slide 32: Module 4 – Knowledge Base and Internal Collaboration

**Main slide content**
- Many escalations can be avoided by checking existing knowledge and collaborating internally.
- Use KB, previous tickets, Senior Support, and Support Lead before Development.

**Suggested visual:** Collaboration process flow.

**Speaker notes**

Introduce Module 4 as the prevention layer. Good support organizations reuse knowledge and collaborate before escalating to engineering.

Explain that KB search and previous ticket review are not optional administrative steps. They identify known workarounds, configuration fixes, release behavior, and prior Development conclusions.

Practical reminder: If no KB article exists for a recurring issue, Support should flag that as an improvement opportunity. Reducing repeat escalations depends on capturing knowledge after resolution.

## Slide 33: Before Escalating to Development

**Main slide content**
- Step 1: Search Knowledge Base: Same error • Same workflow • Same customer
- Step 2: Search Previous Tickets: Has this happened before? Was there a workaround? Was it configuration?
- Step 3: Ask Senior Support: Consult Senior Support Engineer or Support Lead
- Step 4: Escalate Internally: Only then escalate to Development

**Suggested visual:** Four-step pre-escalation workflow.

**Speaker notes**

Walk through the pre-escalation sequence as a required workflow. First search the KB, then previous tickets, then consult senior internal resources, then escalate to Development if needed.

Explain how to search effectively: use exact error text, workflow names, customer name, version, and related modules. Previous tickets may reveal that the issue was configuration or had a known workaround.

Practical reminder: The Development escalation should state the outcome of these checks. For example: “KB searched for exact error and workflow; no matching article found. Senior Support reviewed and confirmed escalation.”

## Slide 34: Escalation Flow

**Main slide content**
- Support Engineer
- Knowledge Base Search
- Senior Support Review
- Support Lead Review
- Development Escalation Team
- Development Team
- Escalation should be a structured process, not a shortcut.

**Suggested visual:** Vertical support-to-development workflow diagram.

**Speaker notes**

Use this slide to describe the support-to-development workflow. The path is intentionally structured so that each stage adds value rather than simply forwarding the ticket.

Explain the role of each participant. The Support Engineer owns initial investigation. KB search prevents repeat work. Senior Support and Support Lead validate completeness and priority. Development Escalation Team routes and prepares for engineering analysis. Development Team investigates product-level issues.

Practical reminder: Skipping steps may feel faster, but it often creates delays later because Development has to request the missing investigation.

## Slide 35: Final Expected Outcomes

**Main slide content**
- Identify whether an issue is a bug, configuration, question, or enhancement.
- Perform standard troubleshooting.
- Gather the correct logs.
- Search existing Knowledge Base articles.
- Consult internal experts appropriately.
- Submit high-quality escalations to Development.
- Reduce unnecessary Development escalations.

**Suggested visual:** Checkmark outcome grid.

**Speaker notes**

Summarize the expected outcomes as observable behaviors. After this training, Support should classify issues correctly, complete standard checks, gather focused evidence, use the KB, consult internal experts, and escalate with quality.

Emphasize that this is a continuous improvement loop. Each resolved ticket should improve future troubleshooting through KB updates, better templates, and stronger examples.

Practical reminder: Encourage the team to use the slides as a desk reference. The checklists are designed to be reused in real tickets, not only remembered from the session.

## Slide 36: Questions and Discussion

**Main slide content**
- What issues are most commonly escalated today?
- What information is usually missing?
- What can we improve immediately?
- What KB articles should be created or updated?

**Suggested visual:** Discussion prompt cards with closing message.

**Speaker notes**

Use the Q&A to turn the training into action. Start with current escalation pain points: common issue types, missing information, delays, and repeated questions from Development.

Capture improvement ideas during discussion. Strong candidates include ticket template updates, KB article creation, training refreshers, quick-reference checklists, and better release note summaries.

Close by reinforcing partnership. The goal is not to reduce escalations by ignoring issues; the goal is to reduce unnecessary escalations and improve the quality of necessary ones.
