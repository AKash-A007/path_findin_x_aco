
import tkinter as tk
import time
def create_grid(canvas, grid, cell_size=30):
    """Create the grid based on the grid layout."""
    rows = len(grid)
    cols = len(grid[0])
    for i in range(rows):
        for j in range(cols):
            x1 = j * cell_size
            y1 = i * cell_size
            x2 = (j + 1) * cell_size
            y2 = (i + 1) * cell_size
            color = 'white'

            if grid[i][j] == "D":  # Obstacle
                color = 'black'
            elif grid[i][j] == "S":  # Survivor
                color = 'green'
            elif grid[i][j] == "R":  # Recharge station
                color = 'blue'

            canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline='black')

def visualize_path(grid, total_path, survivors=None, cell_size=30, speed=500):
    """Visualize the robot's movement through the grid."""
    root = tk.Tk()
    root.title("Robot Path Visualization")

    rows = len(grid)
    cols = len(grid[0])

    canvas = tk.Canvas(root, width=cols * cell_size, height=rows * cell_size)
    canvas.pack()

    create_grid(canvas, grid, cell_size)

    # Start position (first coordinate in the path)
    start = total_path[0]
    robot = canvas.create_oval(
        start[1] * cell_size + 5, start[0] * cell_size + 5,
        start[1] * cell_size + cell_size - 5, start[0] * cell_size + cell_size - 5,
        fill='red'
    )

    # Highlight survivors
    if survivors:
        for survivor in survivors:
            x1 = survivor[1] * cell_size + 5
            y1 = survivor[0] * cell_size + 5
            x2 = survivor[1] * cell_size + cell_size - 5
            y2 = survivor[0] * cell_size + cell_size - 5
            canvas.create_oval(x1, y1, x2, y2, fill="green", outline="black")
            canvas.create_text(survivor[1] * cell_size + cell_size // 2,
                               survivor[0] * cell_size + cell_size // 2,
                               text="S", fill="white", font=("Helvetica", 16, "bold"))

    def move_robot(i=0):
        """Move the robot along the path with recursion."""
        if i < len(total_path):
            current_pos = total_path[i]
            x1 = current_pos[1] * cell_size + 5
            y1 = current_pos[0] * cell_size + 5
            x2 = current_pos[1] * cell_size + cell_size - 5
            y2 = current_pos[0] * cell_size + cell_size - 5

            # Update robot position on the canvas
            canvas.coords(robot, x1, y1, x2, y2)

            # Call the move_robot function recursively after a delay
            root.after(speed, move_robot, i + 1)

    # Start the animation
    move_robot()

    root.mainloop()



if __name__ == "__main__":
    from cave_matrix import generate_cave
    from robot import RescueRobot

    # Initialize the cave grid and robot
    cave_grid = generate_cave()
    robot = RescueRobot(cave_grid)
    robot.start_rescue()

    # Call the visualization function
    visualize_path(cave_grid, robot.path_taken, robot.survivors_rescued)
