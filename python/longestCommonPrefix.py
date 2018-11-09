def prefix(arr):
	count = 1
	result = ""
	count2 = len(arr[0])
	for i in range(1,len(arr)):
		if len(arr[i]) < count2:
			count2 = len(arr[i])
	while count2 > 0:
		word = arr[0][0:count]
		check = True
		for i in range(1,len(arr)):
			if arr[i][0:count] != word:
				check = False
		if check == True:
			result = word
			count+=1
		count2 -=1
	print(result)

prefix(["hell", "hello", "heliiiii"])
