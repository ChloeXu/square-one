from heapq import *
from collections import deque


# heap
a = [4, 2, 3, 7]
heappush(a, 1)
heappop(a)


# queue
q = deque()
q.append(3)
q.appendleft(3)
q.pop()
q.popleft()

q_length = len(q)
