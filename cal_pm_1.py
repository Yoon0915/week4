def cal_plus():
    int_1 = int(input("첫 번째 숫자를 입력하시오: "))
    int_2 = int(input("두 번째 숫자를 입력하시오: "))
    result = int_1 + int_2
    print(f"{int_1} + {int_2} = {result}")


def cal_minus():
    int_1 = int(input("첫 번째 숫자를 입력하시오: "))
    int_2 = int(input("두 번째 숫자를 입력하시오: "))
    result = int_1 - int_2
    print(f"{int_1} - {int_2} = {result}")

def cal_mul():
    int_1 = int(input("첫 번째 숫자를 입력하시오: "))
    int_2 = int(input("두 번째 숫자를 입력하시오: "))
    result = int_1 * int_2
    print(f"{int_1} x {int_2} = {result}")

def cal_div():
    int_1 = int(input("첫 번째 숫자를 입력하시오: "))
    int_2 = int(input("두 번째 숫자를 입력하시오: "))
    result = int_1 / int_2
    print(f"{int_1} / {int_2} = {result}")


def cal_mod():
    int_1 = int(input("첫 번째 숫자를 입력하시오: "))
    int_2 = int(input("두 번째 숫자를 입력하시오: "))
    result = int_1 % int_2
    print(f"{int_1} % {int_2} = {result}")


def calculator():
    while True:
        print("덧셈(+), 뺄셈(-), 곱셉(*), 나눗셈(/), 나머지(%) 중 수행할 연산 기호을 입력하세요(종료를 원하면 q 입력)")
        symbols = input("연산 기호(+,-,*,/,&)를 입력하세요: ")

        if symbols == '+':
            cal_plus()
        elif symbols == '-':
            cal_minus()
        elif symbols == '*':
            cal_mul()
        elif symbols == '/':
            cal_div()           
        elif symbols == '%':
            cal_div()                 
        elif symbols == 'q':
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 연산기호를 입력하였습니다.")

calculator()