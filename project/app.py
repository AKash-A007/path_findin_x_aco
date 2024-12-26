from flask import Flask, render_template, jsonify
from cave_matrix import generate_cave
from robot import RescueRobot
import pprint

app = Flask(__name__)
cave_grid = generate_cave()  # Generate the global grid only once
pprint.pprint(cave_grid)
robot = RescueRobot(cave_grid)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/map')
def rescue_map():
    # Initialize the rescue robot and simulate
    robot.start_rescue()

    # Render the map with the updated state
    return render_template('map.html', 
                           grid=cave_grid, 
                           path=robot.path_taken, 
                           survivors=robot.survivors_rescued)

@app.route('/start')
def start_rescue():
    # Initialize the rescue robot
    robot = RescueRobot(cave_grid)
    robot.start_rescue()

    # Return JSON response with the robot's path and survivors
    return jsonify({
        'grid': cave_grid,
        'path': robot.path_taken,
        'survivors': robot.survivors_rescued
    })

if __name__ == '__main__':
    app.run(debug=True)
