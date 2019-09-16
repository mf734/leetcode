class Solution(object):
	# 中间元素和右边界比较，使用右中位数
	# 所以mid是(left+right+1)>>2，right会变成mid-1
	# mid和right比，然后left和mid-1
	def search(self, nums, target):
		if not nums:
			return -1
		left, right = 0, len(nums)-1
		while left < right:
			mid = left + (right - left + 1)//2
			# mid = (left+right+1)>>2
			if nums[mid] < nums[right]:
				if nums[mid] <= target <= nums[right]:
					left = mid
				else:
					right = mid - 1
			else:
				if nums[left] <= target <= nums[mid-1]:
					right = mid - 1
				else:
					left = mid
		return left if nums[left] == target else -1
	
	
	# 中间元素和右边界比较，使用左中位数
	# 所以mid是(left+right)>>2，left会变成mid+1
	# mid+1和right比，然后left和mid
	def search(self, nums, target):
		if not nums:
			return -1
		left, right = 0, len(nums) -1
		while left < right:
			mid = left + (right - left) // 2
			# mid = (left+right)>>1
			if nums[mid] < nums[right]:
				if nums[mid+1] <= target <= nums[right]:
					left = mid + 1
				else:
					right = mid
			else:
				if nums[left] <= target <= nums[mid]:
					right = mid
				else:
					left = mid + 1
		return left if nums[left] == target else -1
