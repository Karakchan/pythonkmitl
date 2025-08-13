
# max_so_far = None
# while True:
#     n = input()
#     if n=="$":
#         break
#     n = int(n)
#     if (max_so_far is None) or (n >max_so_far):
#         max_so_far= n

# print("The maxium number is ",max_so_far)


# course = ["Myanmar","English","Mathematics","Chem","Physics"]

# course.append("art")
# course_2 = ["Financial Managament"]
# course.insert(0,course_2)  # list.insert(index, element)
# course_3 = ["Business computing and vasualization"]
# course.extend(course_3)  # list.extend(iterable)

# course.remove("Chem")
# popped = course.pop()

# course.reverse()
# course.sort()

# print(popped)
# print(course)
# print(course[4])
# print(course[0:2])
# print(course[:2])
# print(course[2:])


nums = [1,2,3,4,5]

# nums.sort(reverse=True)

# print(nums)
# print(min(nums))
# print(sum(nums))

# print(course.index("Mathematics"))  # 2 

# ----------------------------------------------------

# => enumerate

# for index, course in enumerate(course, start=1):
#     print(index, course)

# ----------------------------------------------------


# course_str =", ".join(course)
# new_list = course_str.split(" - ")

# # print(course_str)
# # print(type(course_str)) # str
# print(new_list)

# ----------------------------------------------------


# list_1 = ["Myanmar","English","Mathematics","Chem","Physics"]
# list_2 = list_1

# print(list_1)
# print(list_2)

# list_1[0] = "art"


# print(list_1)
# print(list_2)  

# ----------------------------------------------------


# tuple_1 = ("Myanmar","English","Mathematics","Chem","Physics")
# tuple_2 = tuple_1

# print(tuple_1)
# print(tuple_2)

# tuple_1[0] = "Art" // can't do that error only on list 

# print(tuple_1) // error
# print(tuple_2) //error


# ----------------------------------------------------

# cs_course = {"Myanmar","English","Mathematics","Chem","Physics"}
# art_course = {"Myanmar","English","Desgin","Art","Architecture"}

# print(cs_course.union(art_course))
# print(cs_course.difference(art_course))
# print(cs_course.intersection(art_course))

# empty lsits
empty_list = []
empty_list = list()

print(empty_list)

# empty tuple
empty_tuple = ()
empty_tuple = tuple()


# empty sets
empty_set = {}
empty_set = set()


print(empty_list)
print(empty_tuple)
print(empty_set)