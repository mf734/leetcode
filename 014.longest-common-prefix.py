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