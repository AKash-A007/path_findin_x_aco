from robot import RescueRobot
from cave_matrix import generate_cave

def main():
    cave_grid = generate_cave()
    robot = RescueRobot(cave_grid)
    survivors_rescued ,path_taken = robot.start_rescue()

    print("\n--- Rescue Operation Complete ---")
    print("Survivors rescued:", survivors_rescued)
    print("Path taken:", path_taken)

if __name__ == "__main__":
    main()
