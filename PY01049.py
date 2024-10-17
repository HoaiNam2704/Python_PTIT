import math 

for t in range(int(input())): 
	def nt(n): 
		if(n < 2): return False  
		for i in range(2, int(math.sqrt(n)) + 1): 
			if(n % i == 0): 
				return False        
		return True      
	def ans(s): 
		if not nt(len(s)) : 
			return 'NO'             
		cnt = 0
		for i in range(len(s)): 
			if(nt(int(s[i]))) : 
				cnt += 1 
		return 'YES' if cnt > len(s) - cnt else 'NO'
	print(ans(input()))

# 3
# 1234567
# 22334455667
# 23400300489898989