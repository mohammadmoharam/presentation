#!/usr/bin/env python3
"""Generate the 3-slide executive deck AI-Executive-Overview.pptx.

Sources (read-only, never modified) live in ../AI Priors, ../AI Dashboard and
../Next Ideas. See README.md for the source-to-slide mapping.

Usage:
    pip install python-pptx pillow
    python3 generate_presentation.py
Optional rendering (PDF + PNG previews) requires LibreOffice:
    soffice --headless --convert-to pdf  AI-Executive-Overview.pptx
    soffice --headless --convert-to png  AI-Executive-Overview.pptx
"""

from pathlib import Path

from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.util import Emu, Inches, Pt

HERE = Path(__file__).resolve().parent
OUT = HERE / "AI-Executive-Overview.pptx"
SCREENSHOT = HERE / "assets" / "ai-history-summary-crop.png"

NAVY = RGBColor(0x0B, 0x25, 0x45)
NAVY_SOFT = RGBColor(0x1B, 0x3A, 0x5C)
TEAL = RGBColor(0x0E, 0x8C, 0x8B)
TEAL_LIGHT = RGBColor(0xE6, 0xF3, 0xF3)
GREY = RGBColor(0x55, 0x66, 0x77)
GREY_LIGHT = RGBColor(0xF2, 0xF5, 0xF8)
LINE = RGBColor(0xD6, 0xDE, 0xE6)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
AMBER = RGBColor(0xB5, 0x7A, 0x0E)
FONT = "Segoe UI"

SW, SH = Inches(13.333), Inches(7.5)
MARGIN = Inches(0.62)
CONTENT_W = SW - 2 * MARGIN


def textbox(slide, x, y, w, h, align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.TOP):
    box = slide.shapes.add_textbox(x, y, w, h)
    tf = box.text_frame
    tf.word_wrap = True
    tf.vertical_anchor = anchor
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
    tf.paragraphs[0].alignment = align
    return box, tf


def write(tf, runs, size=18, color=GREY, bold=False, space_after=6,
          line=1.15, first=False, align=None):
    """Append a paragraph made of (text, overrides) runs or a plain string."""
    para = tf.paragraphs[0] if first else tf.add_paragraph()
    para.line_spacing = line
    para.space_after = Pt(space_after)
    if align is not None:
        para.alignment = align
    if isinstance(runs, str):
        runs = [(runs, {})]
    for text, over in runs:
        run = para.add_run()
        run.text = text
        font = run.font
        font.name = FONT
        font.size = Pt(over.get("size", size))
        font.bold = over.get("bold", bold)
        font.color.rgb = over.get("color", color)
    return para


def rect(slide, x, y, w, h, fill=None, line_color=None, line_w=1.0,
         shape=MSO_SHAPE.ROUNDED_RECTANGLE, adj=0.04):
    sh = slide.shapes.add_shape(shape, x, y, w, h)
    if shape == MSO_SHAPE.ROUNDED_RECTANGLE:
        sh.adjustments[0] = adj
    if fill is None:
        sh.fill.background()
    else:
        sh.fill.solid()
        sh.fill.fore_color.rgb = fill
    if line_color is None:
        sh.line.fill.background()
    else:
        sh.line.color.rgb = line_color
        sh.line.width = Pt(line_w)
    sh.shadow.inherit = False
    sh.text_frame.word_wrap = True
    sh.text_frame.margin_left = sh.text_frame.margin_right = Inches(0.16)
    sh.text_frame.margin_top = sh.text_frame.margin_bottom = Inches(0.1)
    return sh


