# SOP-01: Client onboarding (signed → ready to build)

**Goal:** everything needed to build is in hand within 2 business days of signing.
**Owner:** Founder · **Time:** about 1 hour of your time

## Trigger
MSA and SOW signed, first 50% invoice paid.

## Steps
1. **Create the client record**
   `python kit.py build <client> <agent> --platforms <tools> --ai <platform> --name "<Client Name>"`
   This creates `clients/<client>/`, pins the template, and produces a first sample-data build (status READY FOR SETUP). The build confirms the agent fits their tools and AI platform before you go further.
2. **Record the care plan:** `python kit.py care <client> --status active --tier <tier> --monthly <fee> --since <kickoff date>`.
3. **Send the kickoff email** (template below) with:
   - the list of keys to create, from the build's `.env.example`, with links to `docs/KEYS.md` steps
   - the discovery interview invite (1 hour, the people who do the task)
   - the pilot reviewer request (who checks the top 10 results)
4. **Collect keys safely.** The client creates each key in their own account. You enter it with
   `python kit.py set-key <client> <KEY>` (hidden typing) during a screen share, or the client enters it themselves.
   Never accept keys by email or chat.
5. **Confirm AI platform terms.** Note in the SOW notes which AI platform and plan they use, and whether its
   business/API terms exclude training on their data.
6. **Run the connection check:** `python kit.py check <client>` until every line says ok (placeholder warnings are expected until tuning).
7. **Book the discovery interview** and run it with `/agent-tune <client> <agent>` (see SOP-02 step 3).

## Kickoff email template
> Subject: Kickoff: your [Agent] with PlAIceholder
>
> Hi [Name], thanks for signing on. Three things get us moving:
> 1. **Access:** please create these keys in your accounts: [list]. Steps for each are attached. We'll enter them together on a 10-minute call; please don't email them.
> 2. **Discovery (1 hour):** [date options] with [the people who do the task]. We'll ask how you do it today; your answers become the agent's settings.
> 3. **Pilot reviewer:** who should check the first 20 results?
>
> Target: pilot results by [date], handover by [date]. [Founder Name]

## Done when
- [ ] `kit.py check` passes for every connection
- [ ] Discovery booked, pilot reviewer named
- [ ] Care plan recorded
# SOP-02: Building an agent (catalog or custom)

**Goal:** "this agent, for this company, connected to these platforms" becomes a tested delivery with one command.

## The model: one builder, many templates
We use **one builder** (`kit.py build`, or `/agent-build` in Claude Code), not a separate builder agent per agent type.

- **Templates hold the specialization.** Each catalog agent is a template in `agents/`: its steps, prompts, checks, scoring, chat-mode spec, interview and sample data.
- **The builder holds the process.** It sets up the client, connects tools, pins the template, tests and packages the same way for every agent.
- **Why not one builder per type:** 13 builders would drift apart, and every process improvement would have to be made 13 times. With one builder, a fix to testing or packaging improves every agent at once.
- **Custom agents** become a new template first (`/agent-new`), then go through the same builder. Many "custom" requests are a catalog template with different settings, so check that first.

## Inputs
| You need | Example |
|---|---|
| Agent template | `signal-prospector` (`python kit.py list`) |
| Client folder name | `acme` (lowercase, dashes, never starting with `_`) |
| Their tools | `hubspot,apollo` (also: salesforce, zendesk, slack, quickbooks, csv) |
| Their AI platform | `chatgpt` (also: claude, perplexity, grok, gemini, copilot) |

## Steps
1. **Build** (Claude Code: `/agent-build signal-prospector for acme using hubspot, apollo on chatgpt`):
   ```
   python kit.py build acme signal-prospector --platforms hubspot,apollo --ai chatgpt --name "Acme Corp"
   ```
   If it says **BLOCKED**, read the FAIL line. The usual cause is an AI platform that can't do something the
   agent needs: for example, Gemini can't run web-search research in automated mode. Pick another platform for
   the automated runtime, or deliver chat mode only.
2. **Keys:** follow SOP-01 step 4, then `python kit.py check acme`.
3. **Tune:** `/agent-tune acme signal-prospector`, the discovery interview. Answers go only to
   `clients/acme/agents/signal-prospector.yaml`.
