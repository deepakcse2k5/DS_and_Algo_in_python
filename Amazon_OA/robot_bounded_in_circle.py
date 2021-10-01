# Explanation
#
# This problem is more about math proof than coding.
#
# Consider the location of the robot after one iteration. There are two cases:
#
# The robot is back to the origin. In this case, it's obvious that the robot will stay at the origin after any number of runs.
# The robot is not at the origin.
# For case 2, let's consider where the robot is facing after one iteration. The robot starts facing north, and after one iteration it could face:
#
# North. Since it's facing the same direction after one iteration, it'll get further and further away from origin in the next iteration. And therefore its movement will not be bounded by a circle.
# South. The robot reverses its direction. The distance it traveled in the current movement will be cancelled by the next movement since they are of opposite directions. Therefore, the robot goes back to the origin every two iterations.
# East. If the robot ends up facing east after the iteration 1, it will be facing south after iteration 2, west after iteration 3 and north again after iteration 4. The distance it traveled in north direction cancels that of south, and distance it traveled in the east direction cancels that of west. So the robot is back to origin after 4 iterations.
# West. It's the opposite situation as east but the result is the same - the robot goes back to the origin.
# Therefore, we can simulate the robot movement after one iteration and return true if the robot's coordinate is back to origin or
# it faces a direction that is not north.
#


def is_robot_bounded(movements):
    x, y, dx, dy = 0, 0, 0, 1

    for move in movements:
        if move == 'S':
            x, y = x + dx, y + dy
        elif move == 'R':
            dx, dy = dy, -dx
        else:
            dx, dy = -dy, dx

    return (x, y) == (0, 0) or (dx, dy) != (0, 1)


if __name__ == '__main__':
    movements = input()
    res = is_robot_bounded(movements)
    print('true' if res else 'false')
