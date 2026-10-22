# Telecom multi-agent project — standard operating procedure

## Purpose

Provide general telecom top-up browsing, plans matched to a customer's actual account type, and SIM issue information. The service does not purchase recharge products or modify SIM records.

## Architecture

Telecom_Supervisor welcomes the customer and routes general plan queries to TopUpPlan_Query_Agent, account-specific lookups to UserDataPlan, and SIM support to SIMIssueAgent. Specialists use their assigned tools and return after the current task. A new customer message may start another supported task.

## Tools and data

| Service | Tool/source |
| --- | --- |
| All top-up plans | GET `https://telecom-customer-data.onrender.com/dataTopUp` |
| Prepaid plans | GET `https://telecom-customer-data.onrender.com/dataTopUp/prepaid` |
| Postpaid plans | GET `https://telecom-customer-data.onrender.com/dataTopUp/postpaid` |
| Customer record | GET `https://telecom-customer-data.onrender.com/customers`, using the supplied customer ID |
| Matching plans | GET `https://telecom-customer-data.onrender.com/dataTopUp/{{account_type}}`, using the value retrieved from the customer record |
| SIM support | MCP `https://telecom-mcp.vercel.app/api/sim-issue`: list issues, get issue by title, get issue details by ID, and get customer SIM history |

## General plan workflow

Resolve whether the customer requested prepaid, postpaid or a comparison. Retrieve the appropriate catalog. Preserve the requested type across follow-up requirements unless the customer changes it. Compare prices, data and validity with the requested criteria. State which requested benefits cannot be verified. Keep benefits associated with the category that returned them. Do not infer monthly recurrence, calling or SMS from a data allowance or price.

## Account-specific workflow

Ask for a Customer ID matching `^CUST[0-9]{4}$`. Validate it, retrieve its unique customer record and extract the actual account type. Retrieve matching plans using that type. Handle invalid IDs, missing customers, unsupported account types, empty results and service failures explicitly. A different-customer request must not reuse the previous customer's identity or account type.

## SIM workflow

Use the read-only MCP tools to find the applicable issue and return the supplied symptoms, causes, troubleshooting and escalation information. Clarify ambiguous symptoms. Obtain a customer ID before requesting account-specific issue history. Checking an issue is not confirmation of a repair.

## Guardrails

An active project input LLM check restricts the conversation to telecom support and rejects politics, religion and sensitive personal-belief discussions. Each agent also has an input LLM check for abuse. Normal frustration is not automatically abuse. Required guardrail acceptance tests cover both new chats and active flows, including recovery after a blocked turn.

## Evaluation

Run both Everyday_Telecom_Customer and Detail_Oriented_Customer through General_And_Account_Matched_Plans and SIM_Support_And_Service_Switching, with one variation and both LLM judges. This produces four conversations and eight judgments. Run with concurrency one initially. Preserve raw failures and review tool evidence and transcripts; a judge verdict may itself be incorrect.

The personal trial keeps Mistral for the assistant agents. Evidence-grounded v2 evaluators use a separately configured Gemini connection for independent assessment. Model credentials remain in Artemis and are not included in this SOP.

Current validation status: the independent small diagnostic and positive evaluator calibration passed. The complete four-conversation/eight-judgment run failed, and the subsequent account-switching diagnostic failed. Further Evals starts in the personal workspace are blocked by its 10-run billing-window allowance. This SOP remains a draft; these results do not establish release readiness.

## Deployment and release

Publish the verified agent versions, deploy the project to a web channel with Telecom_Supervisor as its entry agent, and verify the actual end-user experience. Capture the welcome, plan query, account lookup and SIM support. Save the deployment identifier and screenshots after this step succeeds. Deployment has not yet been recorded in this draft.

## Submission package

Include this finalized SOP, the final project ZIP with Evals excluded, a screenshot of the full evaluation output, an actual end-user web-conversation screenshot and a Supervisor conversation transcript demonstrating multi-agent orchestration. Record unresolved limitations honestly rather than presenting a diagnostic pass as full completion.
