# Activity Diagrams For a Movie Recommendation System

---

## 1. User Login Workflow: Handles authentication (FR1, US-001).

```mermaid
flowchart TD
Start --> EnterCredentials
EnterCredentials --> Validate
Validate -->|Valid| LoginSuccess
Validate -->|Invalid| Error
LoginSuccess --> End
Error --> End
```

---

## Search Movies Workflow: Supports movie discovery (FR2, US-002).

```mermaid
flowchart TD
Start --> EnterQuery
EnterQuery --> SearchSystem
SearchSystem --> Results
Results --> End
```

---

## Rate Movie Workflow: 

```mermaid
flowchart TD
Start --> SelectMovie
SelectMovie --> SubmitRating
SubmitRating --> ValidateRating
ValidateRating -->|Valid| SaveRating
ValidateRating -->|Invalid| Error
SaveRating --> End
Error --> End
```

---

## Recommendation Workflow

```mermaid
flowchart TD
Start --> RequestRec
RequestRec --> ProcessData
ProcessData --> GenerateRec
GenerateRec --> DisplayRec
DisplayRec --> End
```

---

## Import Dataset Workflow

```mermaid
flowchart TD
Start --> UploadFile
UploadFile --> ValidateData
ValidateData -->|Valid| StoreData
ValidateData -->|Invalid| Reject
StoreData --> End
Reject --> End
```

---

## View Movie Details

```mermaid
flowchart TD
Start --> SelectMovie
SelectMovie --> LoadDetails
LoadDetails --> DisplayDetails
DisplayDetails --> End
```

---

## Manage Users Workflow

```mermaid
flowchart TD
Start --> SelectUser
SelectUser --> ModifyUser
ModifyUser --> SaveChanges
SaveChanges --> End
```

---

## System Monitoring Workflow

```mermaid
flowchart TD
Start --> MonitorSystem
MonitorSystem --> DetectIssue
DetectIssue -->|Yes| FixIssue
DetectIssue -->|No| Continue
FixIssue --> Continue
Continue --> End
```

---