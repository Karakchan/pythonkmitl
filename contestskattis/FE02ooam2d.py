# B

# v, a, t = map(int, input().split())
# s = v * t + 0.5 * a * t * t
# print(f"{round(s, 9):.9f}")


# ------------------------------------------------------

# D

# a, m = map(int, input().split())
# b = 2 * m - a
# print(b)

# ------------------------------------------------------


# G

# x1, y1 = map(int, input().split())
# x2, y2 = map(int, input().split())
# x3, y3 = map(int, input().split())

# Find x that appears once

# if x1 == x2:
#     x4 = x3
# elif x1 == x3:
#     x4 = x2
# else:
#     x4 = x1

# # Find y that appears once
# if y1 == y2:
#     y4 = y3
# elif y1 == y3:
#     y4 = y2
# else:
#     y4 = y1

# print(x4, y4)

# ------------------------------------------------------


#Stuck In A Time Loop (H)

# n = int(input())

# for i in range(1,n + 1):
#     print(i,"Abracadabra")

# ------------------------------------------------------

# I
# name = str(input())
# n = int(input())
# for i in range(1,n+1):
#     print("Hipp hipp hurra,",name +"!")

# ------------------------------------------------------


# n = int(input(""))

# names = []
# for _ in range(n):
#     name = input()
#     names.append(name)

# for name in names:
#     print("Takk", name)

# ------------------------------------------------------


# K

# n = int(input())
# total_blazes = 0

# for _ in range(n):
#     blazes = int(input())
#     total_blazes += blazes

# print(total_blazes)

# ------------------------------------------------------
# M

# n= int(input())
# total = 0

# for _ in range(n):
#     result = int(input())
#     total += result

# reduce = n - 1 
# final = total - reduce

# print(final)

# ------------------------------------------------------

# N
# n = int(input())
# names = [input() for _ in range(n)]

# for i in range(0, n, 2):
#     print(names[i])


# ------------------------------------------------------

