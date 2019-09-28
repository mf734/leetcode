# 快慢指针
class Solution(object):
	def RemoveDuplicates(self, nums):
		if not nums: 
			return 0
		k = 1
		for i in range(1, len(nums)):
			if nums[i] != nums[i - 1]:
				nums[k] = nums[i]
				k += 1
		return k
'''
这种in place的删除非常适合用快慢指针来做
和19是一样的，只不过19是找index，而这里是找value
因为是sort的，所以用i-1判断重复
有重复的，我们就它跳过去，不做处理，
有不一样，就把它的位置记录到k上，
保证k上顺着过来的全部都是不重复的
'''

class Solution2(object):
	def inPlaceRemoveDup(self, nums):
		i = 0
		while i < len(nums) - 1:
			if nums[i] == nums[i+1]:
				del nums[i]
			else:
				i += 1
		return len(nums)
'''
del函数可以直接用于删除节点
'''