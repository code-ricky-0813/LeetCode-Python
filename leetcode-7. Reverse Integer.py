class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        sign = -1 if x < 0 else 1
        x = abs(x)

        while x != 0:
            digit = x % 10
            x = x // 10
            res = res * 10 + digit

        res = res * sign

        if res < -2**31 or res > 2**31 - 1:
            return 0
        return res

sol = Solution()

print(sol.reverse(123))
print(sol.reverse(-123))
print(sol.reverse(120)) 
print(sol.reverse(0)) 