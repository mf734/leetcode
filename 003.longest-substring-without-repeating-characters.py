'''
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
子串中不能有重复字符
'''
class solution:
	def lengthOfLongestSubstring(self, s):
		seen = {}
		max_length = start = 0
		for i, c in enumerate(s):
			# if c in seen, 
			# start will eliminate any repeating char by +1
			if c in seen and start <= seen[c]:
				start = seen[c] + 1
			else:
				max_length = max(max_length, i-start+1)
			seen[c] = i
		return max_length