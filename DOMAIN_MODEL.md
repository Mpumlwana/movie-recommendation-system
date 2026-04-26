# Domain Model For a Movie Recommendation System

## Overview
The domain model represents the key entities in the Movie Recommendation System and their relationships.

---

## Classes

### 1. User
Attributes:
- userId: String
- name: String
- email: String

Methods:
- login()
- rateMovie()
- getRecommendations()

---

### 2. Movie
Attributes:
- movieId: String
- title: String
- genre: String

Methods:
- getDetails()
- updateMovie()

---

### 3. Rating
Attributes:
- ratingId: String
- score: int

Methods:
- submitRating()
- validateRating()

---

### 4. Recommendation
Attributes:
- recommendationId: String
- generatedDate: Date

Methods:
- generateRecommendations()
- displayRecommendations()

---

### 5. Dataset
Attributes:
- datasetId: String
- source: String

Methods:
- uploadDataset()
- validateDataset()

---

### 6. Search
Attributes:
- query: String

Methods:
- searchMovies()

---

### 7. Admin
Attributes:
- adminId: String

Methods:
- manageUsers()
- manageMovies()

---

## Relationships

- A User can rate many Movies.
- A Movie can have many Ratings.
- A User receives Recommendations.
- Recommendation uses Dataset.
- Admin manages Users and Movies.

---

## Relationship Details

- User (1) → Rating (0..*): A user can give many ratings.
- Movie (1) → Rating (0..*): A movie can receive many ratings.
- User (1) → Recommendation (0..*): A user can receive multiple recommendations.
- Recommendation (1) → Dataset (1): Recommendations are generated from a dataset.
- User (1) → Search (0..*): A user can perform multiple searches.
- Admin (1) → User (0..*): Admin manages users.
- Admin (1) → Movie (0..*): Admin manages movies.