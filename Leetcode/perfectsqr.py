class Solution:
    def isPerfectSquare(self, num):
        if num < 1:
            return False

        left, right = 1, num

        while left <= right:
            mid = (left + right) // 2  
            square = mid * mid

            if square == num:
                return True
            elif square < num:
                left = mid + 1
            else:
                right = mid - 1

        return False

if __name__ == "__main__":
    sol = Solution()
    test_cases = [1, 4, 16, 14, 100, 123456789]
    
    for num in test_cases:
        result = sol.isPerfectSquare(num)
        print(f"{num} is a perfect square: {result}")
