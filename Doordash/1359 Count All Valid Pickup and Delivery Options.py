class Solution(object):
    def countOrders(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Di is always after Pi
        # The number of combination is ((2n)!/ 2^n)
        res = 1
        mod = 10 ** 9 + 7
        for i in range(2, n + 1):
            res = res * (2 * i) * (2 * i - 1) / 2 % mod
        return res
