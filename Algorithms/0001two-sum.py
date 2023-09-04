from typing import List


class Solution:
    # Brute Force
    def twoSumBruteForce(self, nums: List[int], target: int) -> List[int]:
        for i, n1, in enumerate(nums):
            for i, n1, in enumerate(nums):
                for j, n2 in enumerate(nums[i+1:]):
                    if n1 + n2 == target:
                        return [i, i+j+1]


    # Yes, I stole this from the leetcode discussion
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i, n in enumerate(nums):
            t = target - n
            if t in hashmap:
                return [i, hashmap[t]]
            hashmap[n] = i

if __name__ == '__main__':
    nums = [3,2,4]
    target = 6
    solution = Solution()
    s = solution.twoSum(nums, target)
