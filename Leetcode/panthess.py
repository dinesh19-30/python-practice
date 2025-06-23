class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_map = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in bracket_map:
                top = stack.pop() if stack else '#'
                if bracket_map[char] != top:
                    return False
            else:
                stack.append(char)

        return not stack

if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        "()",          
        "()[]{}",      
        "(]",       
        "([)]",        
        "{[]}",        
        "[",           
        "((({{{[[[]]]}}})))"  
    ]

    for s in test_cases:
        result = sol.isValid(s)
        print(f"'{s}' is valid: {result}")
