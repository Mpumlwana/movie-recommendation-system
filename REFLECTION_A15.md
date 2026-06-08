# Reflection – Assignment 15

## Introduction

Assignment 15 provided an opportunity to experience real-world collaborative software development through contributions to classmates' repositories. Unlike previous assignments that focused on developing my own project, this assignment required me to understand other developers' codebases, follow their contribution guidelines, and participate in the pull request review process across three different projects built with different technology stacks.

---

## Contribution Experience

I contributed to three classmates' repositories, each presenting unique challenges and learning opportunities:

**University Research Collaboration Platform (Python/FastAPI)** — I added an `ISSUE_LABELS.md` documentation file that categorized all open issues by label type. This helped new contributors identify beginner-friendly tasks and understand the project roadmap more clearly.

**Finance Management System (Java/Spring Boot)** — I fixed a critical bug where all PUT/update API endpoints were returning HTTP 500 errors due to completely unhandled exceptions. I refactored three controller files to use `ResponseEntity<?>` with proper `try/catch` blocks, null checks, and meaningful HTTP status codes.

**Campus Lost and Found (Node.js/Jest)** — I wrote 27 comprehensive edge-case tests for the `ItemReportBuilder` class, covering missing required fields, empty string validation, optional field defaults, builder reuse via `reset()`, and Director pattern recipes.

Before making any contribution, I reviewed each repository's `CONTRIBUTING.md`, `README`, and open issues. This helped me understand project requirements and identify where I could add value without disrupting existing functionality.

---

## Challenges Faced

**Understanding unfamiliar codebases** was the biggest challenge. Each repository used a different programming language and architecture — Python FastAPI, Java Spring Boot, and Node.js — requiring me to quickly adapt my thinking and match each project's conventions.

**CI/CD pipeline failures** presented an unexpected challenge. When contributing tests to the Campus Lost and Found project, my initial test file failed the Jest CI pipeline because the expected error messages in the tests did not exactly match the error messages thrown by the actual code. This required careful debugging and iterative fixes to align the test assertions with the real implementation.

**Branch management** across multiple repositories simultaneously required discipline. Keeping branches named clearly and linked to specific issues helped avoid confusion when switching between projects.

**Coordinating with repository owners** required patience. Getting PRs reviewed and merged depended entirely on classmates' availability, which was outside my control.

---

## Open-Source Collaboration Lessons

This assignment reinforced the value of **clear documentation and contribution guidelines**. Projects with well-written `CONTRIBUTING.md` files and labeled issues were significantly easier to contribute to than those without.

I also learned that **small, focused pull requests are far more effective** than large ones. Each of my PRs addressed exactly one issue, making them easy to review and quick to merge.

**Reading the existing code before writing new code** was essential. In the Finance Management System, I had to understand the existing controller structure before writing fixes that matched the project's patterns. Submitting code that looked foreign to the codebase would have reduced the chances of acceptance.

Finally, **CI must pass before requesting review**. Two of my three PRs required fixes after the initial submission because CI pipelines caught issues I had missed locally. This taught me to test more carefully before pushing.

---

## Professional Growth

This assignment simulated real-world open-source development practices used by professional software teams. Through issue tracking, pull requests, code reviews, and CI/CD validation, I gained experience that closely mirrors industry workflows on platforms like GitHub.

Working across Java, Python, and JavaScript projects in a single assignment also strengthened my ability to read and contribute to code written in languages I do not use as my primary tool — a critical skill in professional software development environments.

---

## Conclusion

Overall, Assignment 15 was the most realistic simulation of professional software development in the entire course. It improved my communication skills, exposed me to different coding styles and architectures, and provided practical experience contributing to external projects under real constraints. The 2 merged pull requests I achieved represent genuine improvements to classmates' codebases, which is a more meaningful outcome than any solo assignment deliverable.