class Solution(object):
    def reverseLeftWords(self, s, n):
        """
        :type s: str
        :type n: int
        :rtype: str
        """
        if not s:return
        if n > len(s):return s
        s1 = s[:n]
        s2 = s[n:]
        return s2 + s1
        
test = Solution()
print(test.reverseLeftWords("abcdefg",2))