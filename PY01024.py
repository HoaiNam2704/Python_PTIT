t = int(input()) 
import math
def check(n) : 
	sum = (int)(n[0])
	for i in range(1, len(n)): 
		sum += int(n[i])
		if(abs(int(n[i]) - int(n[i-1])) != 2) : 
			return False 
	if(sum % 10 != 0) : return False 
	return True 

for test in range(t) : 
	n = input() 
	if(check(n)): 
		print("YES")
	else : 
		print("NO")

		