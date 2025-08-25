# The function digit(n), where n is a single decimal digit (0-9) is 
# supposed to return the string of the English word (in lower case) 
# for the given digit. For example, digit(5) should return the string "five". 
# If n is not a single decimal digit, the function should return the Python special value None.

# Q 1
# num_word = ["zero","one","two","three","four","five","six","seven","eight","nine","ten"]

# def digit(n):
#     if 0 <= n < len(num_word):  
#         return num_word[n]
#     return None

# print(digit(9))



# ---------------------------------------------------

# Q2

# one_num = ["zero","one","two","three","four","five","six","seven","eight","nine","ten"]
# teen_num = ["ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
# ten_num = ["","","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]

# def digit2(n):
#     if not (0 <=n < 100):
#         return None
#     if 0 <= n < 10:
#         return one_num[n]
#     elif 10 <= n < 19:
#         return teen_num[n-10]
#     elif n % 10 == 0:
#         return ten_num[n//10]
#     else:
#         return ten_num[n//10] + "_" + one_num[n%10]
    
#     if not 0 <= n < 100:
#         return None 

# print(digit2(100))

# --------------------------------------------------- 

# def digit(n):
#     words = ["zero","one","two","three","four",
#              "five","six","seven","eight","nine"]
    
#     for i in range(len(words)):
#         if n == i:         
#             return words[i]
#     return None   

# print(digit(10))

# def mean (a, b=None,c=None):
#     if b == None:
#         return a
#     if c == None:
#         return (a + b) / 2
#     return (a + b + c) / 3

# print(mean(20))

# def median(a,b=None,c=None):
#     if b == None:
#         return a
#     if c == None:
#         return (a + b) / 2
    
#     return (a + b + c) / 3

# print(median(20,60,10))


# one_num = ["zero","one","two","three","four","five","six","seven","eight","nine","ten"]
# teen_num = ["ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
# ten_num = ["","","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]


# # def digit2(n):
# #     if not (0 <=n < 100):
# #         return None
# #     if 0 <= n < 10:
# #         return one_num[n]
# #     elif 10 <= n < 19:
# #         return teen_num[n-10]
# #     elif n % 10 == 0:
# #         return ten_num[n//10]
# #     else:
# #         return ten_num[n//10] + "-" + one_num[n%10]



# def digit3(n):
#     if not (0 <= n < 1000):
#         return None
    
#     # case 0–99 → just reuse digit2
#     if n < 100:
#         return digit2(n)
    
#     # case 100–999
#     hundreds = n // 100
#     remainder = n % 100
    
#     if remainder == 0:   # exact hundred
#         return  digit3(hundreds) + " hundred"
#     else:                # hundred + "and" + remainder
#         return digit3(hundreds) + " hundred and " + digit2(remainder)

# print(digit3(999))





# def median(a,b=None,c=None):
#     if b == None:
#         return a
#     if c == None:
#         return (a + b) // 2

#     return a + b + c - min(a, b, c) - max(a, b, c)

# print(median(20,60))

# def compound(a, r, n=1):
#     return round(a * (1 + r/100) ** n, 3)

# print(compound(100,10,0))
# print(compound(100,10))
# print(compound(100,10,2))
# print(compound(100,10,3))
# print(compound(100,10,4))
# print(compound(100,10,5))


# import math
# from scipy.stats import norm

# x = 0.5
# def cdf(x):
#   return float(norm.cdf(x))

# y = math.exp(x)
# y = math.log(x)
# y = x**0.5

# def call_price(S0, K, r, T, sigma):


def starshapeA(n):
    if n < len(starshapeA):
        n = ("*" * n)

starshapeA(3)