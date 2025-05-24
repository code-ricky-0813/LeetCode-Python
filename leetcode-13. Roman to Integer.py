class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                     'C': 100, 'D': 500, 'M': 1000}
        prev = 0
        total = 0

        for i in reversed(s):
            value = roman_map[i]
            if value < prev:
                total -= value
            else:
                total += value
            prev = value

        return total
    
sol = Solution()
test_cases = ["III", "IV", "IX", "LVIII", "MCMXCIV"]
for roman in test_cases:
    print(f"{roman}: {sol.romanToInt(roman)}")