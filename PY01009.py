from math import * 

s = input() 

cnt = 0 
for i in range(len(s)) : 
	if (s[i] >= 'a' and s[i] <= 'z') : 
		cnt += 1 

if cnt >= len(s) / 2 : 
	print(s.lower()) 
else : print(s.upper())