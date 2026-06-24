# Support Excellence Program – PowerPoint Outline

Generated executive-quality training deck with complete slide content, suggested visuals, and speaker notes.

## Slide 1: Support Excellence Program

**Main slide content**
- Audience: Front-Line Support Team / L1
- Presented By: Development Escalation Team / L2
- Duration: 2.5 – 3 Hours

**Suggested visual:** Professional technology/support visual with workflow steps.

**Speaker notes**

Welcome everyone. Today’s session is a practical enablement program for L1 Support. The goal is to help us resolve more issues independently and make the escalations that do reach Development much faster to investigate.

As we go through the deck, think about recent escalations that took too long, had missing information, or bounced between teams. We will use those real patterns to build a consistent troubleshooting and escalation standard.

Support and Development are on the same side: faster customer resolution. This workflow is not about blocking escalations; it is about making every escalation actionable.

## Slide 2: Training Purpose

**Main slide content**
- Improve support quality through effective troubleshooting, investigation, and escalation readiness.
- Key message: Better investigation leads to faster resolution, fewer delays, and higher customer satisfaction.

**Suggested visual:** Three outcome cards: investigation, resolution, satisfaction.

**Speaker notes**

This training is about the behaviors we use every day: how we classify tickets, gather evidence, use internal expertise, and decide when Development should be engaged.

Development can move quickly only when the issue is scoped, the evidence is complete, and the customer scenario is clear. A ticket that only says ‘not working’ creates delay, even when the underlying issue is important.

Treat each section as a checklist you can apply immediately after this session. The goal is not perfection; the goal is consistency and fewer avoidable escalations.

## Slide 3: Agenda

**Main slide content**
- Product Release Updates & New Features — 30–45 min
- Troubleshooting & Initial Investigation — 45 min
- Escalation Standards & Required Information — 30 min
- Knowledge Base Usage & Internal Collaboration — 20–30 min
- Q&A Session — 15 min

**Suggested visual:** Numbered agenda timeline with duration badges.

**Speaker notes**

Here is the agenda for today. Release awareness helps us identify expected behavior. Troubleshooting and investigation establish facts. Escalation standards make the handoff actionable. Knowledge Base usage and collaboration reduce repeat escalations.

The timing is flexible depending on discussion. If we have current high-volume issue types, we will use them as examples during the troubleshooting and escalation sections.

We have Q&A at the end, but please ask questions during the session when they clarify a process, checklist, or example.

## Slide 4: Module 1 – Product Release Updates and Feature Changes

**Main slide content**
- Release notes should be grouped by business area, not read item by item.
- Support should connect release changes to customer impact and first checks.

**Suggested visual:** Process flow from release note to escalation decision.

**Speaker notes**

Module 1 starts with product release updates because release awareness is the foundation for post-release support. Many tickets that look like defects are actually changed behavior, new validations, configuration gaps, or permission changes introduced by a release.

We do not need to memorize every line of every release note. The practical approach is to group changes by business area and understand which customer workflows may be affected.

Before we continue, think about which release changes usually generate the most tickets for us: reporting, exams, interfaces, filters, or permissions. Those examples will make this module more concrete.

## Slide 5: Release Updates by Business Area

**Main slide content**
- Exam Workflow: Deletion audit, soft delete, finalize controls
- Exam List & Filters: Filtering, locations, permissions, dual-screen behavior
- Reporting & Worksheets: Preview, Conclusion Editor, macros, worksheet fixes
- Integrations: HL7, routing, NPI, WADO, DICOM HTTP
- Infrastructure & Security: Documents, cache, hostname, hardening

**Suggested visual:** Five-column icon layout grouped by business area.

**Speaker notes**

I want us to use these five business areas as the mental model for reviewing a release. Each area maps to common customer symptoms: missing exams, reporting differences, interface failures, performance issues, or access and security changes.

When post-release tickets come in, categorize them using these areas. That helps us see whether a spike is isolated, customer-specific, or part of a broader release adoption issue.

When a customer reports a new issue after an upgrade, capture the business area and version immediately. Those two facts often determine the first troubleshooting path.

## Slide 6: Exam Workflow Updates

**Main slide content**
- Exam deletion audit tracking
- Soft delete enhancements
- Batch finalize current page
- Final exam status restriction
- Verify expected behavior before escalation.

**Suggested visual:** Bullet list with support-impact callout and customer-report table.

**Speaker notes**

For exam workflow changes, remember that behavior may look like a bug to the end user even when it is intentional. A missing exam may relate to soft delete or filters. A finalize problem may relate to the current-page batch operation or a status rule.

