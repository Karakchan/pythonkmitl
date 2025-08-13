student = {'name':"Mark","major":"Finanical Engineering","age":18,'courses':['math','economics']}

# print(student['name']) 
# print(student['phont'])  #key error
# print(student.get('phone')) #None

# student['phone'] = '095-034-2202'

# print(student['phone'])

# student.update({'name':'Mark Maramee','age':21,'phone':'555-5555'})

# print(student) #update what you change

# del student['age']
# print(student)

# age = student.pop('age')

# print(len(student)) #3
# print(student.values())
# print(student.items())
# print(student.keys())

# for key in student:
#     printi(key)

for key in student.items():
    print(key) # a pair of item


for key , value in student.items():
    print(key, value)  # sperate them