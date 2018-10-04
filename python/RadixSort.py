def make_buckets():
	#make an array put 10 empty arrays in that array [[], [], ...]
	#return it
	buckets = []
	for i in range(10):
		buckets.append([])
	return buckets

def flatten(buckets):
	#take a nulti-dimensional array and make it one-dimensional
	flat = []
	for ls in buckets:
		flat += ls
	return flat

def get_max_digits(ls):
	return len(str(max(ls)))

def radix_sort(ls):
	buckets = make_buckets()
	max_digits = get_max_digits(ls)
	current_digit = 1

	for i in range(max_digits):
		for j in range(len(ls)):
			#Get the significant digit onto the end of the number
			sig = ls[j] // current_digit
			# get the bucket number it should go into
			bucket_num = sig % 10
			## Add it to the buckets
			buckets[bucket_num].append(ls[j])

		# Increment the current digit that we're looking at right now
		current_digit *= 10
		# Flatten the buckets back into the list
		ls = flatten(buckets)
		# Make new buckets
		buckets = make_buckets()

	return ls

test = [2,12,323,1333,71,93559,23,1,345,295,24235,71,8]
print(radix_sort(test))
