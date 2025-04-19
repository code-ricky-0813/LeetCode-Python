#myself
class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        if not s:
            return 0
        a = s[0]
        b = 0
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        if a.isdigit():
            for i in range(len(s)):
                if s[i].isdigit():
                    b = b * 10 + int(s[i])
                else:
                    break
            if b > INT_MAX:
                return INT_MAX
            if b < INT_MIN:
                return INT_MIN
            return b
        elif a == "+":
            for i in range(1, len(s)):
                if s[i].isdigit():
                    b = b * 10 + int(s[i])
                else:
                    break
            if b > INT_MAX:
                return INT_MAX
            if b < INT_MIN:
                return INT_MIN
            return b
        elif a == "-":
            for i in range(1, len(s)):
                if s[i].isdigit():
                    b = b * 10 + int(s[i])
                else:
                    break
            b = -b
            if b > INT_MAX:
                return INT_MAX
            if b < INT_MIN:
                return INT_MIN
            return b
        else:
            return 0

#better one
class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        if not s:
            return 0

        sign = 1
        index = 0
        if s[0] == '-':
            sign = -1
            index += 1
        elif s[0] == '+':
            index += 1

        b = 0
        while index < len(s) and s[index].isdigit():
            b = b * 10 + int(s[index])
            index += 1

        b = b * sign

        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        if b > INT_MAX:
            return INT_MAX
        if b < INT_MIN:
            return INT_MIN

        return b
    
print(Solution().myAtoi("42"))              # 42
print(Solution().myAtoi("   -42"))          # -42
print(Solution().myAtoi("4193 with words")) # 4193
print(Solution().myAtoi("words and 987"))   # 0
print(Solution().myAtoi("-91283472332"))    # -2147483648
print(Solution().myAtoi("91283472332"))     # 2147483647
print(Solution().myAtoi("+1"))              # 1
print(Solution().myAtoi(""))                # 0