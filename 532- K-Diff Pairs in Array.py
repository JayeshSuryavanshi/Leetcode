class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        
        count = collections.Counter(nums)
        temp = 0
        
        for i in count:
            if k > 0 and i + k in count or k == 0 and count[i] > 1:
                temp += 1
        return temp
        