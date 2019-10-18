# 类似题目：39， 40， 46
# 和46不同，需要sort以后，continue掉重复的
class Solution(object):
	def permuteUnique(self, nums):
		if not nums:
			return []
		def dfs(nums, path):
			if not nums:
				res.append(path+[])
			for i in range(len(nums)):
				if i > 0 and nums[i] == nums[i-1]:
					continue
				dfs(nums[:]+nums[i+1:], path+[nums[i]])
		nums.sort()
		res = []
		dfs(nums, [])
		return res

