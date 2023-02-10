class Calculate_Lights:
    # class variables for rows and columns to get the 2D light grid array
    rows = 1000
    cols = 1000
    
    def sum_lights_on(self, input_file):
        lights_grid = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        # print(len(lights_grid))
        with open(input_file, "r") as f:
            for line in f:
                details = line.strip().split(" ")
        
                start, end = [list(map(int, x.split(","))) for x in [details[-3], details[-1]]]
                if details[0] == "turn":
                    instruction = " ".join(details[:2])
            
                    for i in range(start[0], end[0]+1):
                        for j in range(start[1], end[1]+1):
                            if instruction == "turn on":
                                lights_grid[i][j] = True
                            elif instruction == "turn off":
                                lights_grid[i][j] = False
                elif details[0] == "toggle":
                    for i in range(start[0], end[0]+1):
                        for j in range(start[1], end[1]+1):
                            lights_grid [i][j] = not lights_grid [i][j]
                            
        return sum([sum(row) for row in lights_grid])
        
    
        
    def sum_lights_state(self, input_file):
        lights_grid = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        with open(input_file, "r") as f:
            for line in f:
                details = line.strip().split(" ")
                start, end = [list(map(int, x.split(","))) for x in [details[-3], details[-1]]]
                for i in range(start[0], end[0]+1):
                    for j in range(start[1], end[1]+1):
                        if details[0] == "turn" and details[1] == "on":
                            lights_grid[i][j] += 1
                            
                        if details[0] == "turn" and details[1] == "off":
                            lights_grid[i][j] = max(lights_grid[i][j] - 1, 0)
                        if details[0] == "toggle":
                            lights_grid[i][j] += 2
                          
                    
    
        
        return sum([sum(row) for row in lights_grid])





if __name__ == '__main__':
    cal = Calculate_Lights()
    

