class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand_around_center(s, left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]
        
        longest = ""
        for i in range(len(s)):
            p1 = expand_around_center(s, i, i)
            p2 = expand_around_center(s, i, i+1)
            longest = max(longest, p1, p2, key = len)

        return longest
    
solution = Solution()
    
s1 = "babad"
result1 = solution.longestPalindrome(s1)
print(result1)

s2 = "cbbd"
result2 = solution.longestPalindrome(s2)
print(result2)