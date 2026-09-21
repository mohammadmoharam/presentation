# AI Executive Overview — 3-slide deck

Executive-ready, 16:9 deck built **only** from the material in `MS-AI/`. Source documents
were read, not rewritten: nothing in `AI Priors`, `AI Dashboard` or `Next Ideas` was
modified.

## Artifacts

| File | Description |
| --- | --- |
| `AI-Executive-Overview.pptx` | 3 editable executive slides (shapes, text and cards are native PowerPoint objects) with embedded speaker notes, plus 4 supporting screenshot slides appended after slide 3 |
| `AI-Executive-Overview.pdf` | PDF export (LibreOffice) |
| `previews/slide-1.png` … `slide-7.png` | Rendered previews used for visual QA (4–7 are the screenshot appendix) |
| `slide-2-preview.png` | Standalone preview of the redesigned slide 2 |
| `slide-3-preview.png` | Standalone preview of the redesigned slide 3 |
| `slide-2-with-screenshot-link.png` | Preview of slide 2 showing the **View Dashboard Screenshots** button |
| `screenshot-appendix-1.png` … `-4.png` | Previews of the four supporting screenshot slides |
| `generate_presentation.py` | Reproducible generation script |
| `update_slide_2.py` | Rebuilds **only** slide 2 in the existing PPTX (slides 1 and 3 untouched) |
| `update_slide_3.py` | Rebuilds **only** slide 3 in the existing PPTX (slides 1 and 2 untouched) |
| `add_screenshot_appendix.py` | Rebuilds the 4 screenshot appendix slides and the slide-2 link (idempotent; slides 1–3 otherwise untouched) |
| `prepare_screenshots.py` | Builds the redacted copies of the four AI Dashboard screenshots used by the appendix |
| `assets/dashboard-screenshots/Screenshot_1.png` … `_4.png` | Redacted copies of `MS-AI/AI Dashboard/Screenshots/*` (signed-in user chip and one requester email pixelated; no crop, aspect ratio unchanged) |
| `assets/ai-history-summary-crop.png` | Tightly cropped product screenshot (demo data, identifiers removed) |

## The story

**Value delivered → value being developed → where to invest next.**

1. **Delivered — AI Patient History Summarization.** Years of prior reports are turned
   into one structured, prioritised patient view that is prefetched and waiting inside the
   existing reporting workflow. Built and generating summaries; pilot/production adoption
   is *not* evidenced by the sources.
2. **In progress — AI Operations Intelligence Dashboard.** Moving PACS / HL7 operations
   from reactive monitoring to predictive service intelligence: a completed foundation
   (monitoring, queue and interface visibility, operational status mapping, automation and
   automated issue classification), an AI intelligence layer on top (risk forecasting,
   storage capacity and performance degradation prediction, with queue backlog forecasting
   *in progress* and prioritized remediation recommendations *next*), and the business
   impact that follows. AI Copilot for Operations is the next step.
3. **Next — three priority themes.** Reporting quality & safety, operational
   intelligence and engineering productivity, presented as focus areas and business
   value. No effort sizing, proposed next steps or roadmap commitments appear on the
   visible slide; the wider initiative list and open questions stay in the notes.

## Screenshot appendix (supporting deep dive)

The core narrative is still slides 1–3. Four **supporting** slides are appended after
slide 3, one AI Dashboard screenshot per slide, because the dashboard screenshots are
~2:1 and unreadable in a 2×2 grid. They are labelled
`SUPPORTING SCREENSHOTS — OPTIONAL DEEP DIVE` so it is clear they are not part of the
three-slide story, and they are reachable only by hyperlink:

| Slide | Content | Navigation |
| --- | --- | --- |
| 2 | Executive summary (unchanged) | Small outlined **View Dashboard Screenshots ›** button, bottom-right corner |
| 4 | `Screenshot_1.png` — Storage Monitoring | Next Screenshot · Back to Slide 2 |
| 5 | `Screenshot_2.png` — CPU & Memory Process Insights | Previous · Next Screenshot · Back to Slide 2 |
| 6 | `Screenshot_3.png` — Alert Management & Failures Control Center | Previous · Next Screenshot · Back to Slide 2 |
| 7 | `Screenshot_4.png` — Automation Rules & Actions Engine | Previous · Back to Slide 2 |

