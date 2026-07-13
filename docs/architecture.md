# OpsPilot Architecture

**Project:** OpsPilot
**Version:** 0.1.0
**Status:** Draft
**Last Updated:** July 2026

---

## Overview

OpsPilot is designed as a modular, extensible, and maintainable command-line application for Linux system administration and DevOps automation.

Rather than becoming a large monolithic script, every feature should exist as an independent module that can evolve without affecting the rest of the project.

The architecture emphasizes:

* Modularity
* Simplicity
* Testability
* Extensibility
* Maintainability

---

## Design Principles

OpsPilot follows several architectural principles.

### Single Responsibility Principle

Every module should have one responsibility.

Examples:

* CPU module → CPU information
* Disk module → Disk usage
* Network module → Network inspection
* Backup module → Backup management

A module should never attempt to perform unrelated tasks.

---

### Modular Design

Every command should be implemented independently.

Instead of one file containing thousands of lines of code:

```text
main.py
```

the project should be structured like this:

```text
commands/
    cpu.py
    disk.py
    memory.py
    network.py
    info.py
```

Adding a new command should require little or no modification to existing modules.

---

### Readability First

Code should prioritize clarity over cleverness.

Readable code is easier to maintain, debug, test, and review.

Whenever two implementations achieve the same result, choose the one that is easier to understand.

---

### Standard Library First

Whenever possible, prefer Python's standard library before introducing third-party dependencies.

For example:

* pathlib
* argparse
* subprocess
* shutil
* logging
* platform

Only introduce external packages when they provide significant value.

---

## High-Level Architecture

```text
                    User
                      │
                      ▼
             Command Line Interface
                      │
                      ▼
                Command Router
                      │
        ┌─────────────┼─────────────┐
        ▼             ▼             ▼
   System Info      Monitoring     Utilities
        │             │             │
        └─────────────┼─────────────┘
                      ▼
                Linux Operating System
```

---

## Project Structure

```text
opspilot/
│
├── assets/
│
├── docs/
│   ├── architecture.md
│   ├── dev_log.md
│   ├── prd.md
│   └── roadmap.md
│
├── scripts/
│
├── src/
│   └── opspilot/
│       │
│       ├── commands/
│       ├── utils/
│       ├── cli.py
│       ├── main.py
│       └── __init__.py
│
├── tests/
│
├── CHANGELOG.md
├── CONTRIBUTING.md
├── LICENSE
├── pyproject.toml
└── README.md
```

---

## Module Responsibilities

### main.py

Project entry point.

Responsibilities:

* Start the application.
* Initialize the CLI.
* Handle program exit.

---

### cli.py

Responsible for:

* Parsing command-line arguments.
* Registering commands.
* Dispatching execution.

The CLI should not contain business logic.

---

### commands/

Each command should live in its own module.

Example:

```text
commands/
    cpu.py
    memory.py
    disk.py
    network.py
    info.py
```

Each module should expose a single public function:

```python
def run(args):
    ...
```

---

### utils/

Shared helper functions.

Examples:

* Formatters
* Logging helpers
* Shell execution
* Validation
* Common utilities

Utilities should never depend on command modules.

---

### tests/

Every command module should eventually have corresponding unit tests.

Example:

```text
tests/
    test_cpu.py
    test_disk.py
    test_memory.py
```

---

## Command Execution Flow

```text
User

↓

main.py

↓

cli.py

↓

Selected Command

↓

Business Logic

↓

Linux System

↓

Output Formatter

↓

Terminal
```

Each layer should have a clearly defined responsibility.

---

## Error Handling

OpsPilot should fail gracefully.

Principles:

* Never expose raw stack traces to users during normal operation.
* Display clear, actionable error messages.
* Return appropriate exit codes.
* Log unexpected exceptions for debugging.

Example:

```text
✓ Backup completed successfully.

✗ Failed to access directory:
/home/user/Documents

Reason:
Permission denied.
```

---

## Logging Strategy

Logging should support troubleshooting while keeping user-facing output clean.

Future versions should implement:

* INFO
* WARNING
* ERROR
* DEBUG

Log files should be stored separately from application code.

---

## Configuration

Future releases should support a centralized configuration file.

Possible location:

```text
~/.config/opspilot/config.toml
```

Configuration may include:

* Default backup location
* Log level
* Output format
* Theme preferences
* Plugin settings

---

## Dependency Philosophy

Dependencies should be introduced cautiously.

Preferred order:

1. Python Standard Library
2. Well-maintained third-party packages
3. Custom implementations only when necessary

This keeps the project lightweight and secure.

---

## Testing Strategy

The project will use:

* pytest
* Unit tests
* Integration tests
* Regression tests (future)

Every new feature should include tests whenever practical.

---

## Documentation Strategy

Documentation is treated as a first-class component of the project.

Major features should include:

* User documentation
* Developer documentation
* Inline docstrings
* Type hints
* Examples where appropriate

---

## Future Architecture

As OpsPilot grows, additional modules may include:

```text
commands/
    backup.py
    restore.py
    logs.py
    services.py
    cron.py
    docker.py
    kubernetes.py
    cloud.py
    monitor.py
    security.py
```

The modular architecture allows these additions without disrupting existing functionality.

---

## Architectural Goals

The architecture should remain:

* Simple enough for beginners to understand.
* Flexible enough for future expansion.
* Easy to test.
* Easy to maintain.
* Easy for contributors to navigate.

Every architectural decision should support the long-term vision of OpsPilot as a modern, production-quality DevOps automation platform.
