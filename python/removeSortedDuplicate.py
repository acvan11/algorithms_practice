def removeDup(arr):
	# dup = []
	# for i in range(1, len(arr)):
	# 	if arr[i] == arr[i-1]:
	# 		dup.append(arr[i])
	# print(dup)
	# for i in dup:
	# 	arr.remove(i)
	# print(arr)
	count = 1
	while count < len(arr):
		if arr[count-1] != arr[count]:
			count +=1
		else:
			arr.remove(arr[count])
	print(arr)

def removeDup2(arr):
	count = 2
	while count < len(arr):
		if arr[count-1] != arr[count] or arr[count-2] != arr[count]:
			count +=1
		else:
			arr.remove(arr[count])
	print(arr)
arr = [0,0,1,1,1,2,2,3,3,4]
removeDup2(arr)