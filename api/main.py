from fastapi import FastAPI
from services.movie_service import MovieService
from src.movie import Movie

app = FastAPI()

movie_service = MovieService()


@app.get("/")
def home():
    return {"message": "Movie Recommendation System API"}


@app.get("/api/movies")
def get_movies():
    return movie_service.get_all_movies()


@app.post("/api/movies")
def add_movie(movie_id: str, title: str, genre: str):

    movie = Movie(movie_id, title, genre)

    movie_service.add_movie(movie)

    return {
        "message": "Movie added successfully",
        "movie": movie.__dict__
    }


@app.post("/api/movies/{movie_id}/checkout")
def checkout_movie(movie_id: str):

    movie = movie_service.checkout_movie(movie_id)

    return {
        "message": f"Movie {movie_id} checked out",
        "movie": movie.__dict__
    }