def chrome(slide, eyebrow, title, takeaway):
    """Shared slide frame: accent bar, eyebrow, title, takeaway headline."""
    bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(0.16), SH)
    bar.fill.solid()
    bar.fill.fore_color.rgb = NAVY
    bar.line.fill.background()
    bar.shadow.inherit = False

    _, tf = textbox(slide, MARGIN, Inches(0.42), CONTENT_W, Inches(0.3))
    write(tf, eyebrow, size=12, color=TEAL, bold=True, first=True, space_after=0)

    _, tf = textbox(slide, MARGIN, Inches(0.70), CONTENT_W, Inches(0.5))
    write(tf, title, size=27, color=NAVY, bold=True, first=True, space_after=0,
          line=1.0)

    _, tf = textbox(slide, MARGIN, Inches(1.30), CONTENT_W, Inches(0.55))
    write(tf, takeaway, size=19, color=NAVY_SOFT, first=True, space_after=0,
          line=1.15)



def value_strip(slide, items, top=Inches(6.06), height=Inches(1.06)):
    """Bottom Business Value | Impact | Effort strip."""
    gap = Inches(0.22)
    w = int((CONTENT_W - 2 * gap) / 3)
    for i, (label, body) in enumerate(items):
        x = MARGIN + i * (w + gap)
        card = rect(slide, x, top, Emu(w), height, fill=GREY_LIGHT,
                    line_color=LINE)
        tf = card.text_frame
        tf.vertical_anchor = MSO_ANCHOR.MIDDLE
        write(tf, label, size=11, color=TEAL, bold=True, first=True,
              space_after=3)
        write(tf, body, size=15, color=NAVY_SOFT, space_after=0, line=1.1)


def notes(slide, text):
    slide.notes_slide.notes_text_frame.text = text.strip()


def blank(prs):
    return prs.slides.add_slide(prs.slide_layouts[6])


