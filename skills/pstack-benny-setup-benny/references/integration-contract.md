# Benny Hermes integration contract

This optional workflow has no active route, schedule, Slack bridge, or recorder built in. All activation and external write types need explicit user authorization. Native skill loading is not configuration/merge/deletion authority.

## Verified platform documentation

- Webhooks: https://hermes-agent.nousresearch.com/docs/user-guide/messaging/webhooks
- Cron: https://hermes-agent.nousresearch.com/docs/user-guide/features/cron
- Configuration: https://hermes-agent.nousresearch.com/docs/user-guide/configuration
- Profiles/bots: https://hermes-agent.nousresearch.com/docs/user-guide/bot-mode
- Plugin extensions if a new adapter is needed: https://hermes-agent.nousresearch.com/docs/developer-guide/plugins

The first four pages and `hermes config --help`, `hermes webhook subscribe --help`, and `hermes cron add --help` were inspected during port authoring. Recheck live schemas/help for future execution. No undocumented Cursor backend, issue action, cloud editor, protocol deep link, or `/automate` dependency is retained.

## Manual first

Native entrypoints are `pstack-benny-setup-benny`, `pstack-benny-triage-issue-reports`, and `pstack-benny-reproduce-and-fix-issues`. Configuration is Benny-owned YAML consumed as data by the skill, not a Hermes config schema. Examples are deliberately placeholders and inactive. Configure GitHub issue repo/number or a verified Slack source adapter explicitly. The GitHub issue is already a tracker record when tracker and source are the same; do not create another ticket for it.

GitHub reads/writes use already available authenticated `gh` and GitHub skills. Validate exact repo/issue identifiers, use explicit repo flags and structured JSON arguments (not arbitrary webhook shell text), retrieve current parent and comments, and verify every write on the same record. Test comments are not authorized by merely loading setup. Never dump auth tokens, `.env`, or broad config. Browser forms use vault tools. API credentials need separate secure local environment/secret-manager provisioning.

## Optional webhook

Current `hermes webhook subscribe` can load native skills, use prompt templates, restrict event types, filter through a script, select delivery, and bind an already authorized route profile. Default explicit `--deliver log` prevents unintended gateway broadcast; the coordinator posts an approved issue/thread verdict separately. The result may contain a generated secret, so setup must not print it. Use narrow payload fields and verified endpoint/signature rules. Secret values remain in secure local environment, not committed YAML.

For GitHub reports, validate configured repository and `action: opened` as well as `X-GitHub-Event: issues`. Route scripts must live under the active profile's scripts directory and be separately authorized/implemented/tested; declarative filters are supported for static routes but do not hand-edit live config. A plain subscription is not a Slack Events API bridge, scheduler, fixture service, or durable queue. Slack channel ingestion/thread writes/media downloads/status edits need explicit supported adapter capabilities; absent actions leave that integration blocked.

## Optional cron

Current CLI accepts `hermes cron create`/`add` with schedule, prompt, repeated `--skill`, `--workdir`, explicit `--deliver`, and `--paused`. Verify help before constructing a payload; tools need schema discovery before calling. No schedule is created by this pack. A paused creation is one write, but still requires approval. Read back the exact job after any write. Existing jobs are updated only by ID with conflict review, never duplicated or replaced automatically.

Model/provider/reasoning pins are user-owned and must not be created or changed automatically. Main-model/global-delegation pin behavior is not per-role model support. `delegate_task` here uses only bounded goal/context tasks, no fabricated model/readonly/environment/background args. Child prompts cannot guarantee credential/tool isolation; sensitive source/tracker/code writes stay with the coordinator when isolation is unproven. Children cannot clarify or redelegate.

Long original Slack budgets are workflow deadlines, not permission to hold a cron/webhook run open for hours. Discover actual runtime limits. Use a separately verified saved checkpoint/queue with source identity, event dedupe, trusted triage verdict, observed evidence, remaining budget, and next-action deadline for resumable work. Revalidate ownership/parent/PR artifacts before each resumed write. No approved persistence adapter means manual bounded work, not an invented recurring integration.

## Source and compensation

Freeze the exact parent identity before any writes. GitHub identity is repo + issue number + canonical source URL; Slack identity is channel + root thread timestamp, not the timestamp of a reply. Immediately preflight parent before tracker writes and comments, then read back the exact target. Source deletion/inaccessibility/uncertainty means no writes, never a fallback parent or channel.

A separate newly created tracker issue needs a preauthorized compensating close/cancel if verdict handoff fails. Never delete/close the original source issue or another actor's existing ticket. If compensation is unavailable, do not create in the first place. If readback fails after a write, report uncertain state, do not blindly retry.

## Activation gates

Resolve dependencies in the execution profile, fill config placeholders, demonstrate tracker/source read/write/dedupe/compensation, test trusted marker and parent safety, prove worker isolation or disable workers, and demonstrate all seven control capabilities. A missing screen recorder blocks the original recording-required repro contract. `computer-use`/browser tools may satisfy parts, not automatically all. Activate only after explicit approval and verified harmless test results. No merge/deploy authority.
