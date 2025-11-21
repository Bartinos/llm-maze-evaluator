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

print(maze_manager)
maze_manager.do_action("NORTH")