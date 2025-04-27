class Solution:
    def myPow(self, x: float, n: int) -> float:
        return x ** n

if __name__ == "__main__":
    param_1 = 2.0   # Example base
    param_2 = 10    # Example exponent
    solution = Solution()
    result = solution.myPow(param_1, param_2)
    print(f"Result: {result}")
