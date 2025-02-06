# Calculator function
# Clean the function
# Write tests
# Implement substraction and multiplication
# for multiplication allow operators to be x,X or *

def calc(num1: int, num2: int, op:str) -> int|str:
    r = ""
    try:
        if op == "+":
            res = num1+num2
        if op == "/":
            if num2 == 0:
                return "ZeroDivision not possible"
            res = num1/num2
        if op in "xX*":
            res = "Operation not allowed"
    except Exception as e:
        return f'**** ERROR:{e}'
    

def log_this(to_log:str) -> None:
    with open("log.txt", "_a") as file_pointer:
        file_pointer.write(to_log)
    # print(res)
    # f = open("log.txt", "+a")
    # log_txt = f"6+2={res}\n"
    # f.write(log_txt)
    # return res

print(f"6+2={calc(6, 2, "+")}")
print(f"6/2={calc(6, 2, "/")}")
# print(f"6+2={calc('6', 2, "+")}")
# print(f"6-2={calc(6, 2, "-")}")
# print(f"6*2={calc(6, 2, "x")}")
# print(f"6*2={calc(6, 2, "d")}")