class Solution(object):
	def generateMatrix(self, n):
		"""
		:type n: int
		:rtype: List[List[int]]
		"""
		ans = [[0] * n for _ in range(n)]
		left, right, up, down = 0, n - 1, 0, n - 1
		k = 1
		while left <= right and up <= down:
			for i in range(left, right + 1):
				ans[up][i] = k
				k += 1
			up += 1
			for i in range(up, down + 1):
				ans[i][right] = k
				k += 1
			right -= 1
			for i in reversed(range(left, right + 1)):
				ans[down][i] = k
				k += 1
			down -= 1
			for i in reversed(range(up, down + 1)):
				ans[i][left] = k
				k += 1
			left += 1
		return ans

	
	def gene(self, n):
		A = [[0]*n for i in range(n)]
		i, j, di, dj = 0, 0, 0, 1
		for k in range(n*n):
			A[i][j] = k + 1
			if A[(i+di)%n][(j+dj)%n]:
				di, dj = dj, -di
			i += di
			j += dj
		return A
