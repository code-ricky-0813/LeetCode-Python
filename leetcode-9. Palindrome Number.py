#str x
class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        for i in range(len(x) // 2):
            if x[i] != x[-i - 1]:
                return False
        return True

#int x
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reversed_half = 0
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10

        return x == reversed_half or x == reversed_half // 10

sol = Solution()
print(sol.isPalindrome(121))   # True
print(sol.isPalindrome(-121))  # False
print(sol.isPalindrome(10))    # False
print(sol.isPalindrome(0))     # True
print(sol.isPalindrome(1221))  # True