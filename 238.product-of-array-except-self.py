class Solution(object):
    # Dynamic Programming
    def productExceptSelf(self, nums):
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            dp[i] = dp[i - 1] * nums[i - 1]
        prod = 1
        for i in reversed(range(0, len(nums))):
        # for i in range(n-1, -1, -1):
            dp[i] *= prod
            prod *= nums[i]
        return dp
'''
因为有重复的数字，所以用dp，
这里有一个思路：题目要求是求一个数所有前面的乘积乘上后面的乘积，
所以首先用dp记录“前面的乘积”，
比如第一位就是1，第二就是第一位，第三位就是前两位，最后一位就是所有前面的，
保存好了以后，再开始用prod记录后面的乘积，
再次从后面遍历，此时dp上的i位记录的只有i以前的乘积，
我们要用它依次乘上它以后的。从prod=1开始，依次将prod乘以前面的。
所以dp依次记录着第0位，一直到i以前的乘积，
而prod从反方向往前代表着最后一位，一直到i位以前的乘积
'''