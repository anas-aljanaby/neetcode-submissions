class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = dict()
        for n in nums:
            res[n] = res.get(n, 0) + 1

        s = dict(sorted(res.items(), key=lambda item: item[1], reverse=True))
        return list(s.keys())[:k]

