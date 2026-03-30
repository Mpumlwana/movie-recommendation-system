# Use Case Diagram For a Movie Recommendation System

## Use Case Diagram

```mermaid
graph TD

User["User (Viewer)"]
Admin["Admin"]
DataScientist["Data Scientist"]
SysAdmin["System Administrator"]
ContentManager["Content Manager"]
Marketing["Marketing Team"]
External["External Data Provider"]

UC1["Register / Login"]
UC2["Search Movies"]
UC3["Rate Movie"]
UC4["Get Recommendations"]
UC5["View Movie Details"]
UC6["Manage Users"]
UC7["Update Movie Data"]
UC8["View Analytics"]
UC9["Monitor System"]
UC10["Import Dataset"]

User --> UC1
User --> UC2
User --> UC3
User --> UC4
User --> UC5

Admin --> UC6
ContentManager --> UC7
Marketing --> UC8
SysAdmin --> UC9

DataScientist --> UC4
DataScientist --> UC10

External --> UC10

%% Relationships
UC4 -->|<<include>>| UC3
UC2 -->|<<extend>>| UC5