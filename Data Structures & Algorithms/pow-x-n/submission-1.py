class Solution:
    def myPow(self, x: float, n: int) -> float:
        result = 1.0
        base = x
        exponent = abs(n)

        while exponent > 0:
            if exponent % 2 == 1:
                result *= base

            base *= base
            exponent //= 2

        return 1 / result if n < 0 else result