# Claude Cowork for Email Marketing
**Course Code:** TGS-2020503109
**Version:** v14.0
**TSC:** ICT-SNM-3006-1.1 Integrated Marketing
## Learning outcomes
- LO1 Propose email marketing strategies to address intended objectives and target customers.
- LO2 Manage newsletter audiences for a particular market segment.
- LO3 Develop effective email campaigns to meet an email campaign objective.
- LO4 Automate marketing processes to improve efficiency.
- LO5 Evaluate campaign effectiveness using analytics reports.

## End-to-end architecture
1. Business objective, customer behaviour and metric hierarchy
2. Consent-aware audience and segment contract
3. Campaign brief, approved sources and brand constraints
4. Grounded Cowork drafting and reusable Skill
5. Least-privilege connector workflow and human approval
6. Reconciled campaign metrics and experiment evidence
7. Owned optimisation decision and review date

## Topic 1: Email Marketing Strategy and Campaign Planning with Claude Cowork

Translate business objectives and customer evidence into a consent-aware lifecycle campaign brief that Claude Cowork can execute and a marketer can verify.

### Email as an owned relationship channel

**Mechanism:** Earn consent → Deliver value → Observe response → Deepen relationship
**Fields:** permission, promise, engagement, next_value
**Measure:** Permission, reach, conversion and lifetime-value contribution
**Control:** Value the address only when permission, purpose and retention remain traceable.
**Evidence:** Channel comparison and consent provenance

### Objective-to-metric hierarchy

**Mechanism:** State outcome → Choose behaviour → Select KPI → Set guardrail
**Fields:** business_goal, behaviour, primary_kpi, guardrail
**Measure:** One primary KPI with counter-metrics
**Control:** Connect campaign activity to a customer action and business outcome.
**Evidence:** Objective tree with metric definitions

### Lifecycle and drip architecture

**Mechanism:** Map stage → Define trigger → Deliver message → Advance state
**Fields:** stage, trigger, message_job, exit_rule
**Measure:** Progression and drop-off by lifecycle stage
**Control:** Give every email one job, entry rule and exit condition.
**Evidence:** Lifecycle map and suppression logic

### Lead magnet value exchange

**Mechanism:** Find tension → Offer utility → Request minimum data → Fulfil promise
**Fields:** pain_point, asset, fields, delivery
**Measure:** Qualified opt-in and downstream engagement
**Control:** Match the asset to an immediate audience problem and ask only for needed fields.
**Evidence:** Lead-magnet hypothesis and consent copy

### Claude Cowork task model

**Mechanism:** Grant scope → State outcome → Observe actions → Review artifact
**Fields:** folder, instructions, tool_actions, deliverable
**Measure:** % tasks whose artifacts meet the declared acceptance contract
**Control:** Delegate an artifact-producing task with boundaries and verification.
**Evidence:** Task record, artifact and review decision

### Campaign brief as control plane

**Mechanism:** Load context → Resolve audience → Define offer → Declare constraints
**Fields:** brand, segment, offer, constraints
**Measure:** % required brief fields complete before drafting
**Control:** Require explicit unknowns, sources and an approval owner.
**Evidence:** Validated campaign brief and assumption log

### Channel and platform selection

**Mechanism:** List needs → Score options → Check integration → Select fit
**Fields:** need, criteria, connector, decision
**Measure:** Weighted fit across capability, cost, control and evidence
**Control:** Score the channel and execution platform against the campaign contract.
**Evidence:** Platform decision matrix with rejected alternatives

### Compliance and trust boundaries

**Mechanism:** Capture consent → Limit purpose → Protect data → Honour exit
**Fields:** consent_at, purpose, retention, unsubscribe
**Measure:** % records with auditable consent and suppression status
**Control:** Block activation when consent, identity or unsubscribe state is uncertain.
**Evidence:** Consent ledger and pre-send gate

## Topic 2: Audience Management, Segmentation and Personalisation

Create a clean, consent-aware audience model and use meaningful segment evidence to personalise messages without exposing sensitive customer data.

### Audience data contract

**Mechanism:** Collect field → Define meaning → Validate value → Assign owner
**Fields:** field, definition, allowed_value, owner
**Measure:** % audience fields with definition, source and lawful purpose
**Control:** Maintain a minimal dictionary and reject ungoverned attributes.
**Evidence:** Audience schema and data-quality report

