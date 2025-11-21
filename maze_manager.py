class MazeManager():
    maze = [[]]
    agent_location = (0,0)
    def __init__(self):
        pass

    def parse_maze_from_ascii_grid(self, maze_description):
        self.maze = [line.split() for line in maze_description.splitlines()]

    """Not ideal for performance"""
    def _find_agent_location(self):
        for row_index, row  in enumerate(self.maze):
            for column_index, column  in enumerate(self.maze):
                if "A" in self.maze[row_index][column_index]:
                    self.agent_location = (row_index, column_index)
        return self.agent_location
    
    def set_maze(self, maze_description):
        self.parse_maze_from_ascii_grid(maze_description)
        self.agent_location = self._find_agent_location()

    def __str__(self):
        str = ""
        for row_index, row  in enumerate(self.maze):
            for column_index, column  in enumerate(self.maze):
                str += self.maze[row_index][column_index] + " "
                str.strip()
            str += "\n"

        return str

    def reset(self):
        pass

    def do_action(self, action) -> float:
        
        pass

    def action_to_coords(self, action):
        new_coords = (-1,-1)
        match action:
            case "UP":
                new_coords = (self.agent_location[0], self.agent_location[1] + 1) 
            case "DOWN":
                new_coords = (self.agent_location[0], self.agent_location[1] - 1) 
            case "LEFT":
                new_coords = (self.agent_location[0] - 1, self.agent_location[1]) 
            case "RIGHT":
                new_coords = (self.agent_location[0] + 1, self.agent_location[1]) 
            case _:
                print("Could not interpret action: ", action)
        
        return (-1, -1)

    def _is_valid_coord(self, coord):
        
        if coord[0] < 0 or coord[1] < 0: # Coordinates outside of the grid is not valid
            return False
        elif "#" in self.maze[coord[0]][coord[1]]: # Walking into a wall is considered invalid
            return False
        
        return True

    