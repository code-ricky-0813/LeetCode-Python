class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [""] * numRows

        current_rows = 0
        going_down = False

        for char in s:
            rows[current_rows] += char

            if current_rows == 0 or current_rows == numRows - 1:
                going_down = not going_down
            
            current_rows += 1 if going_down else -1
        
        return ''.join(rows)
    
solution = Solution()

s1 = "PAYPALISHIRING"
numRows1 = 3
print(solution.convert(s1, numRows1))

s2 = "PAYPALISHIRING"
numRows2 = 4
print(solution.convert(s2, numRows2)) 
    
s3 = "A"
numRows3 = 1
print(solution.convert(s3, numRows3))