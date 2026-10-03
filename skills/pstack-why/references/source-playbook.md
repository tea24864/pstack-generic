# Source playbooks

## Hermes execution contract

Read the owning skill's `references/hermes-runtime.md` first. This reference is a procedure/prompt, not authority to change state. Use `read_file`, `search_files`, and `terminal` for local read-only evidence. Discover deferred tools with `hermes_tool_search`/`tool_describe` before `tool_call`; use only authenticated read operations actually present. Service names identify conditional evidence categories, not guaranteed tools. Missing access, unsupported searches, retention limits, and incomplete pagination are explicit gaps.

For delegation, the parent supplies this full prompt, repository/session scope, and all evidence needed in `delegate_task` goal/context tasks. Children cannot delegate or ask the user and must not write files or external state. They share the filesystem; read-only is a behavior contract, not enforced sandboxing. Return findings in the tool response. The parent owns subsequent waves; async results arrive after the parent yields, never through transcript polling. Role lenses inherit the parent model, so never claim model diversity from role labels.

The `pstack-why` skill spawns one investigator per available evidence category, each reading a single source-specific playbook below. The playbooks are concrete examples for common MCPs. Adapt them for a different MCP in the same category.

- Source control history: [`code-archaeology.md`](./sources/code-archaeology.md), via `terminal` running git/gh plus local file tools.
- Issue/ticket tracker: [`linear.md`](./sources/linear.md), conditional Linear/Jira/GitHub Issues/Plane/Shortcut read source.
- Long-form documents: [`notion.md`](./sources/notion.md), conditional Notion/Confluence/Google Docs/Coda read source.
- Team chat: [`slack.md`](./sources/slack.md), conditional Slack/Discord/Teams/Mattermost read source.
- Infrastructure observability: [`datadog.md`](./sources/datadog.md), conditional Datadog/New Relic/Honeycomb/Grafana/Splunk read source.
- Error/exception tracking: [`sentry.md`](./sources/sentry.md), conditional Sentry/Rollbar/Bugsnag/Airbrake read source.
- Product analytics: [`databricks.md`](./sources/databricks.md), conditional Databricks/Snowflake/BigQuery/ClickHouse/dbt read source.

These are evidence categories and search strategies, not a list of installed tools. Discover schemas per session and record all unavailable/ambiguous categories.

Cross-cutting:

- [`incident-postmortem.md`](./sources/incident-postmortem.md). Add this if the target code looks defensive (null checks, retry, timeout, rate limit, feature flag, egress guard, OOM handler).
