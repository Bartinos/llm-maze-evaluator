from maze import Maze

class MazeManager():
    
    def __init__(self, maze_description):
        self.maze = Maze()
        self.maze.set_maze(maze_description)

    def print_maze(self):
        print(self.maze)

    def reset(self):
        pass

    def do_action(self) -> float:
        pass

    