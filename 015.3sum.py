class Solution(object):
	def threeSum(self, nums):
		res = []
		nums.sort()
		# use one pointer to iterate the nums
		for i in range(len(nums)-2):
			# if there is a duplicated numers
			# use i-1 and i>0 so it can save some times
			if nums[i] > 0:
				break
			if i > 0 and nums[i] == nums[i - 1]:
				continue			
			# since everything before i is already checked
			l, r = i + 1, len(nums) - 1
			while l < r:
				s = nums[i] + nums[l] + nums[r]
				if s < 0:
					l += 1
				elif s > 0:
					r -= 1				
				else:
					res.append([nums[i], nums[l], nums[r]])
					while l < r and nums[l] == nums[l+1]:
						l += 1
					while l < r and nums[r] == nums[r-1]:
						r -= 1
					l += 1
					r -= 1
		return res