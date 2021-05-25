from collections import deque


class TreeNode:
	def __init__(self, val):
		self.val = val
		self.left, self.right = None, None


def traverse1(root):
	if root is None:
		return root

	results = []
	q = deque()
	q.append((root, 0))
	while q:
		item, level = q.popleft()
		if len(results) >= level + 1:
			results[level].append(item.val)
		else:
			results.append([item.val])

		if item.left:
			q.append((item.left, level + 1))
		if item.right:
			q.append((item.right, level + 1))	

	return results


def traverse2(root):
	if root is None:
		return root

	results = deque()
	q = deque()
	q.append(root)
	while q:
		level_size = len(q)
		current_level = []
		for _ in range(level_size):
			current_node = q.popleft()
			current_level.append(current_node.val)
			if current_node.left:
				q.append(current_node.left)
			if current_node.right:
				q.append(current_node.right)	
		results.appendleft(current_level)

	return list(results)


def traverse3(root):
	if root is None:
		return root

	results = []
	q = deque()
	q.append(root)
	leftToRight = True
	while q:
		level_size = len(q)
		current_level = deque()
		for _ in range(level_size):
			current_node = q.popleft()
			if leftToRight:
				current_level.append(current_node.val)
			else:
				current_level.appendleft(current_node.val)
			if current_node.left:
				q.append(current_node.left)
			if current_node.right:
				q.append(current_node.right)	
		results.append(list(current_level))
		leftToRight = not leftToRight

	return results


root = TreeNode(12)
root.left = TreeNode(7)
root.right = TreeNode(1)
root.left.left = TreeNode(9)
root.right.left = TreeNode(10)
root.right.right = TreeNode(5)
print("Level order traversal: " + str(traverse3(root)))






