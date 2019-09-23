'''
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
子串中不能有重复字符
'''
class solution:
	def lengthOfLongestSubstring(self, s):
		seen = {}
		# max_length是最长子串的长度，start是子串的初始指针
		max_length = start = 0
		for i, c in enumerate(s):
			# if c in seen
			# start will skip repeating chars by +1
			if c in seen and start <= seen[c]:
				start = seen[c] + 1
			else:
				max_length = max(max_length, i-start+1)
			# 把c存入seen
			seen[c] = i
		return max_length

'''
同样用到了seen，方便考察是否“已经出现过”
每次有重复出现的，就要更新指针，然后用max看是否长度最长
'''