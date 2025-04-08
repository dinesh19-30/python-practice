class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MAX=2**31-1
        INT_MIN= -2**31

        if dividend==INT_MIN and divisor==-1:
            return INT_MAX
        
        negative= (dividend<0) ^ (divisor<0)

        dividend = abs(dividend)
        divisor = abs(divisor)
        quotient = 0

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
