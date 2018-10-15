'''
Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 


Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''
def longestSub(s):
	print(s)
	longest = 0
	result = ''
	for i in range(len(s)):
		count = 1
		for j in range(i+1, len(s)):
			if s[j] in s[i:j]:
				break
			count += 1
		if count > longest:
			longest = count
			result = s[i:j]
	return result
print('longest sub without repeating: ',longestSub('dabcedabcd'))
print('=======')
print(longestSub('bbbb'))
print('=======')
print(longestSub('abcabcbb'))
print('=======')
print(longestSub('pwwkew'))
