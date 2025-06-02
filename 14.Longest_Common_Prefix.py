from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        output = ''
        for i in range(len(strs)):
            print(i)
            print(strs[i][0])
        

testInput = ["flower","flow","flight"]
testCase = Solution()
print(testCase.longestCommonPrefix(testInput))