# FPF Specification — AI Agent Usage Guide

> First Principles Framework (FPF) is a standards-style pattern language for turning difficult engineering, research, management, and mixed human/AI work into explicit, reviewable, improvable reasoning.

- **Author:** Anatoly Levenchuk, with AI-agent assistance
- **Version:** June 2026
- **Status:** Normative kernel, eternal alpha: already used in working projects and development programs, while still evolving.

This document provides instructions for AI agents on how to use the First Principles Framework (FPF) Core Conceptual Specification from the `spec/` directory.

## What is FPF?

FPF helps when a project has outgrown one clever conversation. It is useful when meanings, claims, options, evidence, architecture, work decisions, publication forms, and improvement criteria must stay coherent across people, teams, tools, time, or AI agents.

Use FPF as a reference model and pattern language, not as a linear textbook. Start from the working question you bring from your project. Bring in internal FPF terms only after they help you keep the work precise.

FPF is designed for:

- Mixed human/AI teams working on complex problems
- Situations where vocabulary, responsibilities, or evidence need explicit stabilization
- Problems requiring auditability, evolvability, and semantic precision across contexts

## Decide Whether FPF Fits

Use FPF when ordinary discussion is no longer enough to keep work coherent. Typical signs:

- several teams, experts, tools, or AI agents must reason about the same work;
- the real-world test is slow, expensive, noisy, risky, or politically hard to repeat;
- different readers need different reports, dashboards, explanations, or decisions about the same underlying work;
- names, roles, responsibilities, options, evidence, or quality criteria are starting to blur;
- the team needs a current view of possible approaches, not just one recommendation;
- a decision is small enough to make now but important enough to leave a durable reason.

FPF is probably too heavy when the task is small, feedback is fast and cheap, the vocabulary is already stable, the decision will not be reused or audited, and a quick answer is enough.

FPF is mainly useful for people who have to keep difficult work understandable across boundaries:

- engineers and systems engineers working with complex products or operations;
- researchers building claims that others must inspect or reuse;
- platform and AI teams coordinating humans, models, tools, and approvals;
- safety, assurance, compliance, and regulatory leads who need visible evidence and responsibility boundaries;
- managers and product leaders who must compare options, budgets, risks, and delivery promises without hiding trade-offs.

There are three common ways to use FPF:

1. **Human-only**: use it as a writing and review discipline for meetings, notes, decisions, and technical documents.
2. **Mixed team**: use it to keep specialists, managers, safety leads, and AI assistants aligned around the same work.
3. **AI-assisted**: attach or index the specification, ask for plain-language project help first, and use pattern names only when they make the answer easier to check.

Stronger AI does not remove the need for FPF. AI can generate fluent options quickly, but projects still need to decide what counts as evidence, which option is being compared, who may rely on an answer, when a claim is stale, what remains only a guess, and what work is actually authorized. FPF helps make those boundaries explicit before a confident answer becomes an expensive mistake.

**Core ideas in plain language:**

- local teams may use local meanings, but translation must be explicit when work crosses a boundary;
- the thing itself, its description, a dashboard about it, a decision about it, and the work done to change it are not the same;
- keep several options alive until the comparison is clear enough to choose;
- say what "better" means before optimizing or scoring;
- make trust depend on evidence, freshness, scope, and intended use;
- publish different views for different readers without changing the underlying claim;
- use mathematics or formal models when they clarify what structure is preserved, what is lost, and what can be checked.

## Specification Structure

The FPF specification is organized in the `spec/` directory with patterns split into individual files by Part:

```
spec/
├── 0-Intro/         # Preface & Introduction (non-normative orientation)
├── A-Kernel/        # Part A - Kernel Architecture Cluster
├── B-Reasoning/     # Part B - Trans-disciplinary Reasoning Cluster
├── C-Calculi/       # Part C - Calculi and Characteristic Spaces
├── D-Discipline/    # Part D - Discipline-Specific Patterns
├── E-Publication/   # Part E - Editorial and Publication Patterns
└── F-Coordination/  # Part F - Coordination and Bridge Patterns
```

### Accessing Patterns

**Each pattern is in its own file** named after its ID:

| Pattern ID | File Path                     |
|------------|-------------------------------|
| `A.1.1`    | `spec/A-Kernel/A.1.1.md`      |
| `A.6.B`    | `spec/A-Kernel/A.6.B.md`      |
| `B.5.2.1`  | `spec/B-Reasoning/B.5.2.1.md` |
| `E.17`     | `spec/E-Publication/E.17.md`  |

**Intro chapters** have numeric prefixes for ordering:

- `spec/0-Intro/01-what-this-specification-is-and-how-to-use-it.md`
- `spec/0-Intro/03-navigating-uncertainty-building-closed-worlds-within-an-open-world-non-normat.md`

