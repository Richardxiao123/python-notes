class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq
        h=[-x for x in nums]
        heapq.heapify(h)
        for i in range(k):
            out= heapq.heappop(h) 
        return -out  
