def pivotNum(arr):
	for i in range(len(arr)):
		left = 0
		for j in range(0,i):
			left += arr[j]
		print(left)
		right = 0
		for k in range(i+1, len(arr)):
			right += arr[k]
		print(right)
		if left == right:
			return i
	return -1

print(pivotNum([2,100,-51,-51,1]))