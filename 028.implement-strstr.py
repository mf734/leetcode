class Solution(object):
    def strStr(self, haystack, needle):
        if len(haystack) == len(needle):
            if haystack == needle:
                return 0
            else:
                return -1
        for i in range(0, len(haystack) - len(needle)+1):
            k = i # k是haystack的index
            j = 0 # j是记录needle有多少位和haystack相等
            while j < len(needle) and k < len(haystack) and haystack[k] == needle[j]:
                j += 1
                k += 1
            if j == len(needle):
                return i
        return -1 if needle else 0
'''
这种方法非常重要这个问题非常常见，
首先在两个一样长的情况下比较。
如果不一样，就要用三个指针：
一个指针遍历haystack，
两个指针分别看haystack和needle同等位置上相不相等。
'''


class Solution1(object):
	def strStr1(self, haystack, needle):
		for i in range(len(haystack) - len(neddle) + 1):
			if haystack[i:i+len(needle)] == needle:
				return i
		return -1
'''
这个方法其实有点pythonic，但是思路也是brute force，
将haystack的第i位开始，往后遍历len(needle)位，
如果发现得出来的东西和needle一样，就直接弹出i
'''