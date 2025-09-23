class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {(m - 1, n- 1): 1}
        
        def dfs(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            # if (
            #     i == (m - 1) or
            #     j == (n - 1)
            # ):
            #     return 1

            if (
                i < 0 or
                j < 0 or 
                i >= m or
                j >= n
            ):
                return 0

            res = dfs(i + 1, j) + dfs(i, j + 1)
            memo[(i, j)] = res

            return res
        return dfs(0, 0)