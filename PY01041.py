for t in range(int(input())): 
	def check(s): 
		if len(s) < 3: return "NO"
		i = len(s) - 1 
		while i > 0 and (s[i] < s[i-1]) : 
			i -= 1
		while i > 0 and (s[i] > s[i-1]) : 
			i -= 1 
		if(i != 0) : 
			return "NO"
		return "YES" 
	print(check(input()))			
		