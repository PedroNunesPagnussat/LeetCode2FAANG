from typing import List

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        numbers_map = {}


        for item in arr:
            if item not in numbers_map:
                numbers_map[item] = 1
            else:
                numbers_map[item] += 1

        return len(set(numbers_map.values())) == len(set(arr))

        

if __name__ == "__main__":
    arr = [1,2]
    c = Solution()
    solution = c.uniqueOccurrences(arr)
    print(solution)