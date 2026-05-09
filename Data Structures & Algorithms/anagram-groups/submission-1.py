class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counts = dict()

        for s in strs:
            count = [0] * 26
            for ch in s: 
                count[ord(ch) - ord('a')] += 1
            counts[tuple(count)] = counts.get(tuple(count), [])
            counts[tuple(count)].append(s)

        return list(counts.values())
