from itertools import combinations

a = [i for i in input("Enter : ").split()]
b = int(a[1])
a = a[0]
lst = [[0]] * b
for i in range(b-1, -1, -1):
    lst[i] = list(combinations(a, i+1))
for j in range(len(lst)):
    for i in range(len(lst[j])):
        list(lst[j][i]).sort
        lst[j][i] = ''.join(lst[j][i])
    lst[j].sort()
s = []
for i in range(len(lst)):
    s = s + lst[i]
for i in s:
    print(i)
