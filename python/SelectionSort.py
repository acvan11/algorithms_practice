def SelectionSort(arr):
	for i in range(len(arr)-1):
		minNum = i
		for j in range(i+1, len(arr)):
			if arr[j] < arr[i]:
				minNum = j
			arr[i], arr[minNum] = arr[minNum], arr[i]
	return arr
print(SelectionSort([2,5,1,9,3,0]))
