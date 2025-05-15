class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        elif x >= 0:
            text_x = str(x)
            if text_x == text_x[::-1]: return True
            else: return False

# Test cases   
test_cases = [123, 12321, 123456, -12321, 1234567890]

for case in test_cases:
    print(Solution().isPalindrome(case))