### Contact status lifecycle

**Mechanism:** Subscribe → Engage → Suppress → Archive
**Fields:** status, source, changed_at, reason
**Measure:** Status transitions with no prohibited sends
**Control:** Use a single authoritative suppression state before every release.
**Evidence:** Status transition ledger

### Bounce and deliverability logic

**Mechanism:** Attempt delivery → Classify bounce → Update status → Protect sender
**Fields:** smtp_result, bounce_type, retry_rule, suppression
**Measure:** Delivery rate, hard-bounce rate and complaint rate
**Control:** Retry temporary failures selectively and suppress permanent failures promptly.
**Evidence:** Bounce decision table and list-health trend

### Segmentation model

**Mechanism:** Choose signal → Write rule → Preview members → Activate cohort
**Fields:** attribute, operator, value, cohort_id
**Measure:** Segment size, stability and response lift
**Control:** Version the rule, evaluation date and member count.
**Evidence:** Segment manifest and sampled members

### Tags, groups and computed segments

**Mechanism:** Apply tag → Capture preference → Combine conditions → Resolve overlap
**Fields:** tag, group, conditions, priority
**Measure:** % contacts assigned consistently across constructs
**Control:** Separate marketer metadata, subscriber choices and computed eligibility.
**Evidence:** Audience taxonomy and overlap check

### Persona and journey evidence

**Mechanism:** Aggregate signals → Describe need → Map barrier → Choose message
**Fields:** evidence, job_to_be_done, barrier, content_job
**Measure:** Persona claims supported by actual audience evidence
**Control:** Label inferred claims and test them against behavioural data.
**Evidence:** Evidence-backed persona card

### Personalisation hierarchy

**Mechanism:** Insert identity → Adapt content → Select offer → Time delivery
**Fields:** identity, context, offer, moment
**Measure:** Incremental response lift without complaint increase
**Control:** Use the least sensitive signal that improves relevance and provide fallbacks.
**Evidence:** Personalisation matrix and fallback test

### Privacy-preserving Cowork workflow

**Mechanism:** Minimise export → Mask identity → Analyse sample → Return aggregate
**Fields:** minimum_fields, pseudonym, sample, aggregate
**Measure:** % tasks completed without unnecessary personal data
**Control:** Grant the narrowest folder/tool scope and use synthetic data in training.
**Evidence:** Access scope, masked dataset and review log

## Topic 3: Creating Email Content and Campaigns with Custom Claude Skills

Turn a campaign brief and brand system into useful, accessible email variants, then package a proven workflow as a reusable Claude Skill.

### Message architecture

**Mechanism:** Open promise → Build relevance → Prove value → Ask action
**Fields:** subject, lead, proof, cta
**Measure:** Message clarity and single-action completion
**Control:** Give every message one primary action and a coherent evidence path.
**Evidence:** Annotated message map

### Subject line and preview pair

**Mechanism:** State benefit → Create specificity → Add preview → Check integrity
**Fields:** benefit, specificity, preview, body_match
**Measure:** Unique open proxy plus downstream click quality
**Control:** Evaluate the subject and preview as one promise against the body.
**Evidence:** Variant table with promise-integrity check

### Brand voice as constraints

**Mechanism:** Define traits → Show examples → Mark exclusions → Score draft
**Fields:** traits, examples, avoid, rubric
**Measure:** % drafts passing brand rubric without manual rewrite
**Control:** Translate voice into word choice, rhythm, proof and prohibited patterns.
**Evidence:** Brand rubric and scored sample

### Content types across the lifecycle

**Mechanism:** Choose moment → Set message job → Select format → Define response
**Fields:** lifecycle, job, format, response
**Measure:** Content-to-stage fit and action rate
**Control:** Match welcome, nurture, launch, transactional and re-engagement content to stage.
**Evidence:** Lifecycle content matrix

### Email layout and accessibility

**Mechanism:** Establish hierarchy → Design mobile → Add alternatives → Test rendering
**Fields:** heading, width, alt_text, preview
**Measure:** % critical content readable without images and on mobile
**Control:** Use semantic structure, descriptive links and a resilient text path.
**Evidence:** Accessibility and rendering checklist

### Grounded drafting with Cowork

