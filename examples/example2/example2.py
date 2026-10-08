# starship.py
class Starship:
    def __init__(self, name, fuel_capacity):
        self.name = name
        self.fuel_level = fuel_capacity
        self.crew = []

    def board_crew(self, crew_member):
        self.crew.append(crew_member)

    def warp(self, distance_ly):
        """Warps the ship. Costs 10 fuel units per lightyear."""
        fuel_needed = distance_ly * 10
        if fuel_needed > self.fuel_level:
            raise ValueError("Insufficient fuel for warp sequence")
        
        self.fuel_level -= fuel_needed
        return f"Warped {distance_ly} lightyears"
