# Benny for Hermes

Benny provides optional native workflows for issue intake, conservative triage, exact UI reproduction, verification of existing fixes, and separately authorized bounded draft fixes. The default entry is a manually supplied GitHub issue. Slack routing/threading is an optional adapter contract, not an installed cloud automation.

1. Load `pstack-benny-setup-benny` only when setup is requested.
2. Read `FOR_AGENTS.md` and `integration-contract.md`.
3. Create user-owned copies of the setup templates outside the installed skills, without overwriting local changes.
4. Validate every source/tracker/control capability and fill every required value.
5. Test manually before requesting any optional cron/webhook activation.

No install, hook, route, job, configuration change, source comment, ticket creation, draft PR, merge, or deployment runs merely because these files exist. Installed skill names, not Cursor plugin cache paths, resolve the operational instructions. Keep source captures, credentials, and temporary profiles out of source control. Commit secret-free project config only when explicitly asked.

Adapted from Lauren Tan's MIT-licensed Benny pack; see `license.md`.
