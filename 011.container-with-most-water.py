class Solution(object):
	def maxArea(self, height):
		res, l, r = 0, 0, len(height) - 1
		while l < r:
			h = min(height[l], height[r])
			res, l, r = max(res,  h * (r - l)), l + (height[l] == h), r - (height[r] == h)
		return res

'''
这又是个最优解的问题。最优解无非就是字典，DP，或者直接算
在这里就是直接算出来的。用双指针，从两边往中间夹，不断更新
在这例里，h就是height[l]和height[r]中小的一个
res就是每次看是否新面积更高
而(height[l]==h)很聪明，就是看h最后选择了谁，如果选择了l，那么就会返回1，所以下次就更新l （这一句是重点）
'''