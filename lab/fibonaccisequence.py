# # Fibonacci Squence 
# # 0 1 1 2 3 5 8 13 21 


# def fibonacci(n):
#     if n==1 :
#         return 0
#     elif n ==2 :
#         return 1
#     return fibonacci(n-1)+fibonacci(n-2)

# # for i in range(1,10):
# #     print(fibonacci(i))
# print(fibonacci(10))


# -------------------------------------------------

# terms = int(input("Enter the number of terms : "))

# n1, n2 = 0, 1

# if terms <= 0:
#     print("Enter the positive integer.")
# elif terms == 1:
#     print(f'Fibonacci Sequence {n1}')
# else:
#     for term in range(terms):
#         print(n1, end=' ')
#         n = n1 + n2 
#         n1 = n2 
#         n2 = n
