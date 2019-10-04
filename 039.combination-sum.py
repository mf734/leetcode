class Solution(object):
	def combinationSum(self, candidates, target):
		if not candidates:
			return []
		def dfs(start, target, path):
			# 找到target后就把整个path加入res
			if target == 0:
				return res.append(path)
			for i in range(start, len(candidates)):
				if target - candidates[i] >= 0:
					dfs(i, target - candidates[i], path+[candidates[i]])
		res = []
		dfs(0, target, [])
		return res

'''
这里dfs的思路就是，用target-当前数，只要大于0，就有戏
只要有戏，就把减掉的当作新target，传入下一个recursion
顺便把当前的数全部加入path，只要最后找到符合的
就把path加入到res中
---------------
如果程序之前candidates是sort的，
那么dfs中的for循环里，
可以用“
if target - candidates[i] < 0:	break
”来加速
'''
