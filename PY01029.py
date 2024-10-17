import math 

def check(s): 
	n = int(s)
	m = int(s[::-1])
	if(math.gcd(n,m) == 1): 
		return True 
	return False

for test in range(int(input())): 
	s = input()
	if(check(s)): 
		print("YES")
	else : 
		print("NO")

	# print(s[::-1])	