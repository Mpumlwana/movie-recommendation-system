# Class Diagram For a Movie Recommendation System

```mermaid
classDiagram

class User {
  -userId: String
  -name: String
  -email: String
  +login()
  +rateMovie()
  +getRecommendations()
}

class Movie {
  -movieId: String
  -title: String
  -genre: String
  +getDetails()
  +updateMovie()
}

class Rating {
  -ratingId: String
  -score: int
  +submitRating()
  +validateRating()
}

class Recommendation {
  -recommendationId: String
  -generatedDate: Date
  +generateRecommendations()
  +displayRecommendations()
}

class Dataset {
  -datasetId: String
  -source: String
  +uploadDataset()
  +validateDataset()
}

class Search {
  -query: String
  +searchMovies()
}

class Admin {
  -adminId: String
  +manageUsers()
  +manageMovies()
}

User "1" -- "0..*" Rating : gives
Movie "1" -- "0..*" Rating : receives

User "1" -- "0..*" Recommendation : gets
Recommendation "1" *-- "1" Dataset : uses

User "1" -- "0..*" Search : performs

Admin "1" -- "0..*" User : manages
Admin "1" -- "0..*" Movie : manages