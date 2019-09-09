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
