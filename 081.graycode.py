'''
格雷编码是一个二进制数字系统:
该系统中，两个连续的数值仅有一个位数的差异。
'''
def graycode(l1, l2):
	'''
	from up to down, then left to right
	
	0   1   11  110
			10  111
				101
				100
				
	start:      [0]
	i = 0:      [0, 1]
	i = 1:      [0, 1, 3, 2]
	i = 2:      [0, 1, 3, 2, 6, 7, 5, 4]
	'''
	res = [0]
	for i in range(n):
		res += [x|(1<<i) for x in res[::-1]]
	return res

def graycode1(self, n):
	res, head = [0], 1
	for i in range(n):
		for j in range(len(res)-1, -1, -1):
			res.append(head+res[j])
		head <<= 1
	return res

def graycode2(self, n):
	if n==0:
		return [0]
	res = []
	def back(path, x):
		if len(path) == n:
			res.append(int(path, 2))
		elif x==0:
			back(path+'0', 0)
			back(path+'1', 1)
		else:
			back(path+'1', 1)
			back(path+'0', 0)
	back('',0)
	return res