**Each Part has a README index** for browsing:

- `spec/0-Intro/README.md` — Introductory chapters (indexed 00-17)
- `spec/A-Kernel/README.md` — All Part A patterns
- `spec/B-Reasoning/README.md` — All Part B patterns
- etc.

### Part Overview

| Part      | Directory         | Focus                      | When to Use                                  |
|-----------|-------------------|----------------------------|----------------------------------------------|
| **Intro** | `0-Intro/`        | Orientation & philosophy   | First-time understanding, context-setting    |
| **A**     | `A-Kernel/`       | Core ontology & boundaries | Responsibility, roles, contracts, time, work |
| **B**     | `B-Reasoning/`    | Reasoning cycles & bridges | Cross-context work, trust, emergence         |
| **C**     | `C-Calculi/`      | Comparison & measurement   | Alternatives, metrics, creativity, novelty   |
| **D**     | `D-Discipline/`   | Discipline extensions      | Domain-specific patterns                     |
| **E**     | `E-Publication/`  | Publication & authoring    | Documentation, views, explanations           |
| **F**     | `F-Coordination/` | Coordination & terminology | Vocabulary, bridges, concept sets            |

## First Practical Entries

A first practical entry is the first useful way to enter FPF from a real working project. Choose it by the project question you are trying to settle, not by the order of patterns in the specification.

The entries below are not a required sequence. They are common places where FPF can start paying rent in a project.

### 1. Develop or review architecture

Use this when you need to design, explain, review, or improve the architecture of a product, organization, technical system, document system, AI-agent setup, research program, or other thing with important internal structure.

FPF helps you ask what is being architected, which structures matter, what property of the architecture is being changed or judged, and which description, diagram, view, promise, decision, evidence, or implementation task is a different matter. It gives you language for selected structures, structural views, architecture characteristics, modularity, interfaces, scale, interlevel tensions, and architecture-changing moves.

**Typical first result:** a short architecture question note that says what is being architected, which structures matter, which architecture characteristic is at stake, what description or view is needed, and what decision or implementation work is still not settled by the architecture statement.

**First inspect:** `C.30`, `A.22`, `C.30.ASV`, `C.30.AD`, `C.31`, `A.6.M`, and the relevant architecture precision-restoration patterns when wording hides the kind of structure being discussed.

### 2. Write rules, methods, and work-process documents

Use this when you need to write or review technical regulations, procedures, method descriptions, operating instructions, work-process descriptions, standards-like project documents, API documents, contracts, SLAs, protocols, permissions, or compliance wording.

FPF helps you keep the described method separate from the method itself, a plan separate from performed work, responsibility separate from permission, an interface contract separate from implementation, and a published document separate from actual execution. It can also describe chains of methods when the chain itself is the subject, while keeping actual work occurrences separate from the document that says how work should be done.

**Typical first result:** a cleaned method, regulation, or interface outline that names what is being governed, the method or interface being described, the roles and responsibilities involved, the expected work result, and any evidence, gate, permission, or compliance claim that the document does not yet justify.

**First inspect:** `A.6`, `A.6.B`, `A.6.C`, `A.15`, `A.15.1`, `A.15.2`, `A.15.3`, `A.15.4`, `E.18`, `E.18.1`, `E.8`, and `E.19`.

### 3. Compare alternatives and make a local choice

Use this when a team needs to compare technologies, vendors, designs, policies, research paths, implementation options, or architecture moves without jumping to one favorite too early.

FPF helps you state what is being compared, which characteristics matter, which candidates are still in play, what evidence is missing, when a local choice is justified, and how to publish a selected set without hiding the comparison logic.

**Typical first result:** a comparison note with declared characteristics, candidate set, evidence gaps, the present scope of the choice, and what a selected-set publication may and may not be used to decide.

**First inspect:** `A.19`, `A.19.ECS`, `C.11`, `C.18`, `C.19`, `G.0`, and `G.5`.

### 4. Turn a vague situation into a usable problem statement

Use this when a project has complaints, opportunities, risks, anomalies, or strategic pressure, but no clear problem yet.

FPF helps you preserve partly formed concerns without pretending they are already requirements, decisions, causes, evidence, or work items. It can turn a vague situation into a problem card or problem portfolio that later work can use without erasing uncertainty.

**Typical first result:** a problem card, problem portfolio, or problem note that records what has been accepted, what remains only a cue, which context is involved, and which first pattern family can use the problem statement.

**First inspect:** `C.22.2`, `C.2.2a`, `A.16`, `A.16.1`, `A.16.2`, `B.4.1`, and `B.5.2.0`.

### 5. Define what "better" means and run improvement

Use this when you need to improve a product, process, architecture, document, pattern, regulation, research program, or organization, but the improvement criteria are vague or competing.

