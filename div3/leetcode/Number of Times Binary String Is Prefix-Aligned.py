class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        c = 0
        maxi = 0
        for i in range(len(flips)):
            maxi = max(maxi, flips[i] - 1)
            if maxi == i:
                c += 1
        return c
