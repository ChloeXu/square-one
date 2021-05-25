def sort_with_n_square_time_complexity(nums):
	i_ind = 0
	while i_ind < len(nums):
		for j in range(i_ind, len(nums)):
			if nums[j] == i_ind + 1:
				nums[j], nums[i_ind] = nums[i_ind], nums[j]
				break

		i_ind += 1

	return nums


def cyclic_sort(nums):
	i_ind = 0
	while i_ind < len(nums):
		num = nums[i_ind]
		if nums[i_ind] != nums[num]:
			nums[i_ind], nums[num] = nums[num], nums[i_ind]
		else:
			i_ind += 1

	return nums


def find_missing_number(nums):
	i = 0
	while i < len(nums):
		num = nums[i]
		if nums[i] < len(nums) and nums[i] != nums[num]:
			nums[i], nums[num] = nums[num], nums[i]
		else:
			i += 1
	for j in range(len(nums)):
		if j != nums[j]:
			return j

	return len(nums)

# a = [1, 5, 6, 4, 3, 2]
# b = [2, 6, 4, 3, 1, 5]
# c = [3, 1, 5, 4, 2]
# ra = cyclic_sort(a)
# print(ra)
# rb = cyclic_sort(b)
# print(rb)
# rc = cyclic_sort(c)
# print(rc)


print(find_missing_number([4, 0, 3, 1]))
print(find_missing_number([8, 3, 5, 2, 4, 6, 0, 1]))
