from math import * 

def check(s) : 
	for i in range (len(s)) : 
		if(s[i] != '4' and s[i] != '7') : 
			return False 
	return True 

for test in range(int(input())) : 
	s = input() 
	if check(s) : 
		print("YES")
	else : 
		print("NO")

# 3
# 4477
# 44444487777777777
# 47474747474777777777777744444