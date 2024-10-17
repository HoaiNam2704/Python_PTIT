from math import * 

for test in range(int(input())) : 
	p, r, a = [float(x) for x in input().split()]
	print(ceil(log(a / p, 1 + r/100))) 