def rotateArray(arr,k):
	while k >0:
		temp = arr[-1]
		arr.pop()
		arr.insert(0,temp)
		k -=1
	print(arr)

rotateArray([1,2,3,4,5,6],3)