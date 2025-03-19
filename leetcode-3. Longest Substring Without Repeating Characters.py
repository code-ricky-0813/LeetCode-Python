class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        start = 0
        max_len = 0
        
        for end in range(len(s)):
            while s[end] in seen:
                seen.remove(s[start])
                start += 1
            seen.add(s[end])
            max_len = max(max_len, end - start + 1)
        
        return max_len

# 測試範例
if __name__ == "__main__":
    solution = Solution()
    
    # 測試例子 1
    s1 = "abcabcbb"
    print(f"Input: {s1}, Output: {solution.lengthOfLongestSubstring(s1)}")  # Output: 3
    
    # 測試例子 2
    s2 = "bbbbb"
    print(f"Input: {s2}, Output: {solution.lengthOfLongestSubstring(s2)}")  # Output: 1
    
    # 測試例子 3
    s3 = "pwwkew"
    print(f"Input: {s3}, Output: {solution.lengthOfLongestSubstring(s3)}")