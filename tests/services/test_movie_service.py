from services.movie_service import MovieService
from src.movie import Movie


def test_add_movie():

    service = MovieService()

    movie = Movie("1", "Inception", "Sci-Fi")

    service.add_movie(movie)

    result = service.get_movie("1")

    assert result.title == "Inception"


def test_checkout_movie():

    service = MovieService()

    movie = Movie("2", "Avatar", "Action")

    service.add_movie(movie)

    service.checkout_movie("2")

    result = service.get_movie("2")

    assert result.status == "Checked Out"


def test_get_movie():

    service = MovieService()

    movie = Movie("3", "Titanic", "Drama")

    service.add_movie(movie)

    result = service.get_movie("3")

    assert result.movie_id == "3"


def test_get_all_movies():

    service = MovieService()

    movie1 = Movie("4", "John Wick", "Action")
    movie2 = Movie("5", "Frozen", "Animation")

    service.add_movie(movie1)
    service.add_movie(movie2)

    result = service.get_all_movies()

    assert len(result) == 2


def test_delete_movie():

    service = MovieService()

    movie = Movie("6", "Black Panther", "Action")

    service.add_movie(movie)

    service.delete_movie("6")

    result = service.get_movie("6")

    assert result is None


def test_checkout_movie_not_found():

    service = MovieService()

    try:

        service.checkout_movie("999")

        assert False

    except Exception as e:

        assert str(e) == "Movie not found"