class Solution(object):
	def countAndSay(self, n):
		ans = "1"
		n -= 1
		while n > 0:
			res = ""
			pre = ans[0]
			count = 1
			for i in range(1, len(ans)):
				# 如果ans[i]==pre，那么又有一个pre
				if pre == ans[i]:
					count += 1
				# 反之，则说明换数字了，将数过的记录在res中
				# 重设pre和count
				else:
					res += str(count) + pre
					pre = ans[i]
					count = 1
			# 每一次都需要将上一次的ans给念出来
			# 所以要用res来记录这一次的报数结果
			# 最后把ans报完之后，再记录到ans中
			res += str(count) + pre
			ans = res
			n -= 1
		return ans
