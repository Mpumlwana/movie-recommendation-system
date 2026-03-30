
```markdown id="final_specs"
# Use Case Specifications — Movie Recommendation System

---

## UC1: Register/Login
**Actor:** User  
**Related Requirement:** FR1  
**Description:** Allows users to access the system  
**Precondition:** User has valid credentials  
**Postcondition:** User is logged in  

**Basic Flow:**
1. User enters username  
2. User enters password  
3. System validates credentials  
4. User is logged in  

**Alternative Flow:**
- Invalid credentials → error message displayed  

---

## UC2: Search Movies
**Actor:** User  
**Related Requirement:** FR2  
**Description:** Search movies by title or genre  
**Precondition:** User is logged in  
**Postcondition:** Results displayed  

**Basic Flow:**
1. User enters search query  
2. User clicks search  
3. System retrieves results  
4. Results displayed  

**Alternative Flow:**
- No results → system shows "No movies found"  

---

## UC3: Rate Movie
**Actor:** User  
**Related Requirement:** FR3  
**Description:** Rate a movie  
**Precondition:** User logged in  
**Postcondition:** Rating stored  

**Basic Flow:**
1. User selects movie  
2. User submits rating  
3. System saves rating  

**Alternative Flow:**
- Invalid rating → error displayed  

---

## UC4: Get Recommendations
**Actor:** User  
**Related Requirement:** FR4  
**Description:** Generate personalized recommendations  
**Precondition:** User has watch history  
**Postcondition:** Recommendations displayed  

**Basic Flow:**
1. User requests recommendations  
2. System processes user data  
3. System generates recommendations  
4. Results displayed  

**Alternative Flow:**
- No history → system shows default recommendations  

---

## UC5: View Movie Details
**Actor:** User  
**Related Requirement:** FR6  
**Description:** View detailed movie information  
**Precondition:** Movie selected  
**Postcondition:** Details displayed  

**Basic Flow:**
1. User selects movie  
2. System loads details  
3. Details displayed  

**Alternative Flow:**
- Data missing → partial information displayed  

---

## UC6: Manage Users
**Actor:** Admin  
**Related Requirement:** FR7  
**Description:** Manage user accounts  
**Precondition:** Admin logged in  
**Postcondition:** User updated  

**Basic Flow:**
1. Admin selects user  
2. Admin edits/deletes user  
3. System saves changes  

**Alternative Flow:**
- Invalid operation → error message  

---

## UC7: Update Movie Data
**Actor:** Content Manager  
**Related Requirement:** FR8  
**Description:** Update movie database  
**Precondition:** Access granted  
**Postcondition:** Data updated  

**Basic Flow:**
1. Select movie  
2. Edit details  
3. Save changes  

**Alternative Flow:**
- Invalid data → rejected  

---

## UC8: Import Dataset
**Actor:** Data Scientist  
**Related Requirement:** FR12  
**Description:** Import external datasets  
**Precondition:** Dataset available  
**Postcondition:** Data stored  

**Basic Flow:**
1. Upload dataset  
2. System validates data  
3. System stores dataset  

**Alternative Flow:**
- Corrupt file → upload rejected  