4. **Prompt test:** `python kit.py test-prompt acme signal-prospector <a domain they know>`. It costs a few cents; walk through what was kept and thrown out.
5. **Rebuild after tuning:** `python kit.py build acme signal-prospector --note "Tuned from discovery"`. The status should now be READY, or READY FOR SETUP only because chat mode doesn't need keys.
6. **Pilot:** SOP-04.
7. **Deliver:** SOP-05.

## Custom agent (not in the catalog)
1. Write a one-paragraph spec: the job, tools in and out, what a person must approve, and what a wrong answer looks like.
2. Check whether an existing template with new settings would do. If so, use that.
3. Otherwise run `/agent-new <name> "<what it does>"`. Claude Code copies the closest template and adds a
   `fake_responder`, sample data, a `portable.md.j2` chat-mode spec and an end-to-end test.
4. Run `python tests/run_tests.py` until it passes, and `python kit.py demo <name>` to see the dashboard.
5. Then build for the client from step 1 above.
6. Price it: tier price plus $1,000 to $3,000 for the new template. It joins the catalog for the next client.

## Rules
- Never edit `agents/` (shared templates) to suit one client. Client-specific changes go in that client's settings file.
- Never pass `--force` unless you've read the failure and the client agrees in writing.
# SOP-03: Delivering on the client's own AI platform

**Goal:** an agent built with Claude works the same in ChatGPT, Perplexity, Grok, Gemini or Copilot, so the client doesn't need a new AI subscription.

## How portability works
Every agent has **one source of truth**: the template plus the client's tuned settings. The builder turns that into:

| File (in the delivery) | Use it for |
|---|---|
| `AGENT.md` | The full portable spec: role, inputs, procedure, rules, scoring, output format, when to stop. Plain markdown that any AI reads. |
| `platforms/claude-project.md` | Claude Project instructions (+ attach AGENT.md) |
| `platforms/claude-skill/SKILL.md` | Claude skill (Claude Code / Claude apps) |
| `platforms/chatgpt.md` | ChatGPT custom GPT or Project instructions (under 8,000 characters) + attach AGENT.md |
| `platforms/perplexity.md` | Perplexity Space instructions + attach AGENT.md |
| `platforms/grok.md` | Grok project / custom instructions + attach AGENT.md |
| `platforms/gemini.md` | Gemini Gem instructions + attach AGENT.md |
| `platforms/copilot.md` | Microsoft Copilot Studio agent instructions (under 8,000 characters) + knowledge |
| `platforms/api-system-prompt.md` | Developers: system prompt for any AI API |
| `runtime/` | Automated mode, using the client's AI platform's API key |

Each platform file starts with setup steps, then a "copy everything below this line" block. The short version is
kept under 7,500 characters, so it fits the instruction boxes on platforms with limits. The full spec rides along as AGENT.md.

## Two modes, and what each platform can do

| Platform | Chat mode | Automated mode (runtime) | Notes |
|---|---|---|---|
| Claude | ✓ | ✓ with web search, Batch API at half price | Default; cheapest for large research runs |
| ChatGPT (OpenAI) | ✓ | ✓ with web search | No batch discount in the kit; tasks run one by one |
| Perplexity | ✓ | ✓, always searches; returns citations | Best fit for research agents |
| Grok (xAI) | ✓ | ✓ with live search citations | Confirm search options in the live test |
| Gemini (Google) | ✓ (turn on Google Search in the Gem for research) | ✓ for non-research agents only | The builder blocks research agents on Gemini automated mode |
| Copilot | ✓ | ✗ (chat files only) | Runtime uses another platform if automation is needed |

