class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0):
            sig = -1
        else:
            sig = 1
        dividend = abs(dividend)
        divisor = abs(divisor)
        res = 0

        while dividend >= divisor:
            b = divisor
            cnt = 1
            while dividend >= b:
                res += cnt
                dividend -= b
                b = b * 2
                cnt = cnt * 2

        res = sig * res

        if res <= -2**31:
            res = -2**31
        if res >= 2**31 - 1:
            res = 2**31 - 1
        return res

if __name__ == "__main__":
    solution = Solution()
    
    print(solution.divide(10, 3))  
    print(solution.divide(7, -3))   
    print(solution.divide(-2147483648, -1))  
