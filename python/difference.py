
def differencce(arr):
	arr2 = []
	for i in arr:
		arr2 += i

	result1 = {}
	for i in arr2:
		if i not in result1:
			result1[i] = 1
		else:
			result1[i] += 1

	result = []
	for i in result1:
		if result1[i] == 1:
			result.append(i)
	print(result)

arr= [[1,2,3],[2,3,4,9],[2,3,4,5]]
differencce(arr)