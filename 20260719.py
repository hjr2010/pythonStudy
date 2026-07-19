class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    def print_info(self):
        print(f"员工名字:{self.name},工号:{self.id}")
class FullTime(Employee):
    def __init__(self, name, id,monthly_salary):
        super().__init__(name, id)
        self.monthly_salary = monthly_salary
    def calculate_monthly_salary(self):
        self.monthly_salary = self.monthly_salary * 12
        return self.monthly_salary
class PartTime(Employee):
    def __init__(self, name, id,daily_salary,working_days):
        super().__init__(name, id)
        self.daily_salary = daily_salary
        self.working_days = working_days
    def calculate_monthly_salary(self):
        return self.daily_salary * self.working_days
ZS=FullTime("ZS",1,6000)
LS=PartTime("LS",1,2309,345)
ZS.print_info()
LS.print_info()
print(ZS.calculate_monthly_salary())
print(LS.calculate_monthly_salary())
with open ("./poem.txt","w",encoding="utf-8") as f:
    f.write("我欲乘风归去\n")
    f.write("惟恐琼楼玉宇\n")
    f.write("高处不胜寒\n")
    f.write("起舞弄清影\n")
with open ("./poem.txt","a",encoding="utf-8") as f:
    f.write("何似在人间\n")
    f.write("转朱阁低绮户照无眠\n")