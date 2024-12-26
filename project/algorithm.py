from heapq import heappop, heappush
from grid import is_valid_move, DIRECTIONS

def a_star(grid, start, goal, visited):
    """A* search to find the shortest path from start to goal."""
    ROWS, COLS = len(grid), len(grid[0])
    open_set = []
    heappush(open_set, (0, start, []))  # (priority, current_position, path)

    g_cost = {start: 0}
    f_cost = {start: heuristic(start, goal)}

    while open_set:
        _, current, path = heappop(open_set)

        if current == goal:
            return path + [current]

        for dx, dy in DIRECTIONS:
            neighbor = (current[0] + dx, current[1] + dy)

            # Check if the move is valid
            if is_valid_move(neighbor[0], neighbor[1], grid, visited):
                tentative_g_cost = g_cost[current] + 1  # Cost to move to neighbor

                if neighbor not in g_cost or tentative_g_cost < g_cost[neighbor]:
                    g_cost[neighbor] = tentative_g_cost
                    f_cost[neighbor] = tentative_g_cost + heuristic(neighbor, goal)
                    heappush(open_set, (f_cost[neighbor], neighbor, path + [current]))

        visited[current[0]][current[1]] = True  # Mark the current node as visited

    return []  # Return an empty path if no valid path exists


def heuristic(a, b):
    """Heuristic for A* - Manhattan distance."""
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def multi_target_pathfinding(grid, start, survivors, recharge_stations):
    """Find paths to rescue all survivors."""
    current_position = start
    total_path = []
    visited_survivors = []
    battery = 1

    # Create a visited grid
    visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]

    while survivors:
        # Find the nearest survivor
        paths_to_survivors = [
            (a_star(grid, current_position, survivor, visited), survivor)
            for survivor in survivors
        ]
        paths_to_survivors = [
            (path, survivor) for path, survivor in paths_to_survivors if path
        ]  # Remove invalid paths

        if not paths_to_survivors:
            break  # No reachable survivors

        # Select the shortest path to a survivor
        shortest_path, nearest_survivor = min(paths_to_survivors, key=lambda x: len(x[0]))

        # Update the current position and battery
        current_position = nearest_survivor
        battery -= len(shortest_path)
        total_path.extend(shortest_path)
        survivors.remove(nearest_survivor)
        visited_survivors.append(nearest_survivor)

        # Recharge if necessary
        if battery <= 10 and recharge_stations:
            paths_to_recharge = [
                (a_star(grid, current_position, recharge, visited), recharge)
                for recharge in recharge_stations
            ]
            paths_to_recharge = [
                (path, recharge) for path, recharge in paths_to_recharge if path
            ]

            if paths_to_recharge:
                shortest_recharge_path, recharge_station = min(
                    paths_to_recharge, key=lambda x: len(x[0])
                )
                total_path.extend(shortest_recharge_path)
                battery = 100
                current_position = recharge_station

    return visited_survivors, total_path
