# James – Local AI Butler

## Overview
James is a **local, extensible AI butler** built on a hybrid architecture:

> **Local-first, cloud-on-demand**

It is designed as a **long-term research and productivity companion**, not a generic AI agent.

---

## Goals

### Primary Focus
- Research workflows (books, investing, game development)
- Structured thinking & productivity

### Secondary Focus
- Home & everyday tools (calendar, notes, automation)

---

## Core Philosophy

James is **not a monolithic agent**.

It is a **controlled system of specialized components**, built around:

- **Determinism over guesswork**
- **Explicit state over hidden context**
- **Control over autonomy**
- **Separation of logic and intelligence**
- **Built from scratch, avoiding high-level agent frameworks**

---

## Key Principles

- **Local-first, Cloud-on-demand**
- **Hardware-agnostic** (no refactoring on upgrades)
- **Capability-based routing instead of fixed models**
- **LLMs propose — the kernel decides**
- **Explicit, inspectable system state**
- **Privacy-first for research & intellectual property**

---

## Build Approach

James is built **from first principles**, with minimal external abstractions.

We intentionally avoid frameworks like LangChain or LangGraph to maintain:
- full control over execution flow
- explicit and inspectable state
- high debuggability

This results in a system that is:
- transparent  
- testable  
- maintainable  

> Trade-off: more upfront engineering, but significantly better long-term control.

---

## Architecture (High-Level)

User (CLI / later Voice)
        │
        ▼
┌─────────────────────┐
│     Interaction     │
│   (CLI / Voice)     │
└─────────┬───────────┘
          │
          ▼
┌─────────────────────┐
│     James Kernel    │  ← Central control
│ (State + Scheduler) │
└─────────┬───────────┘
          │
┌─────────┼───────────────────────────────┐
│         │                               │
▼         ▼                               ▼
Router   Planner                        Memory
(Intent) (Task decomposition)          (Short/Long-term)
│         │                               │
▼         ▼                               ▼
LLM     Plan (Steps)                Context retrieval
│
▼
Executor  ──► Tools (Python, Shell, Web, Home)
│
▼
Critic (Validation & risk assessment)


---

## Core Components

### James Kernel
- Deterministic orchestrator
- Explicit state machine
- Enforces rules, permissions, and flow

---

### Router
- Classifies user intent
- Selects **capabilities**, not models
- Decides local vs. cloud execution

---

### Planner
- Breaks goals into steps
- LLM-based **proposal only**
- No execution

---

### Executor
- Deterministic execution layer
- Uses **whitelisted tools only**
- Supports dry-run & permission checks

---

### Critic
- Validates outputs
- Compares plan vs. result
- Prevents error propagation

---

### Memory System

**Short-term**
- Active session context

**Long-term**
- Episodic (projects)
- Semantic (knowledge, preferences)

Properties:
- explicit
- versionable
- policy-controlled

---

### LLM Backends
- Local models (default)
- Cloud models (escalation only)

All models are accessed via abstraction.

---

## Current Status

James is currently in development of:

> **Feature-Level 1 – Core Interaction (MVP)**

What this means:

- CLI-based interaction
- Deterministic execution
- No planning, no memory, no autonomy

See:
- `status.md` for progress
- `docs/fl1.md` for usage & examples

---

## Project Structure

james/
├─ core/          # Kernel, Router, Planner, Executor, Critic
├─ llm/           # LLM abstraction + backends
├─ memory/        # Short-, long-term, policies
├─ tools/         # Python, Shell, Web, Home
├─ config/        # Hardware, model, policy configs
├─ registry/      # Capability & backend selection
├─ tests/         # Architecture & behavior tests
└─ ui/            # CLI, later Voice


---

## What James Is

- A personal AI co-pilot
- A research & productivity system
- A long-term extensible architecture

---

## What James Is NOT

- Not an autonomous open-world agent
- Not a black-box AI system
- Not uncontrolled or self-directed

---

## Design Decisions

Key architectural decisions include:

- Hybrid architecture (local-first + cloud escalation)
- Explicit state & deterministic kernel
- Strict separation of control (kernel) and intelligence (LLMs)
- Capability-based routing instead of model binding

All decisions are documented in:
- `entscheidungen.md`
- `kernel_design.md`
- `architektur.md`

---

## Roadmap

James is built in **Feature Levels (0–8)**:

1. **FL0** – Foundation (structure, config, logging)
2. **FL1** – Core interaction (CLI, execution)
3. **FL2** – Memory & project context
4. **FL3** – Planning (LLM-assisted)
5. **FL4** – Critic & validation
6. **FL5** – Hybrid intelligence (cloud escalation)
7. **FL6** – Controlled autonomy
8. **FL7–8** – Voice, comfort, long-term stability

---

## Why This Project Exists

Most AI systems today are:
- opaque
- non-deterministic
- hard to control

James is built to be:
- understandable
- controllable
- extensible
- reliable over time

---

## Future Vision

- Hardware-independent scaling
- Modular autonomy
- Long-term memory & project continuity
- Seamless human-AI collaboration

---

## License

TBD
