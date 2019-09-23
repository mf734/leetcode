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

'''
这题的重点是能想到用step来决定遍历的方向，然后用数组的直接+的特性。
也可以引申到二维数组。
''.join(L)是一个很好用的，将iterable转成string的方法。
这一例就是将L中的元素用''（就是空）拼起来。
'''