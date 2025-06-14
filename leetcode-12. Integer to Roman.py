class Solution:
    def intToRoman(self, num: int) -> str:
        thousands = ["", "M", "MM", "MMM"]
        hundreds  = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        tens      = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        ones      = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]

        roman = (
            thousands[num // 1000] +
            hundreds[(num % 1000) // 100] +
            tens[(num % 100) // 10] +
            ones[num % 10]
        )

        return roman

solution = Solution()
print(solution.intToRoman(3749)) 
print(solution.intToRoman(58))  
print(solution.intToRoman(1994)) 
