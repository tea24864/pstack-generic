# Source playbooks

The `pstack-why` skill assigns one investigation per available source, grouped by evidence category, each reading a single source-specific playbook below. The playbooks are concrete examples for common MCPs. Adapt them for a different MCP in the same category.

- Source control history: [`code-archaeology.md`](./sources/code-archaeology.md), via git/gh and local source reads.
- Issue/ticket tracker: [`linear.md`](./sources/linear.md), conditional Linear/Jira/GitHub Issues/Plane/Shortcut read source.
- Long-form documents: [`notion.md`](./sources/notion.md), conditional Notion/Confluence/Google Docs/Coda read source.
- Team chat: [`slack.md`](./sources/slack.md), conditional Slack/Discord/Teams/Mattermost read source.
- Infrastructure observability: [`datadog.md`](./sources/datadog.md), conditional Datadog/New Relic/Honeycomb/Grafana/Splunk read source.
- Error/exception tracking: [`sentry.md`](./sources/sentry.md), conditional Sentry/Rollbar/Bugsnag/Airbrake read source.
- Product analytics: [`databricks.md`](./sources/databricks.md), conditional Databricks/Snowflake/BigQuery/ClickHouse/dbt read source.

These are evidence categories and search strategies, not a list of installed tools. Discover schemas per session and record all unavailable/ambiguous categories.

Cross-cutting:

- [`incident-postmortem.md`](./sources/incident-postmortem.md). Add this if the target code looks defensive (null checks, retry, timeout, rate limit, feature flag, egress guard, OOM handler).
