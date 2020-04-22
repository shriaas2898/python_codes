class Solution:
    def matrix(string_mat):
        string_mat = string_mat.strip('[')
        string_mat = string_mat.strip(']')
        mat = string_mat.split('], [')
        for i in range(len(mat)):
              mat[i] = mat[i].split(',')
        return mat


    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) == 0:
            return 0
        island_count = 1
        for e in grid:
            e.append('#')
        grid.append(['#']*len(grid[0]))
        
        for i in range(len(grid)-1):
            for j in range(len(grid[0])-1):
                print(i,j)
                if grid[i][j] == '1':
                    print("1 found")
                    island_count += 1
                    grid[i][j] = str(island_count)
                if grid[i][j] not in '10#':
                    print('number found')
                    if grid[i][j+1] not in '10#'+grid[i][j]:
                        island_count -=1
                        print("island:",island_count)
                        grid_str = str(grid)
                        grid_str = grid_str.replace(grid[i][j],grid[i][j+1])
                        print("string grid:",grid_str)
                        grid = self.matrix(grid_str)
                        
                    else:    
                        if grid[i][j+1] == '1':
                            grid[i][j+1] = grid[i][j]
                    if grid[i+1][j] == '1':
                        grid[i+1][j] = grid[i][j] 
            print("LOG:",str(grid).replace('],[','],\n['))
        return island_count-1
                