We should not assume that ‘it worked before’ automatically means ‘it is a bug now.’ The first question is whether the release intentionally changed what is allowed.

For this kind of issue, the evidence we need is what proves whether the exam is truly missing, filtered, deleted, or inaccessible because of permissions.

## Slide 7: Exam List & Filters

**Main slide content**
- Enhanced filtering, multi-location support, custom filter permissions, dual-screen next exam behavior.
- Before escalating missing exams: check filters, location access, and user permissions.

**Suggested visual:** Four-step green process flow.

**Speaker notes**

Missing exam reports are high-volume, and many of them are visibility issues rather than data loss. Start with filters, then location access, then user permissions because those checks are common and quick to validate.

For example, if one user cannot see an exam but another user can, that points away from a product defect and toward permissions, filters, or location scope.

Capture screenshots of the active filters and the user permission or location configuration. Those screenshots are usually more useful than a verbal description.

## Slide 8: Reporting & Worksheets

**Main slide content**
- Report Preview, Conclusion Editor, macro, worksheet, and Adult Echo fixes.
- Verify saved worksheet, generated report, macro application, and manual edits before escalation.

**Suggested visual:** Checklist cards for reporting verification.

**Speaker notes**

Reporting issues can involve several layers: data entry, worksheet state, report generation, macros, templates, and manual edits. Our job is to separate those layers before escalation.

If a user says a macro is wrong, confirm whether the worksheet value was saved, whether the report was regenerated, whether the macro applied to the correct section, and whether the user edited the generated text afterward.

For reporting escalations, attach the exam or report identifiers, screenshots before and after generation, and the exact expected text compared with the actual text.

## Slide 9: Integrations

**Main slide content**
- HL7 Ready / QA controls, location-based routing, NPI mapping, WADO, DICOM HTTP.
- Review configuration, endpoints, and job status before Development.

**Suggested visual:** Horizontal integration troubleshooting process flow.

**Speaker notes**

Integrations require disciplined investigation because a failure can happen outside the application: the customer system, network, endpoint, configuration, mapping, or queued jobs.

We need to distinguish ‘the message did not process’ from ‘the application has a bug.’ Confirm whether the message arrived, whether it matched routing rules, whether the endpoint was reachable, and whether jobs are stuck or failed.

The information most often missing from interface tickets includes message IDs, timestamps, endpoints, job status, and customer-side confirmation. Make sure those details are in the ticket.

## Slide 10: Infrastructure & Security

**Main slide content**
- Document handling, cache, multi-tenant hostname, and security hardening changes.
- Check services, configuration, cache status, and logs before escalation.

**Suggested visual:** Infrastructure checklist cards with icons.

**Speaker notes**

Infrastructure and security changes are not always reported as infrastructure issues. Users may describe login failures, document problems, stale screens, invalid redirects, or blocked operations.

Before escalating, validate services, configuration, cache, and logs. This is especially important after upgrades, hostname changes, security hardening, or multi-tenant configuration changes.

Always collect timestamps and the exact user path that led to the symptom. Security-related logs often need precise timing to locate the event.

## Slide 11: Module 1 Key Takeaways

**Main slide content**
- Not every behavior change is a bug.
- Post-release issues may be configuration, permissions, or workflow changes.
- Compare reported behavior against latest release functionality.
- Release understanding reduces unnecessary escalations.

**Suggested visual:** Large checkmark takeaway list.

**Speaker notes**

The key takeaway from Module 1 is that not every behavior change is a bug. After a release, we should first determine whether the behavior is expected, configuration-dependent, or permission-related.

Think back to the examples we covered: missing exams may be filters or permissions, reporting differences may be macro or worksheet flow, and integration failures may be endpoint or routing changes.

Release awareness is only one input. Next, we will move into the structured troubleshooting method that applies to every issue type.

## Slide 12: Module 2 – Troubleshooting & Initial Investigation

**Main slide content**
- Troubleshooting directly affects resolution speed.
- Structured investigation establishes facts before handoff.

**Suggested visual:** Five-step troubleshooting process.

**Speaker notes**

Troubleshooting is one of the highest-leverage support skills. A strong L1 investigation can resolve simple issues immediately and make complex issues easier for L2 or Development to act on.

Structured troubleshooting protects the customer experience. It prevents random checks, repeated questions, and unnecessary escalation delays.

When scope is not established early, we can assign the wrong priority, involve the wrong team, miss the right logs, and create repeated customer follow-up.

## Slide 13: Troubleshooting Mindset

**Main slide content**
- What? What exactly is failing?
- Who? One user or all users?
- When? After upgrade? Always? Intermittent?
- Where? Production? Test? Specific site?
- Scope? One exam? One patient? One modality? All exams?

