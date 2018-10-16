def zigzag(str,n):
	result = {}
	result2 = []
	result3 = ''
	count = 0

	for i in range(n):
		result[i] = []
	while len(str)-1 >= count:
		for j in range(n):
			if count > len(str) -1:
				break
			result[j].append(str[count])
			count += 1
		for l in range (n-2, 0, -1):
			if count > len(str) -1:
				break
			result[l].append(str[count])
			count +=1
	for i in range(n):
		result2 += result[i]
	result3 = ''.join(result2)
	print(result3)

zigzag("PAYPALISHIRING",4)

# result = {}
# result[2] = []
# result[2].append('cry')
# result[2].append('smile')
# print(result)