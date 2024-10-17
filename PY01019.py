from math import * 

def check(s1, s2): 
	i = 0 
	while i < len(s1) - 1 : 
		# print(ord(s1[i+1]) - ord(s1[i]), ord(s2[i+1]) - ord(s2[i]), sep = ' ', end = ' ') 
		# i += 1

		if(abs(ord(s1[i+1]) - ord(s1[i])) != abs(ord(s2[i+1]) - ord(s2[i]))): 
			return False 
		i+=1
	return True 
for test in range(int(input())): 
	s1 = input() 
	s2 = s1[::-1]
	# check(s1, s2)
	if(check(s1, s2)): print("YES")
	else : print("NO")