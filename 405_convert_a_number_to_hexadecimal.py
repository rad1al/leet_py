class Solution(object):
    hex_dict = {'0110': '6', '0111': '7', '0000': '0', '0001': '1', '0011': '3', '0010': '2', '0101': '5', '0100': '4', '1111': 'f', '1110': 'e', '1100': 'c', '1101': 'd', '1010': 'a', '1011': 'b', '1001': '9', '1000': '8'}
    
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "0"
        if num < 0:
            bin_str = '{0:032b}'.format(2**32+num)
        else:
            bin_str = '{0:032b}'.format(num)
        sub_strs = [bin_str[i*4:(i+1)*4] for i in xrange((len(bin_str)/4))]
        chars = map(lambda x: self.hex_dict[x], sub_strs)
        return (''.join(chars)).lstrip('0')
        # zero = True
        # i = 0
        # while i < len(chars):
        #     if chars[i] != '0':
        #         return ''.join(chars[i:])
        #     else:
        #         i += 1
            
            