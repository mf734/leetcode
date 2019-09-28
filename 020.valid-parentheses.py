class Solution(object):
    def isValid(self, s):
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}
        for char in s:
            if char in mapping:
                if not stack:
                	return False
                top = stack.pop()
                if mapping[char] != top:
                    return False
            else:
                stack.append(char)
        return not stack

    def isValid1(self, s):
		if len(s) %2 != 0:
			return False

		mapping = {"(": ")", "[": "]", "{": "}"}
		stack = []

		for char in s:
			if char in mapping:
				stack.append(char)
			else:
				if len(stack) == 0:
					return False
				top = stack.pop()
				if mapping[top] != char:
					return False
		return not stack

	def isValid3(self, s):
		while "()" in s or "{}" in s or "[]" in s:
			s = s.replace("()", "").replace("{}","").replace("[]","")
		return s == ''
'''
重点就在map和stack的灵活运用
只要看到了，就加入stack（有的时候我也叫它为seen），
然后再通过map去pop掉，并且比较是否这个pop出来的可以和前者成对
注意，坚持map的时候，一定要查是否为空栈
'''