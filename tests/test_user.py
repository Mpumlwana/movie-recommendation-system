import pytest
from src.user import User

def test_add_to_watchlist():
    user = User(user_id="1", name="Test User", email="test@test.com")
    user.add_to_watchlist("movie_123")
    
    assert "movie_123" in user.watchlist
    assert len(user.watchlist) == 1

def test_remove_from_watchlist():
    user = User(user_id="1", name="Test User", email="test@test.com")
    user.add_to_watchlist("movie_123")
    user.add_to_watchlist("movie_456")
    
    user.remove_from_watchlist("movie_123")
    
    assert "movie_123" not in user.watchlist
    assert "movie_456" in user.watchlist
    assert len(user.watchlist) == 1