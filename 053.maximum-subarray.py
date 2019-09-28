class Solution(object):
    # brute force easy understand
    def maxSubArray(self, nums):
        if len(nums) == 0:
            return 0
        preSum = res = nums[0]
        for i in nums[1:]:
            preSum = max(preSum + i, i)
            res = max(res, preSum)
        return res
'''
如果i比preSum+i大，那当然就从i开始会更好
否则，就保留preSum，除非后面有比他大的
res就单纯记载最大的结果就行了
'''
    # 只要是正数，就把他的值传递到后一位
    def mSA(self, nums):
        for i in range(1, len(nums)):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
        return max(nums)