class Solution:
    def countNumbersWithUniqueDigits(self, n):
        if n == 0:
            return 1
        tot = 10
        u_digits = 9
        a_digits = 9

        for i in range(2, n + 1):
            u_digits *= a_digits
            tot += u_digits
            a_digits -= 1

        return tot

if __name__ == "__main__":
    param_1 = 2  
    solution = Solution()
    result = solution.countNumbersWithUniqueDigits(param_1)
    print(f"Result: {result}")
