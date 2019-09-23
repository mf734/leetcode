class Solution(object):
	def nextPermutation(self, nums):
		def reverse(lo, hi):
			while lo < hi:
				nums[lo], nums[hi] = nums[hi], nums[lo]
				lo += 1
				hi -= 1
		first = -1
		n = len(nums)
		# 从n-2开始，到-1结束（其实是到0结束），step为-1，
		for i in range(n-2, -1, -1):
			if nums[i] < nums[i+1]:
				first = i
				break
		if first == -1:
			reverse(0, n-1)
			return
		second = -1
		for i in range(n-1, first, -1):
			if nums[i] > nums[first]:
				second = i
				break
		nums[first], nums[second] = nums[second], nums[first]
		reverse(nums, first+1, n-1)