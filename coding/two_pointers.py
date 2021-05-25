def remove_duplicates(arr):
	non_dup_ind = 0
	nextInd = 0
	while nextInd + 1 < len(arr):
		print("=======", non_dup_ind, nextInd)
		if arr[nextInd + 1] != arr[non_dup_ind]:
			print("pre change", arr)
			arr[non_dup_ind] = arr[nextInd]
			non_dup_ind += 1
			print("post change", arr)
		nextInd += 1
	return non_dup_ind


def remove_key(arr, k):
	removed_till_ind = 0
	nextInd = 0 # exl
	while nextInd < len(arr):
		if arr[nextInd] != k:
			arr[removed_till_ind] = arr[nextInd]
			removed_till_ind += 1
		nextInd += 1
	return removed_till_ind


def make_squares(arr):
	squares = []
	negInd = 0
	for i, num in enumerate(arr):
		if num >= 0:
			negInd = i
			break
	b = negInd - 1
	f = negInd
	while b >= 0 and f < len(arr):
		print(b, f)
		bsq = arr[b] * arr[b]
		fsq = arr[f] * arr[f]
		if bsq < fsq:
			squares.append(bsq)
			b -= 1
		else:
			squares.append(fsq)
			f += 1
	if b >= 0:
		while b >= 0:
			squares.append(arr[b] * arr[b])
			b -= 1
	if f <= len(arr) - 1:
		while f <= len(arr) - 1:
			squares.append(arr[f] * arr[f])
			f += 1

	return squares


s = [-6, -2, -1, 0, 2, 3]
print(make_squares(s))


# s = [2, 2, 3, 3, 4, 6, 9, 9]
# print(remove_duplicates(s))

# s = [2, 11, 2, 2, 1]
# k = 2
# s = [3, 2, 3, 6, 3, 10, 9, 3]
# k = 3
# print(remove_key(s, k))

"""
it1 : [3, 2, 3, 6, 3, 10, 9, 3], nextInd = 1
it2 : [2, 2, 3, 6, 3, 10, 9, 3], removed_till_ind = 1, nextInd = 2
it3 : [2, 2, 3, 6, 3, 10, 9, 3], nextInd = 3
it4 : [2, 6, 3, 6, 3, 10, 9, 3], removed_till_ind = 2, nextInd = 4
"""