import math 

for t in range(int(input())): 
	def ans(n): 
		for i in range(1000): 
			if int(n) % 7 == 0 : 
				return n 
			n = str(int(n) + int((str(n)[::-1])))
		return -1

	print(ans(input()))