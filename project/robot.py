from algorithm import multi_target_pathfinding
from grid import find_survivors, find_recharge_stations

class RescueRobot:
    def __init__(self, grid):
        self.grid = grid
        self.start_position = (0, 0)
        self.path_taken = []
        self.survivors_rescued = []

    def start_rescue(self):
        # Locate survivors and recharge stations
        survivors = find_survivors(self.grid)
        recharge_stations = find_recharge_stations(self.grid)

        # Use the improved algorithm
        visited_survivors, total_path = multi_target_pathfinding(
            self.grid, self.start_position, survivors, recharge_stations
        )

        # Update robot state
        self.survivors_rescued = visited_survivors
        self.path_taken = total_path

        return self.path_taken, self.survivors_rescued
