class TreeNode:
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

####################################################################################


def has_path_dfs(node, curr_s, target_s):
	if node is None:
		if curr_s == target_s:
			return True
		else:
			return False

	if curr_s < target_s:
		return has_path_dfs(node.left, curr_s + node.val, target_s) or has_path_dfs(node.right, curr_s + node.val, target_s)
	else:
		return False


def has_path(root, target_s):
	return has_path_dfs(root, 0, target_s)


# root = TreeNode(12)
# root.left = TreeNode(7)
# root.right = TreeNode(1)
# root.left.left = TreeNode(9)
# root.right.left = TreeNode(10)
# root.right.right = TreeNode(5)
# print("Tree has path: " + str(has_path(root, 23)))
# print("Tree has path: " + str(has_path(root, 16)))

"""
sum = 23
      12
   7      1
 9     10   5
 
it1: node = Node(12), 
		node = Node(7), 12 < 23, 12 + 7 = 19
			node = Node(9), 19 + 9 > 23, return False
		node = Node(1), 12 < 23, 12 + 1 = 13
			node = Node(10), 13 < 23, 13 + 10 = 23, 
				node = Node(None), curr == target, return True
			...
		return True
	return True 
"""

####################################################################################


def find_paths_dfs(node, curr_s, arr_at_node, target_s, res):
	if node is None:
		return
	curr_s = curr_s + node.val
	arr_at_node.append(node.val)
	if curr_s < target_s:

		find_paths_dfs(node.left, curr_s, arr_at_node, target_s, res)
		find_paths_dfs(node.right, curr_s, arr_at_node, target_s, res)

	elif curr_s == target_s and node.left is None and node.right is None:
		res.append(arr_at_node[:])

	curr_s -= node.val
	arr_at_node.pop()
	return
def find_paths(root, target_s):
	res = []
	find_paths_dfs(root, 0, [], target_s, res)
	return res

# root = TreeNode(12)
# root.left = TreeNode(7)
# root.right = TreeNode(1)
# root.left.left = TreeNode(4)
# root.right.left = TreeNode(10)
# root.right.right = TreeNode(5)
# sum = 23
# print("Tree paths with sum " + str(sum) +
#       ": " + str(find_paths(root, sum)))

"""
sum = 12
---------------
	   1
   7       9
 4   5   2   7
---------------
res = [ [1, 7, 4] ]
dfs:   Node(1), curr_s(1) < 12, arr_at_n = [1]
			Node(7) 1 < 12 => arr_at_n = [1, 7], curr_s(8)
				Node(4)  8 < 12 => arr_at_n = [1, 7, 4], curr_s(12)
					Node(None) curr_s = target, add result 
				Node(5)  8 < 12 => arr_at_n = [1, 7, 5], curr_s(13)
					Node(None) curr_s != target, move on
"""

####################################################################################

# def find_sum_of_path_nums_dfs(node, curr_paths, all_paths):
# 	if node is None:
# 		return
# 	if node.left is None and node.right is None:
# 		curr_paths.append(node.val)
# 		print(curr_paths[:])
# 		all_paths.append(curr_paths[:])
# 		curr_paths.pop()
# 		return

# 	curr_paths.append(node.val)
# 	find_sum_of_path_nums_dfs(node.left, curr_paths, all_paths)
# 	find_sum_of_path_nums_dfs(node.right, curr_paths, all_paths)
# 	curr_paths.pop()
# 	return

# def find_sum_of_path_nums(root):
# 	all_paths = []
# 	curr_paths = []
# 	find_sum_of_path_nums_dfs(root, curr_paths, all_paths)
# 	print("All paths", all_paths)
# 	s = 0
# 	for path in all_paths:
# 		print("path - ", path)
# 		path_len = len(path)
# 		for i, num in enumerate(path):
# 			pow_of_10 = path_len - i - 1
# 			curr_val = 1
# 			for p in range(pow_of_10):
# 				curr_val = curr_val * 10
# 			s += num * curr_val
# 	return s

def find_sum_of_path_nums_dfs(node, pathSum):
	if node is None:
		return 0
	pathSum = pathSum * 10 + node.val
	if node.left is None and node.right is None:
		return pathSum

	left = find_sum_of_path_nums_dfs(node.left, pathSum)
	right = find_sum_of_path_nums_dfs(node.right, pathSum)
	print("left", left, "right", right)
	return left + right

def find_sum_of_path_nums(root):
	res = find_sum_of_path_nums_dfs(root, 0)
	return res

# root = TreeNode(1)
# root.left = TreeNode(0)
# root.right = TreeNode(1)
# root.left.left = TreeNode(1)
# root.right.left = TreeNode(6)
# root.right.right = TreeNode(5)
# print("Total Sum of Path Numbers: " + str(find_sum_of_path_nums(root)))

"""
---------------
	   1
    0      1
 1       6   5
--------------- 
"""

####################################################################################

def find_sequence_dfs(node, seq, depth):
	if node is None:
		return False
	if seq[depth] == node.val and node.left is None and node.right is None:
		return True

	if seq[depth] == node.val:
		return find_sequence_dfs(node.left, seq, depth + 1) or find_sequence_dfs(node.right, seq, depth + 1)
	else:
		return False


def find_sequence(root, sequence):
	res = find_sequence_dfs(root, sequence, 0)
	return res

root = TreeNode(1)
root.left = TreeNode(0)
root.right = TreeNode(1)
root.left.left = TreeNode(1)
root.right.left = TreeNode(6)
root.right.right = TreeNode(5)
print("Tree has path sequence: " + str(find_sequence(root, [1, 0, 7])))
print("Tree has path sequence: " + str(find_sequence(root, [1, 1, 6])))

"""
---------------
	   1
    0      1
 1       6   5
--------------- 
"""





























