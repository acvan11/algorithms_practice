'''
Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
'''
def sum3Closest(arr, target):
	result = []
	closest = max(arr) * 3
	temp = 0
	arr.sort()
	print('arr= ',arr)
	for i in range(len(arr)-2):
		target2 = target - arr[i]
		low = i + 1
		high = len(arr)-1
		print(target2)
		while low < high:
			count = arr[low] + arr[high]
			print('count = ',count)
			if arr[low] + arr[high] < target2:
				low +=1
			elif (arr[low] + arr[high] > target2):
				high -=1
			else:
				result = [arr[i], arr[low], arr[high]]
				break
	print(result)

sum3Closest([-1, 2, 1, -4], 2)