class Solution(object):
	def multiply(self, num1, num2):
		ans = [0] * (len(num1) + len(num2))
		for i, n1 in enumerate(reversed(num1)):
			for j, n2 in enumerate(reversed(num2)):
				ans[i + j] += int(n1) * int(n2)
				ans[i + j + 1] += ans[i + j] // 10
				ans[i + j] %= 10
		while len(ans) > 1 and ans[-1] == 0:
			ans.pop()
		return "".join(map(str, ans[::-1]))
'''
enumerate(reversed)只改item，不改index。
所以i+j就是从第一位开始的
和加法一样，需要考虑进位，所以从最后一位开始
所有需要进位的都是：
res[i] += n1 * n2
res[i+1] += res[i]//10
res[i] %= 10
------
"".join(map(str, res)) 适用的情况：
由int组成的array，需要将所有的都转成str，
并且元素之间都由空白连接（不是空格）
'''