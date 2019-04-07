n = int(input(""))
spec = [0 for _ in range(8)]
for _ in range(n):
    spec = list(map(int, input().split(" ")))
    for i in range(4):
        spec[i] = spec[i] + spec[i+4]
    if spec[0] < 1: spec[0] = 1
    if spec[1] < 1: spec[1] = 1
    if spec[2] < 0: spec[2] = 0
    total = 1*spec[0] + 5*spec[1] + 2*spec[2] + 2*spec[3]
    print(total)
