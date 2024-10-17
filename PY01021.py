from math import * 

def solve(a): 
	print("1", end = '', sep = '')
	for i in range(2, int(sqrt(a))): 
		if(a % i == 0) :
			print(" * ", end = '')
			cnt = 0 
			while a % i == 0 : 
				cnt += 1 
				a /= i 
			print(i, "^", cnt, sep = '', end = '')
	if(a > 1): 
		print(" * ", int(a) , "^1", sep='', end='')

for test in range(int(input())): 
	a = int(input())
	solve(a)
	print()