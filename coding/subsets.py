from collections import deque

def find_subsets(nums):
	subsets = [[]]
	eleInd = 0
	while eleInd < len(nums):
		print(eleInd)
		n = len(subsets)
		for i in range(n):
			subset = subsets[i]
			new_set = subset[:]
			new_set.append(nums[eleInd])
			subsets.append(new_set)
		eleInd += 1
	return subsets

# print("Here is the list of subsets: " + str(find_subsets([1, 3])))
# print("Here is the list of subsets: " + str(find_subsets([1, 5, 3])))


def find_subsets_with_dups(nums):
	subsets = [[]]
	eleInd = 0
	prev_num = None
	prev_subsets = []
	while eleInd < len(nums):
		print(eleInd)
		inserted_set = []
		if nums[eleInd] == prev_num:
			n = len(prev_inserted)
			for i in range(n):
				subset = prev_inserted[i]
				new_set = subset[:]
				new_set.append(nums[eleInd])
				inserted_set.append(new_set)
				subsets.append(new_set)
		else:
			n = len(subsets)
			for i in range(n):
				subset = subsets[i]
				new_set = subset[:]
				new_set.append(nums[eleInd])
				inserted_set.append(new_set)
				subsets.append(new_set)
		prev_num = nums[eleInd]
		prev_inserted = inserted_set
		eleInd += 1
	return subsets


# print("Here is the list of subsets: " + str(find_subsets_with_dups([1, 3, 3])))
# print("Here is the list of subsets: " + str(find_subsets_with_dups([1, 5, 3, 3])))

def _permutation_dfs(nums, current_combo, curr_ind, res):
	if curr_ind > len(nums) - 1:
		res.append(current_combo)
		return

	num_of_inserts = curr_ind + 1
	for i in range(num_of_inserts):
		new_combo = current_combo[:]
		new_combo.insert(i, nums[curr_ind])
		_permutation_dfs(nums, new_combo, curr_ind + 1, res)


def find_permutations(nums):
	n = len(nums)
	res = []
	_permutation_dfs(nums, [], 0, res)
	return res


print("Here are all the permutations: " + str(find_permutations([1, 3, 5])))




































