# test_starship.py
import pytest
from example2 import Starship

# --- Task 3: The Fixture (Replaces global state) ---
@pytest.fixture
def fresh_ship():
    """Provides a fully fueled ship for each test, eliminating state leaks."""
    return Starship("Enterprise", 100)


# --- Task 1: Fixed the assertion bug ---
def test_initial_state(fresh_ship):
    assert fresh_ship.fuel_level == 100
    # Fixed: Checked against an empty list, not the string "empty"
    assert fresh_ship.crew == [] 


def test_boarding(fresh_ship):
    fresh_ship.board_crew("Picard")
    assert "Picard" in fresh_ship.crew


def test_warp_success(fresh_ship):
    result = fresh_ship.warp(5)
    assert result == "Warped 5 lightyears"
    assert fresh_ship.fuel_level == 50


# --- Task 2: Fixed exception handling ---
def test_warp_insufficient_fuel(fresh_ship):
    # Fixed: Uses pytest.raises to trap the expected ValueError
    with pytest.raises(ValueError) as excinfo:
        fresh_ship.warp(15) # Needs 150 fuel, only has 100
    
    assert "Insufficient fuel" in str(excinfo.value)


# --- Task 4: Parametrization ---
@pytest.mark.parametrize("distance, expected_fuel_remaining", [
    (2, 80),   # 100 - (2 * 10)
    (5, 50),   # 100 - (5 * 10)
    (10, 0),   # 100 - (10 * 10)
])
def test_warp_fuel_calculations(fresh_ship, distance, expected_fuel_remaining):
    fresh_ship.warp(distance)
    assert fresh_ship.fuel_level == expected_fuel_remaining
