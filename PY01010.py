from math import * 

for test in range(int(input())) : 
	s = input() 
	a = int(s[0:2])
	res = s[-2:]
	# res = res[::-1]
	if(a == int(res)) : 
		print("YES")
	else : 
		print("NO")