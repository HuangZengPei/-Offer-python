class Solution(object):
    def strToInt(self, str):
        """
        :type str: str
        :rtype: int
        """
        number = 0
        minus = False
        if not str:return 0
        str = self.strTrim(str)
        for i , s in enumerate(str):
            if i == 0:
                if s == '-':
                    minus = True
                elif s.isdigit():
                    number = int(s)
                elif s =='+':
                    minus = False
                else:
                    return 0
            else:
                if s.isdigit():
                    number = number*10 + int(s)
                else:
                    return max(-number,-2**31) if minus else min(number,2**31-1)
        return max(-number,-2**31) if minus else min(number,2**31-1)
            
    def strTrim(self,str):
        if not str:return ""
        index = 0
        for i in range(len(str)):
            if str[i] == ' ':
                index += 1
            else:
                break
        return str[index:]
        
test = Solution()
print(test.strTrim("     good"))