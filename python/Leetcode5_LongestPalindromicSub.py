'''
Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Input: "cbbd"
Output: "bb"
'''
def PalindromeCheck(str):
	if len(str) <= 1:
		return True
	if str[0] != str[-1]:
		return False
	return PalindromeCheck(str[1:-1])

def longestPalindromicSub(str):
	longest = 0
	result = ''
	for i in range(len(str)-1):
		count = 1
		for j in range(i+1, len(str)):
			if str[i] == str[j]:
				if PalindromeCheck(str[i:j+1]) and count > longest:
					result = str[i:j+1]
					longest = count
					print(result)
				break
			count += 1
	return result

print(longestPalindromicSub('babad'))
