class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        str_ = str.split(' ')
        dct = dict()
        if len(str_) != len(pattern):
            return False
        for i, letter in enumerate(pattern):
            if letter not in dct:
                dct[letter] = str_[i]
            else:
                if dct[letter] != str_[i]:
                    return False
        if len(set(dct.values())) != len(dct.values()):
            return False
        return True