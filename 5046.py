num, budget, hotel, week = map(int, input("").split())
pay = budget + 1

for i in range(hotel):
    cost = int(input(""))
    per = map(int, input("").split())
    for j in per:
        if j < num:
            continue
        if cost*num < pay:
            pay = cost*num

if pay != budget + 1:
    print(pay)
else:
    print("stay home")