**Suggested visual:** Visual checklist cards for What/Who/When/Where/Scope.

**Speaker notes**

This is the core investigation checklist. For a quality escalation, we need to answer what is failing, who is affected, when it started, where it happens, and what the scope is.

A statement like ‘Report not working’ becomes actionable only when we know which report, which user, when it started, which environment, and whether all reports or only one exam type are affected.

These answers belong in the ticket body, not hidden in chat threads. The ticket should tell the next engineer exactly what is known.

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

This matrix shows how the same investigation principle changes by issue type. Our first goal is always to distinguish isolated impact from broad impact.

For each row, think about the evidence that proves the answer. Login may need a user comparison. HL7 may need message IDs and queue status. Viewer issues may need workstation and browser details. Database symptoms may need operation type and timing.

Use this matrix as a triage script. It helps us ask fewer questions, but better questions, during the first customer interaction.

## Slide 15: Initial Checks Before Escalation

**Main slide content**
- Server Health
- Database Health
- Application Health
- Browser-Related Issues

**Suggested visual:** Four icon cards for pre-escalation health checks.

**Speaker notes**

Before escalation, we start with four standard health areas: server, database, application, and browser. These cover the most common non-code causes of customer-impacting symptoms.

The goal is not for L1 to become system administrators or DBAs. The goal is to confirm whether obvious indicators point to infrastructure, database, application jobs, or browser-side causes.

Record what was checked and the result. ‘Checked services: all running’ is much more useful than leaving the next team to repeat the same checks.

## Slide 16: Server Health Checks

**Main slide content**
- Check CPU usage, memory usage, disk space, and services running.
- Infrastructure health can mimic application defects.

**Suggested visual:** Server health checklist with process flow.

**Speaker notes**

Server health issues often appear as application errors: slow screens, failed report generation, timeouts, or unavailable pages. That is why we check basic server indicators before assuming a product defect.

A full disk can stop logging or job processing. High CPU can cause timeouts. Stopped services can break features even though the application code has not changed.

Capture screenshots or exact values when possible. ‘Disk C: has 1% free space’ is actionable. ‘Server looks bad’ is not.

## Slide 17: Database Health Checks

**Main slide content**
- SQL service running, database connectivity, blocking sessions, long-running queries.
- Symptoms include slowness, timeouts, and failed operations.

**Suggested visual:** DB symptom-to-check table.

**Speaker notes**

Database health is often invisible to end users. They only see slow or failed application behavior. That is why SQL service, connectivity, blocking, and long-running queries matter for saving, searching, reporting, and batch processing symptoms.

L1 may not always have permission to perform deep database checks. If that is the case, the ticket should state who checked, what was checked, and what remains unknown.

For database issues, timestamp accuracy matters. A vague ‘today’ is difficult to correlate with SQL logs or performance events.

## Slide 18: Application Health Checks

**Main slide content**
- Check application services, background jobs, queue processing, scheduled tasks.
- Examples: report generation, interface processing, scheduled cleanup.

**Suggested visual:** Application health table with examples.

**Speaker notes**

Application health checks focus on the moving parts inside the product: services, background jobs, queues, and scheduled tasks. These components often affect specific workflows rather than the entire application.

Report generation depends on background jobs. Interface delivery depends on processing queues. Cleanup or cache tasks can affect stale content or storage behavior.

Attach job names, queue counts, failed job details, and timestamps. Development can investigate much faster when the failing component is identified.

## Slide 19: Browser-Related Checks

**Main slide content**
- Browser version, cache cleared, incognito/private mode, different browser.
- Browser cache and client-side issues are common causes.

**Suggested visual:** Browser troubleshooting process flow.

**Speaker notes**

Browser checks are quick and often resolve or isolate issues. Cached scripts, stale sessions, extensions, and browser-specific behavior can all create symptoms that look like application defects.

If the issue continues after cache, private mode, and alternate browser tests, capture console errors and a network trace or HAR file when appropriate.

Never attach browser logs without context. Include the exact time, user action, and whether the trace contains sensitive customer information that needs to be handled according to policy.

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

These recurring root causes should become automatic checks before escalation. Browser cache, permissions, filters, configuration, stopped services, SQL availability, disk space, licenses, endpoints, and customer expectations all come up repeatedly.

Think about which of these we see most often. That tells us where we may need better training, better KB articles, or clearer support documentation.

When a recurring root cause is confirmed, update the ticket with the resolution and recommend a KB update if one does not already exist.

## Slide 21: Module 3 – Escalation Standards and Required Information

**Main slide content**
- Development needs complete information to investigate effectively.
- High-quality escalation reduces back-and-forth and speeds resolution.

