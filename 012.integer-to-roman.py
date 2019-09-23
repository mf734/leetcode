class solution:
	def intToRom(self, num):
		roms = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
		ints = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]        
		ret = ""        
		for i, j in enumerate(ints):
			while num >= j:
				ret += roms[i]
				num -= j
			if num == 0:
				return ret

'''
字典的运用是基础
重点是在递归上，不断减掉数字，将对应的字符加到结果中去
'''