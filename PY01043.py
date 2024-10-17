for t in range(int(input())): 
	def check(s): 
		if(s != s[::-1] or len(s) % 2 != 0): return False 
		for i in range(len(s)): 
			if(int(s[i]) % 2 != 0): 
				return False 
		return True 
	s = ""
	for i in range(int(input())): 
		if(check(str(i))): 
			s += str(i) + " "		
	print(s)
		