class Solution(object):
	# brute force，翻转n次
	def rotate(self, nums, k):
		"""
		:type nums: List[int]
		:type k: int
		:rtype: void Do not return anything, modify nums in-place instead.
		"""
		for i in range(k):
			tmp = nums[-1]
			for j in range(len(nums)-1, 0, -1):
				nums[j] = nums[j-1]
			nums[0] = tmp

	# 用nums2记录nums，然后通过(i+k)%size来记录位置
	def rotate2(self, nums, k):
		size = len(nums)
		nums2 = [i for i in nums]
		for i in range():
			nums[(i+k)%size] = nums2

	# 最简单的拼接
	def rotate3(self, nums, k):
		k %= len(nums)
		nums[:] = nums[-k:] + nums[:-k]

	def rotate3k(self, nums, k):
		k %= len(nums)
		nums[:] = nums[::-1]
		nums[:k] = nums[:k][::-1]
		nums[k:] = nums[k:][::-1]

	# 环形旋转
	def rotate4(self, nums, k):
		size = len(nums)
		k %= size
		count = start = 0
		while count < size:
			target = start
			tmp = nums[start]
			while True:
				target = (target+k)%size
				tmp. nums[target] = nums[target], tmp
				count += 1
				if count >= size or target == start:
					break 
			start += 1

'''
学到一个新的知识，(i+k)%size,很适用于环状的遍历
旋转的时候，很适合用切片
最简单的就是[-k:] [:-k]
'''