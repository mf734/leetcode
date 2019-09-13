class Solution(object):
	# two pointer
	def twoSum(self, nums, target):
		l, r = 0, len(nums) - 1
		while l < r:
			s = nums[l] + nums[r]
			if s > target:
				r -= 1
			elif s < target:
				l += 1
			else:
				return (l + 1, r + 1)

	# dictionary
	def twoSum2(self, nums, target):
		dic = {}
		for i, v in enumerate(nums):
			if target - v in dic:
				return [dic[target-v]+1, i+1]
			dic[num] = i

	# binary search
	def twoSum3(self, nums, target):
		for i in range(len(nums)):
			l, r = i+1, len(nums)-1
			tmp = target - nums[i]
			while l <= r:
				mid = 1 + (r-l)//2
				if nums[mid] == tmp:
					return [i+1, mid+1]
				elif nums[mid] < tmp:
					l = mid + 1
				else:
					r = mid - 1