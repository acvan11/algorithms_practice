# Write a function called binary_search in python 
# that takes a data array and a target value as inputs
def binary_search(data, target):
	# Track minimum and maximum indexes
  min_index = 0
  max_index = len(data) - 1

  # Loop until we...
  # Find the target! Yay!
	# Have the condition min_index > max_index
  while min_index <= max_index:

    # Formulate my guess
    # Note: Double // means integer division
    guess = (min_index + max_index) // 2

    # Check if we found the target value
    if data[guess] == target:

      # We found it - use return, which breaks out of the function
      return guess

    elif data[guess] < target:

      # The target value is higher than my guess
      # So, guess + 1 is my new min_index
      min_index = guess + 1

    else:

      # The target is lower than the guess
      # So, we set the new max_index to guess - 1
      max_index = guess - 1
      
  # Negative one is generally understood to be a "bad" index, AKA not found!
  return -1


# Try out the function
test_target = 14
test_data = [1, 2, 4, 5, 7, 9, 10, 11, 13, 15, 16, 18, 100, 120]
print("Found target value", test_target, "at index", binary_search(test_data, test_target))









