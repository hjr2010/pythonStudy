import openpyxl as pyxl
import os

class PersonInfo:
    def __init__(self, name, age,gender,address):
        self.name = name
        self.age = age
        self.gender = gender
        self.address = address


class DataTool:
     def __init__(self):
            self.txt_tool = TxtDataTool()
            self.xls_tool = XlsDataTool()

     def add(self,person:PersonInfo,kind:str):
        if kind == "txt":
            self.txt_tool.add(person,'txt')
        else:
            self.xls_tool.add(person,'xls')

class XlsDataTool:
    def __init__(self, filename="person_data.xlsx"):
        self.filename = filename

    def add(self,person: PersonInfo, kind:str):
        if os.path.exists(self.filename):
            wb = pyxl.load_workbook(self.filename)
            sheet = wb.active
            # 填入一行单元格内容，列表依次对应A、B、C、D……列
            row_data = [person.name, person.age, person.gender, person.address]
            sheet.append(row_data)
            wb.save("person_data.xlsx")
            wb.close()






class TxtDataTool:
    def __init__(self, filename="person_data.txt"):
        self.filename = filename

    def add(self,person: PersonInfo, kind:str):
        with open(self.filename, "a", encoding="utf-8") as f:
            f.write(person.name+"!"+" "+person.gender+" "+person.age+" "+person.address + "\n")

name=input("type your name")
gender=input("type your gender")
age=input("type your age")
address=input("type your address")
info = PersonInfo(name, age, gender, address)
tool = DataTool()

select = input("请选择保存格式(1-txt  2-xls)：")
if select == "1":
    tool.add(info, "txt")
else:
    tool.add(info, "xls")