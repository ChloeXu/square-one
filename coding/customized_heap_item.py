# leetcode #347

from heapq import *


class PQItem:
    def __init__(self, val, k):
        self.val = val
        self.k = k

    def __lt__(self, other):
        return self.val < other.val


class Solution:
    def top_k_frequent(self, nums, k):
        hashtable = {}
        for num in nums:
            if num in hashtable:
                hashtable[num] += 1
            else:
                hashtable[num] = 1
        pq = []
        revhash = {}
        for ke in hashtable:
            revhash[hashtable[ke]] = ke
            heappush(pq, PQItem(-hashtable[ke], ke))

        res = []
        while pq:
            item = heappop(pq)
            res.append(item.k)
            if len(res) == k:
                break
        return res
