class Solution(object):
	def threeSumClosest(self, nums, target):
		if len(nums) < 3:
			return
		nums.sort()
		res = nums[0] + nums[1] + nums[2]
		for i in range(len(nums)-2):
			l, r = i + 1, len(nums) - 1
			while l < r:
				s = nums[i] + nums[l] + nums[r]
				if s == target:
					return s
				if abs(s - target) < abs(res - target):
						res = s
				if s < target:
					l += 1
				elif s > target:
					r -= 1
		return res
'''
思维和3sum一模一样，但是判断条件不一样
3sum是找到一组解以后，手动推动程序继续执行，包括手动去重
而这一例，while会自动把所有的iter给走完，
所以只需要通过s和target来控制l和r的走向
然后每次比较差值（是否closest）就可
注意事项：1，s一定要放在while里面，否则不会变的
2，res要先记录三个作为已知的标准点
'''