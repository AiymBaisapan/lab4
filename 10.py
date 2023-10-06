n, k = [int(i) for i in input().split()]
a = set()
mass = [[int(i) for i in input().split()] for j in range(k)]
for i in range(k):
    day = mass[i][0]
    start = mass[i][0]
    step = mass[i][1]
    while day <= n:
        if day % 7 != 0 and day % 7 != 6:
            a.add(day)
        day += step
print(len(a))
