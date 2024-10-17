import math 

a, b = map(int, input().split())

def check(n, m): 
	if(math.gcd(n,m) == 1): 
		return True 
	return False 

for i in range(a, b-1): 
	for j in range(i + 1, b): 
		if(check(i, j)): 
			for k in range(j + 1, b+1): 
				if(check(i, k) and check(j, k)): 
					res = "(" + str(i) + ", " + str(j) + ", " + str(k) + ")"
					print(res)