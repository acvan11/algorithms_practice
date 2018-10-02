def quick_sort(arr):
  if len(arr) <= 1:
    return arr
  else:
    pivot = arr.pop(0)
    left = [x for x in arr if x < pivot]
    print(left)
    right = [x for x in arr if x >= pivot]
    print(right)
    print('==========')
    return quick_sort(left) + [pivot] + quick_sort(right)

test_arr = [3, 1, 6, 2, 4]
print('ORIGINAL:', test_arr)
print('SORTED:', quick_sort(test_arr))
