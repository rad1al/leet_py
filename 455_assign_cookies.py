class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        result = 0
        s_ = sorted(s)
        g_ = sorted(g)
        while True:
            try:
                if g_[0] <= s_[0]:
                    g_.pop(0)
                    s_.pop(0)
                    result += 1
                else:
                    s_.pop(0)
            except:
                break
        return result
        
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        result = 0
        s_ = sorted(s)
        g_ = sorted(g)
        i = 0
        j = 0
        while True:
            try:
                if g_[i] <= s_[j]:
                    i += 1
                    j += 1
                    result += 1
                else:
                    j += 1
            except:
                break
        return result
                
                        


Solution().findContentChildren([1,2,3], [1,1])