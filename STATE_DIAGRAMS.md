---

```markdown
# Activity Diagrams — Movie Recommendation System

---

## 1. User Login Workflow

```mermaid
flowchart TD
Start --> EnterCredentials
EnterCredentials --> Validate
Validate -->|Valid| LoginSuccess
Validate -->|Invalid| Error
LoginSuccess --> End
Error --> End