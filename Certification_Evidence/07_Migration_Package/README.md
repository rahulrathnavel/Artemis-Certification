# Telecom workspace migration package

Use `Telecom_Migration_With_Evals_Verified_2026-10-19.zip`.

This archive contains four agent definitions, eleven tool-library definitions, MCP configuration, the telecom-domain policy, project configuration and evaluation assets. It is a diagnostic migration backup, not a completed certification submission.

Verification: all recorded file hashes and the root hash pass the CLI verification command. The ZIP was decompressed in memory and every entry compared with its source bytes. See `Verification.txt` and `Verified_Archive_Integrity.json`.

The installed CLI's lockfile recompute and verify commands sort object keys differently. The verified archive uses the verifier's canonical key ordering for its root hash. File contents were not changed to conceal differences.

## Destination setup

1. Create the destination workspace through an available Artemis workspace-creation control, or have a platform administrator create it. The installed MCP/CLI exposes workspace listing and switching, not workspace creation.
2. Tell the agent the new workspace name or ID so access and any assigned Evals allowance can be checked. A new allowance is not guaranteed merely because the workspace is new.
3. Create the destination project with the assignment-compliant name `RahulRathnavel_telecom_assignment_project` and import this ZIP through the supported import workflow.
4. Configure/select the destination workspace's model connections. API keys are not contained in the project export; the existing workspace's connection IDs must not be reused as if they were destination credentials.
5. Bind the assistant, simulator and judge models explicitly using the destination IDs. Set Telecom_Supervisor as the entry agent.
6. Run one focused multi-service test, review its full exported transcript, and fix actual failures before using another full-matrix start.
7. Once the four required conversations and eight judgments, functional guardrail checks and actual web-channel tests have been reviewed, produce the final submission export with Evals excluded.

## Known unfinished validation

- The independent judges correctly passed the unchanged under-USD-5 transcript during positive calibration.
- The latest complete matrix failed all eight judgments and its failures were reviewed. Account routing, unsupported facts/actions and simulated-customer progression remain risks.
- A comparative Gemini reasoning configuration timed out; the preceding Mistral agent definitions were restored. No successful broader functional repair is claimed.
- The current personal workspace rejected further starts after 10 of 10 evaluation starts were consumed in the billing window. Its reported reset is 14 November 2026.
- Web deployment, end-user screenshots, final orchestration transcript and a passing/reviewed final build remain pending.

Do not submit this migration archive as the assignment's final export: it intentionally includes Evals to transfer the test assets.
