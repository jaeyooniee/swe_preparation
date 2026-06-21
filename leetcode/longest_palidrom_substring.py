class Solution:
    def longestPalindrome(self, s: str) -> str:  
        def finding_pal(start, end):
            while start >= 0 and end < len(s) and s[start] == s[end]:
                start -= 1
                end += 1
            
            return s[start+1:end]

        res = ''

        for i in range(len(s)):
            res = max(res, finding_pal(i, i), finding_pal(i, i+1), key=len)

        return res

