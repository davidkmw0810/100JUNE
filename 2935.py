a = len(input(""))
oper = input("")
b = len(input(""))

if oper == "*":
    print("1", end="")
    for i in range(a+b-2): print("0", end="")
else:
    if a == b:
        print("2", end="")
        for i in range(a-1): print("0", end="")
    else:
        print("1", end="")
        for i in range(max(a, b)-1):
            if i == abs(a-b)-1:
                print("1", end="")
            else:
                print("0", end="")
