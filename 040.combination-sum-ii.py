class Solution(object):
    def combinationSum2(self, candidates, target):
        if not candidates:
            return []
        def dfs(target, start, path):
            if target == 0:
                return res.append(path + [])
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                if target - candidates[i] < 0:
                    break
                dfs(target - candidates[i], i + 1,  path+[candidates[i]])
                    
        candidates.sort()
        res = []
        dfs(target, 0, [])
        return res
'''
有几处和39不太一样
跳过重复的，因为不能用一样的
如果有小于0的，则直接不看了
传过去的时候要传i+1，因为不能重复使用
'''