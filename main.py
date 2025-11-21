from maze_manager import MazeManager

dummy_maze_description = """A . . . . . . . . .
. # . # . . # . # .
. # . . . # . . # .
. # # # . # . # # .
. . . . . . . . . .
. . # . K . . # . .
. # . . . # . . . .
. . . # . . . . # .
. # . . # . . . . .
. . . . . . # . . E"""

maze_manager = MazeManager()
maze_manager.set_maze(dummy_maze_description)

print("Options: up, down, left, right")
while True:
    print(maze_manager)
    reward_state_pair = maze_manager.do_action(input("Go: "))
    # print(reward_state_pair[1])
