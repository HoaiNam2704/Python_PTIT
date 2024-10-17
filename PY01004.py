from math import * 

def check(a) : 
	if a == 2 : return True  
	if a < 2 : return False
	if a % 2 == 0 : return False 
	for i in range(3, int(sqrt(a)) + 1) : 
		if(a % i == 0) : 
			return False 
	return True  
for test in range(int(input())) : 
	n = int(input()) 
	cnt = 0 
	for i in range(n) : 
		if gcd(n, i) == 1 : 
			cnt += 1 
	if(check(cnt))  :
		print("YES")
	else : print("NO")