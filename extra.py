# Function to print all quadruplet present in a list with a given sum
# 2 inputs: #array  and int number for the target sum
# 1 2 3 4 5 6 7 0 9 6
# 8 
# sum output: 
# [0, 1, 2, 5]
# [0, 1, 3, 4]

# Function to print all quadruplet present in a list with a given sum
# def quadTuple(A, target):

	# sort the list in ascending order
	# A.sort()

	# check if quadruplet is formed by `A[i]`, `A[j]`, and a pair from
	# sublist `A[j+1…n)`
	# for i in range(len(A) - 3):
	# 	for j in range(i + 1, len(A) - 2):

			# `k` stores remaining sum
			# k = target - (A[i] + A[j])

			# check for sum `k` in sublist `A[j+1…n)`
			# low = j + 1
			# high = len(A) - 1

			# while low < high:
			# 	if A[low] + A[high] < k:
			# 		low = low + 1
			# 	elif A[low] + A[high] > k:
			# 		high = high - 1
				# quadruplet with a given sum found
				# else:
					# print((A[i], A[j], A[low], A[high]))
					# (low, high) = (low + 1, high - 1)


# if __name__ == '__main__':

# 	A = [2, 7, 4, 0, 9, 5, 1, 3]
# 	target = 20

# 	quadTuple(A, target)

