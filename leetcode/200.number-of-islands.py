
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        m, n = len(grid), len(grid[0])
        grid1 = [['0'] * (n + 2)]
        for i in grid:
            grid1.append(['0'] + i + ['0'])
        grid1.append(['0'] * (n + 2))  

        def search(x, y):
            if grid1[x][y] == '0':
                return 0
            grid1[x][y] = '0'
            search(x + 1, y)
            search(x - 1, y)
            search(x, y + 1)
            search(x, y - 1)
            return 1

        cnt = 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                cnt += search(i, j)

        return cnt
