"""
tests/test_input_validation.py
Input validation tests for creational pattern classes.
Addresses issue #17 — Validate movie input data.
"""

import pytest
from creational_patterns.simple_factory import MovieFactory
from creational_patterns.builder import RecommendationBuilder
from creational_patterns.prototype import MoviePrototype
from creational_patterns.singleton import DatabaseConnection


# ── MovieFactory (SimpleFactory) ─────────────────────────────────────────────

class TestMovieFactoryValidation:
    def test_creates_action_movie(self):
        assert MovieFactory.create_movie("action") == "Action Movie Created"

    def test_creates_comedy_movie(self):
        assert MovieFactory.create_movie("comedy") == "Comedy Movie Created"

    def test_unknown_type_returns_unknown_message(self):
        assert MovieFactory.create_movie("horror") == "Unknown Movie Type"

    def test_empty_string_type_returns_unknown_message(self):
        assert MovieFactory.create_movie("") == "Unknown Movie Type"

    def test_none_type_returns_unknown_message(self):
        assert MovieFactory.create_movie(None) == "Unknown Movie Type"

    def test_numeric_type_returns_unknown_message(self):
        assert MovieFactory.create_movie(42) == "Unknown Movie Type"

    def test_case_sensitive_type_returns_unknown(self):
        # "Action" (capitalised) should not match "action"
        assert MovieFactory.create_movie("Action") == "Unknown Movie Type"


# ── RecommendationBuilder ────────────────────────────────────────────────────

class TestRecommendationBuilderValidation:
    def test_get_result_without_any_steps_returns_empty(self):
        builder = RecommendationBuilder()
        result = builder.get_result()
        assert result == []

    def test_add_data_only_result_has_one_step(self):
        builder = RecommendationBuilder()
        result = builder.add_data().get_result()
        assert result == ["Data added"]

    def test_build_model_only_result_has_one_step(self):
        builder = RecommendationBuilder()
        result = builder.build_model().get_result()
        assert result == ["Model built"]

    def test_steps_accumulate_in_order(self):
        builder = RecommendationBuilder()
        builder.add_data().build_model().add_data()
        assert builder.get_result() == ["Data added", "Model built", "Data added"]

    def test_fluent_methods_return_builder_instance(self):
        builder = RecommendationBuilder()
        assert builder.add_data() is builder
        assert builder.build_model() is builder

    def test_fresh_builder_steps_independent_from_previous(self):
        b1 = RecommendationBuilder()
        b1.add_data().build_model()

        b2 = RecommendationBuilder()
        assert b2.get_result() == []


# ── MoviePrototype ────────────────────────────────────────────────────────────

class TestMoviePrototypeValidation:
    def test_clone_has_same_title(self):
        original = MoviePrototype("Inception")
        clone = original.clone()
        assert clone.title == "Inception"

    def test_clone_is_independent_object(self):
        original = MoviePrototype("Interstellar")
        clone = original.clone()
        clone.title = "Tenet"
        assert original.title == "Interstellar"

    def test_original_unchanged_after_clone_mutation(self):
        original = MoviePrototype("The Dark Knight")
        clone = original.clone()
        clone.title = "Batman Begins"
        assert original.title == "The Dark Knight"

    def test_empty_title_is_preserved_in_clone(self):
        original = MoviePrototype("")
        clone = original.clone()
        assert clone.title == ""

    def test_clone_is_not_same_reference(self):
        original = MoviePrototype("Avatar")
        clone = original.clone()
        assert original is not clone


# ── DatabaseConnection (Singleton) ───────────────────────────────────────────

class TestDatabaseConnectionValidation:
    def test_two_instances_are_same_object(self):
        db1 = DatabaseConnection()
        db2 = DatabaseConnection()
        assert db1 is db2

    def test_three_instances_are_same_object(self):
        db1 = DatabaseConnection()
        db2 = DatabaseConnection()
        db3 = DatabaseConnection()
        assert db1 is db2 is db3

    def test_singleton_identity_preserved_after_reassignment(self):
        db1 = DatabaseConnection()
        db2 = DatabaseConnection()
        db1 = DatabaseConnection()  # re-assign
        assert db1 is db2
