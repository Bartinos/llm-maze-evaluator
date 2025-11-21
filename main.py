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

maze_manager = MazeManager(dummy_maze_description)
maze_manager.print_maze()
maze_manager.do_action()