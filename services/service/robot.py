import sys

# sys.setrecursionlimit(900000)
sys.setrecursionlimit(10)


class Solution:
    def robotArea(self):
        grid = dict()
        res = 0

        def sum_of_digits(num):
            return sum(int(digit) for digit in str(abs(num)))

        def bfs(x, y):
            if not grid.get(x):
                grid[x] = dict()
            if not grid[x].get(y):
                grid[x][y] = 0
            if grid[x][y] == 1:
                return

            if sum_of_digits(x) + sum_of_digits(y) > 23:
                grid[x][y] = 1
                return

            nonlocal res
            res += 1
            grid[x][y] = 1
            bfs(x - 1, y)
            bfs(x + 1, y)
            bfs(x, y - 1)
            bfs(x, y + 1)

        bfs(0, 0)
        return res


# sol = Solution()
# print(sol.robotArea())

def greeting():
    print("Assalomu aleykum!")

i = 1
while i < 6:
    greeting()
    if i == 3:
        break
    i += 1