All navigation uses internal PowerPoint slide hyperlinks (no external file links). The
appendix slides are left **visible** rather than hidden so that the PDF export and the
PNG previews contain them; the eyebrow label carries the “optional deep dive” framing.
Images are placed with their native aspect ratio (scaled to fit a 12.09 × 5.24 in box).
The screenshots come from the non-production `MS-TEST` environment and are embedded
uncropped, but `prepare_screenshots.py` pixelates the personally identifiable regions
first: the signed-in user chip in every header and the `REQUESTED BY` email address in
`Screenshot_4.png`. What remains visible is host/volume names, alert counts and rule
definitions — no credentials, API keys, patient data or configuration secrets. Run
`prepare_screenshots.py` before `add_screenshot_appendix.py` if the sources change. Re-run
`add_screenshot_appendix.py` after `update_slide_2.py`, which rebuilds slide 2 from
scratch and therefore removes the link button.

## Source mapping

| Slide | Sources (all paths relative to repo root) |
| --- | --- |
| 1 | `MS-AI/AI Priors/AI-Powered Patient History Summarization.docx` (objectives, key capabilities, expected business value); `MS-AI/AI Priors/Patient History Summarization .pptx` slides 2–3, 5–9, 11–12 + speaker notes; `MS-AI/AI Priors/Patient-History-Summarization-UseCase 1.pdf` pages 1–2; `MS-AI/AI Priors/AI Patient Summary Customer Perspective 1.html`; `MS-AI/AI Priors/AI Patient Summary Support Runbook 1.html` sections 1–4, 7; screenshot cropped from slide 6 of the Priors PPTX |
| 2 | `MS-AI/AI Dashboard/AI Dashboard Brief Project Description.docx` (objectives, key capabilities, business value); `MS-AI/AI Dashboard/Proactive Infrastructure Management_ A Monitoring, Alerting, and Auto-Remediation Solution_20260513141714.pptx` slides 2–9, 13–15 + notes; “Next” column items also appear in `MS-AI/Next Ideas/Q4 and 2027 ideas.docx` |
| 3 | `MS-AI/Next Ideas/Q4 and 2027 ideas.docx` (all numbered proposals, comparator sections 6–7 and the unnumbered items after the separators) |

Theme composition (full mapping, also summarised in the slide-3 speaker notes):

- **Reporting quality & safety** (on slide: AI Report Discrepancy Detector, AI ECG findings
  from signals) — discrepancy detection covers critical/major/follow-up/laterality/
  measurement changes with a pre-sign-off warning and a prelim-to-final quality score;
  follow-up recommendation tracking and ORU/report enrichment stay in the notes.
- **Operational intelligence** (on slide: unified PACS / HL7 investigation, proactive log
  analysis) — interface issue triage, HL7 troubleshooting executive summary mode, log error
  grouping and AI dashboard ↔ CRM contract alerts stay in the notes.
- **Engineering productivity** (on slide: AI-assisted test orchestration, codebase knowledge
  assistant) — EHR Orchestrator test-automation POC and natural-language codebase knowledge
  access; dead-code cleanup stays in the notes.
- **Not shown as a theme** — PACS independence & platform modernisation (EMR dependency
  removal, thick-client/web separation with cross-OS file handling, admin tool for PACS-only
  installations, OCI bucket storage POC) is kept out of the three-theme portfolio; AI ECG
  findings moved into reporting quality & safety.

Deliberately excluded from the visible slide (kept in notes): the Us2.ai and Intelerad
market comparators — they are references to what the market is doing, **not** our
achievements.

## Evidence rules applied

- No savings, ROI, accuracy, adoption, staffing, budget or date figures were invented; the
  sources contain none, so none appear.
- Benefits are labelled as **expected**. Slide 1 says “time saved not yet measured”;
  slide 2 says “no measured MTTR data yet”.
- “Accomplished” is framed as *development complete and generating summaries*, explicitly
  not as pilot validation or production adoption.
