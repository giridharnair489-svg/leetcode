class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        arr_counter = Counter(arr)
        min_heap = []
        for num, freq in arr_counter.items():
            heapq.heappush(min_heap, (freq, num))

        while k > 0 and min_heap:
            freq, num = heapq.heappop(min_heap)
            if k >= freq:
                k -= freq
            else:
                heapq.heappush(min_heap, (freq - k, num))
                break

        return len(min_heap)