n, m =[int(i) for i in input().split()]
kub_anna = set(int(input()) for _ in range(n))
kub_borya = set(int(input()) for _ in range(m))
for i in (kub_anna & kub_borya,kub_anna - kub_borya,kub_borya - kub_anna):
    print(len(i))
    print(*(sorted(i)))