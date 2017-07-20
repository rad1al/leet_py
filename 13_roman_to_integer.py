class Solution(object):
    roman_dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        	# I	V	X	L	C	D	M
            # 1	5	10	50	100	500	1,000
        # roman_dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        nums = map(lambda x : self.roman_dict[x], s)
        # [1000, 100, 1000, 50, 1, 5]
        result = 0
        i = 0
        while i < len(nums)-1:
            if nums[i] < nums[i+1]:
                result -= nums[i]
            else:
                result += nums[i]
            i += 1       
        return result + nums[-1]

    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Faster implementation.
        result = 0
        i = 0
        while i < len(s)-1:
            if  self.roman_dict[s[i]] <  self.roman_dict[s[i+1]]:
                result -=  self.roman_dict[s[i]]
            else:
                result +=  self.roman_dict[s[i]]
            i += 1       
        return result + self.roman_dict[s[-1]]