for t in range(int(input())): 
	def check(s): 
		for i in range(len(s)): 
			if s[i] != '1' and s[i] != '2' and s[i] != '0' : 
				return "NO"
		return "YES"

	print(check(input()))