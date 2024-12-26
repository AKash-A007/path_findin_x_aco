import random
ROWS, COLS = 20, 20
EMPTY, DANGER, SURVIVOR, RECHARGE = ".", "D", "S", "R"
def generate_cave():
    grid = [[EMPTY for _ in range(COLS)] for _ in range(ROWS)]
    for _ in range(15):  # Hazards
        x, y = random.randint(0, ROWS-1), random.randint(0, COLS-1)
        if (x,y)!=(0,0):
            grid[x][y] = DANGER
    for _ in range(3):  # Survivors
        while True:
            x, y = random.randint(0, ROWS-1), random.randint(0, COLS-1)

            if grid[x][y] == EMPTY:
                grid[x][y] = SURVIVOR
                break
    for _ in range(2):  # Recharge stations
        while True:
            x, y = random.randint(0, ROWS-1), random.randint(0, COLS-1)
            if grid[x][y] == EMPTY:
                grid[x][y] = RECHARGE
                break
    return grid
