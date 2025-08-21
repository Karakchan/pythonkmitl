# + → Addition

# - → Subtraction

# * → Multiplication

# / → Division (returns float)   10/2 =5.0 7/2 =3.5

# // → Floor Division (removes decimal) 10//2=5 7//2=3

# % → Modulus (remainder)10/2=0 7/2=1

# ** → Exponent (power) 2**2=4 2**3=8

# c='12'
# d='5'
# print(c+d)
# # print(a*c)


# a=14 
# # b=a/5 #2.8
# # c=int(b)  #2
# # d=a//5 # -2
# # e=a%5  #-4
# # print(a,b,c,d,e)

# a=-a  #-14
# b=a/5 #-2.8
# c=int(b) #-2
# d=a//5
# e=a%5
# print(a,b,c,d,e)

# a=3
# b=5
# # print(a,b)  #3 5
# b=a #b = 3
# a=b # a =3
# print(a,b) #5 3
# # a=10
# # b=2
# # b+=1
# # a-=b #7
# # print(a,b) #7 3

# x=1
# y=x+1 #y = 2
# z=2*Y+1 #z = error
# print(x,y,z)

# x=12
# if x%2=0:
#     print('Even')
# else:
#     print('Odd')

# = is a assigment operator == is a comparison operator 

# x=int(input('Enter an integer: '))
# if x>=10:
#     print('A')
# elif x<=20:
#     print('B')
# if x%2==0:
#     print('C')
# else:
#     print('D')
#     if (x%3==0) and (x>0):
#       print('E')
#     print('F')

# n=9
# for i in range(1,n):
#     print(i) 

# n=5
# x=0
# y=0
# for i in range(0,n+1): # 0 6 = 0 1 2 3 4 5
#     x+=1
#     y+=i
# print(x,y)

# n=5
# i=0
# while n>0: 
#     print(n,i)
#     n-=1
#     i+=1

# n=5
# while True: 
#     print(n)
#     n-=1
#     if n<=0:
#       break

# x=int(input('Enter x: '))
# y=int(input('Enter y: '))
# z=0
# for i in range(0,x):
#     for j in range(0,y):
#         print(z, end='')
#         z=1-z
# print('')

# def fun(x, y):
#     if x>y:
#         z=x-y
#     else:
#          z=y-x
#     return z
# def main():
#     print(fun(4,10))
#     print(fun(10,4))
#     print(fun(5,5))
# main()

# def funfun(x,y):
#     z=x
#     x=y
#     y=z
# a=1
# b=2
# print(a,b)
# funfun(a,b)
# print(a,b)


# x=5
# y=20
# def funfunfun(num):
#     y=num
#     print("A",x,y)
#     y+=1
# print("B",x,y)
# funfunfun(10)
# print("C",x,y)

# def multiprint(s,n):
#     for i in range(0,n):
#         print(s)
# multiprint(4,"Hello")


# def fun_range(a,b=None,c=None):
#     if b==0 or a == 0:
#         return max(a,b,c)
#     if c ==None:
#         if a > b:
#             return a -b
#         else:
#             return b - a

#     if b== None and c== None:
#         return 0

# # print(fun_range(8,1))

# def rec(i):
#     if i>0:
#         print('#'*i)
#         rec(i-1)
#         print('#'*i)
# rec(5)

# p = 1
# while True:
#     x = int(input())
#     if x==0:
#         break
#     if x<0:
#         continue
# p *= x
# print(p)

# input = input("Enter a string :")
# input_len = len(input)

# if input_len %2 == 0:
#     print("Even length")
# else:
#     print("Odd length")


# x = int(input("Enter an integer:"))
# if x < 0:
#     print("Please enter a positive integer.")
# else:
#     print(x*x)

# n = int(input())
# i = 0
# n -= 1
# while i < n:
#     i += 1
#     print(i)

# for i in range(0,100):
#     print(i, end='')

# for k in range(0,11):
#     print(2*k+1)

# def down(n):
#     if n >= 0:
#         print(n, end='\n')
#         down(n-1)

# down(4)

# def multiprint(n,s):
#     for i in range(0,n):
#         print(s)

# # multiprint(10,"Hello")
# item = 1
# sum = 0
# while item != 0:
#     sum += item
#     item -= 0.1
# print(item)

# s = input()
# t = input()
# if s <t or s>t:
#     print(True)
# else:
#     print(False)

# def increment():
#     global x
#     x += 1

# x = int(input())
# increment()
# print(x)

# 