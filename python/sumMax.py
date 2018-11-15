def sumMax(arr):
	arr2 = arr
	arr2.sort()
	sum = 0
	count = 0
	for i in range(len(arr2)-1, -1, -1):
		if count != 2:
			sum += arr2[i]
			count += 1
		else:
			count = 0
	print(sum)

arr= [1,2,5,4,3]
sumMax(arr)