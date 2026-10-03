# Linear Tickets

## What this source contains

- Issues describing features, bugs, and their motivation
- Project docs attached to issues (often PRDs or specs)
- Parent/sub-issue relationships (broader initiative → specific tickets)
- Comments on issues (clarifications, scope changes, "why we're doing this" rationale)
- Labels (e.g., `compliance`, `customer-request`, `perf`) that signal the type of motivation
- Status updates that explain scope changes
- Attachments and linked GitHub PRs

Linear is where the product/business context often lives: the "we're doing this because customer X asked" or "this is for the Q3 compliance initiative" layer.

## How to search it

{{runtime.integrations}}

Use an actually discovered authenticated issue-tracker read connector (Linear is an example, not an assumed MCP). Inspect the schema before invoking it. No connector means a named issue-tracker coverage gap.

1. Fetch seed ticket IDs, preserving identifiers literally, and read the full issue plus paginated comments.
2. Search related issues by feature name, key symbol, and business term; try multiple phrasings.
3. Follow parent/sub-issue and duplicate-of relationships to the canonical motivation.
4. Read attached project docs where supported. Return cross-source links as leads for the parent, not permission to open another source.
5. Inspect labels, milestones, ownership, and historical status changes. Record queries, IDs, timestamp bounds, and access gaps.

## What good evidence looks like here

- An issue description stating the business problem: "Customer Acme needs X because of their SOC2 audit"
- A comment recording a decision: "We decided to go with approach B because approach A would require touching the billing service"
- A parent issue titled like an initiative: "Q3 Enterprise Readiness" or "Reduce Payment Failures"
- An attached PRD or spec
- Labels like `customer:acme`, `incident-followup`, `compliance`, `perf-regression`

## Common pitfalls

- **Scope drift.** The ticket the PR references may have been closed and reopened with a different scope. Read the whole history.
- **Mechanical templates.** Some teams require "Why" sections but fill them with boilerplate. Generic text ("improve user experience") is probably not a real answer.
- **Stale tickets.** Old tickets often reflect a version of the plan that changed. Check dates and cross-reference with the code's ship date.
- **Closed-as-duplicate chains.** Follow the duplicate-of relationships back to the canonical ticket.
- **Private workspace content.** If you can't access an issue, note that as a gap rather than guessing.

## What to return

For each relevant ticket:
- Ticket ID and title
- The problem/motivation quoted from the description or comments (not paraphrased. The synthesizer needs the exact text to cite)
- Labels, parent issue, project
- Author, created date, closed date
- Link to the ticket if available
