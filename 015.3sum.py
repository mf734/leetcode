class Solution(object):
	def threeSum(self, nums):
		nums.sort()
		res = []
		# use one pointer to iterate the nums
		for i in range(len(nums)-2):
			 #这个条件可加可不加，但是只适用于3sum，4sum或者3sum的closest都不行
			if nums[i] > 0:
				break
			
			# 剪枝
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

'''
对应的题目还有16，18。
3sum需要用到三指针，一个指针作为基础指针，从左到右遍历
两个指针作为剩下部分的左右指针，通过他们的变化来调整数组的大小
所以三指针:1，是需要sort的
这里也学到了2，剪枝去重,所以要让i>0，否则会out
因为3sum需要找到确切的target（此例为0），所以：
3，每找到一组解后，都需要手动去重。去重的过程就是将l和r往中间拉，避免重复计算
4，对于target大小的判断，一定要用elif，否则会来回震荡
'''