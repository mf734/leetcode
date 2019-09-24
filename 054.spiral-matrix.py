class Solution(object):
	def spiralOrder(self, matrix):
		"""
		:type matrix: List[List[int]]
		:rtype: List[int]
		"""
		if len(matrix) == 0 or len(matrix[0]) == 0:
			return []
		ans = []
		left, right, up, down = 0, len(matrix[0])-1, 0, len(matrix)-1
		while left <= right and up <= down:
			for i in range(left, right+1):
				ans.append(matrix[up][i])
			up += 1
			for i in range(up, down+1):
				ans.append(matrix[i][right])
			right -= 1
			for i in reversed(range(left, right+1)):
				ans.append(matrix[down][i])
			down -= 1
			for i in reversed(range(up, down+1)):
				ans.append(matrix[i][left])
			left += 1
		return ans[:len(matrix)*len(matrix[0])]
	
	def sp2(self, matrix):
		res = []
		while matrix:
			res += matrix.pop(0)
			if matrix and matrix[0]:
				for row in matrix:
					res.append(row.pop())
			if matrix:
				res += matrix.pop()[::-1]
			if matrix and matrix[0]:
				for row in matrix[::-1]:
					res.append(row.pop(0))
		return res