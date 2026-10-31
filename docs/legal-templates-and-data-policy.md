# Care Plan Terms (Exhibit A, template)

> Template, not legal advice. Review with an attorney before use.

## 1. What the Care Plan is
A monthly service that keeps a delivered Agent working and improving. The Agent itself belongs to
Client under the license in the MSA; the Care Plan is the people and process around it.

## 2. Included each month
| | Starter | Standard | Advanced |
|---|---|---|---|
| Fee (from month 4) | $250 | $450 | $750 |
| Monitoring of runs and costs | ✓ | ✓ | ✓ |
| Monthly results email | ✓ | ✓ | ✓ |
| Fixes when a connected tool or AI model changes | ✓ | ✓ | ✓ |
| Moves to newer AI models when the current one is retired | ✓ | ✓ | ✓ |
| Tuning hours (prompts, scoring, settings) | 1 | 2 | 3 |
| Quarterly tuning call | | ✓ | ✓ |
| Response time | 2 business days | 2 business days | 2 business days |

Unused tuning hours don't roll over.

## 3. Fix guarantee
If a change in a connected third-party tool breaks the Agent, Provider will restore it within 5 business days
of being told (or of detecting it). If Provider misses that, the Care Plan fee for that month is waived.
This doesn't apply when the cause is Client revoking access, an account lapsing, or a third-party outage.

## 4. Access
Client gives Provider a **separate, limited credential** (for example a dedicated integration user or API key)
used only for Care Plan work. Client can revoke it at any time. Provider stores it encrypted and uses it only
for monitoring, fixes and approved changes.

## 5. Not included
New agents or new kinds of tasks, new tool connections, data cleanup, work during third-party outages,
and changes beyond the included tuning hours (billed at $125/hour or quoted).

