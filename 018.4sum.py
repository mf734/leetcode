class Solution:
	def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
		n = len(nums)
		if n < 4: return []
		nums.sort()
		res = []
		for i in range(n-3):
			# 剪枝去重
			if i > 0 and nums[i] == nums[i-1]:
				continue
			# 当四数和都大于target 跳出
			if nums[i] + nums[i+1] + nums[i+2] + nums[i+3] > target:
				break
			if nums[i] + nums[n-1] + nums[n-2] + nums[n-3] < target:
				continue
			for j in range(i+1,n-2):
				if j > i + 1 and nums[j] == nums[j-1]: 
					continue
				if nums[i] + nums[j] + nums[j+1] + nums[j+2] > target:
					break
				if nums[i] + nums[j] + nums[n-1] + nums[n-2] < target:
					continue
				# 双指针
				left = j + 1
				right = n - 1
				while left < right:
					tmp = nums[i] + nums[j] + nums[left] + nums[right]
					if tmp == target:
						res.append([nums[i], nums[j], nums[left], nums[right]])
						while left < right and nums[left] == nums[left+1]:
							left += 1
						while left < right and nums[right] == nums[right-1]:
							right -= 1
						left += 1
						right -= 1
					elif tmp > target:
						right -= 1
					else:
						left += 1

'''
不管是三数还是四数，都有一定的套路:
首先是判空加sort，然后剪枝去重，（可用最小值break掉不必要的数），
如果要算closet，要先有存储值当作标准
while l < r，算合，移指针
如果不是closet而是找target，那么再找到第一个以后，需要手动再次剪枝去重

'''	