- Claims such as “fully autonomous”, “production-ready” or “compliant” are avoided. The
  autonomous-operations phases in the dashboard deck are presented as roadmap.
- The screenshot is cropped to the problem-list panel only; patient name, sex, date of
  birth, MRN and facility/address/phone were cropped out. No credentials, API keys,
  mission/folder IDs or configuration secrets appear on any slide or in the notes.

## Effort-estimate basis

| Work | Effort statement | Basis |
| --- | --- | --- |
| Slide 1 (delivered) | “Effort not documented” | No source records delivery effort. Known effort concentrations (Matcha model evaluation, caching) are described qualitatively in the Priors deck, slides 8–9. |
| Slide 2 (in progress) | “Sizing to be confirmed” + named remaining work | The project description states file transfer provides “policy decisions and audit records before enabling full real file streaming”, and that AgentRelay is “introduced and validated in stages”. No sizing or dates exist in any source. |
| Slide 3 (future) | No effort statement | Effort, sizing and proposed next steps were removed from the visible slide by design; sizing remains an open discovery question recorded in the speaker notes. No source contains effort figures, and prototype-scale evidence was **not** extrapolated into delivery estimates. |

## Assumptions and unresolved questions

1. **Folder names.** The task referenced `AI Priors ` and `AI Dashboard ` with trailing
   spaces; the actual directories are `MS-AI/AI Priors` and `MS-AI/AI Dashboard`.
2. **Dashboard status discrepancy.** The May 2026 deck presents an AI-assisted **proof of
   concept** with generated mockups (slide 15), while `AI Dashboard Brief Project
   Description.docx` describes implemented platform capabilities. The project description
   is used as the status of record and the deck as roadmap/vision. **Needs confirmation.**
3. **Scope discrepancy.** The dashboard deck is framed around PACS/HL7 healthcare
   operations; the project description is framed around Windows server monitoring and
   remote operations. HL7/PACS monitoring is therefore shown under **Next**.
4. **Secure image and report sharing** — requested as a slide-3 topic, but not present
   anywhere in `Q4 and 2027 ideas.docx`. It is intentionally omitted and flagged as a gap.
5. **Attribution in the ideas document.** Several unnumbered items (log-analysis platform,
   log error-grouping service, internal codebase assistant) are written in first person but
   mention an external organisation; the numbers quoted there (for example daily error
   volumes and cost multiples) are **not** reproduced on the slides and should not be
   presented as our results until ownership is confirmed.
6. **Pilot evidence.** No pilot results, customer adoption or accuracy measurements exist
   in the sources for either project; the recommended next step on slide 1 is to agree the
   metrics that would produce them.
7. **Word budget.** Slides 1 and 2 sit inside the ~60–90 visible-word guidance; slide 3 is
   marginally above it once the eyebrow, theme numbers and “VALUE” labels are counted.

## Regeneration

```bash
pip install python-pptx pillow            # deck generation
python3 MS-AI/Executive-Presentation/generate_presentation.py

# slide 2 or slide 3 only, edited in place in the existing deck
cd MS-AI/Executive-Presentation && python3 update_slide_2.py
cd MS-AI/Executive-Presentation && python3 update_slide_3.py

# redacted screenshot assets, then the appendix slides + slide-2 link
# (idempotent; slides 1-3 and their speaker notes are kept as they are)
cd MS-AI/Executive-Presentation && python3 prepare_screenshots.py
cd MS-AI/Executive-Presentation && python3 add_screenshot_appendix.py

# optional: PDF export and PNG previews (LibreOffice + PyMuPDF)
sudo apt-get install -y libreoffice-impress
pip install pymupdf
cd MS-AI/Executive-Presentation
soffice --headless --convert-to pdf AI-Executive-Overview.pptx
python3 -c "import pymupdf;d=pymupdf.open('AI-Executive-Overview.pdf');[p.get_pixmap(dpi=140).save(f'previews/slide-{i}.png') for i,p in enumerate(d,1)]"
```

The screenshot asset was produced once from slide 6 of
`MS-AI/AI Priors/Patient History Summarization .pptx` by cropping to the problem-list panel
(pixel box 62,462 → 878,800 of the extracted image) and upscaling 2×.
