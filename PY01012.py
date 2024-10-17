from math import * 

def nt(x) : 
	if x == 2 : 
		return True 
	if x < 2 : 
		return False 
	if x % 2 == 0 : 
		return False 
	for i in range(3, int(sqrt(x))): 
		if x % i == 0 : 
			return False 
	return True 

for test in range(int(input())) : 
	a, b = map(int, input().split())
	x = gcd(a, b) 
	cnt = 0 
	s = str(x)
	for i in range(len(s)) : 
		cnt += int(s[i])
	if(nt(cnt)) : 
		print("YES")
	else : print("NO")