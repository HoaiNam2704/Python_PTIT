import math 

for t in range(int(input())): 
	def nt(n): 
		if n < 2 : return False 
		for i in range(2, int(math.sqrt(n))+1): 
			if(n % i == 0): 
				return False
		return True 
	
	def check(s): 
		sum = 0 
		for i in range(len(s)): 
			sum += int(s[i])
		if nt(sum): 
			return "YES"
		return "NO"

	print(check(input()))

# 2
# 12341
# 22222222222222222222