li = [0] * 100001

n, target = input("").split()
n = int(n)
target = int(target)

num = sorted(map(int, input("").split()))

max = 0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            sum = num[i] + num[j] + num[k]
            if sum > target:
                continue
            elif target - max > target - sum:
                max = sum

print(max)