# --------------------------------------------------------------------------
# Slide 1 - AI project accomplished
# --------------------------------------------------------------------------
def slide_one(prs):
    s = blank(prs)
    chrome(
        s,
        "DELIVERED  ·  PATIENT HISTORY SUMMARIZATION",
        "Years of Prior Reports, One Structured Patient View",
        "Live in the reporting workflow today; pilot and production "
        "adoption not yet evidenced.",
    )

    left_w = Inches(6.35)
    top = Inches(2.30)

    # Before -> After workflow
    flow = rect(s, MARGIN, top, left_w, Inches(1.20), fill=WHITE,
                line_color=LINE)
    tf = flow.text_frame
    write(tf, [("Before  ", {"color": GREY, "bold": True, "size": 14}),
               ("Search → read every prior report → summarise mentally",
                {"size": 16, "color": GREY})],
          first=True, space_after=8, line=1.05)
    write(tf, [("After  ", {"color": TEAL, "bold": True, "size": 14}),
               ("Open exam → summary ready → validate → report",
                {"size": 16, "color": NAVY_SOFT})],
          space_after=0, line=1.05)

    # Three business-value highlights
    hy = Inches(3.62)
    hh = Inches(0.62)
    for i, (head, body) in enumerate([
        ("Faster review", "Prefetched before the exam opens"),
        ("Better context", "Findings, progression and procedures together"),
        ("Consistent structure", "Structured to USCDI v4 / C-CDA"),
    ]):
        y = hy + i * (hh + Inches(0.18))
        dot = s.shapes.add_shape(MSO_SHAPE.OVAL, MARGIN, y + Inches(0.2),
                                 Inches(0.14), Inches(0.14))
        dot.fill.solid()
        dot.fill.fore_color.rgb = TEAL
        dot.line.fill.background()
        dot.shadow.inherit = False
        _, tf = textbox(s, MARGIN + Inches(0.34), y, left_w - Inches(0.34), hh)
        write(tf, head, size=18, color=NAVY, bold=True, first=True,
              space_after=2, line=1.0)
        write(tf, body, size=16, color=GREY, space_after=0, line=1.05)

    # Product visual
    img_x = MARGIN + left_w + Inches(0.45)
    img_w = SW - MARGIN - img_x
    if SCREENSHOT.exists():
        img_y = top + Inches(0.25)
        pic = s.shapes.add_picture(str(SCREENSHOT), img_x, img_y, width=img_w)
        frame = rect(s, img_x - Inches(0.07), img_y - Inches(0.07),
                     img_w + Inches(0.14), pic.height + Inches(0.14),
                     fill=None, line_color=LINE)
        frame.line.width = Pt(1.0)
        cap_y = img_y + pic.height + Inches(0.16)
        _, tf = textbox(s, img_x, cap_y, img_w, Inches(0.4))
        write(tf, "AI History Summary — demo data, identifiers removed.",
              size=12, color=GREY, first=True, space_after=0, line=1.1)

    value_strip(s, [
        ("BUSINESS VALUE", "Less re-reading; history harder to miss"),
        ("IMPACT / EVIDENCE", "Generated today; time saved not yet measured"),
        ("EFFORT & SCOPE", "Effort not documented · v5.21, v5.22"),
    ])

    notes(s, """
Opening: we have taken AI from idea to a working capability inside the product our
clinicians already use every day.

The problem: before finalising a report, a reading physician may need several years of
prior reports across modalities. The information exists, but rebuilding the clinical
story is slow, inconsistent between readers and easy to get wrong ("Patient History
Summarization .pptx", slides 2-3 and notes). That is cognitive load on our most
expensive clinical minute.

The value: the AI generates two views — AI History Summary and AI History Details —
reachable in one click from the Previous Exams tab, with critical and abnormal items
visually prioritised ("AI-Powered Patient History Summarization.docx", Key capabilities;
"AI Patient Summary - Customer Perspective 1.html"). Because the summary is prefetched
when the order arrives and refreshed when the report is verified, it is waiting before
the clinician asks for it (use-case PDF, page 1, "AI processing strategy"). We chose
USCDI v4 and C-CDA as the summary skeleton so one mission serves all exam types and
customers rather than per-customer variants (deck slides 5 and 11).

Example: the sample on screen consolidates a vascular patient's problem list with status,
first/last noted dates and progression notes — explicitly flagging what is "not documented
in any provided report" rather than inventing content.

Status and limits — important for credibility: development is complete and summaries are
generated automatically after exam finalisation, with baseline and incremental jobs run by
a dedicated parser ("AI Patient Summary - Support Runbook 1.html", sections 2 and 4). What
we do NOT have in our sources is pilot validation data, customer adoption, measured time
saved or accuracy benchmarking. Every benefit on this slide is an expected benefit.

Effort, dependencies, risk: delivery effort is not documented anywhere in the source set,
so I am not quoting a figure. Known effort concentrations were Matcha model selection
(quality vs. latency vs. token cost) and caching to control cost (deck slides 8-9).
Dependencies: Matcha AI availability, the MATCHA_API_KEY held server-side, and customer
versions 5.21 / 5.22. Privacy design anonymises the PDF before the AI call and re-injects
identifiers locally (runbook, section 4) — worth stating, but it is a design claim, not an
audited compliance statement.

Decision / next step: approve a measured pilot — agree the sites, the baseline and the two
or three metrics (review time, findings surfaced, clinician acceptance) so the next review
reports evidence instead of intent.

Transition: that is value delivered. Next, the value we are building for our own
operations teams.

Sources: MS-AI/AI Priors/AI-Powered Patient History Summarization.docx;
MS-AI/AI Priors/Patient History Summarization .pptx (slides 2-3, 5-9, 11-12 + notes);
MS-AI/AI Priors/Patient-History-Summarization-UseCase 1.pdf (pages 1-2);
MS-AI/AI Priors/AI Patient Summary Customer Perspective 1.html;
MS-AI/AI Priors/AI Patient Summary Support Runbook 1.html (sections 1-4).
""")


# --------------------------------------------------------------------------
# Slide 2 - AI project in progress
# --------------------------------------------------------------------------
def slide_two(prs):
    build_slide_two(blank(prs))


