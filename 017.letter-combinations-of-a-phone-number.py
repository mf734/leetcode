class Solution(object):
	def letterCombinations(self, digits):
		mapping = {1: "", 2: "abc", 3: "def", 4: "ghi", 5: "jkl", 6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz"}
		# index是现在digit中的位数，path是一种组合(列表type），即每一位选一个字母
		def dfs(index, path):
			# 如果index到最后一位数了，直接将path加入进去
			# 为什么是len(digits)，而不是+1：
			# 因为我们传进来的时候，还未做任何操作。如果i已经到了len，则直接弹出答案即可
			if index == len(digits):
				# #''.join(a)# 这个函数指的就是将a这个列表的元素，以''（就是空格）连接，输出一个str
				# 比如a=[1,2,3,4]，用了以上函数就会变成一个'1234'string
				return res.append("".join(path))
			# digit是digits在index位的数字
			digit = int(digits[index])
			# 用c遍历digit在mapping中对应的字母
			for c in mapping.get(digit, []):
				# 并将遍历的所有的字母（c）加入到已经有的path中，
				dfs(index + 1, path+[c])
		# res就是由path们构成的
		res = []
		if digits:
			dfs(0, [])
		return res
	
class Solution2(object):
	def letterComb(self, digits):
		mapping = {2: 'abc', 3: 'def', 4: 'ghi', 5: 'jkl', 6: 'mno', 7: 'pqrs', 8: 'tuv', 9: 'wxyz'}
		if len(digits) == 0:
			return []
		# 这就是recursion的跳出点
		# list 可以把string转化成list
		# 当只剩一个的时候（因为是倒着切的，所以这必然是头一个）
		# 将值return （到prev）
		if len(digits) == 1:
			return list(mapping[int(digits[0])])
		# 不断从尾部切，这样recursion最底层的就是最前面的一个
		# prev就是len=1剩下的一个，返回到上一步，
		# 记住上一步的len=2，而上一步的prev就是这一步的prevreturn过去的
		# 而add就是prev后面的一位的编码
		# 此时再用s和c将prev和add的编码组合起来，将组合起来的整个答案再传到上一步的prev，以此类推
		prev = self.letterComb(digits[:-1])
		add = mapping[int(digits[-1])]
		return [s + c for s in prev for c in add]

'''
字典的运用
学到的知识：
1，用len判断比用not digits要快一点
2，字典中int比str快，那么str就是'int'
   这一题中，因为给的输入是str，所以需要用int()函数转化
3, DFS。不断地recursion。
   第一种方法是从0往len挖，每挖一次就把这个digit对应的mapping给记录到path中
   挖到底了就将整个path输出到结果
   第二种方法是每次从后往前传字符串的slice
   传到最深处（就是第一个）的时候，开始mapping

   两种方法策略一样，方式不一样。
   一个从前往后，先mapping，再记录路径，最后直接传结果
   一个从后往前，先记录路径，最后才mapping
'''