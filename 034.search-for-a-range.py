class Solution(object):
	def searchRange(self, nums, target):
		# 左和右的target的条件不一样
		# 左的x>A[mid]，会使得在mid已经定位到target后，仍然把right往左边赶，这样就尽可能找到低处的target
		# 右的x>=A[mid]，会使得在mid已经定位到target后，就将left往右边顶，这样就会尽可能定位到高处的target
		def binarySearchLeft(A, x):
			left, right = 0, len(A) - 1
			while left <= right:
				# mid = left + (right - left)//2
				mid = (left+right)>>1
				if x > A[mid]: 
					left = mid + 1
				else: 
					right = mid - 1
			return left
		def binarySearchRight(A, x):
			left, right = 0, len(A) - 1
			while left <= right:
				# mid = left + (right - left)//2
				mid = (left+right)>>1
				if x >= A[mid]: 
					left = mid + 1
				else: 
					right = mid - 1
			return right

		left, right = binarySearchLeft(nums, target), binarySearchRight(nums, target)
		return (left, right) if left <= right else [-1, -1]


class Solution2(object):
	def searchRange(self, nums, target):
		def extreme_inse(self, nums, target, lo):
			lo, hi = 0, len(nums) - 1
			while lo < hi:
				mid = lo + (hi - lo)//2
				if nums[mid] > target or (left and target==nums[mid]):
					hi = mid
				else:
					lo = mid + 1
			return lo
		def searchR(self, nums, target):
			left = self.extreme_inse(nums, target, True)
			if left == len(nums) or nums-left != target:
				return [-1, -1]
			return [left, searchRange(nums, target, False)-1]