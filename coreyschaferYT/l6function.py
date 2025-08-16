# def hello_fun():
#     print("Hello function!")

# print(hello_fun) # <function hello_fun at 0x773f7fb20d60> nothing ()
# hello_fun()  # we just change in the above of the function 
  
# def hello_fun():
#     return "Hello function!"

# hello_fun()  # blank box no output
# print(hello_fun())  # output
# print(hello_fun().upper())  # output HELLO FUNCTION

# def hello_fun(greeting, name= "Costumer"):
#     return "{} , {}".format(greeting,name)

# print(hello_fun("Hi","Xtun Lynn"))

# def stu_info(*arg,**kwargs):
#     print(arg)
#     print(kwargs)

# stu_info('Math',name = "june",age = 20)  # arg is matn (string) # kwargs is name = june age = 20 (keyvalue)

# def stu_info(*arg,**kwargs):
#     print(arg)
#     print(kwargs)

# course = ["Math","Financial"]
# info = {"name":"min kyaw moe oo","age":21}

# stu_info(*course,**info)

month_day = [0,31,28,31,30,31,30,31,31,30,31,30,31]

def is_leap(year):
    return year % 4 == 0 and (year % 100 !=0 or year % 400 == 0)

def day_in_month(year,month):

    if not 0 <= month <= 13:
        return 'Invaild month'
    
    if month == 2 and is_leap(year):
        return 29
    
    return month_day[month]    

# print(is_leap(2020))
print(day_in_month(2020,12))