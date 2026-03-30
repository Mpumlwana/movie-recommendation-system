# Test Cases For a Movie Recommendation System

## Functional Test Cases

| Test Case ID | Requirement ID | Description | Steps | Expected Result | Actual Result | Status |
|-------------|---------------|-------------|-------|----------------|---------------|--------|
| TC-001 | FR1 | User login | 1. Open login page 2. Enter username 3. Enter password 4. Click login | User redirected to dashboard within ≤2 seconds | | |
| TC-002 | FR2 | Search movie | 1. Enter movie title 2. Click search | Results displayed within ≤2 seconds | | |
| TC-003 | FR3 | Rate movie | 1. Select movie 2. Submit rating | Rating saved successfully | | |
| TC-004 | FR4 | Get recommendations | 1. Request recommendations | Recommendations displayed with ≥85% relevance | | |
| TC-005 | FR5 | View history | 1. Open watch history | History displayed correctly | | |
| TC-006 | FR6 | View details | 1. Click movie | Movie details displayed within ≤2 seconds | | |
| TC-007 | FR7 | Manage users | 1. Admin edits user 2. Save changes | Changes saved within ≤3 seconds | | |
| TC-008 | FR12 | Import dataset | 1. Upload dataset 2. Submit | Dataset stored successfully | | |

---

## Non-Functional Test Cases

### Test Type: Performance
**Steps:** Simulate 1000 concurrent users performing searches  
**Expected Result:** Response time ≤ 2 seconds  

### Test Type: Security
**Steps:** Attempt login without credentials  
**Expected Result:** Access denied and attempt logged  

---

**Note:** Actual Result and Status will be filled after execution (Pass/Fail)