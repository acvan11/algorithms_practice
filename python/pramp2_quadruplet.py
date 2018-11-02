'''
input:  arr = [2, 7, 4, 0, 9, 5, 1, 3], s = 20

output: [0, 4, 7, 9] # The ordered quadruplet of (7, 4, 0, 9)
                     # whose sum is 20. Notice that there
                     # are two other quadruplets whose sum is 20:
                     # (7, 9, 1, 3) and (2, 4, 9, 5), but again you’re
                     # asked to return the just one quadruplet (in an
                     # ascending order)
'''
def find_array_quadruplet(arr, s):
  arr.sort()
  for i1 in range(len(arr)-1):
    for i2 in range(i1+1, len(arr)):
      count = s - arr[i1] - arr[i2]
      low = i2+1
      high = len(arr)-1
      while low < high:
        if arr[low] + arr[high] < count:
          low += 1
        elif arr[low] + arr[high] > count:
          high -= 1
        else:
          return [arr[i1], arr[i2], arr[low], arr[high]]
  return []
