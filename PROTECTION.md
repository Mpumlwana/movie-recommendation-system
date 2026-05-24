# Branch Protection Rules

## Overview

Branch protection rules were added to protect the `main` branch from unstable or untested code.

---

## Rules Applied

### 1. Require Pull Request Reviews

At least one review is required before merging changes into the main branch.

This helps improve code quality and prevents accidental mistakes.

---

### 2. Require Status Checks to Pass

The CI workflow must complete successfully before pull requests can be merged.

This ensures that:
- All tests pass
- The system remains stable
- Bugs are detected early

---

### 3. Disable Direct Pushes

Direct commits to the `main` branch are restricted.

All changes must go through:
- Feature branches
- Pull requests
- Automated testing

---

## Benefits

These rules improve:
- Collaboration
- Code quality
- Security
- Reliability
- Continuous Integration practices

Branch protection is an important industry-standard DevOps practice.