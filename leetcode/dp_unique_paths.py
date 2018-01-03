# @file  Unique Paths
# @brief How many possible unique paths are there?

# https://leetcode.com/problems/unique-paths/

'''
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?


Above is a 3 x 7 grid. How many possible unique paths are there?

Note: m and n will be at most 100.
'''


# time complexity: O(length of str) = O(mn)
# space complexity: O(mn)
def uniquePaths(self, m, n):
    # Initialize first row and first column number paths as 1
    dp = [[1]*n for i in range(m)]  # dp[1][] = dp[][1] = 1
    # Go over all the remaining rows/columns.
    for i in range(1, m):
        for j in range(1, n):
            # Current #paths = #paths from prev row + #paths from prev column
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[m-1][n-1]
