class Solution(object):
	# 快慢指针
	def RemoveDuplicates(self, nums):
		if not nums: 
			return 0
		k = 1 # 从1开始 和i一致 用来记载不重复的数组的长度
		for i in range(1, len(nums)):
			if nums[i] != nums[i - 1]: # 只要有不重复的，就把i移到k上去
				nums[k] = nums[i]
				k += 1
			# 反过来说，只要有重复的，我们就直接把它跳过去，等待下一个不重复的时候，用k覆盖它
		return k


	def inPlaceRemoveDup(self, nums):
		i = 0
		while i < len(nums) - 1:
			if nums[i] == nums[i+1]:
				del nums[i]
			else:
				i += 1
		return len(nums)