def checkSub(str, sub):
	if sub in str:
		return True
	return False

print(checkSub('abcabcd', 'ab'))