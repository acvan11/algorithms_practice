def subset(arr):
	result = []
	result.append([])
	for i in range(len(arr)):
		for j in range(i,len(arr)):
			result.append(arr[i:j+1])
	return result
print(subset([1,2,3]))