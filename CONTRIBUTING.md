# Contributing to OpsPilot

First off, thank you for your interest in contributing to **OpsPilot**! 🎉

Whether you're fixing a bug, improving documentation, proposing a new feature, or refining the user experience, your contributions are appreciated.

Our goal is to build a modern, reliable, and approachable DevOps automation platform for the Linux community.

---

## Code of Conduct

We are committed to fostering a welcoming, respectful, and inclusive community.

Be kind.

Be constructive.

Assume good intent.

Provide helpful feedback.

Treat everyone with respect.

---

## Before You Start

Please:

* Read the project documentation.
* Search existing Issues before opening a new one.
* Check the project roadmap to understand current priorities.
* Keep discussions respectful and focused on improving the project.

---

## Development Philosophy

OpsPilot follows a few guiding principles:

* Simplicity over complexity.
* Readability over cleverness.
* Automation over repetition.
* Security by default.
* Documentation is part of the product.
* Every feature should be maintainable.

When in doubt, choose the solution that is easiest to understand and maintain.

---

## Ways to Contribute

You can contribute by:

* Fixing bugs
* Improving documentation
* Adding tests
* Optimizing performance
* Refactoring code
* Suggesting new features
* Improving accessibility
* Enhancing the CLI experience
* Reporting issues
* Reviewing pull requests

Every contribution matters.

---

## Getting Started

Clone the repository:

```bash
git clone https://github.com/ikwukao/opspilot.git
```

Move into the project:

```bash
cd opspilot
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it:

Linux/macOS

```bash
source .venv/bin/activate
```

Install the project:

```bash
pip install -e .
```

---

## Branch Naming

Use descriptive branch names.

Examples:

```text
feature/system_info

feature/docker_support

feature/log_parser

bugfix/cpu_parser

bugfix/memory_report

docs/readme_update

docs/architecture

refactor/cli_router

test/process_module

chore/update_dependencies
```

Avoid generic names such as:

```text
new

fix

test

update
```

---

## Commit Messages

OpsPilot follows the **Conventional Commits** specification.

Examples:

```text
feat(cli): add CPU information command

feat(backup): implement archive compression

fix(network): handle missing interfaces

refactor(commands): simplify command dispatcher

docs(readme): update installation guide

test(cpu): add unit tests

chore(deps): upgrade project dependencies
```

---

## Coding Standards

## Python

* Follow PEP 8.
* Use type hints.
* Prefer `pathlib` over `os.path`.
* Write descriptive variable names.
* Keep functions focused on one responsibility.

---

## Go

* Follow standard Go formatting (`gofmt`).
* Keep packages cohesive.
* Handle errors explicitly.
* Favor composition over inheritance.

---

## Bash

* Use `#!/usr/bin/env bash`.
* Enable strict mode where appropriate.
* Quote variables.
* Write portable scripts whenever possible.

---

## Documentation

Documentation is a first-class citizen.

New features should include updates to:

* README (when user-facing)
* Architecture documentation (when design changes)
* Roadmap (when milestones change)
* Changelog (for released changes)

---

## Testing

Every new feature should include tests whenever practical.

Future tooling will include:

* pytest
* GitHub Actions
* Integration tests
* Static analysis
* Linting

Code that isn't tested should be clearly identified if testing isn't yet feasible.

---

## Pull Requests

Before opening a Pull Request:

* Ensure your branch is up to date.
* Run tests locally.
* Update documentation if needed.
* Keep changes focused on a single objective.
* Write a clear PR description explaining the motivation and impact of the change.

Small, focused pull requests are easier to review and merge.

---

## Reporting Bugs

When reporting a bug, include:

* Operating system
* Python version
* Go version (if applicable)
* Steps to reproduce
* Expected behavior
* Actual behavior
* Error messages or logs

Providing this information helps us reproduce and resolve issues more quickly.

---

## Suggesting Features

Feature requests should explain:

* The problem being solved.
* The proposed solution.
* Possible alternatives.
* Any potential trade-offs.

Well-defined proposals are easier to evaluate and discuss.

---

## Recognition

Every contributor helps improve OpsPilot.

Whether you fix a typo, write documentation, or implement a major feature, your work is valued and appreciated.

Thank you for helping build OpsPilot.