**Chat mode** means a person gives the agent data (paste, attach, or the platform's own connectors to their CRM)
and reads the results. **Automated mode** runs on a schedule, reads from and writes back to their tools, and needs an API key.

## Steps
1. At kickoff, ask: "Which AI tool does your team already pay for, and do they want chat, automation, or both?"
2. Build with that platform: `--ai chatgpt` (or claude, perplexity, grok, gemini, copilot). The builder sets the runtime
   provider, clears the old model name, and blocks combinations that can't work.
3. Set the current model name for automated mode in `clients/<client>/client.yaml` under `llm.model`. Model names
   change; check the provider's model list. Defaults: Claude `claude-sonnet-5-5`, ChatGPT `gpt-5`, Perplexity `sonar-pro`,
   Grok `grok-4`, Gemini `gemini-2.5-pro`.
4. **Chat-mode install (on a screen share, 10 minutes):** open the platform file, follow its steps, paste the block, attach AGENT.md,
   turn on web search or data analysis as the file says, then run one real example together.
5. **Same-result check:** run 3 records in chat mode and the same 3 in automated mode (or the sample in AGENT.md).
   The scores and flags should match closely. Big gaps mean a platform setting (search off, file not attached) or a model that's too small.
6. Record the platform and model in the SOW notes. Rebuild with `--note` if anything changed.

## Writing templates that stay portable (for new agents)
- Use plain markdown only: headings, lists, tables, one fenced JSON block. No XML tags or tool-specific syntax.
- Fixed sections: **Your role · What you work on · Procedure · Rules you must follow · Scoring · Output format · Stop and ask a person when**. The builder fails a spec missing the core sections.
- Write rules as testable sentences ("No source, no signal"), not vibes.
- Never rely on a feature only one platform has. Say "if you can run code, use it for math" rather than naming a tool.
- Keep the short version under 7,500 characters. Long reference material (talk tracks, examples) goes in the full version only.
- Give an example input and output in the full version. It's the best way to make different models agree.

## Limits to tell clients plainly
- Different models give somewhat different wording and borderline scores. The rules and checks keep the results consistent, not identical.
- Chat mode depends on the person attaching the right data, and on the platform's search being turned on.
- Model names and platform menus change. The care plan covers re-testing when they do.
# SOP-04: Testing and QA

**Rule:** nothing goes to a client without a test report, and nothing goes live without a pilot.

## The four layers
| Layer | What it proves | How |
|---|---|---|
| 1. Kit tests | Code, connectors and AI platform adapters work as documented | `python tests/run_tests.py` (after any code change; all must pass) |
| 2. Build tests | This client's configuration, tuned settings and chat files work | Automatic in `kit.py build`, written to `TEST_REPORT.md` |
| 3. Live trial check | Real accounts accept our calls | Our own trial accounts, once per connector or platform, before the first client uses it |
| 4. Client pilot | The agent is useful for this client | 20 records, reviewed by the client |

## Build test checks (TEST_REPORT.md)
- Configuration and AI platform fit (FAIL blocks delivery)
- Client keys present (WARN until the client adds them)
- Settings tuned, with no placeholders (WARN until `/agent-tune`)
- End-to-end run on sample data with the client's settings and pinned template (FAIL blocks)
- Portable AGENT.md renders, the short version fits, and the core sections are present (FAIL blocks)
- Secrets scan: no key value anywhere in the delivery (the build is deleted if one is found)

## Live trial checklist (once per connector or platform)
- [ ] HubSpot developer test account · [ ] Salesforce Developer Edition · [ ] Apollo trial · [ ] Zendesk trial
- [ ] Slack test workspace webhook · [ ] QuickBooks sandbox
- [ ] AI platforms in use: Anthropic, OpenAI, Perplexity, xAI, Google (about $5 of credit each)
- For each: `kit.py check`, then `kit.py run <test-client> <agent> --limit 5 --live`. Fix anything, add a stub test, and record the date here.

## Pilot (per client)
1. `python kit.py run <client> <agent> --limit 20` (dry run), then add `--live` and approve each step.
2. The client's reviewer marks each of the top 10 results useful or not useful.
3. Check every finding links to its source or evidence, and look at the verify audit file.
4. Time 10 records done the old way against reviewing the agent's output. Record the minutes per record.
5. Record the usage cost per record from the run summary.
6. Accept against the SOW criteria, or tune and re-pilot once.

## Record the result (it's your case study)
| Client | Agent | Records | Useful (top 10) | Minutes/record before → after | Cost/record | Date |
|---|---|---|---|---|---|---|
# SOP-05: Delivery and handover

**Goal:** the client owns a working agent, knows how to use it, and has moved onto the care plan.

## How we sell and maintain an agent we hand over
We hand over the agent: the client keeps the files and runs them in their own accounts. We can't lock a copy
of plain files, and we don't try to. Three things protect the business instead:

1. **The license (legal).** The MSA grants an internal-use license once the launch package is paid. No resale,
   no sharing, no competing use. If the launch package isn't paid, there's no license. Enforcement is contractual, like any software license.
2. **The service (value).** What keeps clients paying is the care plan, not access to the files. Tools and AI
   models change every few months and agents slowly break or drift. The care plan includes monitoring, fixes,
   model moves, tuning, a monthly results report and the fix guarantee.
3. **Being the easiest path.** Settings history, the pinned template, versioned deliveries and our test setup
   make us much faster at fixing their agent than anyone else would be.

## Steps
1. **Final build:** `python kit.py build <client> <agent> --note "Pilot accepted"`. The status must be READY.
2. **Send the delivery zip:** `deliveries/<client>/<agent>/<client>-<agent>-vN.zip`, by a shared drive link or an email attachment.
   It contains no keys.
3. **Install with them (30-minute training call):**
   - Chat mode: open `platforms/<their platform>.md`, follow the steps, paste the block, attach AGENT.md, and run a real example.
   - Automated mode: they unzip `runtime/`, add keys (`set-key`), run `check`, then the schedule or `/agent-run`.
   - Show the dashboard, how to read it, and what needs a person's approval.
4. **Remove our setup access:** delete `clients/<client>/.env` and `runs/` and any local exports. Ask the client to
   rotate any key we used during the build.
5. **Set up care access:** the client creates a separate, limited credential for care work (for example a dedicated
   integration user). Store it encrypted. They can revoke it at any time.
6. **Send the handover email** (template below) and the second 50% invoice.
7. **Set the care plan's month-4 start date:** `python kit.py care <client> --status active --since <handover date>`.

## Handover email
> Subject: Your [Agent] is live: results and next steps
>
> Hi [Name],
> - **Pilot result:** [X of 10 useful], [minutes before → after] per record, ~$[cost] per record in AI usage.
> - **Your files:** [link]. Start with README.md. They're yours to use internally under our agreement.
> - **Care plan:** months 1 to 3 are included. I'll send your first results report on [date]. From month 4 it's $[fee]/mo, cancel anytime with 30 days' notice.
> - **Access:** I've removed my setup access. Please send the limited care-plan login when you can (steps attached).
>
> Thanks, [Founder Name]

## Done when
- [ ] Client ran the agent themselves once
- [ ] Our setup keys and data deleted; the client confirmed key rotation
- [ ] Care credential received
- [ ] Final invoice sent; testimonial requested (founding clients)
# SOP-06: Maintenance, edits and versioning

**Goal:** change one client's agent quickly without ever touching another client's.

## How the files are organized
```
agents/<agent>/                      shared templates (the catalog). Only changed on purpose, with tests.
clients/<client>/
    client.yaml                      tools, AI platform, care plan, delivery history
    .env                             care-plan credential only (never shared)
    agents/<agent>.yaml              THIS client's tuned settings  ← most edits happen here
    pinned/<agent>/                  THIS client's private copy of the template (frozen at their version)
    runs/                            logs (deleted at handover)
deliveries/<client>/<agent>/
    v1/ v2/ v3/ …                    immutable deliveries; never edited
    CHANGELOG.md                     what changed in each version
    <client>-<agent>-vN.zip          the file you send
```

### The four safety rules
1. **Every command names one client.** `build`, `run`, `diff`, `upgrade` and `care` only touch that client's folders.
2. **Pinned templates.** Each client runs its own frozen copy of the template, so improving a shared template
   never changes a delivered client by accident.
3. **Immutable versions.** A change is a new version (vN+1) with a changelog note. The previous version stays for rollback.
4. **Tests on every build.** A rebuild re-runs the full sample-data test with that client's settings before anything is delivered.

## Monthly care routine (per client, about 30 to 60 minutes)
The agent runs in the client's systems, so monitoring comes from three places:
1. **Health check with the care credential:** `python kit.py check <client>`, then a dry run on 5 records:
   `python kit.py run <client> <agent> --limit 5`. A dry run reads live data but writes and spends nothing,
   and confirms their tools still answer and every step still works.
2. **Their run summaries:** ask clients on automated mode to add your email to the agent's Slack channel, or forward
   the run summary. Look for failures, rising cost per record, and a jump in thrown-out findings in the verify audit
   (a sign of drift).
3. **Chat-mode clients:** run the 3-record same-result check (SOP-03 step 5) on their platform with sample data.

Then:
4. Send the monthly results email: what ran, key findings, cost per record, anything fixed.
5. Note any tuning requests and use the plan's tuning hours.

## Making a change for one client
Claude Code: `/agent-edit <client> <agent> "<what to change>"`. By hand:
1. Edit **only** `clients/<client>/agents/<agent>.yaml`. Only edit `clients/<client>/pinned/<agent>/` if a setting can't express the change.
2. `python kit.py build <client> <agent> --note "<what changed>"` creates vN+1, tested.
3. `python kit.py diff <client> <agent>` shows exactly what changed. Check that only what you intended changed.
4. Send the new zip. Chat mode: they replace the instructions block and AGENT.md. Automated: they replace the runtime folder and keep their `.env`.
5. **Rollback:** resend the previous version's zip.

## When a tool or AI model changes (the fix guarantee: 5 business days)
1. Reproduce it on a test client, then fix it in `core/` (connectors, AI adapters) and add a stub test. Run `python tests/run_tests.py`.
2. `core/` fixes reach clients when you rebuild them: `python kit.py build <client> <agent> --note "Fix: <tool> change"`.
   Rebuild every affected client with an active care plan (`python kit.py clients` lists who uses what).
3. Model retired? Update `llm.model` in each affected client's `client.yaml`, rebuild, and re-run the same-result check (SOP-03 step 5).

## Improving a shared template (all future clients)
1. Change `agents/<agent>/`, bump `version` in its `agent.yaml`, and run the tests.
2. Existing clients don't change. For each one who should get it: `python kit.py upgrade <client> <agent>` (preview), then
   `--apply` (keeps a backup and their settings), then `build --note "Upgrade to template vX"`.
3. Clients without a care plan stay on their version unless they pay for the upgrade.

## Never
- Edit a delivered `vN` folder.
- Change shared templates to fix one client.
- Run commands on a client folder you didn't name.
# SOP-07: Offboarding (cancellation or non-payment)

**Principle:** we never switch off or delete anything in a client's systems. Their license survives (once the
launch package is paid). What ends is our service and our access.

