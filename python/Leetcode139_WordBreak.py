def dictWord(s, wordDict):
	segment = []
	s2 = s
	while True:
		for j in range(len(wordDict)):
			for i in wordDict[j:len(s2)+1]:
				if i in s2:
					segment.append(i)
					s2 = s2[len(i):len(s2)+1]
					print("s2 = ", s2)
					print("segment =", segment)
				elif i in segment:
					s2 = s2[len(i):len(s2)+1]
					print("s2 = ", s2)
					print("segment =", segment)
			if len(s2) == 0:
 				return True
			if len(s2) != 0 and s2 in segment:
				print("s2 = ", s2)
				print("segment =", segment)
				return True
		return False

print(dictWord("leetcode", ["leet", "code"]))
print(dictWord("applepenapple", ["apple", "pen"]))
print(dictWord("catsandog", ["cats", "dog", "sand"]))
print(dictWord("bb", ["a", "b", "bbb"]))