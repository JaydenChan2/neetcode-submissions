class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        tar = [0, 0]

        for i in range(0, len(nums)):
            for j in range(i, len(nums)):
                if nums[i] + nums[j] == target and i != j:
                    tar[0] = i
                    tar[1] = j

        return tar;