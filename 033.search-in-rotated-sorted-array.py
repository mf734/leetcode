class Solution(object):
	def search(self, nums, target):
		n = len(nums)
		if n == 0:
			return -1
		lo, hi = 0, n - 1
		while lo < hi:
			mid = lo + (hi - lo)//2
			if nums[mid] == target:
				return mid
			# 在左边的区间，所以查看target是不是在lo和mid之间
			elif nums[lo] <= nums[mid]:
				if nums[lo] <= target < nums[mid]:
					hi = mid - 1
				else:
					lo - mid + 1
			else:
				if nums[mid] < target <= nums [hi]:
					lo = mid + 1
				else:
					hi = mid - 1
		return lo if nums[lo] == target else -1
