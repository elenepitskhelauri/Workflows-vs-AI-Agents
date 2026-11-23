# Workflows vs AI Agents: Choosing the Right Automation Approach

**NEXLEVR Quest 3 — Design document**

## Core distinction

A **fixed workflow** follows predefined steps and rules. It is suitable when the process is stable, repeatable, auditable, and has predictable inputs. An **AI agent** uses observations, tools, and adaptive decisions to pursue a goal when the path is not known in advance. Agents need constraints, monitoring, and human oversight. A **hybrid** system uses a reliable workflow to orchestrate selected adaptive steps.

## Example 1 — Employee onboarding

**Business need:** Create a new employee's account, assign mandatory training, send a welcome message, and notify HR.

**Recommendation: Fixed workflow.** These steps are predictable and compliance-sensitive. A workflow is easier to test, audit, and rerun. Missing approvals or failures should stop execution and alert HR. An autonomous agent adds unnecessary variability.

**Demo:** `onboarding_workflow()` returns the same ordered sequence for each employee.

## Example 2 — Customer support triage

**Business need:** Route varied questions about billing, account access, and delivery to an appropriate next action.

**Recommendation: Constrained AI agent when request variety is high; fixed rules for simple cases.** An agent could interpret ambiguous requests, retrieve approved policy information, and decide whether to ask a question or escalate. It must not independently approve refunds, expose account information, or take irreversible actions without authorization. For a small, stable list of request types, rules are simpler and cheaper.

**Demo:** `support_decision_agent()` is a *rule-based agent prototype*, not a true autonomous or LLM agent. It illustrates branching decisions and escalation; production use would need authenticated systems, policy retrieval, privacy safeguards, and evaluation.

## Example 3 — Daily technology news digest

**Business need:** Collect recent articles, select relevant stories, summarize them, attach source links, and propose brand content ideas each day.

**Recommendation: Hybrid workflow.** Scheduling, RSS collection, deduplication, source attribution, and report formatting are predictable pipeline stages. A constrained AI component can improve relevance ranking, summarization, and tailored post ideas. Human review is advisable before publishing because summaries can be inaccurate or omit context.

**Demo:** `hybrid_news_workflow()` uses fixed filtering and formatting with a basic topic-dependent content idea. It uses sample articles rather than live RSS; Quest 2 demonstrates the live RSS implementation separately.

## Decision guide

| Criterion | Fixed workflow | AI agent | Hybrid |
|---|---|---|---|
| Predictable sequence | Best | Usually unnecessary | Good |
| Ambiguous inputs | Limited | Potentially useful | Useful at selected steps |
| Auditability | High | Requires extra controls | High for deterministic stages |
| Cost and complexity | Usually lower | Usually higher | Moderate |
| Human oversight | Exceptions and approvals | Important for risky actions | Review adaptive outputs |

## Conclusion

**Use the simplest reliable approach that meets the business need.** Choose fixed workflows for repeatable, regulated processes; use constrained agents for genuinely variable decisions where their flexibility provides measurable value; and use hybrid architectures when reliable orchestration and selective AI reasoning are both beneficial.

## Limitations

The included code is an educational simulation. It does not use an LLM, connect to business systems, send emails, retrieve real customer records, or fetch live news. It demonstrates architectural choices rather than production-grade agent autonomy.
