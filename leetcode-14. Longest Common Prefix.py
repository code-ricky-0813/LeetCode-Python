from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = []

        for i in range(len(strs[0])):
            ch = strs[0][i]
            for s in strs[1:]:
                if i >= len(s) or s[i] != ch:
                    return "".join(prefix)
            prefix.append(ch)
            
        return "".join(prefix)

solution = Solution()
print(solution.longestCommonPrefix(["flower", "flow", "flight"]))
print(solution.longestCommonPrefix(["dog", "racecar", "car"]))