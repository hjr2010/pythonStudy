import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(0,2*np.pi,1000)
y=np.cos(x)
plt.plot(x, y, color='blue', label='y = cos(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Cosine Function y = cos(x)')
plt.legend()
plt.show()
x=np.linspace(0,500,500)
y=x**2 + 2*x - 3
plt.plot(x, y, color='blue', label='y = x**2+2*x-3')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

 '''class Employee:
            def __init__(self, name, id):
                self.name = name
                self.id = id

            def print_info(self):
                print(f"员工名字:{self.name},工号:{self.id}")

        class FullTime(Employee):
            def __init__(self, name, id, monthly_salary):
                super().__init__(name, id)
                self.monthly_salary = monthly_salary

            def calculate_monthly_salary(self):
                self.monthly_salary = self.monthly_salary * 12
                return self.monthly_salary

        class PartTime(Employee):
            def __init__(self, name, id, daily_salary, working_days):
                super().__init__(name, id)
                self.daily_salary = daily_salary
                self.working_days = working_days

            def calculate_monthly_salary(self):
                return self.daily_salary * self.working_days

        ZS = FullTime("ZS", 1, 6000)
        LS = PartTime("LS", 1, 2309, 345)
        ZS.print_info()
        LS.print_info()
        print(ZS.calculate_monthly_salary())
        print(LS.calculate_monthly_salary())'''