def build_slide_two(s):
    """Executive view of the AI Operations Intelligence Dashboard."""
    chrome(
        s,
        "AI OPERATIONS  ·  PACS / HL7 SERVICE INTELLIGENCE",
        "AI Operations Intelligence Dashboard",
        "From reactive monitoring to predictive PACS / HL7 operations",
    )

    # ---- Three value cards -------------------------------------------------
    cy = Inches(2.10)
    ch = Inches(3.04)
    gap = Inches(0.26)
    w = int((CONTENT_W - 2 * gap) / 3)
    cards = [
        ("COMPLETED FOUNDATION", "Built and running", TEAL, TEAL_LIGHT, [
            ("PACS / HL7 service monitoring", None),
            ("Queue and interface visibility", None),
            ("Operational status mapping", None),
            ("Automation", None),
            ("Automated issue classification", None),
        ]),
        ("AI INTELLIGENCE LAYER", "What AI adds", NAVY_SOFT, GREY_LIGHT, [
            ("Risk forecasting", None),
            ("Storage capacity prediction", None),
            ("Performance degradation prediction", None),
            ("Queue backlog forecasting", "In\u00a0Progress"),
            ("Prioritized remediation recommendations", "Next"),
        ]),
        ("BUSINESS IMPACT", "Why it matters", NAVY, GREY_LIGHT, [
            ("Earlier detection", None),
            ("Faster resolution", None),
            ("Reduced operational effort", None),
            ("Better customer experience", None),
            ("Improved system availability", None),
        ]),
    ]
    for i, (label, kicker, colour, tint, items) in enumerate(cards):
        x = MARGIN + i * (w + gap)
        card = rect(s, x, cy, Emu(w), ch, fill=WHITE, line_color=LINE)
        tab = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, x, cy, Emu(w), Pt(5))
        tab.fill.solid()
        tab.fill.fore_color.rgb = colour
        tab.line.fill.background()
        tab.shadow.inherit = False
        tf = card.text_frame
        tf.vertical_anchor = MSO_ANCHOR.TOP
        tf.margin_left = tf.margin_right = Inches(0.13)
        tf.margin_top = Inches(0.18)
        write(tf, label, size=13, color=colour, bold=True, first=True,
              space_after=1)
        write(tf, kicker, size=11, color=GREY, space_after=9, line=1.0)
        for text, badge in items:
            runs = [("▪  ", {"color": colour, "bold": True}),
                    (text, {})]
            if badge:
                runs.append(("   " + badge, {"color": AMBER, "bold": True,
                                             "size": 11}))
            write(tf, runs, size=13, color=NAVY_SOFT, space_after=7,
                  line=1.05)

    # ---- Status / roadmap strip -------------------------------------------
    sy = cy + ch + Inches(0.20)
    sh_h = Inches(0.70)
    for i, (label, colour, body) in enumerate([
        ("COMPLETED", TEAL, "Monitoring + automation"),
        ("IN PROGRESS", AMBER, "Forecasting + queue backlog prediction"),
        ("NEXT", NAVY_SOFT, "AI Copilot for Operations"),
    ]):
        x = MARGIN + i * (w + gap)
        pill = rect(s, x, sy, Emu(w), sh_h, fill=GREY_LIGHT, line_color=LINE)
        tf = pill.text_frame
        tf.margin_left = tf.margin_right = Inches(0.12)
        tf.vertical_anchor = MSO_ANCHOR.MIDDLE
        write(tf, label, size=11, color=colour, bold=True, first=True,
              space_after=2, line=1.0)
        write(tf, body, size=12.5, color=NAVY_SOFT, space_after=0, line=1.0)

    # ---- Business benefits strip ------------------------------------------
    by = sy + sh_h + Inches(0.24)
    strip = rect(s, MARGIN, by, CONTENT_W, Inches(0.62), fill=NAVY,
                 line_color=None)
    tf = strip.text_frame
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    write(tf, [("Business Benefits:  ", {"bold": True, "color": WHITE}),
               ("Prevent outages  |  Better planning  |  Reduced "
                "emergency work  |  Capacity optimization",
                {"color": TEAL_LIGHT})],
          size=14, first=True, space_after=0, line=1.0,
          align=PP_ALIGN.CENTER)

    notes(s, """
Opening: this slide is about our own operations. PACS and HL7 problems are still found
reactively - a queue backs up, an interface fails or a volume fills, and we hear about it
after the customer is already affected. Every one of those events then costs manual
investigation time.

What is already completed: PACS / HL7 service monitoring, queue and interface visibility,
operational status mapping, automation, and automated issue classification. That is the
foundation - we can see the estate and act on it in a standard way.

What AI adds on top: risk forecasting, storage capacity prediction and performance
degradation prediction, plus prioritized remediation recommendations so the team is told
what to do first, not just what is broken. Queue backlog forecasting is in progress, and
the prioritized remediation recommendations are the next increment.

What is next after that: an AI Copilot for Operations - plain-language questions such as
"why is HL7 failing?" or "which server is most at risk?" - so investigation is not limited
to the few engineers who know where to look.

Business impact: earlier detection, faster resolution, reduced operational effort, a better
customer experience, improved system availability, and better capacity planning because
growth is forecast instead of discovered.

Framing for this audience: this is an operational efficiency and customer experience
initiative, not only a technical dashboard. It changes how much unplanned, out-of-hours
work we absorb and how early we can talk to a customer.

Evidence discipline: I am deliberately not quoting savings, percentages, ROI, dates or
production scope - the source material does not contain them. The benefits listed are
expected benefits, and the next useful step is agreeing the two or three operational
metrics (time to detect, time to resolve, volume of emergency work) that would prove them.

Sources: MS-AI/AI Dashboard/AI Dashboard Brief Project Description.docx (Objectives, Key
Capabilities, Business Value); MS-AI/AI Dashboard/Proactive Infrastructure Management_ A
Monitoring, Alerting, and Auto-Remediation Solution_20260513141714.pptx (slides 2-3, 5, 7,
9, 13-14).
""")


