class Solution(object):
    rows = {0: set('qwertyuiop'),
            1: set('asdfghjkl'),
            2: set('zxcvbnm')}
    
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        return filter(self.can_type, words)
    
    def can_type(self, word):
        for i in range(3):
            state = 0
            for j in word.lower():
                if j in self.rows[i]:
                    state += 1
            if state == len(word):
                return True
        return False

Solution().findWords(["Hello", "Alaska", "Dad", "Peace"])