FPF helps you define characteristics for evaluation, evaluate what is being improved, generate a portfolio of improvement proposals, choose changes that really improve the situation, and repeat the cycle without reducing quality to one score.

**Typical first result:** a quality-and-improvement note with evaluation characteristics, one evaluation of the object under improvement, a portfolio of proposed changes, and a condition for stopping or reopening the cycle.

**First inspect:** `A.19.ECS`, `E.22`, `E.23`, `C.16`, `C.25`, `E.21`, `E.9.DA`, and `E.2.DA` when the object is an FPF artifact.

### 6. Prepare evidence, assurance, or gate decisions before commitment

Use this when a project cannot responsibly act yet because evidence, assurance, constraints, gate validity, or decision permission is unclear.

FPF helps you separate what is being claimed from the evidence path, assurance argument, internal constraint validity, gate decision, local choice, and performed work. That separation matters when the cost of acting too early is high.

**Typical first result:** a commitment-readiness note that lists the claim, the evidence or assurance still needed, the gate or decision condition, and the work that remains blocked until those checks exist.

**First inspect:** `A.10`, `B.3`, `A.20`, `A.21`, `C.11`, `C.28`, and the relevant work or architecture pattern if the claim is about planned or performed work.

### 7. Check timing, freshness, rhythm, and action windows

Use this when a project depends on timing: freshness, latency, rate, cadence, action window, synchronization, inertia, aging, or rhythm.

FPF helps you separate timing information from evidence, permission, work completion, or vague urgency. It can say what timestamp, interval, cadence, freshness limit, action window, or rhythm claim is being used, and when that claim is no longer current enough for action.

**Typical first result:** a timing note that names what the timing is about, the relevant time relation or rhythm, the freshness or action-window limit, and the action that remains blocked when the timing claim is stale or underspecified.

**First inspect:** `C.27`, `A.10`, `A.20`, `A.21`, `C.11`, and the pattern that governs the thing whose timing matters.

### 8. Use causal explanations, interventions, responsibility, and model outputs safely

Use this when a project says that one thing causes another, a model output justifies an action, a change will produce an effect, or a role is responsible for an outcome.

FPF helps you separate causal use, counterfactual use, intervention claims, responsibility claims, model-output reliance, evidence, and decisions. It keeps a plausible explanation, prediction, or dashboard output from becoming permission to act.

**Typical first result:** a causal-use or model-output-use note that names the claim, the intervention or counterfactual being considered, the evidence or validation still needed, the responsibility limit, and the decision or work that remains blocked.

**First inspect:** `C.28`, `A.10`, `B.3`, `A.20`, `A.21`, `C.11`, and the domain pattern that governs the affected thing.

### 9. Compare descriptions, dashboards, explanations, and views of the same thing

Use this when a project has several descriptions, dashboards, explanations, renderings, model slices, or views and needs to know whether they are about the same thing, serve the same concern, or can be relied on in the same way.

FPF helps you keep the thing being described separate from its description, publication form, rendering, viewpoint, and same-thing claim. It can keep a diagram, dashboard, generated explanation, or view from silently becoming the thing itself, evidence, assurance, or decision.

**Typical first result:** a description-use note that names what is being described, which description or view is being used, how it is published or rendered, whether the same thing is really being addressed, and what the publication may and may not be used to claim.

**First inspect:** `E.17`, `E.17.0`, `E.17.EFP`, `A.15.4`, `A.7`, `C.30.AD`, and the pattern that governs the described thing.

### 10. Give things better names

Use this when project terms are misleading, overloaded, politically convenient, too broad, too local, or hard to translate between teams.

FPF helps you name products, roles, work processes, architecture elements, standards, document types, claims, characteristics, and project objects without treating a catchy label as ontology.

**Typical first result:** a naming card or term sheet that says what is being named, which local contexts use the name, which candidate names were rejected, which plain and technical names are allowed, and which alternate names are risky.

**First inspect:** `F.17`, `F.18`, `F.19`, `E.10`, `E.10.ARCH`, and the subject pattern that governs the thing being named.

### 11. Repair wording in technical documents before it changes action

Use this when standards, specifications, contracts, policies, dashboards, model cards, explanations, or working documents use words that may quietly change what can be claimed or done.

FPF helps you repair wording by first recovering the ontology: what thing, relation, value, evidence path, publication use, gate, decision, work, or architecture claim is actually being made. The repair is not word-policing; it succeeds only when the repaired text still tells someone what can now be used, checked, or named, or which related pattern to apply.

**Typical first result:** a repaired paragraph, claim register, term sheet row, or non-use decision that says what the text may now be used for and what claim or action remains blocked.

**First inspect:** `E.10`, `E.10.ARCH`, `F.18`, `F.19`, `A.6.P`, `C.2.P`, `C.16.P`, `C.16.Q`, `C.30.P`, `A.6.F`, and `A.6.M`.

