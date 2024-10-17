from math import * 

for test in range(int(input())) : 
	s = input()
	if s[len(s)-1] == '6' and s[len(s)-2] == '8' : 
		print("YES")
	else: print("NO")
	# print(s[-1])