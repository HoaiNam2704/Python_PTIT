import math 

def check(a, b): 
	if(math.gcd(a, b) == 1): 
		return True 
	return False 

n, k = map(int, input().split())
cnt = 0 
for i in range(pow(10, k-1), pow(10, k)-1): 
	if(check(i, n)): 
		cnt += 1 
		print(i, end = ' ')
		if(cnt == 10): 
			print()
			cnt = 0 