### 12. Decide whether mathematics or formal modeling would help

Use this when intuition is not enough and a mathematical model, formal declaration, invariant, or explicit structure could make the work easier to review, compare, or improve.

FPF helps with two opposite mistakes: missing useful mathematics, and using mathematics without saying what structure it preserves and what it loses. It keeps mathematical-lens use, formal declarations of the assumed substrate, mechanism import or realization, and first-principles-to-work carry-through as different claims that may need different patterns.

**Typical first result:** a short modeling note that names what is being modeled, the candidate mathematical lens, any formal declaration that is needed, preserved and lost structure, payoff, validation limit, and next project action.

**First inspect:** `C.29`, `A.6.0`, `A.6.1`, `E.18.1`, `C.16`, `C.27`, `C.30.LCA`, `C.30.ILC`, and the domain pattern that governs the modeled claim.

### 13. Build a state-of-the-art or option portfolio

Use this when the project needs the current field of possible solutions, schools of thought, research lines, technologies, or design options, rather than one recommendation.

FPF helps you harvest alternatives, keep novelty and diversity visible, define comparison characteristics, avoid early collapse to one winner, and refresh the portfolio as the field changes.

**Typical first result:** a SoTA pack, option portfolio, candidate set, archive, or selector-ready publication with declared scope, comparison characteristics, and refresh condition.

**First inspect:** `G.0`, `G.1`, `G.2`, `G.5`, `G.10`, `G.11`, `C.18`, `C.19`, `A.19`, and `A.19.ECS`.

## How to Use This Specification

### 1. Identify the Live Question

Before consulting FPF, clarify what problem is actually live:

- Is this about **responsibility boundaries**? → Part A kernel (`A-Kernel/`)
- Is this about **comparing options**? → Part C calculi (`C-Calculi/`)
- Is this about **unpacking boundary claims**? → A.6 cluster (`A-Kernel/A.6*.md`)
- Is this about **publication or explanation**? → Part E patterns (`E-Publication/`)
- Is this about **temporal or causal adequacy**? → C.27, C.28 (`C-Calculi/`)
- Is this about **vocabulary or terminology**? → Part F (`F-Coordination/`)

### 2. Select the Entry Pattern

**For orientation:**

- `spec/0-Intro/what-this-specification-is-and-how-to-use-it.md` — What FPF is
- `spec/0-Intro/navigating-uncertainty-building-closed-worlds-within-an-open-world-non-normative.md` — Closed vs open
  world
- Part README files for pattern lists

**For specific problems:**

- Use the table above to find relevant patterns
- Read individual pattern files directly (e.g., `spec/A-Kernel/A.6.B.md`)
- Check "Builds on:" and "Coordinates with:" fields in patterns for related patterns

### 3. Apply the Pattern Structure

Each FPF pattern file includes:

- **Problem frame**: What situation this pattern addresses
- **Keywords & Search Queries**: How to recognize when this pattern applies
- **Dependencies**: What patterns this builds on or coordinates with
- **Signature block**: The structured form to fill in (U.Signature)
- **Work instructions**: How to apply the pattern to concrete situations
- **Conformance Checklist**: Normative requirements

### 4. Produce Stabilized Artifacts

A successful FPF session should yield concrete outputs:

- Bounded context definitions (`A.1.1`)
- Role assignments and responsibility maps (`A.2`, `A.15`)
- Decision criteria and characteristic spaces (`A.19`, `C.11`)
- Alternative portfolios (not premature single winners) (`G.5`, `C.18`)
- Evidence gap lists (`A.10`, `B.3`)
- Decision records (`E.9` DRR)
- Terminology sheets (`F.17` UTS)
- Audience-specific publication views (`E.17` MVPK)

## One-Minute Example

A platform team asks:

> Should we buy, fine-tune, or build an agent stack for our product?

Without FPF, the conversation often mixes architecture, vendor comparison, safety, evidence, budget responsibility, user value, and implementation planning. The loudest option can win before the team knows what is being compared.

With FPF, the first pass can become a small set of explicit project objects:

- architecture question: what stack architecture is being changed or chosen;
- comparison frame: which alternatives are in the candidate set;
- evaluation characteristics: cost, latency, controllability, safety, maintainability, time to first use, and other project-specific characteristics;
- evidence gaps: what must be tested before commitment;
- current choice state: whether the team is choosing now, keeping a selected set, or doing more discovery;
- reader reliance: what engineering, management, and assurance readers may responsibly rely on.

That same shape can be used for a factory modernization, laboratory protocol, construction design change, supply-chain decision, safety case, or research program. The point is not the AI topic; the point is one body of reasoning that can be reviewed, improved, and published without changing meaning on the way.

