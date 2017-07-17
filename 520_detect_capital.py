class Solution(object):
    def detectCapitalUse_1(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if all([x.isupper() for x in word]):
            return True
        elif all([x.islower() for x in word]):
            return True
        elif word[0].isupper():
            if all([x.islower() for x in word[1:]]):
                return True
        return False

    def detectCapitalUse_2(self, word):
        """
        :type word: str
        :rtype: bool
        """
        sum_ = sum([x.isupper() for x in word])
        # print(sum_)
        if abs(sum_) == len(word) or abs(sum_) == 0:
            return True
        elif word[0].isupper() and sum_ == 1:
            return True
        return False

    def detectCapitalUse_3(self, word):
        """
        :type word: str
        :rtype: bool
        """
        # sum_ = sum([x.isupper() for x in word])
        # # print(sum_)
        # if abs(sum_) == len(word) or abs(sum_) == 0:
        #     return True
        # elif word[0].isupper() and sum_ == 1:
        #     return True
        # return False
        if word.isupper() or word.islower() or word.istitle():
            return True
        else:
            return False

Solution().detectCapitalUse_1("USA")


            
