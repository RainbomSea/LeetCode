"""

给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。

"""


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        res = ['']
        t = {'2':'abc', '3':'def',
             '4':'ghi', '5':'jkl',
             '6':'mno', '7':'pqrs',
             '8':'tuv', '9':'wxyz'}
        
        if digits == '':
            return []

        for s in digits:
            ans = res
            res =[]
            for i in t[s]:
                for a in ans:
                    a += i
                    res.append(a)

        return res