## What FPF Is

FPF is a pattern language for disciplined thinking in projects where ordinary prose, local expert judgment, or one-off AI output is not enough.

It helps teams:

- keep meanings stable when work crosses teams, tools, documents, and time;
- separate the thing being discussed from diagrams, dashboards, explanations, promises, decisions, and actual work;
- state what a claim can responsibly be used for before people rely on it;
- compare options without collapsing too early to one favorite;
- define quality criteria before improvement starts;
- keep evidence, assurance, decisions, and implementation work visible as different questions;
- repair confusing wording by first asking what the wording is doing in the project, not by swapping synonyms;
- leave each pass with one useful next result: a clearer question, a better name, a comparison note, an evidence gap, a safer document, or a reason to inspect a specific pattern.

## What FPF Is Not

FPF is not:

- a shrink-wrapped project methodology;
- a checklist bureaucracy;
- a quick-answer cheat sheet;
- a replacement for domain expertise;
- a demand to study the whole specification before useful work begins;
- a promise that every project needs every pattern.

FPF is most useful when the cost of semantic drift, premature convergence, hidden evidence gaps, weak architecture, vague quality, or unreviewable work is higher than the cost of using a disciplined pattern language.

## How to Use This Repository

Start with the first practical entry that matches your project question. Then inspect the named pattern family and apply its Problem frame, Solution, examples, and checklist.

Use the `Preface` for the cross-cutting ideas behind the pattern language. Use the Table of Content when you already know the pattern family or need a search-oriented overview. Use extended cases only when the compact first entry is not enough.

If you use an AI assistant, attach or index `FPF-Spec.md` and ask for plain-language project help first. Let internal pattern names enter the conversation only when they make the reasoning more precise.

**A good first prompt is:**

```text
You have the FPF specification as a file.
Help me structure this project:
[short project description]

Use plain language for engineer-managers.
Propose the first useful FPF entry:
architecture, rules and methods, API or interface wording, permission or compliance wording, comparison and choice,
problem shaping, quality improvement, evidence and assurance,
temporal claims, causal or model-output use, publication or view use,
naming, technical-text precision, mathematical modeling,
or current options and state of the art.
For the selected entry, give:
1. the main project thing or claim at stake,
2. the first useful written result,
3. the first FPF patterns to inspect,
4. what still cannot be decided, trusted, or used responsibly.
```

## Key Concepts for AI Agents

### Bounded Context (`A.1.1`)

**File:** `spec/A-Kernel/A.1.1.md`

Every claim lives within a semantic boundary. Never assume terms transfer unchanged across contexts. When reusing
vocabulary across contexts, apply bridge patterns (`F.9`).

### Role vs. System (`A.2`)

**File:** `spec/A-Kernel/A.2.md`

Distinguish:

- **System/Entity**: What something *is*
- **Role**: What something *does* in a specific context
- **Capability**: What something *can do* (dispositional)
- **Work**: What actually *happened*

### Boundary Claims (`A.6`)

**Files:** `spec/A-Kernel/A.6.md`, `A.6.B.md`, `A.6.C.md`

When encountering contract-like language (APIs, SLAs, policies, compliance statements), decompose into atomic claims:

- **L (Laws)**: Rules that govern
- **A (Admissibility)**: Gates that must pass
- **D (Deontics)**: Commitments/obligations
- **E (Evidence)**: Work effects and support

### Relational Precision Restoration (`A.6.P`)

**File:** `spec/A-Kernel/A.6.P.md`

When encountering overloaded relation words (coupling, measurement, export, quality terms, action invitations), restore
precision by:

1. Detecting the under-specified relational language
2. Unpacking the local ontology
3. Choosing a stable mathematical or structural substrate
4. Refactoring with precise lexemes and guardrails

### Multi-View Architecture (`E.17`)

**File:** `spec/E-Publication/E.17.md`

Different audiences need different views of the same underlying work:

- Engineering views
- Management views
- Research views
- Assurance/audit views

All views must be **projections** of the same underlying work, not independent documents.

### Same-Entity Transformations (`A.6.3`)

**Files:** `spec/A-Kernel/A.6.3.md`, `A.6.3.CR.md`, `A.6.3.RT.md`, `A.6.3.CSC.md`

When rewriting, summarizing, translating, or re-rendering:

- **A.6.3.CR** (ConservativeRetextualization): Same entity, textual re-expression
- **A.6.3.RT** (RepresentationTransduction): Same entity, representation scheme change
- **A.6.3.CSC** (Controlled Semantic Coarsening): Narrower admissible use only

Always maintain a **source tether** and specify admissible downstream uses.

### Characteristic Spaces (`A.19`, `C.11`)

**Files:** `spec/A-Kernel/A.19.md`, `spec/C-Calculi/C.11.md`

