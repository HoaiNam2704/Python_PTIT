from math import * 

for test  in range ((int)(input())) : 
	n = input() 
	cnt = len(n) - 1 
	l = 1 
	n = (int)(n) 
	while l <= cnt : 
		n /= pow(10, l)
		if n - (int)(n) >= 0.5 : 
			n = ceil(n) 
		else : 
			n = int(n) 
		n *= pow(10, l) 
		l += 1 
	print(int(n)) 