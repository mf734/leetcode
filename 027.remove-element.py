class Solution(object):
	def removeElement(self, nums, val):
		k = 0
		for i in range(len(nums)):
			if nums[i] != val:
				nums[k] = nums[i]
				k += 1
		return k
'''
同样的，结点的inplace删除就用快慢指针，
i去遍历，只要不是要删除的，就说明k需要保留这个i，
即i就和k一起动。
而当找到了需要删除的，我们就不加k，k就留在了原地，而让i跳过了它
'''

	# pythonic
    def removeElement2(self, nums, val):
        k = 0
        while k <len(nums):
            if nums[i] == val:
                del nums[i]
            else:
                i += 1