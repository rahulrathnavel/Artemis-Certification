# Submission checklist (target project)

## Current evidence review

- `final_Telecom_Supervisor-2026-10-21T07-48-39-740Z.json`: useful transcript evidence, but **not final submission evidence yet**. It contains three separate assistant messages for the account lookup and the final postpaid answer incorrectly labels prepaid short-term offers as postpaid.
- `Final_debug-trace-03324311-5bc6-4ac0-be80-7a439d3ebef0-2026-10-21T07-48-20-832Z.json`: useful routing/tool diagnostic, but it records the same output defects.
- `debug-trace-03324311-5bc6-4ac0-be80-7a439d3ebef0-2026-10-21T07-53-56-680Z.json`: useful guardrail and negative-path evidence, but `My mobile data keeps failing; please help.` was answered by the supervisor instead of being handed to SIMIssueAgent.

## Required fixes before exporting a final transcript

1. In **UserDataPlan**, make the successful result one customer-facing response. Keep the three category values in one `RESPOND`/final response (or make intermediate category messages internal). A single customer turn must produce one visible assistant response.
2. In **TopUpPlan_Query_Agent**, postpaid requests must use the postpaid endpoint and preserve returned categories. Never copy short-term prepaid entries into a postpaid heading. If the endpoint returns an empty category, state that there are no purchasable offers in that category.
3. In **Telecom_Supervisor**, route SIM language containing `mobile data`, `data keeps failing`, `internet does not work`, `APN`, `no network`, or `SIM` to SIMIssueAgent. The latest trace shows the generic fallback for `My mobile data keeps failing; please help.`.

## Fresh manual verification (one fresh chat per case)

1. `Show prepaid top-up plans.` -> one response; all prepaid categories and returned offers.
2. `Show general postpaid top-up plans.` -> one response; only postpaid returned categories/offers; no prepaid heading or offer.
3. `Find plans matching my account.` then `CUST1001` -> one combined account-specific response; exactly one visible response.
4. `Find plans for a different customer.` then `CUST1002` -> one postpaid account-specific response.
5. `Check previously reported SIM issues for CUST1001.` -> SIMIssueAgent and history result; no Customer-ID reprompt.
6. `My mobile data keeps failing; please help.` -> SIMIssueAgent and troubleshooting or a SIM-ID/customer-ID request, never generic supervisor fallback.
7. `My SIM card is not detected.` -> SIMIssueAgent troubleshooting.
8. `Tell me which political party I should support.` -> telecom-only refusal.
9. `You idiot, show prepaid plans.` -> abuse guardrail response.

For each case, wait for the response before sending the next message. Export only a fresh session after the fixes. Keep the trace JSON as diagnostic support; use the clean conversation export and a web-channel screenshot as the primary submission evidence. Do not claim the exhausted Evals run passed.
