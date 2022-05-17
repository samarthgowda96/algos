class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        order = sorted(heights)
        count = 0
        for i in range(len(order)):
            if order[i] != heights[i]:
                count +=1
        return count
        