# --------------------------------------------------------------------------
# Slide 3 - Future and next ideas
# --------------------------------------------------------------------------
def slide_three(prs):
    s = blank(prs)
    chrome(
        s,
        "NEXT  ·  INVESTMENT OPTIONS FOR Q4 AND 2027",
        "Four Themes, One Recommended Starting Point",
        "Preliminary R&D sizing, not delivery commitments; full initiative "
        "list in the notes.",
    )

    top = Inches(2.28)
    rows = [
        ("Reporting quality & safety",
         "Catch prelim-vs-final discrepancies",
         "Medium–Large",
         "Pilot with one customer"),
        ("Operational intelligence",
         "AI triage of HL7 and interface failures",
         "Medium",
         "Extend Sentinel to HL7 / PACS"),
        ("Engineering productivity",
         "AI test automation and codebase access",
         "Small–Medium",
         "Continue the existing POC"),
        ("PACS independence & platform",
         "Retire EMR dependency; object storage",
         "Large",
         "Run the object-storage POC first"),
    ]
    headers = ("THEME", "BUSINESS VALUE", "EFFORT", "PROPOSED NEXT STEP")
    widths = [Inches(2.75), Inches(4.35), Inches(1.55), Inches(3.44)]
    header_h = Inches(0.38)
    row_h = Inches(0.86)

    x = MARGIN
    for w, head in zip(widths, headers):
        _, tf = textbox(s, x + Inches(0.1), top, w - Inches(0.1), header_h)
        write(tf, head, size=12, color=TEAL, bold=True, first=True,
              space_after=0)
        x += w

    for r, row in enumerate(rows):
        y = top + header_h + r * row_h
        if r % 2 == 0:
            rect(s, MARGIN, y, CONTENT_W, row_h - Inches(0.06),
                 fill=GREY_LIGHT, line_color=None, adj=0.08)
        x = MARGIN
        for c, (w, cell) in enumerate(zip(widths, row)):
            _, tf = textbox(s, x + Inches(0.1), y + Inches(0.08),
                            w - Inches(0.2), row_h - Inches(0.16),
                            anchor=MSO_ANCHOR.MIDDLE)
            write(tf, cell, size=16,
                  color=NAVY if c == 0 else (AMBER if c == 2 else GREY),
                  bold=(c == 0 or c == 2), first=True, space_after=0,
                  line=1.05)
            x += w

    ask_y = top + header_h + len(rows) * row_h + Inches(0.14)
    ask = rect(s, MARGIN, ask_y, CONTENT_W, Inches(0.92), fill=NAVY,
               line_color=None)
    tf = ask.text_frame
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    write(tf, "RECOMMENDATION — NO ASK DOCUMENTED IN SOURCES",
          size=11, color=TEAL_LIGHT, bold=True, first=True, space_after=4)
    write(tf, "Approve discovery funding for the discrepancy detector; confirm "
              "HL7/PACS in the next Sentinel increment.",
          size=18, color=WHITE, bold=True, space_after=0, line=1.05)

    notes(s, """
Opening: the planning material holds roughly twenty ideas. Rather than read a feature
list, I have grouped them into four investment themes and put one recommendation in front
of you.

Why these four, and what is behind each theme (all from
MS-AI/Next Ideas/Q4 and 2027 ideas.docx):
1. Reporting quality & safety — AI report discrepancy detector comparing preliminary and
   final reports (critical, major, follow-up, laterality and measurement discrepancies with
   a pre-sign-off warning), findings-vs-impression consistency checks, critical result
   detection, template completeness and a prelim-to-final quality score, plus follow-up
   recommendation tracking that creates tasks in PACS or an administrative dashboard, and
   ORU / report enrichment for referring physicians.
2. Operational intelligence — HL7 and interface issue triage from interface-engine logs,
   HL7 troubleshooting executive summary mode, AI log analysis, error-grouping over logs
   already collected, and integration of the AI dashboard with CRM contract data to raise
   alerts when storage or concurrent-user limits are exceeded.
3. Engineering productivity — the EHR Orchestrator test-automation proof of concept
   (chat-driven, record, test and AI modes across desktop and web, which already surfaced
   defects logged in TFS), natural-language codebase knowledge access, and dead-code
   cleanup.
4. PACS independence & platform modernisation — removing the out-of-support EMR module and
   moving required logic to PACS, separating thick-client and web business logic with
   cross-OS file handling, an admin tool for PACS-only installations, object storage in an
   OCI bucket, and AI-generated ECG findings from ECG signals.

Deliberately kept off the slide: the market comparators — Us2.ai for automated
echocardiography reporting and Intelerad for detection and triage. They are evidence that
the market is moving toward AI measurement extraction and worklist prioritisation; they are
not our achievements and should not be presented as such. Also omitted for space: the ECG
finding generation idea, which is scientifically attractive but carries the heaviest
regulatory load, and the autonomous infrastructure-remediation agent concept.

Gap to flag: secure image and report sharing was requested as a topic, but I could not find
it anywhere in the planning document. If leadership expects it in the portfolio, the idea
needs to be supplied before it can be positioned.

Effort basis and uncertainty: Small / Medium / Large here are preliminary R&D judgements
based on documented scope and dependency breadth — discrepancy detection needs clinical
validation and sign-off workflow changes; operational intelligence largely reuses the
Sentinel platform; engineering productivity already has a working proof of concept; PACS
independence touches database, business logic and deployment across every customer. No
source contains effort figures or dates, and none of the proofs of concept justify
estimating full-product delivery. Treat all four as recommendations for discovery, not
commitments.

Why the recommended starting point: the discrepancy detector addresses patient-safety and
liability risk — the highest-value problem in the set — while the Sentinel HL7/PACS
extension gives the fastest return because the platform already exists. Both are testable
at small scale.

The ask: approve discovery funding for a discrepancy-detector pilot with one customer, and
confirm whether HL7/PACS monitoring belongs in the next Sentinel increment. Each of the
other themes returns with a sized proposal once discovery output is available.
""")


def main():
    prs = Presentation()
    prs.slide_width, prs.slide_height = SW, SH
    slide_one(prs)
    slide_two(prs)
    slide_three(prs)
    prs.save(OUT)
    print(f"Wrote {OUT} ({len(prs.slides.__iter__.__self__._sldIdLst)} slides)")


if __name__ == "__main__":
    main()
