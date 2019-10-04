# 类似题目：39， 40， 47
class Solution(object):
	def permute(self, nums):
		def dfs(nums, path):
			if not nums:
				res.append(path)
			for i in range(len(nums)):
				dfs(nums[:i]+nums[i+1:], path+[nums[i]])	
		res = []
		dfs(nums, [])
		return res
'''
如果nums空了，说明全部看完了，将path全部输出为结果
用i遍历，将i前面的和后面的传入下一个dfs，并将path记录
'''