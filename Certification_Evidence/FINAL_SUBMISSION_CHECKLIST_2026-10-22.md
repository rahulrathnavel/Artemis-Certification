# Final submission checklist — 2026-10-22

## Already ready

- [x] Live Artemis preview link available for the Gradious workspace/project: https://agents.kore.ai/preview#share_token=eyJwcm9qZWN0SWQiOiIwMWExNDQxNC1kMDIzLTdjNmYtYWMwZC03ODcxMWQ5YWViOGYiLCJ0ZW5hbnRJZCI6IjAxOWVhNmE0LTcyYTEtN2NhMS04NTJkLTRmYWFhOWVmZDhjZCIsImNoYW5uZWxJZCI6IjAxYTE2MzdhLTI2MjAtNzQyMi05YWNhLTM2ZTY1ZmMzN2UwNiIsInBlcm1pc3Npb25zIjpbInNlc3Npb246c2VuZF9tZXNzYWdlIiwiYXR0YWNobWVudDpyZWFkIiwiYXR0YWNobWVudDp3cml0ZSIsInNlc3Npb246cmVhZCJdLCJleHAiOjE3OTMyNzUxMTc5OTYsInR5cGUiOiJzaGFyZSJ9.zvyBclJMtVeDda3oYRLtrcRiysJA7oR_v3ErrBoM5k8
- [x] Active full multi-agent dev deployment for `Telecom_Supervisor`, `TopUpPlan_Query_Agent`, `UserDataPlan`, and `SIMIssueAgent`.
- [x] Source project ZIP copied under `Project_Source`.
- [x] 49 configuration and runtime screenshots under `Submission_Screenshots`.
- [x] Evals dashboard evidence under `10_Evals`.
- [x] Runtime traces and conversation exports under `11_Final_Runtime`.
- [x] Existing requirements checklist and readiness report.

## Remaining manual evidence

1. Open a new Artemis chat from the live preview link.
2. Capture one clean conversation for each required path, waiting for each response:
   - prepaid plans;
   - postpaid plans;
   - prepaid plans under a budget;
   - account lookup for `CUST1001`;
   - another-account lookup for `CUST1002`;
   - SIM issue catalogue;
   - reported SIM issues for `CUST1001`;
   - mobile-data troubleshooting;
   - unrelated political request;
   - abusive-language request.
3. Export the clean conversation and debug trace for each successful path.
4. Confirm the customer lookup response is understandable and uses the correct customer/account type.
5. Re-export the project only if you changed the project after creating the source ZIP.
6. Put any new JSON exports in `11_Final_Runtime` with descriptive filenames.
7. Create one final ZIP containing the project source and the complete `Certification_Evidence` folder.

## Submission contents

- Final project source ZIP.
- `Certification_Evidence/Submission_Screenshots`.
- `Certification_Evidence/10_Evals`.
- `Certification_Evidence/11_Final_Runtime`.
- This checklist and `Submission_Readiness_2026-10-21.md`.
- Artemis live preview link and project link.

Do not describe a simulated or edited screenshot as a real evaluation run. Evals quota is exhausted, so use the recorded Evals evidence and fresh manual conversation exports for the remaining verification.
