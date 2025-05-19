import math

def calculate(x, y):
    result = x + y
    if x > 0 and y > 0:
        return "正数相加"
    elif x < 0 and y < 0:
        return "负数相减"
    else:
        return f" {x} 和 {y} 相乘"

while True:
    try:
        num1 = float(input("请输入第一个数字: "))
        num2 = float(input("请输入第二个数字: "))
        print(calculate(num1, num2))
        break
    except ValueError:
        print("输入的不是有效的数字，请重新输入。")
