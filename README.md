## Ziel
James ist ein lokaler, erweiterbarer AI-Butler mit Hybrid-Architektur (lokal-first, cloud-on-demand).

Primärer Fokus:
- Research & Produktivität (Buch, Aktien, Spieleentwicklung)

Sekundärer Fokus:
- Home- & Alltagstools (Kalender, Notizen, Automatisierung)

James ist **kein monolithischer Agent**, sondern ein kontrollierbares System aus spezialisierten Komponenten.

---

## Grundprinzipien
- **Lokal-first, Cloud-on-demand**
- **Hardware-agnostisch** (Upgrades ohne Code-Neuschreiben)
- **Capability-based Routing statt Modell-Fixierung**
- **LLMs schlagen vor, der Kernel entscheidet**
- **Expliziter Zustand statt impliziter Magie**
- **Privacy-first für Research & IP**

---

## High-Level-Architektur

```
User (CLI / später Voice)
        │
        ▼
┌─────────────────────┐
│     Interaction     │
│   (CLI / Voice)     │
└─────────┬───────────┘
          │
          ▼
┌─────────────────────┐
│     James Kernel    │  ← Zentrale Steuerung
│ (State + Scheduler) │
└─────────┬───────────┘
          │
┌─────────┼───────────────────────────────┐
│         │                               │
▼         ▼                               ▼
Router   Planner                        Memory
(Intent) (Task-Zerlegung)              (Kurz/Lang)
│         │                               │
▼         ▼                               ▼
LLM     Plan (Steps)                Kontext-Retrieval
│
▼
Executor  ──► Tools (Python, Shell, Web, Home)
│
▼
Critic (Validierung & Risikoabschätzung)
```

---

## Zentrale Komponenten

### 1. James Kernel
- Orchestrator & Zustandsautomat
- Koordiniert alle Komponenten
- Setzt Sicherheits- & Entscheidungsregeln durch

Verantwortlich für:
- Ablaufsteuerung
- State-Updates
- Abbruch / Eskalation

---

### 2. Router
- Klassifiziert User-Intents
- Wählt Fähigkeiten statt konkrete Modelle
- Entscheidet lokal vs. cloud

Beispiel-Intents:
- writing
- research
- coding
- finance
- home

---

### 3. Planner
- Zerlegt Ziele in Schritte
- Nutzt LLMs **nur zur Vorschlagserstellung**
- Gibt strukturierte Pläne zurück (kein Ausführen)

---

### 4. Executor
- Führt Pläne deterministisch aus
- Arbeitet ausschließlich über whitelisted Tools
- Unterstützt Dry-Run & Permission-Checks

---

### 5. Critic
- Bewertet Ergebnisse und Risiken
- Prüft Plan- vs. Ergebnis-Konsistenz
- Verhindert Fehlerfortpflanzung

---

### 6. Memory-System

**Kurzzeitgedächtnis**
- Aktuelle Konversation
- Temporärer Kontext

**Langzeitgedächtnis**
- Episodisch (Projektverlauf)
- Semantisch (Wissen, Präferenzen)

Memory ist:
- explizit
- versionierbar
- policy-gesteuert

---

### 7. LLM-Backends

- Lokale Modelle (Standard)
- Cloud-Modelle (Eskalation)

LLMs werden über eine Abstraktionsschicht angebunden.

---

## Projektstruktur (geplant)

```text
james/
├─ core/          # Kernel, Router, Planner, Executor, Critic
├─ llm/           # LLM-Abstraktion + Backends
├─ memory/        # Kurz-, Langzeit-, Policies
├─ tools/         # Python, Shell, Web, Home
├─ config/        # Hardware-, Modell-, Policy-Konfigs
├─ registry/      # Capability- & Backend-Auswahl
├─ tests/         # Architektur- & Verhaltenstests
└─ ui/            # CLI, später Voice
```

---

## Abgrenzung
James ist:
- ein persönlicher Co-Pilot
- ein Research- & Produktivitätsassistent

James ist **nicht**:
- autonom im Open-World-Sinn
- ein bewusstes System
- ein unkontrollierter Agent

---

## Zukunftssicherheit
Die Architektur erlaubt:
- Hardware-Upgrades ohne Refactoring
- Austausch einzelner Modelle
- Erweiterung um neue Tools & Agenten
- Langfristige Wartbarkeit
- Autonomie ist modular, abstufbar und jederzeit einschränkbar