When comparing alternatives:

- Declare the characteristic space explicitly
- Define measurement scales and units
- Keep comparison logic visible
- Avoid collapsing to single scores prematurely
- Publish selected sets with comparison traces

### Open-Ended Evolution (`A.4`, `A.0`)

**Files:** `spec/A-Kernel/A.4.md`, `A.0.md`

For novelty, diversity, and state-of-the-art work:

- Maintain descriptor maps
- Archive variants systematically
- Apply explore/exploit policies explicitly
- Publish portfolios, not just winners

## Common Anti-Patterns to Catch

| Anti-Pattern                                                             | FPF Repair                    | Pattern File                                  |
|--------------------------------------------------------------------------|-------------------------------|-----------------------------------------------|
| **Contract                                                               |                               |                                               |
| soup** — mixing rules, gates, duties, evidence in one blob               | `A.6.C` Contract Unpacking    | `A-Kernel/A.6.C.md`                           |
| **                                                                       |                               |                                               |
| Interface-as-agent** — treating an API/interface as if it has intentions | `A.6.C`, `A.2` Role Taxonomy  | `A-Kernel/A.6.C.md`, `A.2.md`                 |
| **Premature                                                              |                               |                                               |
| convergence** — choosing one option before honest comparison             | `A.19`, `C.11`, `G.5`         | `A-Kernel/A.19.md`, `C-Calculi/C.11.md`       |
| **Semantic                                                               |                               |                                               |
| drift** — terms changing meaning across contexts                         | `A.1.1`, `F.9`, `F.17` (UTS)  | `A-Kernel/A.1.1.md`, `F-Coordination/F.9.md`  |
| **                                                                       |                               |                                               |
| Correlation-as-causation** — using observation as intervention support   | `C.28`, `A.10`, `B.3`         | `C-Calculi/C.28.md`, `A-Kernel/A.10.md`       |
| **                                                                       |                               |                                               |
| Dashboard-as-permission** — treating a display as work authorization     | `E.17`, `A.15.4`, `A.6.3.CSC` | `E-Publication/E.17.md`, `A-Kernel/A.15.4.md` |
| **Time-ignoring                                                          |                               |                                               |
| claims** — temporal claims without window/effort/rhythm                  | `C.27`, `C.16`                | `C-Calculi/C.27.md`, `C.16.md`                |
| **Overloaded                                                             |                               |                                               |
| relations** — "coupling", "quality", "affordance" without precision      | `A.6.P`, `A.6.Q`, `A.6.A`     | `A-Kernel/A.6.P.md`, `A.6.Q.md`, `A.6.A.md`   |

## Working with the Specification Files

### File Characteristics

- **Location**: `spec/` directory in repository root
- **Structure**: One pattern per file, organized by Part
- **Total**: ~239 Markdown files (19 intro chapters + 210 patterns + 10 README indexes)
- **Format**: Individual pattern files with formatted tables
- **Status**: "Eternal alpha" — stable kernel with evolving extensions
- **Tables**: ~890 tables formatted across 200+ files

### Python Scripts for Specification Management

The repository includes Python scripts for managing the split FPF specification:

| Script | Purpose | Usage |
|--------|---------|-------|
| `split_spec.py` | Split monolithic `FPF-Spec.md` into `spec/` directory | `python3 split_spec.py` |
| `format_tables.py` | Format markdown tables for consistent appearance | `python3 format_tables.py` |
| `compare_spec.py` | Compare original spec with split files (content-aware) | `python3 compare_spec.py` |
| `verify_split.py` | Verify all patterns are present in split files | `python3 verify_split.py` |
| `split_summary.py` | Show split statistics with pretty tables | `python3 split_summary.py` |
| `summary.py` | Display file statistics by Part | `python3 summary.py` |
| `check_split.py` | Quick content check for each file | `python3 check_split.py` |

#### Complete Workflow

**1. Split the specification:**
```bash
python3 split_spec.py
```
Creates individual pattern files in `spec/` directory with pretty table output showing:
- File counts by type (patterns, intro chapters, READMEs)
- Breakdown by Part (A-Kernel, B-Reasoning, etc.)

**2. Format all tables:**
```bash
python3 format_tables.py
```
Formats ~890 tables across 200+ files with:
- Consistent column widths (auto-calculated)
- Alignment preservation (left, center, right)
- Clean separator rows

**3. Verify the split:**
```bash
python3 split_summary.py
```
Shows verification with pretty tables:
- File statistics with percentages
- Pattern verification status
- Files by Part breakdown

**4. Check content integrity:**
```bash
python3 check_split.py
```
Quick content check that ignores formatting differences:
- Table borders and column widths
- Whitespace variations
- Reports semantic content matches