**Mechanism:** Read approved files → Draft to schema → Cite claims → Flag unknowns
**Fields:** sources, output_schema, claim_map, unknowns
**Measure:** % factual claims traceable to approved source material
**Control:** Constrain drafting to approved evidence and require an assumption log.
**Evidence:** Draft, source map and unresolved questions

### Custom Skill anatomy

**Mechanism:** Define trigger → Package instructions → Attach resources → Test outputs
**Fields:** description, workflow, templates, tests
**Measure:** % representative tasks that activate and pass the skill contract
**Control:** Specify positive and near-miss triggers, inputs, outputs and quality gates.
**Evidence:** Skill package and activation test

### Editorial quality gate

**Mechanism:** Check objective → Check brand → Check compliance → Approve release
**Fields:** objective_fit, brand_score, risk_scan, approver
**Measure:** % releases passing all gates before platform entry
**Control:** Separate creative assessment from deterministic release conditions.
**Evidence:** Editorial scorecard and named decision

## Topic 4: Email Marketing Automation with Claude Cowork and MCP Tools

Design a controlled automation that uses Cowork, Skills and connectors while preserving permissions, approval, idempotency and evidence.

### Automation suitability

**Mechanism:** Find repetition → Stabilise rules → Bound consequence → Select posture
**Fields:** frequency, rule_clarity, impact, posture
**Measure:** Time saved at equal or better quality and control
**Control:** Automate stable work; retain human ownership of material release decisions.
**Evidence:** Suitability score and automation boundary

### Trigger-condition-action model

**Mechanism:** Receive event → Evaluate condition → Perform action → Record result
**Fields:** event, condition, action, result
**Measure:** % events producing exactly one valid transition
**Control:** Use typed inputs, explicit conditions and deterministic terminal states.
**Evidence:** Workflow graph and event log

### Cowork projects and instructions

**Mechanism:** Select project → Load context → Apply rules → Create artifact
**Fields:** project, folder_context, instructions, artifact
**Measure:** % sessions using the current approved brand and campaign context
**Control:** Keep global preferences separate from campaign-specific folder instructions.
**Evidence:** Instruction hierarchy and version record

### Connectors and MCP boundaries

**Mechanism:** Authorize service → Expose tool → Call operation → Inspect response
**Fields:** identity, scope, tool_schema, result
**Measure:** % calls using least privilege and validated responses
**Control:** Prefer precise connectors, narrow scopes and schema validation.
**Evidence:** Permission inventory and tool-call evidence

### Prompt injection and untrusted content

**Mechanism:** Read input → Classify trust → Ignore embedded command → Escalate anomaly
**Fields:** content_source, trust_level, instruction_origin, decision
**Measure:** % untrusted instructions blocked before tool action
**Control:** Treat external content as data, never authority; stop on unexpected requests.
**Evidence:** Injection test and blocked action

### Human approval before send

**Mechanism:** Prepare draft → Freeze payload → Review evidence → Release or reject
**Fields:** draft_id, content_hash, approver, decision
**Measure:** % sends matching the approved payload and audience
**Control:** Bind approval to a content hash, cohort ID and expiry time.
**Evidence:** Approval receipt and matching send manifest

### Idempotency, retries and suppression

**Mechanism:** Create run key → Attempt action → Classify failure → Retry or stop
**Fields:** run_key, attempt, error_class, terminal_state
**Measure:** Duplicate-send rate and recovery success
**Control:** Use idempotency keys and reconcile remote state before retry.
**Evidence:** Run ledger with one terminal outcome

### Scheduled task operations

**Mechanism:** Define routine → Set cadence → Choose approval → Review runs
**Fields:** task, schedule, approval_mode, run_history
**Measure:** % scheduled runs reviewed with exceptions resolved
**Control:** Use saved cloud files/connectors for remote runs and review history regularly.
**Evidence:** Schedule definition and exception report

## Topic 5: Campaign Analytics, A/B Testing and Performance Optimisation

Read campaign reports critically, run valid experiments and recommend improvements that connect engagement, conversion, deliverability and business value.

### Email metric system

**Mechanism:** Count sends → Measure delivery → Measure engagement → Measure outcome
**Fields:** sent, delivered, clicks, conversions
**Measure:** Delivery, click, conversion, unsubscribe and value metrics
**Control:** Define every metric with numerator, denominator, window and decision use.
**Evidence:** Metric dictionary and reconciled report

