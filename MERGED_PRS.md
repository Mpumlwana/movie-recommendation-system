# Merged Pull Requests – Assignment 15

## PR 1 ✅ Merged

**Repository:** https://github.com/Ngandana/university-research-collaboration-platform

**Pull Request Link:** https://github.com/Ngandana/university-research-collaboration-platform/pull/67

**Issue Addressed:** #61 — Label existing issues as good-first-issue and feature-request

**Summary:**
Added `ISSUE_LABELS.md` to the root of the repository. This file categorizes all open issues by label type (`good-first-issue`, `feature-request`, `security`) to help new contributors quickly find suitable tasks. The file documents 15 good-first issues across all development phases and 13 feature-request issues, improving contributor discoverability and onboarding.

**Files Changed:**
- `ISSUE_LABELS.md` (added)

**Status:** ✅ Merged by Ngandana

---

## PR 2 ✅ Merged

**Repository:** https://github.com/BokaMokoena/Finance-Management-System

**Pull Request Link:** https://github.com/BokaMokoena/Finance-Management-System/pull/22

**Issue Addressed:** #16 — Fix error 500 on all PUT/update API endpoints

**Summary:**
All PUT endpoints across `TransactionController`, `BudgetController`, and `UserController` were returning HTTP 500 errors because exceptions were completely unhandled. Fixed by:
- Wrapping all endpoints in `try/catch` blocks
- Returning proper HTTP status codes (400 Bad Request, 404 Not Found, 500 Internal Server Error)
- Adding null and range checks on all PUT input parameters
- Using `ResponseEntity<?>` return type for full control over responses
- Adding descriptive error messages instead of raw stack traces

**Files Changed:**
- `TransactionController.java` (modified)
- `BudgetController.java` (modified)
- `UserController.java` (modified)

**Status:** ✅ Merged by BokaMokoena

---

## PR 3 🟡 Awaiting Review

**Repository:** https://github.com/Skiet88/campus-lost-and-found

**Pull Request Link:** https://github.com/Skiet88/campus-lost-and-found/pull/51

**Issue Addressed:** #26 — Add edge-case tests for ItemReportBuilder

**Summary:**
Added a comprehensive edge-case test file `test_ItemReportBuilder.edge.js` with 27 tests across 7 test groups covering:
- Missing required fields (all 6 required fields)
- Empty string and whitespace-only values
- Optional fields (`imageUrl` defaults to null, `category` defaults to `GENERAL`)
- Successful builds for both LOST and FOUND reports
- Builder reuse via `reset()`
- Fluent interface / method chaining verification
- Director recipes (`buildMinimalLostReport` and `buildFullFoundReport`)

**Files Changed:**
- `tests/test_ItemReportBuilder.edge.js` (added)

**Status:** 🟡 Open — awaiting approval from Skiet88

---

## Contribution Summary

| Metric | Count |
|---|---|
| Total Pull Requests Submitted | 3 |
| Total Pull Requests Merged | 2 |
| Feature Requests Completed | 1 |
| Bug Fixes | 1 |
| Documentation Contributions | 1 |

---

## Lessons Learned

- Communicating on issues before coding avoids duplicate work
- Small, focused PRs are reviewed and merged faster
- Following the existing code style increases acceptance rate
- CI pipelines must pass before maintainers will consider merging
- Different projects use different tech stacks — adaptability is key