class Solution(object):

    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:return ""
        temp = s.split()
        begin = 0
        end = len(temp)-1
        while begin < end:
            temp[begin], temp[end] = temp[end],temp[begin]
            begin += 1
            end -= 1
        return " ".join(temp)
        
        
test = Solution()
print(test.reverseWords("I am a Student"))