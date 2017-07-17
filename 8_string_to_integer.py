class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        val = None
        signs = {'+': 1, '-': -1}
        numbers = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
        if len(str) == 0:
            return None
        elif len(str) == 1:
            if str in signs:
                return None
            else:
                try:
                    return int(str)
                except:
                    return None
        else:
            if str[0] in signs:
                val = signs[str[0]] * int(''.join([x for x in str[1:] if x in numbers]))
                print val
            else:
                val = int(''.join([x for x in str if x in numbers]))
        return val

Solution().myAtoi("1")