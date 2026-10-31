class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        max_k = {}

        for num in nums:
            if num in freq:
                freq[num] += 1
            
            else:
                freq[num] = 1
        
        return [i[0] for i in sorted(freq.items(), key=lambda f: f[1], reverse=True)[:k]]