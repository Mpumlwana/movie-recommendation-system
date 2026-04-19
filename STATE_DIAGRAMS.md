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