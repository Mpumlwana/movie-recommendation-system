from creational_patterns.prototype import MoviePrototype
from creational_patterns.singleton import DatabaseConnection
from creational_patterns.builder import RecommendationBuilder
from creational_patterns.simple_factory import MovieFactory


def test_prototype():
    m1 = MoviePrototype("Inception")
    m2 = m1.clone()

    assert m1.title == m2.title


def test_singleton():
    db1 = DatabaseConnection()
    db2 = DatabaseConnection()

    assert db1 is db2


def test_builder():
    builder = RecommendationBuilder()
    result = builder.add_data().build_model().get_result()

    assert "Data added" in result
    assert "Model built" in result


def test_simple_factory():
    movie = MovieFactory.create_movie("action")

    assert movie == "Action Movie Created"