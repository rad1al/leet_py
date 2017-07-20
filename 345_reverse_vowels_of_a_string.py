class Solution(object):
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        # if len(s) == 2 and s[0] in self.vowels and s[1] in self.vowels:
            # return s[::-1]
        stack = list()
        for i, item in enumerate(s):
            if item in self.vowels:
                stack.append(item)
        # print stack, ['a', 'A']
        s_lst = list(s)
        # stack = stack[::-1]
        for i, item in enumerate(s_lst):
            if item in self.vowels:
                s_lst[i] = stack.pop()
        return ''.join(s_lst)
        

assert Solution().reverseVowels('leetcode') == 'leotcede'