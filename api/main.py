from http.client import HTTPException

from fastapi import FastAPI
from services.movie_service import MovieService
from services.user_service import UserService
from src.movie import Movie

app = FastAPI()

movie_service = MovieService()
user_service = UserService()


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

@app.get("/api/users/{user_id}/watchlist")
def get_watchlist(user_id: str):
    try:
        return {"user_id": user_id, "watchlist": user_service.get_watchlist(user_id)}
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

@app.post("/api/users/{user_id}/watchlist")
def add_to_watchlist(user_id: str, movie_id: str):
    try:
        watchlist = user_service.add_to_watchlist(user_id, movie_id)
        return {"message": "Movie added to watchlist", "watchlist": watchlist}
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

@app.delete("/api/users/{user_id}/watchlist/{movie_id}")
def remove_from_watchlist(user_id: str, movie_id: str):
    try:
        watchlist = user_service.remove_from_watchlist(user_id, movie_id)
        return {"message": "Movie removed from watchlist", "watchlist": watchlist}
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))