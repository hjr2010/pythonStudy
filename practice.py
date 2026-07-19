# name="老林"
# year="虎"
# message_content=(f"'新春佳节，祝{name}{year}年大吉，万事顺意！"
# "'")
# print(message_content)
gpa_dict = {"A": 3.65432, "B": 7.763, "C": 9.87654}
for name, gpa in gpa_dict.items():
    print(f"{name} {gpa:.2f}")


class CuteCat:
    def __init__(self, cat_name, cat_type):
        self.cat_name = cat_name
        self.cat_type = cat_type

    def action(self):

        print("睡觉")

cat1 = CuteCat("Ginger", "麻猫")
print(f"小猫{cat1.cat_name}是{cat1.cat_type}")
cat1 = CuteCat("Ginger", "麻猫")

cat1.action()
#类
