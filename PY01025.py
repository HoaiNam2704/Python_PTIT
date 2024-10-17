s = input()

ans = s[-3:]

for i in range(len(s) - 3, 0, -3): 
	if(i - 3 >= 0): 
		ans = s[i-3:i] + "," + ans
	else : 
		ans = s[:i] + "," + ans

print(ans)
# 153920529

