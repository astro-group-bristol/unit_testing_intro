# test_starship.py
import pytest
from example2 import Starship

# WARNING: Global state! This is a bad testing practice.
ship = Starship("Enterprise", 100)

def test_initial_state():
    assert ship.fuel_level == 100
    # BUG 1: This assertion is failing. Can you fix it?
    assert ship.crew == "empty" 

def test_boarding():
    ship.board_crew("Picard")
    assert "Picard" in ship.crew

def test_warp_success():
    result = ship.warp(5) # Costs 50 fuel
    assert result == "Warped 5 lightyears"
    assert ship.fuel_level == 50

def test_warp_insufficient_fuel():
    # BUG 2: This test just crashes! We want to prove it raises an error.
    # Refactor this to properly use pytest.raises
    ship.warp(10)