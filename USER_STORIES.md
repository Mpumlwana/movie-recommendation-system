# User Stories For a Movie Recommendation System

---

| Story ID | User Story | Related Requirement | Acceptance Criteria | Priority |
|----------|-----------|---------------------|--------------------|----------|
| US-001 | As a user, I want to register and log in so that I can access the system | FR1 | Login completes ≤2 seconds AND redirects to dashboard AND no errors | High |
| US-002 | As a user, I want to search movies so that I can find content quickly | FR2 | Results load ≤2 seconds AND correct movies displayed AND no errors | High |
| US-003 | As a user, I want to rate movies so that I get better recommendations | FR3 | Rating saved instantly AND stored correctly AND updates recommendations | High |
| US-004 | As a user, I want recommendations so that I discover movies | FR4 | Recommendations generated ≤2 seconds AND ≥85% relevance AND no duplicates | High |
| US-005 | As a user, I want to view movie details so that I understand content | FR6 | Details load ≤2 seconds AND include title, genre, rating AND no missing data | High |
| US-006 | As an admin, I want to manage users so that I maintain system control | FR7 | User updates saved ≤3 seconds AND changes reflected correctly | Medium |
| US-007 | As a content manager, I want to update movie data so that info is accurate | FR8 | Updates saved ≤3 seconds AND visible in system AND no data loss | Medium |
| US-008 | As a data scientist, I want to import datasets so that I train models | FR12 | Dataset imported ≥95% accuracy AND no corruption AND processed successfully | High |
| US-009 | As a system admin, I want to monitor system so that performance is stable | FR10 | Metrics updated every ≤5 seconds AND system uptime visible | Medium |
| US-010 | As a marketing team member, I want analytics so that I understand users | FR11 | Reports generated ≤5 seconds AND data accurate AND readable | Medium |
| US-011 | As a system admin, I want secure authentication so that data is protected | NFR10 | Unauthorized access blocked AND login attempts logged AND data protected | High |
| US-012 | As a system, I want to handle 1000 users so that performance scales | NFR7 | System supports 1000 users AND no slowdown AND response ≤2 seconds | High |