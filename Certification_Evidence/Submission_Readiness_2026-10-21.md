# Submission readiness — 2026-10-21

## Completed

- Project source ZIP copied to `Certification_Evidence/Project_Source/rahulrathnavel-telecom-assignment-project (3).zip`.
- The ZIP contains the four agents, project metadata, model configuration, runtime configuration, guardrail policy, MCP configuration, HTTP tools, and SIM MCP tools (24 files).
- Configuration screenshots are collected under `Certification_Evidence/Submission_Screenshots` (49 PNG files).
- Runtime trace and conversation evidence are under `Certification_Evidence/11_Final_Runtime`.
- Evals dashboard evidence is under `Certification_Evidence/10_Evals`.
- An active Artemis deployment exists for Telecom_Supervisor in the dev environment.

## Evidence that is currently usable

- General prepaid plan browsing.
- General postpaid plan browsing in the latest final trace.
- Budget filtering for prepaid plans.
- SIM issue catalogue and troubleshooting.
- Telecom-only refusal for unrelated requests.
- Abuse-language guardrail response.
- Project configuration, tools, MCP, guardrail, and overview screenshots.

## Remaining gaps to verify before submission

1. **UserDataPlan response shape:** the account lookup can produce multiple visible category messages. The required final evidence should show one combined customer-facing response.
2. **Fresh customer lookup cases:** test `Find plans matching my account.` followed by `CUST1001`, and `Find plans for a different customer.` followed by `CUST1002` in separate fresh chats. Confirm the correct customer and account type are used.
3. **Postpaid freshness:** run one fresh postpaid chat and keep its clean conversation export plus trace. Confirm no prepaid offers appear under a postpaid heading.
4. **Mobile-data routing:** run one fresh chat with `My mobile data keeps failing; please help.` and retain evidence that SIMIssueAgent handles it.
5. **Submission packaging:** include the Artemis project export ZIP, screenshots, clean conversation exports, runtime traces, checklist, and this report. Do not present a simulated eval screenshot as a real run.

## Steps to finish

1. Open the deployed Telecom_Supervisor chat in Artemis.
2. Start a new chat for each remaining case; wait for each response before sending the next message.
3. Export the clean conversation and debug trace for each successful case.
4. Save those exports under `Certification_Evidence/11_Final_Runtime` with clear names.
5. If the account lookup still emits three visible messages, fix the UserDataPlan final response before capturing final evidence.
6. Re-export the project after any change and replace the source ZIP in `Project_Source`.
7. Submit the complete `Certification_Evidence` folder together with the source ZIP and Artemis project link.
