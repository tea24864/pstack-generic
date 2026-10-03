# Notion Docs

## What this source contains

- PRDs (product requirement documents)
- Technical specs and RFCs
- Architectural decision records (ADRs)
- Meeting notes from design reviews
- Team pages with domain context
- Postmortems from incidents
- Runbooks that may explain defensive code
- Strategy documents that set priorities

Notion is where "why" often lives in long-form before it becomes code. A significant feature usually has a doc.

## How to search it

{{runtime.integrations}}

Use an actually discovered authenticated document read connector (Notion is an example, not a promised tool). Inspect its search/fetch schemas; missing access is a long-form-doc coverage gap.

1. Search feature names, symbols/classes, author handles, error strings, and user-visible terms. Use the relevant ship-date window where supported.
2. Fetch candidate pages fully, including paginated blocks/content; do not use previews as rationale evidence.
3. Follow within-source backlinks and child pages for alternatives, appendices, and implementation notes.
4. Query related document collections/databases or meeting notes only if that read operation exists.
5. Search author spaces only within approved project/team scope. Capture authors, dates, finalized/draft status, section locations, and verbatim motivation text.

## What good evidence looks like here

- A PRD with a "Problem statement" or "Motivation" section that matches the target code's purpose
- An "Alternatives considered" or "Rejected approaches" section
- A postmortem that names the target code as the fix for a specific incident
- Meeting notes that record "we decided X because Y" and tie to the same author/date range as the PR
- An ADR template filled out non-trivially (status, context, decision, consequences)

## Common pitfalls

- **Outdated docs.** Specs are often written before implementation and not updated. The doc may describe a plan that changed. Cross-check against the actual PR.
- **Doc vs. reality drift.** A spec may say "we'll do X" but the code actually does Y. Flag the divergence. The synthesizer will surface the contradiction.
- **Boilerplate templates.** Some orgs require a "Why" section that gets filled with fluff. Look for specificity.
- **Unlinked docs.** The most relevant doc may not be linked from anywhere. Broad keyword searches help.
- **Multiple drafts.** If a topic has multiple docs, find the one that was finalized or most recently updated. Check dates.
- **Access-restricted pages.** If you can't access a page, note it as a gap.

## What to return

For each relevant doc:
- Title and URL
- Authors and last-updated date
- The motivation text (verbatim quote), with page/section location
- Relevant linked pages (so the synthesizer can cite them)
- Whether the doc was finalized or draft
