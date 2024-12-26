DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def is_valid_move(x, y, grid, visited):
    """Check if a move is valid."""
    return (
        0 <= x < len(grid) and
        0 <= y < len(grid[0]) and
        not visited[x][y] and
        grid[x][y] != "D"
    )

def find_survivors(grid):
    """Find all survivors in the grid using DFS."""
    def dfs(x, y):
        """Perform DFS to find connected survivors."""
        if not is_valid_move(x, y, grid, visited):
            return
        visited[x][y] = True  # Mark the cell as visited
        if grid[x][y] == "S":  # If it's a survivor, add to the list
            survivors.append((x, y))
        # Explore all 4 directions
        for dx, dy in DIRECTIONS:
            dfs(x + dx, y + dy)

    rows, cols = len(grid), len(grid[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    survivors = []

    # Perform DFS starting from every unvisited cell
    for x in range(rows):
        for y in range(cols):
            if not visited[x][y] and grid[x][y] == "S":
                dfs(x, y)

    return survivors

def find_recharge_stations(grid):
    return [(x, y) for x, row in enumerate(grid) for y, cell in enumerate(row) if cell == "R"]
