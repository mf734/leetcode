class Solution(object):
    def countAndSay(self, n):
        ans = '1'
        n -= 1
        while n>0:
            prev = ''
            num = ans[0]
            count = 1
            for i in range(1, len(ans)):
                if ans[i] == num:
                    count += 1
                else:
                    prev += str(count) + num
                    num = ans[i]
                    count = 1
            prev += str(count) + num
            ans = prev
            n -= 1
        return ans
'''
数多少个重复数字。
其实就是循环做一件事：
重置res（上一个人的总数）
更新pre（上一个人的第一个数）
重置count
'''