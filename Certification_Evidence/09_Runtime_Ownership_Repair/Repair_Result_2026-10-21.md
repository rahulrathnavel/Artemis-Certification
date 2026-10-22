# Runtime ownership repair — 2026-10-21

Target workspace: `RahulRathnavel_telecom_assignment_project`
Target project: `RahulRathnavel_telecom_assignment_project`
Project ID: `01a153f0-fe87-71e0-b96b-485f4feb2bee`

## Root causes confirmed from the supplied traces

1. After the first specialist handoff, TopUpPlan_Query_Agent returned `continue` and retained the handoff stack. Later customer messages therefore entered that agent directly. SIM and account requests were answered by a plan-only agent.
2. UserDataPlan correctly retained control while waiting for its required Customer ID. Sending a SIM request at that point was treated as an answer to the pending gather field; a pending scripted gather cannot switch services mid-flow.
3. The project telecom-domain guardrail misclassified “Find plans for a different customer” as unrelated even though the saved policy allowed it.
4. The postpaid response mixed features from the mid-tier category into the premium category.

## Changes applied to the target project

- Added explicit nonterminal completion rules to TopUpPlan_Query_Agent and SIMIssueAgent so a completed specialist response can return to the Supervisor.
- Disabled the stale multi-intent queue in `config/runtime-config.json` so a completed handoff cannot keep a queued prior route active.
- Changed Supervisor handoff history to `none`; each new user message is classified by the Supervisor instead of being biased by a specialist's previous response.
- Added deterministic Supervisor route conditions for general plans, customer/account lookup and SIM requests.
- Rewrote the project domain check to explicitly allow another-customer lookup and follow-up messages within a telecom task.
- Added a deterministic abusive-term check to all four agents; the original LLM abuse check remains in place.
- Added category-hierarchy and exact-value constraints to TopUpPlan_Query_Agent.

The package was imported into the target project in operation `01a15d42-ffd2-7480-ae10-82224b5d8f35`. Supervisor, TopUpPlan_Query_Agent and SIMIssueAgent compiled successfully before import.

## Sequential checks completed

- Different-customer request opened UserDataPlan and requested a Customer ID.
- `CUST1002` returned the postpaid matching plan.
- SIM symptom request returned SIM detection guidance.
- `SIM-005` returned the requested issue details.
- Postpaid browsing returned the postpaid catalogue without the previous premium/mid-tier feature mixing.

One later history lookup was not run because Artemis returned `Concurrent session limit exceeded`; no Eval was started.

## Follow-up repair — mixed SIM/customer request

Trace `0002ac51-03e9-433e-901c-c79d85efcce6` showed that `Check previously reported SIM issues for CUST1001` matched the broad customer route before the SIM route. UserDataPlan then correctly asked for its own Customer ID because it had been selected incorrectly. The Supervisor customer route was narrowed to exclude SIM, mobile-data, APN and no-network requests. The updated project was imported in operation `01a15d4a-f5b1-7b94-b7d2-c1511a9b45b6` and compiled successfully.

The focused post-import test was temporarily blocked by Artemis's existing concurrent-session limit. Run that one message in a fresh chat after the limit clears; it should enter SIMIssueAgent and call `get_customer_sim_issues` with `CUST1001`, rather than enter UserDataPlan.

## Known limitation

The compiler still reports deterministic-parameter warnings for model-selected SIM tools and UserDataPlan handoff fields. They are nonblocking warnings; the scripted UserDataPlan gather and the tested SIM tool calls function. The next acceptance test must use a fresh session and send the customer ID only when UserDataPlan asks for it.
