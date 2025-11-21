class MazeManager():
    maze = [[]]
    agent_location = (0,0)

    def __init__(self):
        pass

    def _parse_maze_from_ascii_grid(self, maze_description):
        self.maze = [line.split() for line in maze_description.splitlines()]

    def _from_maze_to_ascii_grid(self) -> str:
        return "maze ascci grid..."
        # return [value for value in [row for row in self.maze]]
        

    """Not ideal for performance"""
    def _extract_agent_location(self):
        for row_index, row  in enumerate(self.maze):
            for column_index, column  in enumerate(self.maze):
                if "A" in self.maze[row_index][column_index]:
                    self.agent_location = (row_index, column_index)
                    self.maze[row_index][column_index] = "."
        return self.agent_location
    
    def set_maze(self, maze_description):
        self._parse_maze_from_ascii_grid(maze_description)
        self.agent_location = self._extract_agent_location()

    def __str__(self):
        str = ""
        for row_index, row  in enumerate(self.maze):
            for column_index, column  in enumerate(self.maze):
                if (row_index, column_index) != self.agent_location:
                    str += self.maze[row_index][column_index] + " "
                else: 
                    str += "A "
            str = str.rstrip() + "\n"

        return str

    def reset(self):
        pass

    def do_action(self, action):
        new_coords = self._action_to_coords(action)
        
        if self._is_valid_coord(new_coords) == False:
            print("Walked into invalid coord: ", new_coords)
            return -1, self._from_maze_to_ascii_grid()
        
        self.agent_location = new_coords

        return 1, self._from_maze_to_ascii_grid()

    def _action_to_coords(self, action):
        new_coords = (-1,-1)
        match action.lower():
            case "up":
                new_coords = (self.agent_location[0] - 1, self.agent_location[1]) 
            case "down":
                new_coords = (self.agent_location[0] + 1, self.agent_location[1]) 
            case "left":
                new_coords = (self.agent_location[0], self.agent_location[1] - 1) 
            case "right":
                new_coords = (self.agent_location[0], self.agent_location[1] + 1) 
            case _:
                print("Could not interpret action: ", action)
        
        return new_coords

    def _is_valid_coord(self, coord):
        
        if coord[0] < 0 or coord[0] >= len(self.maze) or coord[1] < 0 or coord[1] < 0 or coord[1] >= len(self.maze[0]): # Coordinates outside of the grid is not valid
            return False
        elif "#" in self.maze[coord[0]][coord[1]]: # Walking into a wall is considered invalid
            return False
        
        return True

    