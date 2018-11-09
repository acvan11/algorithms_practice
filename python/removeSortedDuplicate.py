def removeDup(arr):
	dup = []
	for i in range(1, len(arr)):
		if arr[i] == arr[i-1]:
			dup.append(arr[i])
	print(dup)
	for i in dup:
		arr.remove(i)
	print(arr)

arr = [0,0,1,1,1,2,2,3,3,4]
removeDup(arr)