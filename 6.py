a = int(input())
c = ' '.join(''.join(x for x in input()) for i in range(a))
print(len(set(c.split())),sep='',end='')