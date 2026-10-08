# orbital_math.py
def calculate_total_mass(module_a_mass, module_b_mass):
    """Calculates the combined mass of two space station modules."""
    # BUG: The developer accidentally cast the result to an int!
    return int(module_a_mass + module_b_mass)
