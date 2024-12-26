def update_real_time_map(grid, path_taken, survivors):
    print("\n--- Real-Time Map ---")
    for x, row in enumerate(grid):
        for y, cell in enumerate(row):
            if (x, y) in path_taken:
                print("R", end=" ")
            elif (x, y) in survivors:
                print("S", end=" ")
            elif cell == 'D':
                print("D", end=" ")
            else:
                print(".", end=" ")
        print()
