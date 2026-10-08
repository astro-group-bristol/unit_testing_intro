# test_orbital_math.py
from example1 import calculate_total_mass

def test_calculate_total_mass():
    result = calculate_total_mass(500., 250.5)
    
    # This assertion will fail! 
    # pytest will output: E   AssertionError: assert '750' == 750
    assert result == 750.5
