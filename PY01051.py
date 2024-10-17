import math 

for t in range(int(input())): 
	def check(s): 
		sum = 0 
		for i in range(len(s)): 
			sum += int(s[i])
		if(len(str(sum)) > 1 and sum == int((str(sum))[::-1])): 
			return "YES"
		return "NO"

	print(check(input()))

# 2
# 12341
# 22222222222222222222