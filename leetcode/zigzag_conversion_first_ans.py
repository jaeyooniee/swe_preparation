class Solution:
    def convert(self, s: str, numRows: int) -> str:
        res = ''
        length = len(s)

        if numRows == 1:
            return s

        for i in range(numRows):
            diff = [numRows * 2 - 2*i - 2, 2*i]
            index = i
            check = 0

            while index < length:
                if diff[check] == 0:
                    check = 1 if check == 0 else 0
                    continue

                res = res + s[index]
                index += diff[check]
                check = 1 if check == 0 else 0

        return res
