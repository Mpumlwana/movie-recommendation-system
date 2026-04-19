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

stateDiagram-v2
[*] --> Available
Available --> Updated : edit
Updated --> Available
Available --> Removed : delete

stateDiagram-v2
[*] --> Submitted
Submitted --> Stored : valid
Submitted --> Rejected : invalid

stateDiagram-v2
[*] --> Requested
Requested --> Processing
Processing --> Generated : success
Processing --> Failed : error
Generated --> Displayed

stateDiagram-v2
[*] --> Uploaded
Uploaded --> Validated
Validated --> Stored : valid
Validated --> Rejected : invalid

stateDiagram-v2
[*] --> Idle
Idle --> Searching
Searching --> ResultsDisplayed : found
Searching --> NoResults : none


