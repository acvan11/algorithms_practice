'''
Smallest Substring of All Characters
Given an array of unique characters arr and a string str, Implement a function getShortestUniqueSubstring that finds the smallest substring of str containing all the characters in arr. Return "" (empty string) if such a substring doesn’t exist.

Come up with an asymptotically optimal solution and analyze the time and space complexities.

Example:

input:  arr = ['x','y','z'], str = "xyyzyzyx"

output: "zyx"
'''
def smallest(arr, s):
	result = ""
	small = len(s) + 1
	for i in range(len(s)-len(arr)+1):
		for j in range(i + len(arr), len(s)+1):
			print(s[i:j])
			if sub(arr,s[i:j]) and len(s[i:j]) < small:
				result = s[i:j]
				small = len(s[i:j])
	return result

def sub(arr, s):
	result = True
	for i in arr:
		if i not in s:
			result = False
	return result
print(sub(['A'], ""))

print(smallest(['A'],"A"))
