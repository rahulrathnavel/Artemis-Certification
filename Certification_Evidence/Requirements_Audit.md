# Telecom certification requirements audit

Source: `Artemis Telecom Project for Certification.docx` in this workspace.
Working project: `01a15398-32be-703d-b7a1-7d2ba6e402d7` in Rahul Rathnavel k Workspace.

This is a working audit, not a completion certificate. A configured feature is not treated as an end-to-end pass.

| Requirement | Implementation/evidence | Acceptance still required |
| --- | --- | --- |
| Project named `<yourName>_telecom_assignment_project` | Original company project has the required name; personal copy currently has a trial name | Give the final personal submission project the required name |
| Reasoning TopUpPlan_Query_Agent with all/prepaid/postpaid HTTP tools | Present in saved project export | General browsing, price/data filters, plan-type continuity and factual grounding |
| Flow UserDataPlan | Pattern validation, customer lookup, actual account type extraction, matching-plan lookup and presentation are defined | Valid/invalid/missing customer IDs, prepaid/postpaid records, switching customer, complete rendered output |
| Reasoning SIMIssueAgent with MCP tools | Four read-only SIM tools are attached | Symptoms, issue ID details, customer history, clarification and service switching |
| Supervisor intents, welcome, start agent | Defined; import sets Telecom_Supervisor as entry agent | Fresh chat welcome and all three routes, including follow-ups |
| Project telecom-domain LLM check | Active project input policy in export | Block unrelated/politics/religion requests; permit telecom continuation and IDs |
| Agent abuse LLM checks | Present in all four agents as quoted single-line checks | Block an insult before and during a flow; permit ordinary frustration; recover on the next polite turn |
| Two end-user personas | Everyday_Telecom_Customer and Detail_Oriented_Customer exist | Both participate in the full matrix |
| Two realistic scenarios | General_And_Account_Matched_Plans and SIM_Support_And_Service_Switching exist | Both run against each persona |
| Response quality and tool correctness LLM judges | Original judges retained; evidence-grounded v2 judges added | Review all eight full-matrix judgments; investigate failures instead of treating a high score alone as proof |
| Web-channel deployment | Not yet evidenced for the personal copy | Publish tested agents, create web deployment, test actual end-user channel |
| End-user conversation screenshot | Pending | Capture the deployed web conversation |
| SOP | Draft prepared separately | Update with final deployment and observed results |
| Project export with Evals deselected | Core-only diagnostic export exists; not designated final submission | Generate final ZIP after verification, exclude Evals, check archive integrity |
| Evals output screenshot | User supplied diagnostic screenshots | Capture final full-matrix result with failures/review status visible |
| Supervisor orchestration transcript | Direct regression records exist | Save a verified multi-service conversation from the final tested build |

## Confirmed diagnostic findings

1. The supplied R3-001 budget-filter reply correctly lists USD 1.99 and USD 2.99 under USD 5. Its tool judge misquotes that reply and confuses the full tool catalog with the filtered customer response. This is a judge false failure, not evidence to add a special-case allowlist to the agent.
2. Earlier transcripts separately showed unsupported postpaid recommendations and invented validity/benefit associations. These remain genuine regression risks and must not be dismissed because one judge was wrong.
3. A legacy model binding alone does not select a model for the project. Adding the independent judge initially failed preflight with NO_PROJECT_DEFAULT. A core-only import adds the existing Gemini connection to the selected list and preserves Mistral as the default.
4. Minimal evaluations have completed; previous awaiting_retry states do not establish that the entire company workspace quota was exhausted.
5. A later normal-chat request returned HTTP 429 with the explicit error `Concurrent session limit exceeded`. Several completed diagnostic sessions remained marked active. The precise concurrent-session allowance and cleanup behavior have not been established; no session histories were deleted.
6. The independent judges passed the unchanged R3-001 budget-filter transcript during evaluator-only calibration (run `01a153e9-725a-7e98-ad79-1f4f22192593`). This supports the false-failure diagnosis. The planned negative calibration was blocked before it could start.
7. Full matrix run `01a153dd-3ccd-7f6a-b58a-c4ad40e93717` completed all four conversations and eight numeric judgments, scoring 0/100. Its exported transcripts show incomplete simulated-customer messages, missed scenario stages, unsupported account-lookup refusals, and false SIM escalation/resolution claims. This is a reviewed failed run, not a missing result or a pass.
8. The simulator's configured output limit was increased from 256 to 4096 and scenario milestones were split into individual requirements. A focused follow-up produced complete customer utterances but still failed account switching (run `01a153e8-b55b-7d95-95a3-7bf01ac46544`). These harness changes have not yet passed the full matrix.
9. Artemis rejected another evaluator-only start: the personal workspace has used 10 of 10 evaluation run starts in its billing window, resetting at `2026-11-14T12:53:01.316Z`. This is an Artemis Evals allowance, separate from the concurrent-session error and provider token quotas.
10. A Gemini reasoning-agent comparison timed out during normal chat. The three changed reasoning definitions were restored from their preceding backups. The revised independent evaluators, selected-model configuration and revised scenario assets remain; agent behavior is still awaiting a verified functional repair.

## Completion rule

Do not label the project production-ready or certification-complete until functional checks, the full evaluation matrix, web-channel evidence and all submission files are reviewed. Preserve failed runs and their explanations.
