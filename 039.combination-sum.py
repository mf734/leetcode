class Solution(object):
	def combinationSum(self, candidates, target):
		if not candidates:
			return []
		def dfs(nums, start, target, path):
			# 找到target后就把整个path加入res
			if target == 0:
				return res.append(path + [])
			for i in range(start, len(nums)):
				if target - nums[i] >= 0:
					dfs(nums, i, target - nums[i], path+[nums[i]])
		res = []
		dfs(candidates, 0, target, [])
		return res
