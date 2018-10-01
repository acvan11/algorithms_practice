def merge_sort(arr):
  if len(arr) <= 1:
    return arr
  else:
    middle_index = len(arr) // 2
    left = arr[:middle_index]
    right = arr[middle_index:]
    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)
    return merge(left_sorted, right_sorted)


def merge(arr1, arr2):
  results = []
  while len(arr1) > 0 and len(arr2) > 0:
    if arr1[0] <= arr2[0]:
      results.append(arr1.pop(0))
    else:
      results.append(arr2.pop(0))

  return results + arr1 + arr2