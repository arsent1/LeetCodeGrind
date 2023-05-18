class Solution:
    def mySqrt(self, x: int) -> int:
        oddnum = 1
        square = 0
        while (x > 0):
            x = x - oddnum
            if (x > 0):
                oddnum += 2
                square += 1
            elif (x == 0):
                square += 1

        return square