### Measurement reliability

**Mechanism:** Inspect tracking → Find bias → Triangulate signal → Set confidence
**Fields:** tracking, privacy_effect, secondary_signal, confidence
**Measure:** Decision confidence after tracking limitations
**Control:** Use clicks, conversions and longitudinal evidence to qualify open signals.
**Evidence:** Reliability note beside each KPI

### Funnel and cohort diagnosis

**Mechanism:** Build funnel → Locate loss → Split cohort → Form hypothesis
**Fields:** stage_counts, dropoff, cohort, hypothesis
**Measure:** Largest meaningful loss with reproducible cohort evidence
**Control:** Compare stable cohorts before recommending a causal change.
**Evidence:** Funnel chart and segment comparison

### A/B test contract

**Mechanism:** Write hypothesis → Change one variable → Randomise audience → Choose winner rule
**Fields:** hypothesis, variable, allocation, decision_rule
**Measure:** Pre-declared effect and decision rule
**Control:** Freeze the audience, metric, duration and stopping rule before launch.
**Evidence:** Experiment contract and allocation check

### Interpreting experiment results

**Mechanism:** Check exposure → Estimate lift → Inspect uncertainty → Decide action
**Fields:** sample, baseline, lift, interval
**Measure:** Practical lift with uncertainty and guardrails
**Control:** Report magnitude, uncertainty, limitations and next action.
**Evidence:** Results card with continue/stop decision

### Deliverability optimisation

**Mechanism:** Audit source → Clean list → Improve relevance → Monitor complaints
**Fields:** source_quality, bounce, engagement, complaints
**Measure:** Sustained delivery and complaint health
**Control:** Fix permission, list health and content relevance before scaling.
**Evidence:** Deliverability trend and remediation log

### Cowork analytics brief

**Mechanism:** Load exports → Validate schema → Calculate metrics → Write recommendation
**Fields:** files, schema, calculations, recommendation
**Measure:** % reported values reproducible from supplied exports
**Control:** Require formula-level calculation evidence and explicit missing fields.
**Evidence:** Analysis workbook, chart and recommendation

### Optimisation backlog

**Mechanism:** Prioritise finding → Design treatment → Assign owner → Review outcome
**Fields:** finding, experiment, owner, review_date
**Measure:** % recommendations converted into measured experiments
**Control:** Rank by impact, confidence, effort and risk; close the learning loop.
**Evidence:** Prioritised backlog and decision history

## Labs

### Lab 01: Build a Grounded Campaign Strategy Brief

Use Claude Cowork with supplied brand and market evidence to propose a consent-aware email strategy for Northstar Fitness.

- Folder: `labs/lab-01-campaign-strategy-brief/`
- Workflow: Open project, Read evidence, Frame objective, Score channel, Set metrics, Review brief
- Detailed guide: `README.md` and `README.pdf` in the individual folder
- Acceptance: One primary objective, audience, value exchange, metrics, guardrails and source-backed assumptions are explicit.

### Lab 02: Design a Lead Magnet and Drip Lifecycle

Turn a customer tension into a credible lead magnet and five-state lifecycle sequence.

- Folder: `labs/lab-02-lead-magnet-lifecycle/`
- Workflow: Find tension, Define asset, Minimise fields, Map stages, Set exits, Approve promise
- Detailed guide: `README.md` and `README.pdf` in the individual folder
- Acceptance: The promise matches the source evidence, consent is explicit and every lifecycle state has entry and exit rules.

### Lab 03: Audit and Repair an Audience Dataset

Use synthetic subscriber data to identify consent, status, duplicate and quality defects before segmentation.

- Folder: `labs/lab-03-audience-data-quality/`
- Workflow: Read schema, Profile rows, Find defects, Apply rules, Reconcile counts, Export evidence
- Detailed guide: `README.md` and `README.pdf` in the individual folder
- Acceptance: All rows reconcile to kept, suppressed or review states; no personal data leaves the lab folder.

### Lab 04: Create Explainable Segments and Personalisation

Create reproducible audience segments and a safe personalisation matrix from the cleaned mock audience.

- Folder: `labs/lab-04-segment-personalisation/`
- Workflow: Choose signal, Write rule, Preview cohort, Check overlap, Set fallback, Approve use
- Detailed guide: `README.md` and `README.pdf` in the individual folder
- Acceptance: Rules reproduce member counts, suppressed contacts are excluded and sensitive attributes are not used.