## 6. Term, cancellation and lapse
- Months 1 to 3 are included in the launch package (6 months committed for founding clients).
- After that, month to month. Either party may cancel with 30 days' written notice.
- Unpaid Care Plan invoices more than 15 days late pause Care Plan services (not the Client's license).
- When the Care Plan ends: Client revokes the Care Plan credential, Provider deletes Client data and keys it holds,
  and the Agent keeps running in Client's systems under the license, without monitoring or fixes.
- **Reactivation:** restarting care after a lapse costs a one-time reactivation fee ($500 / $750 / $1,000 by tier),
  which covers re-testing and repairing the Agent, then the monthly fee resumes.

## 7. Annual prepay
Paying 12 months in advance costs 10 months' fees. Refunds on early cancellation are pro-rated at the monthly rate.
# Data Handling and Security Policy (Exhibit B)

Version 1.0 · October 2026 · Owner: [Founder Name]

## Principles
1. **Client data stays in client systems.** Agents run in the client's accounts with the client's keys.
2. **Least access, shortest time.** We get only the access a step needs, and give it back when done.
3. **Nothing leaves the delivery that shouldn't.** Every build scans its files for secrets and refuses to deliver if it finds one.
4. **Humans approve.** Agents draft, score and flag; people send, pay and decide.

## What we access, when
| Phase | Access | Where it lives | Removed when |
|---|---|---|---|
| Build and pilot | Client-created API keys for the tools in the SOW | `clients/<client>/.env` on Provider's encrypted laptop; never in email or chat | Handover |
| Pilot data | Records pulled during the pilot (logs, results, backups) | `clients/<client>/runs/` on the same laptop | Handover (deleted) |
| Care Plan | One limited, revocable credential | Password manager / encrypted `.env` | Care Plan ends, or client revokes it |
| After the Care Plan | None | None | n/a |

## Key handling
- Keys are typed with hidden input (`kit.py set-key`); they're never pasted into chats, emails or documents.
- Keys are never committed to version control (`.gitignore` excludes every `.env`).
- Deliveries contain a `.env.example` with key **names** only. The builder scans for key **values** and stops if it finds one.
- We ask clients to create keys with the narrowest permissions the agent needs (see `docs/KEYS.md`), and to set spending limits on AI platforms.

## Devices and accounts
- Full-disk encryption, a screen lock, and automatic OS updates on every device that touches client data.
- Multi-factor authentication on email, code hosting, password manager and every provider account.
- Client folders are kept separate: one folder per client, with no shared data between clients.

## AI platforms
- The client chooses the AI platform and holds the account; data is processed under that provider's business/API terms.
- Major providers publish terms for their API and business products, including whether data is used for training. Confirm the current terms for the client's chosen provider during kickoff and record it in the SOW notes.
- Agents send the AI only the fields a task needs (for example ticket text, not payment details).

## Retention and deletion
- At handover we delete the client's `.env`, `runs/`, exports and any local copies, and confirm it in writing.
- We keep the client's settings, pinned template and delivery history (no client records or keys) so care and reactivation are fast. On request, we delete those too.

## Incidents
If we suspect a key or client data was exposed, we:
1. revoke or ask the client to rotate the affected keys immediately;
2. tell the client within 72 hours of discovery, with what happened, what was affected and what we did;
3. write a short postmortem and fix the cause.

## Review
Reviewed every 6 months, and whenever we add a new tool or AI platform.
# Master Services Agreement (template)

> **Template, not legal advice.** Have a licensed attorney in your state review and adapt
> this before first use. [Bracketed text] is filled in per client.

This Master Services Agreement ("Agreement") is entered into on [Date] between
**[Legal entity name] d/b/a PlAIceholder** ("Provider"), [address], and **[Client legal name]**
("Client"), [address].

## 1. Services
1.1 Provider will build, configure, test and deliver AI agents ("Agents") and provide related
services as described in one or more Statements of Work ("SOW"). Each SOW is governed by this Agreement.
1.2 Optional ongoing support ("Care Plan") is governed by the Care Plan Terms (Exhibit A).

## 2. Fees and payment
2.1 Client pays the fees in each SOW. Unless the SOW says otherwise: 50% of the launch package at
signing, 50% at handover. Care Plan fees are billed monthly in advance.
2.2 Invoices are due within [15] days. Late amounts accrue interest at the lesser of 1.5% per month or
the maximum legal rate.
2.3 **Third-party usage costs** (AI platforms such as Anthropic, OpenAI, Perplexity, xAI or Google; data
providers such as Apollo; and Client's software subscriptions) are paid by Client directly to those providers
and are not part of Provider's fees.

## 3. Ownership and license
3.1 **Provider materials.** Provider owns its pre-existing and generally applicable materials,
including agent templates, the agent kit software, prompts, scoring frameworks, documentation and know-how,
and any improvements to them ("Provider Materials").
3.2 **Client materials.** Client owns its data, its systems, the settings tuned for Client, and the outputs the
Agents produce for Client ("Client Materials").
3.3 **License to Client.** Upon payment in full of the applicable launch package, Provider grants Client a
perpetual, non-exclusive, non-transferable, non-sublicensable license to use, copy and modify the delivered
Agent (including the Provider Materials embedded in it) **solely for Client's internal business purposes**.
Client may not sell, resell, distribute, publish, or provide the Agent or Provider Materials to third parties,
or use them to offer competing services. The license survives termination of any Care Plan.
3.4 **Unpaid delivery.** If the launch package is not paid in full, no license is granted and Client must stop
using and delete the Agent within 10 days of written notice.
3.5 **Reuse.** Provider may reuse Provider Materials, including improvements made during Client's project, for
other clients, but never Client Materials or Client's Confidential Information.

## 4. Client responsibilities
Client will: (a) provide timely access, accounts and API keys it controls; (b) make a knowledgeable person
available for the discovery interview and pilot review; (c) ensure it has the right to process the data it
connects; (d) keep its keys secure and revoke Provider's access when no longer needed; (e) review Agent outputs
before acting on them.

## 5. AI outputs
5.1 Agents use third-party AI models that can produce incomplete or incorrect results. Agents are designed to
draft, score and flag, with human approval before sending communications, changing records or making payments.
5.2 Client is responsible for decisions made using Agent outputs, including decisions about customers,
vendors, payments and hiring, and for complying with laws that apply to those decisions (including any
rules on automated decision-making in employment).

## 6. Confidentiality and data
6.1 Each party will protect the other's Confidential Information with reasonable care and use it only to
perform under this Agreement.
6.2 Provider will handle Client data per Provider's Data Handling and Security Policy (Exhibit B), including
deleting Client data and Provider's copies of keys at handover, and keeping only a limited, Client-revocable
credential while a Care Plan is active.

## 7. Warranties
7.1 Provider will perform services in a professional and workmanlike manner. Each Agent is tested on sample
data and piloted on up to [20] records before full delivery; if the pilot results do not meet the acceptance
criteria in the SOW, Provider will revise the Agent or, at Client's option, end the SOW and refund the second
50% payment.
7.2 EXCEPT AS STATED IN THIS SECTION, SERVICES AND AGENTS ARE PROVIDED "AS IS". PROVIDER DOES NOT WARRANT
UNINTERRUPTED OPERATION OR ERROR-FREE AI OUTPUTS, OR THE AVAILABILITY OF THIRD-PARTY SERVICES.

## 8. Limitation of liability
Neither party is liable for indirect, incidental, special or consequential damages or lost profits. Each
party's total liability under this Agreement is limited to the fees Client paid Provider in the 12 months
before the claim. These limits do not apply to breach of confidentiality, Client's payment obligations, or
breach of Section 3.3.

## 9. Term and termination
9.1 This Agreement continues until terminated. Either party may terminate it with 30 days' written notice
when no SOW is in progress.
9.2 Either party may terminate an SOW for material breach not cured within 15 days of notice.
9.3 **Effect of termination.** Provider's access is removed; Provider deletes Client data and keys it holds;
paid-in-full licenses survive; unpaid fees become due. Sections 2, 3, 5, 6, 8, 9.3 and 10 survive.

## 10. General
Provider is an independent contractor. Neither party may assign this Agreement without consent, except to a
successor of its business. [Founding clients only: Client agrees Provider may name Client and publish the
measured pilot result and an approved testimonial.] Governing law: [State]. Venue: [County, State]. This
Agreement, its SOWs and exhibits are the entire agreement; changes must be in writing.

**Exhibit A:** Care Plan Terms (CARE_PLAN_TERMS.md) · **Exhibit B:** Data Handling and Security Policy

| Provider | Client |
|---|---|
| Name: | Name: |
| Title: | Title: |
| Signature / date: | Signature / date: |
# Statement of Work #[N] (template)

Under the Master Services Agreement dated [Date] between [Legal entity name] d/b/a PlAIceholder and [Client legal name].

## 1. Agent
| | |
|---|---|
| Agent | [Signal Prospector / Renewal Risk Radar / Invoice Checker / custom: name] |
| Tier | [Starter / Standard / Advanced] |
| Job it does | [one sentence from the catalog, tuned to Client] |
| Client tools connected | [e.g. HubSpot, Apollo, Slack] |
| AI platform | [Claude / ChatGPT / Perplexity / Grok / Gemini / Copilot (chat mode only)] |
| Modes delivered | [Chat mode files for the AI platform above] and/or [automated runtime] |
| Records in scope | [e.g. up to 1,000 companies per month] |

## 2. Deliverables
1. Discovery interview (1 hour) and tuned settings.
2. Agent delivery package: AGENT.md, ready-to-paste files for Client's AI platform, automated runtime (if in scope), test report, changelog.
3. Pilot on up to 20 records, with results reviewed by Client.
4. Measured result: time per record before and after, and AI/data cost per record.
5. 30-minute training session and handover notes.
6. Care Plan, months 1 to 3 (included in the launch package).

## 3. Pilot acceptance criteria
The pilot is accepted when **[e.g. at least 7 of the top 10 results are judged useful by Client's reviewer, and every finding links to its source/evidence]**. If it isn't, Provider revises and re-pilots once. If the second pilot doesn't meet the criteria, Client may end this SOW and the second payment isn't owed.

## 4. Timeline (target)
| Step | Target date |
|---|---|
| Kickoff and access | [date] |
| Discovery interview | [date] |
| Pilot results | [kickoff + ~7 business days] |
| Handover and training | [kickoff + ~10 business days] |

## 5. Fees
| Item | Amount |
|---|---|
| Launch package ([tier], includes 3 months of care) | $[2,250 / 4,850 / 8,250] |
| Discounts ([founding client / second agent 25%]) | -$[ ] |
| **Total** | **$[ ]**, 50% at signing, 50% at handover |
| Care Plan from month 4 | $[250 / 450 / 750] per month, month to month, 30 days' notice |
| Estimated usage (paid by Client to providers) | ~$[ ] per [record], measured in the pilot |

## 6. Assumptions
- Client's data is reasonably clean. Cleanup is quoted separately at $125/hour.
- Client creates and controls all accounts and API keys.
- Client provides a reviewer for the pilot within 3 business days.
- Third-party tools keep providing the access used at kickoff.

## 7. Out of scope
New agent types, additional tools beyond those listed, data migration, custom dashboards beyond the agent's standard one, and changes after acceptance (covered by the Care Plan tuning hours or quoted separately).

| Provider | Client |
|---|---|
| Signature / date: | Signature / date: |
