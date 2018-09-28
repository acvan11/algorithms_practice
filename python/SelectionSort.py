# SELECTION SORT: O(n^2) always
def selection_sort(l):
  # Outer loop: 0..length of list-1
  for i in range(len(l)):

    # lowest index starts at i - after each iteration, one more item is "sorted"
    lowest_index = i

    # Inner loop: i+1..length of list-1
    for j in range(i + 1, len(l)):
      if l[j] < l[lowest_index]:
        lowest_index = j

    # Swap the lowest into its place
    l[lowest_index], l[i] = l[i], l[lowest_index]

  # Return the fully sorted array!
  return l

test_list = [2, 5, 8, 0, -1, 3, 6, 7, -2, 4, 10, 9, 1]
print('UNSORTED:', test_list)
print('SELECTION SORTED:', selection_sort(test_list))

# def SelectionSort(arr):
# 	for i in range(len(arr)-1):
# 		minNum = i
# 		for j in range(i+1, len(arr)):
# 			if arr[j] < arr[i]:
# 				minNum = j
# 			arr[i], arr[minNum] = arr[minNum], arr[i]
# 	return arr
# print(SelectionSort([2,5,1,9,3,0]))
