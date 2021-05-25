from collections import deque

def topological_sort(vertices, edges):
	t_sorted_order = []
	in_degrees = {i: 0 for i in range(vertices)}
	children = {i: [] for i in range(vertices)}
	for edge in edges:
		source = edge[0]
		child = edge[1]
		in_degrees[child] += 1
		children[source].append(child)

	q = deque()
	for k in in_degrees:
		if in_degrees[k] == 0:
			q.append(k)

	while q:
		node = q.popleft()
		t_sorted_order.append(node)
		del in_degrees[node]
		for child in children[node]:
			in_degrees[child] -= 1
			if in_degrees[child] == 0:
				q.append(child)

	# topological sort is not possible as the graph has a cycle
	if len(t_sorted_order) != vertices:
		return []

	return t_sorted_order


# print("Topological sort: " +
#     str(topological_sort(4, [[3, 2], [3, 0], [2, 0], [2, 1]])))
# print("Topological sort: " +
#     str(topological_sort(5, [[4, 2], [4, 3], [2, 0], [2, 1], [3, 1]])))
# print("Topological sort: " +
#     str(topological_sort(7, [[6, 4], [6, 2], [5, 3], [5, 4], [3, 0], [3, 1], [3, 2], [4, 1]])))



def is_scheduling_possible(tasks, prerequisites):
	in_degrees = {i: 0 for i in range(tasks)}
	children = {i: [] for i in range(tasks)}

	for pre in prerequisites:
		source = pre[0]
		child = pre[1]
		in_degrees[child] += 1
		children[source].append(child)

	q = deque()
	for k in in_degrees:
		if in_degrees[k] == 0:
			q.append(in_degrees[k])

	courses_taken = []
	while q:
		course = q.popleft()
		courses_taken.append(course)
		for child in children[course]:
			in_degrees[child] -= 1
			if in_degrees[child] == 0:
				q.append(child)

	if len(courses_taken) == tasks:
		return True

	return False


print("Is scheduling possible: " +
    str(is_scheduling_possible(3, [[0, 1], [1, 2]])))
print("Is scheduling possible: " +
    str(is_scheduling_possible(3, [[0, 1], [1, 2], [2, 0]])))
print("Is scheduling possible: " +
    str(is_scheduling_possible(6, [[0, 4], [1, 4], [3, 2], [1, 3]])))










