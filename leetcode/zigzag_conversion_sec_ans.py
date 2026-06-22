class Solution:
    def convert(self, s: str, numRows: int) -> str:
        index_list = []
        res = ''
        length_s = len(s)
        length_res = len(index_list)

        if length_s <= numRows or numRows == 1:
            return s

        index = 0
        row = 0
        check = 0
        diff = [2*numRows-2, 0]

        while row < numRows:
            if index >= length_s:
                row += 1
                index = row
                diff[0] -= 2
                diff[1] += 2
                check = 0

                if row == numRows:
                    break

            if diff[check] == 0:
                check = 1 if check == 0 else 0

            res = res + s[index]
            index += diff[check]

            check = 1 if check == 0 else 0

        return res



