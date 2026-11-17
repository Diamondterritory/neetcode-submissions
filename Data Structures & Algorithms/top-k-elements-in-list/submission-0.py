class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_dict = {}
        for i in nums:
            nums_dict[i] = 1 + nums_dict.get(i, 0)
        
        top_k_list = sorted(nums_dict, key=nums_dict.get, reverse=True)
        return top_k_list[:k]