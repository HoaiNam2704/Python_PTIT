import math 
for t in range(int(input())): 
	def nt(n): 
		for i in range(3, int(math.sqrt(n))): 
			if(n % i == 0): 
				return False 
		if(n == 2) : return True  
		if(n < 2) : return False      
		return True 
	n = input()
	m = int(n[-4:])
	# print(m)
	if(nt(m)): print("YES")
	else : print("NO")
	
# 3
# 12234323130097
# 3443354654654654461123
# 43543543434554659999