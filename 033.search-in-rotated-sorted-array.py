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
'''
符合要求的就是二分法，
mid用老方法lo+(hi-lo)//2。
然后一定要判断target是在左边还是右边，
因为是旋转列表，所以要保证二分法要在顺序的列表里面。
所以，比如先比较lo和mid上的值，如果lo<mid，说明至少lo到mid是递增的
那么再把target在lo到mid里面去比。
每更新一次lo或者mid，都要再做一次这样的比较，确保二分法一定要用在递增列表里面。
'''