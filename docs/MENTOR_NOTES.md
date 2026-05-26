# Mentor Notes

## Why this project exists
I built this project to demonstrate core Python OOP and state management in a small but complete product flow.

## Technical decisions
- Kept domain classes explicit (`Book`, `Reader`, `Library`) for readability over abstraction.
- Used JSON persistence to keep the project easy to run without infrastructure.
- Added tests on the core flow (borrow/return/save/load) to show repeatable behavior.

## Build vs polish
- Build phase: classes, business rules, persistence, tests.
- Polish phase: README clarity, screenshots, and naming cleanup (`digital-library`).

## What I learned
- Deterministic business rules are easier to test and explain.
- Small projects become interview-ready when structure + tests + docs are aligned.
