'''
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).


Example 1:

Input: x = 2.00000, n = 10
Output: 1024.00000
'''
# Time : O(log2 n)
def calPower(x,n):
    # x^-n = 1 / x ^ n
    def helper(x, n):
        if x == 0: return 0
        if n == 0: return 1

        
        res = helper(x, n // 2)
        res = res * res 
        # handle odd no eg if x = 5 : x^2, x^2 ,(x^1 = x)
        return x * res if n % 2 else res
        

    res = helper(x, abs(n))
    return res if n >= 0 else 1 / res






# def calPower(x, n):
#     return x ** n

x = 2.00000
n = 10
print(calPower(x,n))