**Suggested visual:** Escalation readiness process flow.

**Speaker notes**

Module 3 defines what a Development-ready escalation looks like. Development wants to help, but incomplete tickets slow everyone down.

A good escalation does not need to prove the root cause. It needs to define the problem, scope, evidence, and prior checks clearly enough for the next team to act.

The next slides cover the required ticket fields and examples of good versus bad escalation quality.

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

This is the Development escalation checklist. Every escalated ticket should contain these fields, or it should explicitly explain why a field does not apply.

The checklist prevents missing information from being discovered after handoff. The goal is to reduce repeated customer follow-up and internal rework.

This checklist is a strong candidate for a ticket template or required macro so Support does not have to rebuild the structure manually each time.

## Slide 23: Customer and Environment Information

**Main slide content**
- Customer name
- Environment: Production or Test
- Version
- Installation Type: PACS Only, All-In-One, Enterprise

**Suggested visual:** Required-detail table plus why-it-matters card.

**Speaker notes**

Customer and environment details may seem basic, but missing basics cause major delays. Development must know the customer, environment, version, and installation type before interpreting behavior.

Installation type matters because PACS Only, All-In-One, and Enterprise deployments can differ in routing, services, integrations, and operational ownership.

Do not rely on assumptions from the ticket title. Put the customer and environment details in the escalation body where they are immediately visible.

## Slide 24: Access and Upgrade Information

**Main slide content**
- Application URL, server access method, VPN required, RDP available.
- Last upgrade date, upgrade version, recent changes.

**Suggested visual:** Two side-by-side required-information tables.

**Speaker notes**

Access and upgrade information removes friction at the start of investigation. If Development cannot access the environment or does not know recent changes, the ticket may pause before technical analysis begins.

Upgrade timing is especially important. Issues that begin immediately after upgrade often relate to release behavior, migration, configuration, cache, or permissions.

If access is restricted, identify the owner and the process. Do not escalate without telling Development how access will be coordinated.

## Slide 25: Issue Classification

**Main slide content**
- Question: User is asking how functionality works.
- Configuration Request: Expected behavior but setup is needed.
- New Feature Request: Enhancement request.
- Bug/Error: System is not behaving as expected.

**Suggested visual:** Decision-tree visual with four classification cards.

**Speaker notes**

Issue classification is critical because each class has a different next action. Questions need answers or KB articles. Configuration requests need setup guidance. Feature requests need product review. Bugs need evidence and Development investigation.

Use the decision tree this way: if behavior is expected, it is not a bug. If setup is required, it is configuration. If the customer wants new behavior, it is an enhancement. If the system fails against expected behavior, it may be a bug.

Misclassification creates delays and frustration. A configuration request escalated as a bug may bounce back, and a true bug labeled as a question may not receive the right urgency.

## Slide 26: Scope Assessment

**Main slide content**
- Users: one/group/all
- Exams: one/multiple/all
- Exam Type: Echo/Vascular/Cath/Nuclear/All
- Location: one/multiple sites

**Suggested visual:** Scope assessment table.

**Speaker notes**

Scope determines almost everything about the next step: priority, owner, reproduction approach, and likely root cause. A single exam problem is investigated differently from an all-user production outage.

One user points to permissions or browser. One exam points to data or workflow. All exams point to service, configuration, or systemic defect. One site points to location routing or infrastructure.

If scope is unknown, say what has been tested and what still needs confirmation. Unknown scope is acceptable only when the ticket explains the gap and the plan to close it.

## Slide 27: Reproduction Steps

**Main slide content**
- Open exam → Click Reports → Generate report → Error occurs
- Include expected result, actual result, screenshot or recording.

**Suggested visual:** Four-step process flow and required evidence table.

**Speaker notes**

Reproduction steps are one of the most important parts of a Development escalation. They turn a vague symptom into an actionable scenario.

Write the steps as a sequence of user actions and system responses. Include the expected result, actual result, and evidence. If the issue is intermittent, describe the frequency and known triggers.

Use customer-safe screenshots or recordings when available. A short recording can eliminate ambiguity around the exact click path or message shown.

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

For the 10-minute guidance, collect a window before and after the issue so investigators can see setup, failure, and after-effects. Adjust the window for intermittent or long-running jobs when needed.

Always include the timezone and exact timestamp of reproduction. A log file without timing context can be difficult to use.

## Slide 29: Priority Classification

**Main slide content**
- P1 — System Down: Critical business impact. No workaround.
- P2 — Major Function Impact: Major functionality affected for multiple users or departments.
- P3 — Limited Functionality: Partial impact with workaround available.
- P4 — Question / Enhancement: How-to request, minor issue, or feature request.

