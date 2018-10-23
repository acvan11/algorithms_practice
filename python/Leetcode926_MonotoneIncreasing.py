def monotone(s):
	count1 = counting(s,1)
	s1 = ""
	for i in range(len(s)):
		if s[i] == "1":
			s1 = s[i:len(s)+1]
			break
	count2 = counting(s1,0)
	if count1 < count2:
		print(count1)
	else:
		print(count2)
def counting(s,n):
	count = 0
	for i in range(len(s)):
		if s[i] == str(n):
			count += 1
	return count


monotone("00110")
monotone("010110")
monotone("00011000")