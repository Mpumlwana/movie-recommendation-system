from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)


def test_home():
    response = client.get("/")

    assert response.status_code == 200


def test_add_movie():
    response = client.post(
        "/api/movies",
        params={"movie_id": "10", "title": "Arrival", "genre": "Sci-Fi"},
    )

    body = response.json()

    assert response.status_code == 200
    assert body["message"] == "Movie added successfully"
    assert body["movie"]["movie_id"] == "10"
    assert body["movie"]["title"] == "Arrival"
    assert body["movie"]["genre"] == "Sci-Fi"


def test_checkout_movie():
    client.post(
        "/api/movies",
        params={"movie_id": "11", "title": "Dune", "genre": "Sci-Fi"},
    )

    response = client.post("/api/movies/11/checkout")

    body = response.json()

    assert response.status_code == 200
    assert body["message"] == "Movie 11 checked out"
    assert body["movie"]["status"] == "Checked Out"