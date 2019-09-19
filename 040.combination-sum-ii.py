class Solution(object):
	def combinationSum2(self, candidates, target):
		if not candidates:
			return []
		def dfs(nums, target, start, path):
			if target == 0:
				return res.append(path + [])
			for i in range(start, len(nums)):
				# 有几处和39不太一样
				# 跳过重复的，因为不能用一样的
				# 如果有小于0的，则直接不看了
				# 传过去的时候要传i+1
				if i > start and nums[i] == nums[i - 1]:
					continue
				if target - nums[i] < 0:
					break
				dfs(nums, target - nums[i], i + 1,  path+[nums[i]])
					
		candidates.sort()
		res = []
		dfs(candidates, target, 0, [])
		return res
		