**5. Compare with original:**
```bash
python3 compare_spec.py
```
Detailed comparison that normalizes:
- Whitespace and blank lines
- Header levels (# vs ##)
- End markers (### A.Y.Z:End)
- Dash styles (— vs -)
- Table borders and column widths

#### Output Features

All scripts use **pretty table formatting** with:
- Unicode box-drawing characters (`─`, `│`, `+`, `┼`)
- Aligned columns (left, center, right)
- Percentage calculations
- Section separators

**Example output:**
```
+──────────+──────────────────────+────────────+
|   Part   |      Directory       |  Patterns  |
+──────────+──────────────────────+────────────+
| A        | A-Kernel             | 73         |
| B        | B-Reasoning          | 24         |
|  TOTAL   |                      |    210     |
+──────────+──────────────────────+────────────+
```

#### Normalization Features

The `compare_spec.py` and `check_split.py` scripts ignore formatting differences:
- Whitespace and blank lines
- Header levels (# vs ##)
- End markers (### A.Y.Z:End)
- Dash styles (— vs -)
- **Table borders** (+, ─, │, ┼, etc.)
- **Table column widths** (spacing variations)

This ensures comparisons focus on **semantic content** rather than presentation.

#### Table Formatting

The `format_tables.py` script ensures uniform table appearance:
- Consistent column widths (auto-calculated from content)
- Proper alignment preservation (left, center, right)
- Clean separator rows with correct dash counts
- Minimum column width of 3 characters

Run after splitting to ensure all tables have uniform appearance.

### Search Strategies

**By Pattern ID (direct file access):**

```bash
# Open specific pattern
code spec/A-Kernel/A.6.B.md
code spec/E-Publication/E.17.md
```

**By browsing Part indexes:**

- Read `spec/A-Kernel/README.md` for all kernel patterns
- Read `spec/0-Intro/README.md` for orientation chapters

**By keywords within pattern files:**
Each pattern includes a Keywords field with searchable terms like:

- "boundary norm square, atomic claims, L/A/D/E claim classification"
- "role, assignment, holder, context, function vs identity"

**By query examples:**
Patterns include example queries like:

- "How do I classify boundary statements?"
- "What is a holon in FPF?"
- "How to separate ability from permission?"

**By dependencies:**
Use "Builds on:" and "Coordinates with:" fields in pattern files to navigate related patterns

### Citation Format

When referencing FPF patterns in outputs:

```
FPF A.6.B (Boundary Norm Square) — spec/A-Kernel/A.6.B.md
FPF C.27 (Temporal Adequacy) — spec/C-Calculi/C.27.md
FPF E.17 (Multi-View Publication) — spec/E-Publication/E.17.md
```

## Integration Patterns

### As Individual Pattern Files

Load specific pattern files directly for focused work:

```bash
# Read pattern before task
cat spec/A-Kernel/A.1.1.md  # Bounded Context
cat spec/A-Kernel/A.6.C.md  # Contract Unpacking
```

### As a Retrieval Index

Index the `spec/` directory for semantic search:

- Each Part README provides pattern listings
- Individual pattern files contain full searchable content
- Cross-references link related patterns

### As a Reasoning Scaffold

Use FPF patterns as structured templates for:

- Problem framing (read pattern's Problem frame section)
- Alternative generation (see `C.18`, `G.5`)
- Evidence organization (see `A.10`, `B.3`)
- Decision documentation (see `E.9` DRR)
- Publication alignment (see `E.17` MVPK)

### As a Quality Gate

Apply FPF patterns as review criteria:

- Are responsibility boundaries explicit? (`A.1.1`, `A.2`)
- Are boundary claims decomposed atomically? (`A.6.B`, `A.6.C`)
- Is comparison logic visible and honest? (`C.11`, `A.19`)
- Are publication views tethered to source work? (`E.17`, `A.6.3.CSC`)
- Are temporal claims adequacy-checked? (`C.27`, `C.16`)

## Example Usage Scenarios

### Scenario 1: API Contract Review

**Situation**: Reviewing an API specification that mixes SLA guarantees, access rules, and usage examples.

**FPF Approach**:

1. Read `spec/A-Kernel/A.6.RSIG.md` to recognize description type
2. Read `spec/A-Kernel/A.6.C.md` to unpack contract bundles
3. Apply `spec/A-Kernel/A.6.B.md` (L/A/D/E quadrants) to classify claims
4. Check `spec/A-Kernel/A.6.P.md` → `A.6.Q.md` / `A.6.A.md` for quality/action language
5. Produce a Claim Register with routed atomic claims

### Scenario 2: Technology Selection

**Situation**: Choosing between build, buy, or fine-tune options for an AI platform.

**FPF Approach**:

1. Define bounded contexts (`spec/A-Kernel/A.1.1.md`): product, infrastructure, safety, evaluation
2. Declare characteristic space (`spec/A-Kernel/A.19.md`): cost, latency, controllability, risk, time-to-value
3. Generate alternative portfolio (`spec/C-Calculi/C.18.md`, `C.19.md`): build/buy/fine-tune/hybrid
4. Apply comparison logic (`spec/C-Calculi/C.11.md`): keep comparison visible, avoid premature scoring
5. Document decision rationale (`spec/E-Publication/E.9.md` DRR) with evidence gaps explicit

### Scenario 3: Dashboard Publication

**Situation**: Publishing a management dashboard showing project status.

**FPF Approach**:

1. Identify source-bearing episteme or publication
2. Apply `spec/A-Kernel/A.6.3.CSC.md` if coarsening (summaries, redactions)
3. Specify admissible uses narrowly (state-reading only, not work authorization)
4. Apply `spec/E-Publication/E.17.md` multi-view discipline for different audiences
5. Maintain source tether and reopen triggers

### Scenario 4: Research Claim Adequacy

**Situation**: A research report makes causal claims from observational data.

**FPF Approach**:

1. Read `spec/C-Calculi/C.28.md` to separate observation from intervention support
2. Check evidence role (`spec/A-Kernel/A.2.4.md`) and trust structure
3. Apply `spec/B-Reasoning/B.3.md` for engineering justification assessment
4. Specify what additional evidence would upgrade the claim
5. Publish with appropriate use boundaries

### Scenario 5: Vocabulary Harmonization

**Situation**: Multiple teams use the same terms with different meanings.

**FPF Approach**:

1. Establish bounded contexts (`spec/A-Kernel/A.1.1.md`) for each team's usage
2. Harvest terms (`spec/F-Coordination/F.2.md`) from each context
3. Create bridges (`spec/F-Coordination/F.9.md`) to map relationships
4. Publish unified terminology sheet (`spec/F-Coordination/F.17.md` UTS)
5. Maintain context-local meanings with explicit cross-context translations

## Quick Reference Card

| If you need to...              | Start with...                | File Location                 |
|--------------------------------|------------------------------|-------------------------------|
| Separate responsibilities      | `A.1.1`, `A.2`, `A.15`       | `A-Kernel/`                   |
| Unpack contract language       | `A.6`, `A.6.B`, `A.6.C`      | `A-Kernel/`                   |
| Repair vague relation words    | `A.6.P` (+ `A.6.Q`, `A.6.A`) | `A-Kernel/`                   |
| Compare alternatives           | `A.19`, `C.11`, `G.5`        | `A-Kernel/`, `C-Calculi/`     |
| Generate novelty/diversity     | `A.0`, `C.18`, `C.19`        | `A-Kernel/`, `C-Calculi/`     |
| Publish for multiple audiences | `E.17`, `A.6.3.*`            | `E-Publication/`, `A-Kernel/` |
| Check temporal claims          | `C.27`, `C.16`               | `C-Calculi/`                  |
| Repair causal overreach        | `C.28`, `A.10`, `B.3`        | `C-Calculi/`, `A-Kernel/`     |
| Stabilize vocabulary           | `F.17` (UTS)                 | `F-Coordination/`             |
| Document decisions             | `E.9` (DRR)                  | `E-Publication/`              |
| Navigate uncertainty           | `C.2.2a`, `A.16`             | `C-Calculi/`, `A-Kernel/`     |
| Bridge contexts                | `F.9`                        | `F-Coordination/`             |
| Understand FPF basics          | `0-Intro/` chapters          | `0-Intro/`                    |

## Further Orientation

### Introductory Chapters (Non-Normative)

- `spec/0-Intro/01-what-this-specification-is-and-how-to-use-it.md` — Core orientation
- `spec/0-Intro/03-navigating-uncertainty-building-closed-worlds-within-an-open-world-non-normat.md` — Open/closed world
- `spec/0-Intro/04-fpf-as-an-evolutionary-architecture-for-thought.md` — FPF as architecture

### Pattern Navigation

- Part README files list all patterns in each Part
- Pattern files include "Builds on:" and "Coordinates with:" cross-references
- Use `grep` or IDE search across `spec/` directory for keywords

### Pattern Templates

- `spec/E-Publication/E.8.md` — Pattern writing template
- `spec/E-Publication/E.19.md` — Pattern review checklist

## Citation

If you use FPF, please cite:

```text
Levenchuk, Anatoly. First Principles Framework (FPF).
GitHub repository: https://github.com/ailev/FPF
```

---

*FPF is a normative specification for admissible action in problematic engineering, research, and mixed human/AI work.
Use it as a co-thinking scaffold, not as a replacement for good questions or domain expertise.*

**Pattern files are in `spec/` directory — always reference the specific pattern file path for precision.**
