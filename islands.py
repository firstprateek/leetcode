# solution that includes cross neighbours
class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        res = 0
        if not grid:
            return res
        
        max_row = len(grid)
        max_col = len(grid[0])
        
        def check_all_neighbours(row, col):
            if row >= 1:
                if col >= 1 and grid[row - 1][col - 1] == '1':
                    grid[row - 1][col - 1] = '0'
                    check_all_neighbours(row - 1, col - 1)
                
                if grid[row - 1][col] == '1':
                    grid[row - 1][col] = '0'
                    check_all_neighbours(row - 1, col)
                    
                if col < max_col and grid[row - 1][col + 1] == '1':
                    grid[row - 1][col + 1] = '0'
                    check_all_neighbours(row - 1, col + 1)
            
            if col < max_col - 1 and grid[row][col + 1] == '1':
                    grid[row][col + 1] == '0'
                    check_all_neighbours(row, col + 1)
                    
            if row < max_row - 1:
                if col < max_col - 1 and grid[row + 1][col + 1] == '1':
                    grid[row + 1][col + 1] = '0'
                    check_all_neighbours(row + 1, col + 1)
                    
                if grid[row + 1][col] == '1':
                    grid[row + 1][col] = '0'
                    check_all_neighbours(row + 1, col)
                    
                if col >= 1 and grid[row + 1][col - 1] == '1':
                    grid[row + 1][col - 1] = '0'
                    check_all_neighbours(row + 1, col - 1)
            
            if col >= 1 and grid[row][col - 1] == '1':
                grid[row][col - 1] = '0'
                check_all_neighbours(row, col - 1)
        
        for row in range(max_row):
            for col in range(max_col):
                if grid[row][col] == '1':
                    print("selected [{}, {}]".format(row, col))
                    res += 1
                    check_all_neighbours(row, col)
        
        return res

# solution that does not include cross neighbours