# back tracking
class Solution(object):
	def generateParenthesis(self, n):
		ans = []
		def backtrack(s='', left=0, right=0):
			if len(s) == 2*n:
				return ans.append(s)
			if left < n:
				backtrack(s+'(', left+1, right)
			if right < left:
				backtrack(s+')', left, right+1)
		backtrack()
		return ans

'''
用回溯递归dfs。
只有生成了有效的s后，才加入ans中。
s是现有的path，
left和right分别代表两边的括号数量。
首先从left开始，左边加"("，并递归到dfs里，
当有n个"("的时候，其实也有n个dfs了。
第n个dfs的时候，开始执行右边的，
此时因为left到n了，所以会一直在右边递归n个dfs。
当right==left的时候，就将答案加入到res，返回到上一步。
此时left=n的全部搞定，退回一步到n-1，并且开始当前的right，
然而right刚刚带着")"进入dfs，就会又进入left<n的判断，并且递归一个"("。
所以这个时候得出来的s就会是，以n=3为例，"(()("。
这个时候，left到nl ，再继续添加")"。
当right==left（即为n-1）的时候，这一例就是"(()())"。
以此类推，所有的结果为
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
这个方法保证了只有在保证了左右平衡且n对生成完了的时候才会加入结果
'''
		

# Dynamic Programming
class Solution3(object):
	def generateParenthesis3(self, n):
		if n==0:
			return []
		tot = []
		tot.append([None]) # n=0
		tot.append(['()']) # n=1
		for i in range(2, n+1):
			res = []
			for j in range(i):
				now1 = tot[j] # p的括号组合
				now2 = tot[i-1-j] # q的括号组合
				for k1 in now1:
					for k2 in now2:
						if not k1:
							k1 = ''
						if not k2:
							k2 = ''
						el = '(' + k1 + ')' + k2
						res.append(el) # 把所有valid的情况添加进去
			tot.append(res)
		return tot[n]
'''
DP适用于自底向上。
这一题的重点就是，成对的永远的是()，
然后新增的要么在上一组括号的内部，要么在上一组右括号的正右侧。
所以这里有自底向上的条件：i相比i-1时的条件是一样的
"("+【i=p时所有括号的排列组合】+')'+ 【i=q时所有括号的排列组合】
且p+q=i-1，p从0到i-1，q从n-1到0，最后整个组合就是i的所有情况
'''


# brute force
class Solution2(object):
	def generateParenthesis2(self, n):
		def generate(A=[]):
			if len(A) == 2*n:
				if valid(A):
					ans.append(''.join(A))
			else:
				A.append('(')
				generate(A)
				A.pop()
				A.append(')')
				generate(A)
				A.pop()
		def valid(A):
			bal = 0
			for c in A:
				if c == '(':
					bal += 1
				else:
					bal -= 1
				if bal < 0:
					return False
			return bal == 0
		ans = []
		generate()
		return ans
'''
是第一种办法的丑实现，但是思路是一样的,

生成2^(2n)个由“（”和“）”构成的序列，然后检查是否有效
时间复杂度：O(2^{2n}*n)
对于2^{2n}个序列中的每一个
我们用于建立和验证该序列的复杂度为O(n)。
空间复杂度：O(2^{2n}n)
'''

# 闭合数
class Solution4(object):
	def generateParenthesis4(self, n):
		if N == 0:
			return [' ']
		ans = []
		for c in range(n):
			for left in self.generateParenthesis4(c):
				for right in self.generateParenthesis4(n-1-c):
					ans.append('({}){}'.format(left, right))
		return ans