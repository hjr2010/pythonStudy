'''
def get_username_from_email(email: str) -> str:
    username = email.split("@")[0]
    return username

print(get_username_from_email(str(input("Enter your email: "))))
h = int(input())
n = int(input())
total = 3 * h - h / (2 ** (n - 1))
print(int(total))
'''
import pandas as pd
df = pd.read_excel(r"C:\Users\Hjr\OneDrive\Desktop\文件.xlsx")
print(df)
print(type(df))
print(df.dtypes)
ages=df["age"].values
print(ages)
sex_age=df[["sex","age"]]

import os

excel_file = "用户信息表.xlsx"

def add_user_info():
    name = input("请输入姓名：")
    age = input("请输入年龄：")
    address = input("请输入地址：")

    data = {
        "姓名": [name],
        "年龄": [age],
        "地址": [address]
    }
    df_new = pd.DataFrame(data)

    if os.path.exists(excel_file):
        df_old = pd.read_excel(excel_file)
        df_total = pd.concat([df_old, df_new], ignore_index=True)
    else:
        df_total = df_new

    # 写入Excel，index=False 不保存行号
    df_total.to_excel(excel_file, index=False)
    print("信息保存成功！\n")


if __name__ == "__main__":
    while True:
        print("========信息录入系统========")
        add_user_info()
        cont = input("是否继续录入(y继续 / 其他按键退出)：")
        if cont.lower() != "y":
            print("程序结束")
            break
class PersonInfo:
    def __init__(self,name,age,sex,phonenumber):
        self.name = name
        self.age = age
        self.sex=sex
        self.phonenumber=phonenumber
    def show_info(self):
        print(self.name)
        print(self.age)
        print(self.phonenumber)
        print(self.sex)

dataList = []

# 3. 遍历excel每一行，实例化对象存入dataList
for index, row in df.iterrows():
    # 根据每行数据创建PersonInfo实例
    person = PersonInfo(
        name=row["name"],
        age=row["age"],
        sex=row["sex"],
        phonenumber=row["phonenumber"]
    )
    dataList.append(person)
    # 4. 遍历dataList，逐个调用showInfo打印信息
    for p in dataList:
        p.show_info()