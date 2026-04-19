stateDiagram-v2
    direction LR

    state "User Account" as UserAccount {
        [*] --> Registered
        Registered --> LoggedIn : login
        LoggedIn --> LoggedOut : logout
        LoggedIn --> Suspended : violation
        Suspended --> LoggedOut : admin action
    }

    state "Movie Data" as MovieData {
        [*] --> Available
        Available --> Updated : edit
        Updated --> Available
        Available --> Removed : delete
    }

    state "User Feedback" as Feedback {
        [*] --> Submitted
        Submitted --> Stored : valid
        Submitted --> Rejected : invalid
    }

    state "Recommendation" as Recommendation {
        [*] --> Requested
        Requested --> Processing
        Processing --> Generated : success
        Processing --> Failed : error
        Generated --> Displayed
    }

    state "Bulk Upload" as Upload {
        [*] --> Uploaded
        Uploaded --> Validated
        Validated --> Stored : valid
        Validated --> Rejected : invalid
    }

    state "Search Logic" as Search {
        [*] --> Idle
        Idle --> Searching
        Searching --> ResultsDisplayed : found
        Searching --> NoResults : none
    }

    state "System Health" as Health {
        [*] --> Running
        Running --> Overloaded : high load
        Overloaded --> Stable : resolved
        Stable --> Running
    }