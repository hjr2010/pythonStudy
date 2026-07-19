#9.
#公鸡：x只  母鸡：y只  小鸡：z只  x最大值为20，y最大值为33
for x in range(0,21):
    for y in range(0,34):
        z=100-x-y
        if z>=0 and z%3 == 0 and 5*x+3*y+z/3==100:
            print(f"公鸡{x}只，母鸡{y}只,小鸡{z}只")
#10.
number=int(input("type a number"))
total=sum(int(i) for i in str(abs(number)))
if total%2==0:
    print(number)
if total%2!=0:
    reverse_number=str(number)[::-1]
    print(reverse_number)
#12.
class A:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def sum(self):
        return self.a+self.b
#13
sum_even=0
for i in range(0,101):
    if i % 2 == 0:
        sum_even+=i
print(sum_even)
#15
def f(x):
    if x <0 :
        return 0
    elif 0<=x<5:
        return x
    elif 5<=x<10:
        return 3*x-5
    elif 10<=x<20:
        return 0.5*x-2
    else:
        return 0
#18
import random
nums = [random.randint(0, 99) for _ in range(20)]
print(nums)
for i in range(len(nums)-1, -1, -1):
    if nums[i] % 2 != 0:
        del nums[i]
print(nums)
