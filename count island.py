class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) == 0:
            return 0
        island_count = 0
        for e in grid:
            e.append('#')
        grid.append(['#']*len(grid[0]))
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                print(i,j)
                if grid[i][j] == '1':
                    print("1 found")
                    island_count += 1
                    grid[i][j] = '*'
                if grid[i][j] == '*':
                    print('* found')
                    if grid[i][j+1] == '*' or grid[i+1][j] == '*':
                        island
                    if grid[i+1][j] == '1':
                        grid[i+1][j] = '*'
                     
                    if grid[i][j+1] == '1':
                        grid[i][j+1] = '*'
                     
                print("LOG:",grid)
        return island_count
                
