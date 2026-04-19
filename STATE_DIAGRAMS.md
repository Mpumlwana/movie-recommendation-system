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
```

---

## Movies can be updated or removed from the system.

```mermaid
stateDiagram-v2
[*] --> Available
Available --> Updated : edit
Updated --> Available
Available --> Removed : delete
```

---

## Ratings are validated before being stored.

```mermaid
stateDiagram-v2
[*] --> Submitted
Submitted --> Stored : valid
Submitted --> Rejected : invalid
```

---

## Recommendations are processed and shown to the user.

```mermaid
stateDiagram-v2
[*] --> Requested
Requested --> Processing
Processing --> Generated : success
Processing --> Failed : error
Generated --> Displayed
```

---

## Datasets are validated before being stored.

```mermaid
stateDiagram-v2
[*] --> Uploaded
Uploaded --> Validated
Validated --> Stored : valid
Validated --> Rejected : invalid
```

---

## Search either returns results or none.

```mermaid
stateDiagram-v2
[*] --> Idle
Idle --> Searching
Searching --> ResultsDisplayed : found
Searching --> NoResults : none
```

---

## System handles load and returns to stable state.

```mermaid
stateDiagram-v2
[*] --> Running
Running --> Overloaded : high load
Overloaded --> Stable : resolved
Stable --> Running
```

---