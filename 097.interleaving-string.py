class Solution(object):
    def DFS(self, s1, s2, s3):
        n1, n2, n3 = len(s1), len(s2), len(s3)
        if n1 + n2 != n3:
            return False
        stack，visited = [(0,0)], set((0,0))
        while stack:
            x, y = stack.pop()
            # x, y = stack.pop(0)
            # 加上这一句就变成bfs了
            if x+y == n3:
                return True
            if x < n1 and s1[x]==s3[x+y] and (x+1, y) not in visited:
                stack.append((x+1, y))
                visited.add((x+1, y))
            if y < n2 and s2[y]==s3[x+y] and (x, y+1) not in visited:
                stack.append((x, y+1))
                visited.add((x, y+1))
        return False
'''
这个和二维矩阵是一样的，
但是利用了更少的存储空间。
'''


# top down 2d matrix
class Solution(object):
    def isInterleave(self, s1, s2, s3):
        n1, n2, n3 = len(s1), len(s2), len(s3)
        if n1 + n2 != n3:
            return False
        dp = [[False] * (n2+1) for i in range(n1 + 1)]
        dp[0][0] = True
        for j in range(1, n2+1):
            dp[0][j] = (dp[0][j-1] and s2[j-1]==s3[j-1])
        for i in range(1, n1+1):
            dp[i][0] = (dp[i-1][0] and s2[i-1]==s3[i-1])
        for i in range(1, n1+1):
            for j in range(1, n2+1):
                dp[i][j] = (dp[i-1][j] and s1[i-1] == s3[i+j-1]) or \
                (dp[i][j-1] and s2[j-1] == s3[i+j-1])
        return dp[-1][-1]
'''
top down
用dp[i][j]表示s1的前i元素和s2前j元素是否交错组成s3前i+j元素
dp[i-1][j]如果为True，说明上一个字符是s1提供的
dp[i][j-1]如果为True，说明上一个字符是s2提供的
上一个字符如果是s1提供的，那么s2不能在未提供之前字符的情况下直接比较这一个字符
所以，一个字符串提供字符的可能性必须是他之前的提供完了
'''
