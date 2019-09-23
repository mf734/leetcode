# Time O(n), Space O(n)
def dictHash(self, nums, target):
	seen = {}
	for i, n in enumerate(nums):
		if target - n in seen:
			return [seen[target - n], i]
		else: 
			seen[n] = i
	return []

# Time O(n^2), Space O(1)
def bruteForce(self, nums, target):
	for i, n in enumerate(nums):
		while j < len(nums)+1:
			if target == (n + nums[j]):
				return [i, j]
			else:
				j += 1
'''
字典的考察，seen的运用
虽然双指针也可以用，但是配合seen，一次iteration就可以快速查看它是否被遍历过
'''