class Solution:
    def partition(self, s):
        steps = []
        output = []
        self._dfs(s, 0, steps, output)
        print(output)
    
    def _dfs(self, s, ind, steps, output):
        if ind >= len(s):
            print(steps)
            output.append(steps)
            # steps = []
            return
        for i in range(ind, len(s)):
            if s[ind: ind + i] and self._isPalindrome(s[ind: ind + i]):
                print("{} - {}, {}".format(s[ind: ind + i], ind, i))
                steps.append(s[ind: ind + i])
                self._dfs(s, ind + i, steps, output)
                steps = []
                
    def _isPalindrome(self, s):
        if len(s) == 1:
            return True
        if len(s) % 2 == 0:
            return "".join(reversed(s[0: len(s)//2])) == s[len(s)//2:]
        else:
            return "".join(reversed(s[0: (len(s) - 1)//2])) == s[(len(s) - 1)//2 + 1:]


Solution().partition("acbc")