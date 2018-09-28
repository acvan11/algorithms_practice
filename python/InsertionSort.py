def InsertionSort(arr):
	for i in range(1,len(arr)):
		for j in range(i):
			if (arr[i-j] < arr[i-j-1]):
				arr[i-j], arr[i-j-1] = arr[i-j-1], arr[i-j]
	return arr

print(InsertionSort([2,4,7,1,4]))