# 类似题目：39， 40， 47
class Solution(object):
	def permute(self, nums):
		if not nums:
			return []
		def dfs(nums, path):
			if not nums:
				res.append(path+[])
			for i in range(len(nums)):
				dfs(nums[:i]+nums[i+1:], path+[nums[i]])	
		res = []
		dfs(nums, [])
		return res