**Suggested visual:** Color-coded priority classification table.

**Speaker notes**

Priority classification must be objective. Frustration is understandable, but priority is based on business impact, scope, and workaround availability.

A single user with a workaround is usually not P1. A production system unavailable to all users with no workaround is P1. A major function down for a department may be P2.

State the business impact in the ticket. ‘All echo reports blocked for production cardiology with no workaround’ supports priority much better than ‘customer is upset.’

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

The message is not ‘do not ask for help.’ The message is ‘use the right path first.’ Senior Support and Support Leads are part of that path.

If a customer insists on escalation for a known limitation or expected behavior, escalate internally through Support leadership or the Product process rather than labeling it as a Development bug.

## Slide 31: Bad vs Good Escalation Example

**Main slide content**
- Bad: “Report not working.” Missing customer, version, scope, steps, logs, screenshot, expected/actual.
- Good: ABC Hospital, version 5.22.3, all users affected, after upgrade, one exam type, steps/logs/screenshot attached, KB checked, Senior Support reviewed.

**Suggested visual:** Side-by-side comparison slide.

**Speaker notes**

This comparison makes escalation quality tangible. The bad example is common because it feels urgent, but it gives the next team almost nothing to act on.

The good example includes customer, version, impact, timing, scope, evidence, KB check, and senior review. With that information, Development can immediately decide how to reproduce or inspect logs.

For a reporting issue, we would add details such as report ID, exam ID, expected text, actual text, and exact timestamp.

## Slide 32: Module 4 – Knowledge Base and Internal Collaboration

**Main slide content**
- Many escalations can be avoided by checking existing knowledge and collaborating internally.
- Use KB, previous tickets, Senior Support, and Support Lead before Development.

**Suggested visual:** Collaboration process flow.

**Speaker notes**

Module 4 is the prevention layer. Strong support teams reuse knowledge and collaborate internally before escalating to engineering.

KB search and previous ticket review are not optional administrative steps. They identify known workarounds, configuration fixes, release behavior, and prior Development conclusions.

If no KB article exists for a recurring issue, flag that as an improvement opportunity. Reducing repeat escalations depends on capturing knowledge after resolution.

## Slide 33: Before Escalating to Development

**Main slide content**
- Step 1: Search Knowledge Base: Same error • Same workflow • Same customer
- Step 2: Search Previous Tickets: Has this happened before? Was there a workaround? Was it configuration?
- Step 3: Ask Senior Support: Consult Senior Support Engineer or Support Lead
- Step 4: Escalate Internally: Only then escalate to Development

**Suggested visual:** Four-step pre-escalation workflow.

**Speaker notes**

Before escalating to Development, follow this required sequence: search the KB, search previous tickets, consult Senior Support or the Support Lead, and then escalate if Development is still needed.

Search using exact error text, workflow names, customer name, version, and related modules. Previous tickets may show that the issue was configuration or had a known workaround.

The Development escalation should state the outcome of these checks. For example: ‘KB searched for exact error and workflow; no matching article found. Senior Support reviewed and confirmed escalation.’

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

This is the support-to-development workflow. The path is intentionally structured so each stage adds value instead of simply forwarding the ticket.

The Support Engineer owns initial investigation. KB search prevents repeat work. Senior Support and Support Lead validate completeness and priority. The Development Escalation Team routes and prepares the issue for engineering analysis. The Development Team investigates product-level issues.

Skipping steps may feel faster, but it often creates delays later because Development has to request the missing investigation.

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

By the end of this training, the expected behaviors are clear. We should classify issues correctly, complete standard troubleshooting, gather focused evidence, use the KB, consult internal experts, and escalate with quality.

This is also a continuous improvement loop. Each resolved ticket should improve future troubleshooting through KB updates, better templates, and stronger examples.

Use these slides as a desk reference after today. The checklists are designed to be reused in real tickets, not only remembered from the session.

## Slide 36: Questions and Discussion

**Main slide content**
- What issues are most commonly escalated today?
- What information is usually missing?
- What can we improve immediately?
- What KB articles should be created or updated?

**Suggested visual:** Discussion prompt cards with closing message.

**Speaker notes**

For Q&A, let’s turn the training into action. What issue types are most commonly escalated today? What information is usually missing? Where do delays happen? What questions does Development ask repeatedly?

As we discuss, capture improvement ideas. Strong candidates include ticket template updates, KB article creation, training refreshers, quick-reference checklists, and better release note summaries.

The goal is not to reduce escalations by ignoring issues. The goal is to reduce unnecessary escalations and improve the quality of necessary ones.
