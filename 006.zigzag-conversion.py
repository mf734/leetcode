class Solution(object):
	def convert(self, s, numRows):
		if numRows <= 1 or numRows >= len(s):
			return s
		L = ['']*numRows
		# index可以用来遍历rows，将s中的元素塞到对应的位置
		# step更像是方向，如果到底了，index就往+1走，相反则往-1走
		index, step = 0, -1
		for n in s:
			L[index] += n
			if index == 0 or index == numRows - 1:
				step = - step
			index += step
		return ''.join(L)

