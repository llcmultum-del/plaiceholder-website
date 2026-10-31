# BUILDER.md: the formula for building an agent

This is the procedure the worker (Claude Code in this folder) follows every time someone says
"build this agent for this company." It produces a tested, versioned delivery and nothing else.
Run it with `/build`, or by hand with `python kit.py build-request <request.yaml>`.

---

## Part A. The four inputs

Every build starts from one request file in `requests/`. Copy `requests/_TEMPLATE.yaml`.

| Input | Field in the request | Notes |
|---|---|---|
| 1. Which agent | `agent:` | A catalog slug (`python kit.py list`), or `custom` plus a `custom:` block |
| 2. The company | `client:` | `folder` and `name` are required; website, what they sell, ideal customer and contact make it better |
| 3. Connections | `connections:` (+ `connection_settings:`) | hubspot, salesforce, apollo, zendesk, slack, quickbooks, csv |
| 4. AI platform | `ai_platform:` (+ optional `model:`) | claude, chatgpt, perplexity, grok, gemini, copilot |

Optional: `tuning:` holds the discovery answers. To see which keys an agent takes, run
`python kit.py intake <agent>`. Anything left blank becomes a question in the build summary.
It never blocks the build.

**When the person gives free text instead of a file** (for example "build renewal risk for Beta Co, they use
Salesforce, Zendesk and Slack, on ChatGPT"):
1. Write `requests/<folder>-<agent>.yaml` from what they said.
2. Look up the company's public website to fill `what_they_sell` and `industry`. Mark any guess
   `# ASSUMPTION` in the YAML.
3. Never invent tuning numbers (points, tolerances, credit caps). Leave them blank so the template default
   is used and the gap shows up in the summary.
4. Show the person the request in five lines or fewer, then build. Ask before building only when a required
   field is missing or two inputs contradict each other.

---

## Part B. Decision tree

```
agent in catalog? ──yes──► Part D (catalog build)
       │
       no / "custom"
       │
template agents/<custom.slug> exists and version >= 1.0.0? ──yes──► Part D
       │
       no
       ▼
build-request writes requests/<client>-<slug>.spec.md and stops (exit 5)
       ▼
Part C (build the template), then run the request again ──► Part D
```

**Fit checks** run automatically and block the build:
- **Research agents** (`needs_web_search: true`) can't run automated on Gemini. Offer Claude, ChatGPT,
  Perplexity or Grok for automation. Gemini can still be the chat platform.
- **Copilot** gets chat files only. Automation stays on the client's other AI platform, or Claude.
- **Every role the agent needs** must be covered by a connection. Example: renewal-risk needs a CRM, and a
  help desk that can be the same CRM.

---

## Part C. Building a custom template (only when no template fits)

The goal is a new catalog-quality template. A one-off client agent is still built as a template, so it can
be maintained, upgraded and sold again.

1. **Scaffold** from the closest template (the spec names it):
   `python kit.py new-template <slug> --from <closest> --title "<Name>" --area "<Area>" --tier <Tier>`
   This creates a draft at version 0.1.0 with `TODO.md`. The builder refuses to deliver a 0.x template.
2. **Fill in the pattern** (Pull → Think → Check → Write back → Show and ask) in the spec's table. Each part
   must name a real connector role or a local step.
3. **agent.yaml**: summary, `needs`, `needs_web_search`, `pattern`, and `steps` with the right kind:
   `read` (free and safe), `local` (computes only), `spend` (costs money: AI calls or credits),
   `write` (changes a client system).
4. **settings.yaml**: generic defaults with "Your Company" placeholders. Every number someone might want to
   tune lives here, never in code.
5. **prompts/**: the AI asks for JSON only, and every claim must cite evidence (a link it found, a record id,
   or a row). Spell out what to do when there is no evidence: return nothing.
6. **steps.py**: one `step_<name>(ctx)` per step.
   - Use only `ctx.conn("<role>")` and `ctx.llm`. Never call an API directly.
   - Call `ctx.require("<step>", summary)` before every spend or write step, with a cost or change estimate.
   - Back up anything before overwriting it. Never delete client data.
   - Add a check step that throws out AI output not tied to real evidence (see `core/checks.py`).
   - Add `fake_responder(task)` so the demo runs without accounts, plus `status_summary(state)`.
   - Optionally add `intake_warnings(settings)` for consistency checks the worker shows in the summary.
7. **sample_data/**: realistic fake records, including the bad cases (a duplicate, a missing field, a record
   the AI should reject).
8. **intake.yaml**: map every client fact and tuning answer to a setting. Mark `live: true` for what must be
   known before going live.
9. **interview.md** (discovery questions) and **portable.md.j2**, with these sections: Your role,
   What you work on, Procedure, Rules you must follow, Scoring, Output format, Stop and ask.
   The short version must stay under 7,500 characters.
10. **Prove it**:
    - `python kit.py demo <slug>` runs clean, and the dashboard makes sense to a non-technical reader.
    - Add a test in `tests/run_tests.py`, then run `python tests/run_tests.py` and confirm all pass.
11. Add a `docs/CATALOG.md` entry, then set `version: 1.0.0`. Rerun the request (Part D).

New tool needed? Add a connector in `core/connectors/` on the base classes, stub routes in
`tests/stub_server.py`, the keys in `docs/KEYS.md` and `KEYS`, and the platform in `PLATFORM_ROLES`
(core/builder.py).

---

## Part D. Catalog build (what `build-request` does)

1. Validate the request (required fields, known tools, known AI platform).
2. Create or update `clients/<folder>/` only, then:
   - map connections to roles, set the AI platform and model, and save `connection_settings`;
   - save the company profile in `client.yaml`;
   - pin a private copy of the template.
3. Copy company info and tuning answers into `clients/<folder>/agents/<agent>.yaml` using the template's
   `intake.yaml`. New answers are merged over earlier ones; nothing earlier is wiped.
4. Build tests:
   - the template is finished;
   - config and AI-platform fit;
   - keys (a warning until the client adds them);
   - placeholders;
   - a full end-to-end run on sample data with the client's settings;
   - portable files render;
   - a secrets scan.
5. Write the delivery: `deliveries/<folder>/<agent>/vN/` plus a zip (AGENT.md, a file per platform, the
   runtime, TEST_REPORT, MANIFEST, CHANGELOG). Deliveries are immutable.
6. Write `BUILD_SUMMARY-vN.md` next to the delivery. It is internal and never zipped, and covers:
   - what was filled in;
   - questions to ask before going live;
   - things to look at;
   - defaults kept;
   - next steps.

**Exit codes:**
- 0: delivered
- 1: invalid request, or blocked
- 5: a custom template is needed (Part C)

---

## Part E. Quality bar (don't send unless every line is true)

- [ ] TEST_REPORT status is READY or READY FOR SETUP. Never send BLOCKED, and never use `--force` for a client.
- [ ] The client's platform file mentions the client's name and has no "Your Company" left.
- [ ] Every live-required question is answered, or listed for the setup call.
- [ ] Spend steps show a cost estimate and a cap. Write steps show what will change, and back it up first.
- [ ] Every AI claim must be tied to evidence, and a check step drops anything unsupported.
- [ ] No key values anywhere in the delivery (the secrets scan enforces this).
- [ ] Only `clients/<folder>/` and `deliveries/<folder>/` changed. `agents/` changes only in Part C.

---

## Part F. What the person gets back

Report in four lines or fewer:
- the status;
- the zip path, plus the single platform file the client needs (for example `platforms/chatgpt.md`);
- the open questions, if any;
- the next step: setup call, keys, then a 20-record pilot.

Don't recap the steps.

## Changing an agent later

- **One client:** edit their `tuning:` in the request (or use `/agent-edit`), then run `build-request` again.
  That makes vN+1, and `python kit.py diff` shows what changed.
- **Template improvement:** change `agents/<agent>/` and bump the version. Each client opts in with
  `python kit.py upgrade <client> <agent> --apply`, then rebuild.
