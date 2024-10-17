for t in range(int(input())): 
	def check(s):
		for i in range(1, len(s)-2): 
			if(s[i] != s[i+2] or s[i-1] != s[i+1]): 
				return False  
		return True 
	if(check(input())): print("YES")
	else : print("NO")