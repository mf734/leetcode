class Solution(object):
    def longestCommonPrefix(self, strs):
		if not strs:
			return ''
		shortest = min(strs, key = len)
		for i, j in enumerate(shortest):
			for other in strs:
				if other[i] != j:
					return shortest[:i]
		return shortest

'''
遍历string的题目
双层遍历，一层遍历一个shortest，一层遍历其他的元素的对应的位置
重点是，找到一个shortest后，遍历这个shortest的char，并且比较其他的元素与之对应的digit
这就教我们一个意识，两层遍历不一定要是同一级别
比如这一题，一个指针指的是digit（或者说index），一个遍历的是其他的item，将由string组成的list看成是二维数组
'''