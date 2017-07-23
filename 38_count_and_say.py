class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return "1"
        else:
            s = '1'
            for i in xrange(n-1):
                s = self.grow(s)
            return s
        
    def get_score(self, s):
        n = s[0]
        count = 1
        lst = list()
        for i in xrange(1,len(s)):
            if s[i] != n:
                lst.append((n, count))
                n = s[i]
                count = 1
            else:
                count += 1
            # if i == len(s)-1:
                # lst.append((n, count))
        lst.append((n, count))
        return lst
    
    def grow(self, s):
	    score = self.get_score(s)
	    next_s = ''.join(['{1}{0}'.format(*t) for t in score])
	    return next_s