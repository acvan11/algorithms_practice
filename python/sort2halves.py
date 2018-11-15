import math
def sort2halves(arr):
	arr.sort()
	n = math.floor(len(arr)/2)
	arr1 = arr[0:n]
	arr2 = arr[n:]
	# for i in arr2:
	# 	arr1.insert(n,i)
	for i in range(len(arr2)-1, -1, -1):
		arr1.append(arr2[i])
	print(arr1)
a1 = [5, 2, 4, 7, 9, 3, 1, 6, 8]
a2 = [1, 2, 3, 4, 5, 6]
sort2halves(a1)
sort2halves(a2)