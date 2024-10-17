import math 

for t in range(int(input())): 
	def solve(s): 
		sum = int(s[0])
		for i in range(1, len(s)): 
			sum = sum * 10 + (int(s[i]))
		if(sum % 3 == 0) : return "YES"
		return "NO"

	print(solve(input()))