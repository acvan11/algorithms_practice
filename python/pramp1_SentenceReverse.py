def reve(arr):
	result = []
	arr1 = arr[::-1]
	arr2 = []
	for i in arr1:
		if i != ' ':
			arr2.append(i)
		else:
			result += arr2[::-1] + [' ']
			arr2 = []
	result += arr2[::-1]
	return result

arr = ['p', 'e', 'r', 'f', 'e', 'c', 't', ' ',
                'm', 'a', 'k', 'e', 's', ' ',
                'p', 'r', 'a', 'c', 't', 'i', 'c', 'e'
               ]

print(reve(arr))
