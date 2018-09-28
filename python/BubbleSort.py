# BUBBLE SORT
# O(n) best case, O(n^2) worst case
def bubble_sort(l):
  # Outer loop: 0..length of list-1
  for i in range(len(l)):
    # Track whether there were any swaps this round
    swapped = False

    # Inner loop: 0..length of list - 1 - i
    for j in range(len(l) - i - 1):
      if l[j] > l[j + 1]:
        swapped = True
        l[j], l[j + 1] = l[j + 1], l[j]

    # Check if I can break out early
    if not swapped:
      break
      
  return l

test_list = [9, 3, 1, 2, 7, 8, -1, 4, 0, 10, 6, 5]
print('BUBBLE SORTED', bubble_sort(test_list))


# def bubbleSort(arr):
# 	index = len(arr)
# 	for i in range(index):
# 		for j in range(index-i-1):
# 			if (arr[j] > arr[j+1]):
# 				arr[j], arr[j+1] = arr[j+1], arr[j]		
# 	return arr

# print(bubbleSort([4,2,5,6]))
