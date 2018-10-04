
def longestSub(s):
	max = 0
	seen = ''
	i = 0
	while i < len(s):
		if s[i] not in seen:
			seen += s[i]
		else:
			if len(seen) > max: max = len(seen)
			seen = seen[seen.index(s[i]) + 1:] + s[i]
		i += 1
	if len(seen) > max: max = len(seen)
	return max

print(longestSub('dabcedabcd'))