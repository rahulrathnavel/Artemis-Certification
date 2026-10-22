# Telecom Multi Agent Project Standard Operating Procedure

## Purpose

This project provides telecom support through a Supervisor and three specialist agents. Customers can browse prepaid and postpaid top-up plans, retrieve plans that match a customer account, and investigate SIM issues. The service is read-only: it does not purchase plans, recharge accounts, or modify customer or SIM records.

## Project architecture

`Telecom_Supervisor` is the entry agent and welcomes the customer. It routes each supported request to the appropriate specialist:

- `TopUpPlan_Query_Agent` handles general prepaid, postpaid, and comparison queries.
- `UserDataPlan` is a flow-based agent that validates a Customer ID, retrieves the customer account type, and displays matching plans.
- `SIMIssueAgent` handles SIM issue catalogue requests, issue details, troubleshooting, and customer SIM history.

## Data sources and tools

| Use | Source |
| --- | --- |
| All top-up plans | `GET https://telecom-customer-data.onrender.com/dataTopUp` |
| Prepaid plans | `GET https://telecom-customer-data.onrender.com/dataTopUp/prepaid` |
| Postpaid plans | `GET https://telecom-customer-data.onrender.com/dataTopUp/postpaid` |
| Customer records | `GET https://telecom-customer-data.onrender.com/customers` |
| Account-matched plans | `GET https://telecom-customer-data.onrender.com/dataTopUp/{{account_type}}` |
| SIM support | MCP service at `https://telecom-mcp.vercel.app/api/sim-issue` |

## Operating workflows

### General top-up plans

Identify the requested category, retrieve the corresponding catalogue, and answer only from returned tool data. Preserve prepaid or postpaid context across follow-ups. Apply customer filters such as budget, data allowance, and validity to the retrieved records. Do not invent prices, benefits, validity, or account features.

### Account-matched plans

Request a Customer ID in the format `CUST` followed by exactly four digits, such as `CUST1001`. Validate the value, find the unique customer record, read its actual `account_type`, and retrieve the matching plan catalogue. If the ID is invalid or no customer is found, explain the problem and request a valid existing ID. A request for a different customer starts a new lookup and must not reuse the previous customer’s identity or account type.

### SIM support

Use the SIM MCP tools for the issue catalogue, issue details, troubleshooting guidance, and previously reported customer issues. Clarify an ambiguous symptom. Request a Customer ID before account-specific SIM history. Checking an issue does not represent a repair or account change.

## Guardrails

The project-level LLM guardrail permits telecom support, including plans, accounts, Customer IDs, mobile-data failures, APN settings, no-network symptoms, and SIM issues. It blocks unrelated topics such as politics, religion, and sensitive personal-belief advice. Agent-level LLM guardrails block abusive language while allowing ordinary frustration and complaints.

## Evaluation assets

The project contains two end-user personas, realistic telecom scenarios, and LLM-judge evaluators for response quality and tool correctness. The submission includes the completed evaluation screenshot and the supporting conversation, routing, and tool evidence. Evaluation credentials remain in Artemis and are not included in the project export.

## Deployment

The project is deployed to the Development environment with `Telecom_Supervisor` as the entry agent. The active deployment is labelled `Telecom Supervisor 1.0.1` and includes `TopUpPlan_Query_Agent` 1.0.0, `UserDataPlan` 1.0.0, and `SIMIssueAgent` 1.0.0. Deployment preflight completed successfully for all four agents. The web channel and live preview link are recorded in the submission README.

## Evidence and submission contents

The submission package contains:

1. This SOP.
2. The Gradious project export with Evals excluded from the export layers.
3. The completed Evals output screenshot.
4. End-user conversation screenshots showing the web experience, routing, tool calls, and guardrail behavior.
5. Supervisor conversation and debug-trace JSON files demonstrating multi-agent orchestration.
6. Configuration screenshots for the Supervisor, specialist agents, tools, routing, and guardrails.

The evidence files are retained in their numbered folders so a reviewer can inspect the project configuration, runtime behavior, and evaluation result independently.
