# Benny integration contract

This optional workflow has no active route, schedule, Slack bridge, or recorder built in. All activation and external write types need explicit user authorization. Native skill loading is not configuration/merge/deletion authority.

## Observed integration capabilities

Read current official documentation and inspect supported source, tracker, event-route, scheduler and configuration capabilities before use. Documentation alone is not execution proof. The workflow creates no capabilities and installs nothing.

{{runtime.integrations}}

## Manual first

Native entrypoints are `pstack-benny-setup-benny`, `pstack-benny-triage-issue-reports`, and `pstack-benny-reproduce-and-fix-issues`. Configuration is Benny-owned YAML consumed as data by the skill, not a runtime settings schema. Examples are deliberately placeholders and inactive. Configure GitHub issue repo/number or a verified Slack source adapter explicitly. The GitHub issue is already a tracker record when tracker and source are the same; do not create another ticket for it.

GitHub reads/writes use already available authenticated `gh` and GitHub skills. Validate exact repo/issue identifiers, use explicit repo flags and structured JSON arguments (not arbitrary webhook shell text), retrieve current parent and comments, and verify every write on the same record. Test comments are not authorized by merely loading setup. Never dump auth tokens, `.env`, or broad config. Browser forms use the approved secure credential-entry channel. API credentials need separate secure local environment/secret-manager provisioning.

## Optional webhook

An optional verified event route must load the operational skills and completed prompt, restrict event types/repository/actions through a tested filter, select explicit log-only delivery and bind the authorized execution context. The coordinator posts approved verdicts separately. Management output may contain generated credentials; never print it. Narrow payload fields and verify endpoint/signature rules. Secrets remain in secure local environment, never committed YAML.

For GitHub reports, validate configured repository and `action: opened` as well as `X-GitHub-Event: issues`. Filter scripts must use the verified runtime-supported location and be separately approved, implemented and tested; do not assume declarative filtering support or hand-edit live settings. A plain subscription is not a Slack Events API bridge, scheduler, fixture service, or durable queue. Slack channel ingestion/thread writes/media downloads/status edits need explicit supported adapter capabilities; absent actions leave that integration blocked.

## Optional cron

An optional schedule must support the confirmed cadence, bounded prompt, actual skill attachments, exact working directory, explicit output destination and a verified paused/inactive state. Check current management controls before constructing it. If paused creation is unsupported, leave scheduling unconfigured. Even a paused write needs approval. No schedule is created by this pack. Read the exact job back after every approved write; update existing IDs only after conflict review, never duplicate or replace automatically.

{{runtime.persistent_work}}

Model/provider/reasoning choices are user-owned and never changed automatically. No per-role capability is assumed. Independent workers need self-contained bounded briefs and observed controls. Prose restrictions cannot guarantee isolation; source/tracker/code writes stay with the coordinator when isolation is unproven. Leaves return questions and proposed next waves to the coordinator.

{{runtime.delegation}}

Long original Slack budgets are workflow deadlines, not permission to hold a cron/webhook run open for hours. Discover actual runtime limits. Use a separately verified saved checkpoint/queue with source identity, event dedupe, trusted triage verdict, observed evidence, remaining budget, and next-action deadline for resumable work. Revalidate ownership/parent/PR artifacts before each resumed write. No approved persistence adapter means manual bounded work, not an invented recurring integration.

## Source and compensation

Freeze the exact parent identity before any writes. GitHub identity is repo + issue number + canonical source URL; Slack identity is channel + root thread timestamp, not the timestamp of a reply. Immediately preflight parent before tracker writes and comments, then read back the exact target. Source deletion/inaccessibility/uncertainty means no writes, never a fallback parent or channel.

A separate newly created tracker issue needs a preauthorized compensating close/cancel if verdict handoff fails. Never delete/close the original source issue or another actor's existing ticket. If compensation is unavailable, do not create in the first place. If readback fails after a write, report uncertain state, do not blindly retry.

## Activation gates

Resolve dependencies in the execution profile, fill config placeholders, demonstrate tracker/source read/write/dedupe/compensation, test trusted marker and parent safety, prove worker isolation or disable workers, and demonstrate all seven control capabilities. A missing screen recorder blocks the original recording-required repro contract. Desktop/browser drivers may satisfy parts, not automatically all. Activate only after explicit approval and verified harmless test results. No merge/deploy authority.