## Case A: the client cancels the care plan (30 days' notice)
1. Acknowledge in writing: the end date, that the agent stays theirs to use internally, and what's no longer
   covered (monitoring, fixes when tools change, tuning, model moves).
2. Offer the alternatives once, without pressure: annual prepay (2 months free), a lower tier, or on-call help at $125/hour.
3. On the end date: `python kit.py care <client> --status ended`. It prints this checklist:
   - [ ] Ask the client to revoke the care-plan credential, and confirm it's done
   - [ ] Delete `clients/<client>/.env`, `runs/` and any exports
   - [ ] Resend the latest delivery zip and handover notes
   - [ ] Remind them of the hourly and reactivation rates
   - [ ] Keep `clients/<client>/` settings, pinned template and delivery history (no client data) for a fast reactivation
4. Calendar a friendly check-in for 90 days later. A tool change has often broken something by then.

## Case B: care plan invoice unpaid
| Days late | Action |
|---|---|
| 1 | Automatic reminder |
| 7 | Personal email |
| 15 | Care services paused (per Care Plan Terms). Written notice; the agent keeps running |
| 30 | Care plan ended, then Case A steps 3 and 4. Unpaid amounts go to normal collections |

We don't disable the agent for an unpaid care plan. It's a service, not a license.

## Case C: launch package unpaid after delivery
1. Reminders on day 1, 7 and 15.
2. Day 30: formal written notice that no license was granted (MSA 3.4), and that they must stop using and delete the agent within 10 days.
3. Revoke any access we still hold. Don't access their systems to delete anything yourself.
4. If unresolved, take it to an attorney or small-claims court. The signed MSA/SOW and the delivery MANIFEST (dates, versions) are your evidence.

## Reactivation
1. The client pays the reactivation fee ($500 / $750 / $1,000) and restarts the care plan.
2. They create a new care credential, and you run `kit.py check`.
3. `python kit.py upgrade <client> <agent>` (if templates moved on), then `build --note "Reactivation"`, then a short re-pilot.
4. `python kit.py care <client> --status active`.
