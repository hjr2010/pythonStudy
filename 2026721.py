input_str = input("请输入一个包含若干自然数的列表：")
num_list = eval(input_str)
max_num = max(num_list)
print(max_num)
new_list = [len(str(num)) for num in num_list]
print(new_list)
import random

def create_verify_code(length: int) -> str:
    chars = "23456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghjkmnpqrstuvwxyz"
    code = random.sample(chars, length)
    return "".join(code)

print(create_verify_code(4))

# 获取输入
score = float(input("请输入成绩："))
if 0 <= score <= 100:
    if score < 60:
        grade = "不合格"
    elif score < 70:
        grade = "合格"
    elif score < 90:
        grade = "良好"
    else:
        grade = "优秀"
    print(grade)
def bubble_sort(arr):
    n = len(arr)
    # 外层控制排序轮次
    for i in range(n):
        # 内层比较，每轮减少i次（末尾i个已有序）
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # 交换元素
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr