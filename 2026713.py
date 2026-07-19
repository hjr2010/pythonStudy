#user_age=int(input("type your age:"))
#BMI=weight/(height ** 2)
#user_weight=float(input("type your weight: (kg)"))
#user_height=float(input("type your height: (m)"))
from unittest import result

from unicodedata import category
print("hello")
try:
    total=0
    count=0
    user_input=input("type a number and type q to quit")
    while user_input != "q":
        num =float(user_input)
        total+=num
        count+=1
        user_input=input("type a number and type q to quit")
    if count==0:
        result=0
    else:
        result=total/count
        print("the result is"+str(result))
except ValueError:
    print("please input a number")