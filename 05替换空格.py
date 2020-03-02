class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        # 双指针替换
        if not s:return ''
        spaceNum = 0
        for i in s:
            if i == " ":
                spaceNum += 1
        newStrLen = len(s) + spaceNum * 2
        newStr = newStrLen * [None]
        indexOfOriginal, indexOfNew = len(s) - 1, newStrLen - 1
        while indexOfOriginal >= 0:
            if s[indexOfOriginal] == ' ':
                newStr[indexOfNew-2:indexOfNew+1] = '%20'
                indexOfNew -= 3
                indexOfOriginal -= 1
            else:
                newStr[indexOfNew] = s[indexOfOriginal]
                indexOfNew -= 1
                indexOfOriginal -= 1
        return newStr


