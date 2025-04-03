class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def expand_around_center(s, left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]
        
        longest = ""
        for i in range(len(s)):
            p1 = expand_around_center(s, i, i)
            p2 = expand_around_center(s, i, i + 1)
            longest = max(longest, p1, p2, key=len)
        
        return longest

if __name__ == "__main__":
    solution = Solution()
    
    s1 = "babad"
    result1 = solution.longestPalindrome(s1)
    print(f"Example 1: {s1}")
    print("Longest Palindromic Substring:", result1)
    print()

    s2 = "cbbd"
    result2 = solution.longestPalindrome(s2)
    print(f"Example 2: {s2}")
    print("Longest Palindromic Substring:", result2)