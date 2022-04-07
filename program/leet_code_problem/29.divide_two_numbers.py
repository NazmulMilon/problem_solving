class Solution(object):
    # int dividend, divisor, result
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        self.dividend = dividend
        self.divisor = divisor

    def result_view(self):
        dividend = int(input("Enter Dividend: "))
        divisor = int(input("Enter divisor: "))
        result = dividend / divisor
        print(int(result))


obj = Solution()
# result = obj.divide(dividend, divisor)
obj.result_view()
print()

'''
class Test:

    def findsum(self, a, b):
        s = a + b
        return s


a = int(input("Enter first number:"))
b = int(input("Enter second number:"))

obj = Test()
s = obj.findsum(a, b)

print("Sum is:", s)
'''