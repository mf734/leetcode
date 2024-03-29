'''
你有一个日志数组 logs。每条日志都是以空格分隔的字串。
对于每条日志，其第一个字为字母数字标识符。然后，要么：

标识符后面的每个字将仅由小写字母组成，或；
标识符后面的每个字将仅由数字组成。
我们将这两种日志分别称为字母日志和数字日志。保证每个日志在其标识符后面至少有一个字。

将日志重新排序，使得所有字母日志都排在数字日志之前。字母日志按内容字母顺序排序，忽略标识符；在内容相同时，按标识符排序。数字日志应该按原来的顺序排列。

返回日志的最终顺序。

'''

class Solution(object):
	def reorder(self, logs):
		digits = []
		let = []
		for log in logs:
			if log.split()[1].isdigit():
				digits.append(log)
			else:
				letters.append(log)

		letter.sort(key=lambda x: x.split()[0])
		letter.sort(key=lambda x: x.split()[1:])
		result = letters + digits
		return result

