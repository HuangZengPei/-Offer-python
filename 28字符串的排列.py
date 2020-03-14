# -*- coding:utf-8 -*-
class Solution:
    def Permutation(self, ss):
        # write code here
        if len(ss) <= 1:
            return ss
        result = []
        for i in range(len(ss)):
            s = ss[:i] + ss[i+1:]
            permuta = self.Permutation(s)
            for p in permuta:
                result.append(ss[i:i+1]+p)
        return sorted(list(set(result)))