### Lab 05: Draft Grounded Email Variants

Create welcome and launch email variants from a campaign brief, product facts and brand rubric.

- Folder: `labs/lab-05-grounded-email-variants/`
- Workflow: Load brief, Read brand, Draft schema, Map claims, Score quality, Revise once
- Detailed guide: `README.md` and `README.pdf` in the individual folder
- Acceptance: Each email has one CTA, accessible structure, supported claims and a passed brand/compliance scorecard.

### Lab 06: Package a Reusable Email Campaign Skill

Convert the proven drafting and QA workflow into a reusable Claude Skill with trigger and near-miss tests.

- Folder: `labs/lab-06-custom-email-skill/`
- Workflow: Define trigger, Specify inputs, Write workflow, Attach rubric, Run tests, Refine scope
- Detailed guide: `README.md` and `README.pdf` in the individual folder
- Acceptance: The Skill activates only for intended campaign tasks and produces a schema-valid, brand-scored draft.

### Lab 07: Design a Safe Cowork Connector Workflow

Map a draft-to-platform workflow with least privilege, untrusted-input handling and explicit tool boundaries.

- Folder: `labs/lab-07-connector-risk-design/`
- Workflow: Name systems, Select tools, Limit scope, Classify trust, Test injection, Approve design
- Detailed guide: `README.md` and `README.pdf` in the individual folder
- Acceptance: No live send occurs; scopes are minimal; embedded instructions are blocked and surfaced for human review.

### Lab 08: Control an Approved Scheduled Campaign

Create a dry-run automation contract that binds human approval to a frozen content and audience payload.

- Folder: `labs/lab-08-approval-scheduled-campaign/`
- Workflow: Build draft, Freeze payload, Request approval, Verify hash, Dry-run schedule, Log outcome
- Detailed guide: `README.md` and `README.pdf` in the individual folder
- Acceptance: Exactly one dry-run schedule is recorded for the approved payload; rejection, expiry and retry cases stop safely.

### Lab 09: Analyse Campaign Performance

Calculate and visualise delivery, engagement, conversion and unsubscribe metrics from mock exports.

- Folder: `labs/lab-09-campaign-analytics/`
- Workflow: Load exports, Validate schema, Reconcile totals, Calculate KPIs, Compare cohorts, Write finding
- Detailed guide: `README.md` and `README.pdf` in the individual folder
- Acceptance: All values reproduce from source rows and the finding distinguishes observation from causal hypothesis.

### Lab 10: Evaluate an A/B Test and Prioritise Improvements

Interpret a simulated subject-line test and translate evidence into a governed optimisation backlog.

- Folder: `labs/lab-10-ab-test-optimisation/`
- Workflow: Read contract, Check balance, Compute lift, Assess uncertainty, Choose posture, Plan next test
- Detailed guide: `README.md` and `README.pdf` in the individual folder
- Acceptance: The decision uses the frozen metric and guardrails, reports uncertainty and names an owner and review date.

## References
- Original v13 trainer deck: Local reference/legacy-v13/WSQ - Master Trainer Slides - Creating High-Converting Email Campaigns with Mailchimp - v13.pptx — Primary WSQ sequence, TSC mapping, outcomes and legacy campaign examples
- Email Marketing & AI: Local reference/Email Marketing  AI.pdf — Email strategy, lifecycle content, compliance, segmentation, optimisation and AI applications
- Mastering Claude Code and Cowork: Local reference/MASTERING CLAUDE Cowork.pdf — Agentic loop, Cowork tasks, projects, connectors, Skills, safety and end-to-end workflows
- [Current course page](https://www.tertiarycourses.com.sg/wsq-claude-cowork-for-email-marketing.html) — Current course identity, duration, outcomes and five-topic syllabus
- [Claude Cowork help collection](https://support.claude.com/en/collections/19667525-claude-cowork) — Current Cowork concepts, availability and operating surfaces
- [Get started with Claude Cowork](https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork) — Projects, folder instructions, permissions, plugins and scheduled tasks
- [Use Claude Cowork safely](https://support.claude.com/en/articles/13364135-use-claude-cowork-safely) — Untrusted content, permissions and safe task operation
