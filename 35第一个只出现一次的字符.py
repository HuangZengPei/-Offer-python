# -*- coding:utf-8 -*-
class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        if not s:return
        charCount = {}
        for char in s:
            try:
                charCount[char] += 1
            except:
                charCount[char] = 1
        for char in s:
            if charCount[char] == 1:
                return s.index(char)
        return -1