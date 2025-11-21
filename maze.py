class Maze():
    maze = [[]]

    def __init__(self):
        self.maze = [[]]

    def parse_maze_from_ascii_grid(self, maze_description):
        self.maze = [line.split() for line in maze_description.splitlines()]
        
    
    def set_maze(self, maze_description):
        self.parse_maze_from_ascii_grid(maze_description)

    def __str__(self):
        str = ""
        for row_index, row  in enumerate(self.maze):
            for column_index, column  in enumerate(self.maze):
                str += self.maze[row_index][column_index] + " "
                str.strip()
            str += "\n"

        return str
        
