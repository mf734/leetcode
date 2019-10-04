class Solution(object):
    def searchInsert(self, nums, target):
        if nums[-1] < target:
            return len(nums)
        lo = 0
        hi = len(nums) - 1
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] > target:
                hi = mid
            elif nums[mid] < target:
                lo = mid + 1
            else:
                return mid
        return lo
'''
为什么hi=mid，防止hi减成了lo
'''
    # code is way easier, but less time efficiency
    def iterInsert(self, nums: List[int], target: int) -> int:
        if nums[-1] < target:
            return len(nums)
        for i in range(0, len(nums)):
            if nums[i] >= target:
                return i