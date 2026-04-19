# State Transition Diagrams For a Movie Recommendation System

---

## 1. User Account State

```mermaid
stateDiagram-v2
[*] --> Registered
Registered --> LoggedIn : login
LoggedIn --> LoggedOut : logout
LoggedIn --> Suspended : violation
Suspended --> LoggedOut : admin action

Explanation

This workflow shows how a user logs into the system (FR1, US-001).

2. Search Movies Workflow
Explanation

This supports movie searching functionality (FR2, US-002).

3. Rate Movie Workflow
Explanation

Handles rating submission and validation (FR3, US-003).

4. Recommendation Workflow
Explanation

Generates personalized recommendations (FR4, US-004).

5. Import Dataset Workflow
Explanation

Handles dataset upload and validation (FR12, US-008).

6. View Movie Details
Explanation

Displays movie information (FR6, US-005).

7. Manage Users Workflow
Explanation

Admin manages user accounts (FR7, US-006).

8. System Monitoring Workflow
Explanation

Monitors system performance (FR10, US-009).