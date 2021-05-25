from heapq import *


def find_k_largest_numbers(nums, k):
	q = [-n for n in nums]
	# q = list(map(lambda x: x * -1, nums))
	heapify(q)
	
	# for num in nums:
	# 	heappush(q, -num)

	res = []
	ind = 0
	while ind < k:
		res.append(-heappop(q))
		ind += 1

	return res


# time complexity: O(nlogk)
print("Here are the top K numbers: " + str(find_k_largest_numbers([3, 1, 5, 12, 2, 11], 3)))

print("Here are the top K numbers: " + str(find_k_largest_numbers([5, 12, 11, -1, 12], 3)))
