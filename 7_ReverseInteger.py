class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        ## Attempt 1
        # str_x = str(x)
        # is_neg = (str_x[0] == '-')
        # res = int(str_x[::-1]) if not is_neg else int('-' + str_x[::-1][:-1])
        # if res.bit_length() > 31:
        #     res = 0
        # return res 
        ## Attempt 2
        sign = -1 if x < 0 else 1
        res = int(str(abs(x))[::-1]) * sign
        return res if -(2**31) <= res <= (2**31 - 1) else 0