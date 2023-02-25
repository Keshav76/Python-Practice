n,k = input().split()
n , k , count = int(n), int(k), 0
q = [int(i) for i in input().split()]
a = []
for i in range(k):
    x = [int(j) for j in input().split()]
    a.append(x)
b = a.copy()
a.clear()
for i in range(len(a)):
    if a[i][0] != q[0] and a[i][1] != q[1] and abs(a[i][0] - q[0]) != abs(a[i][1] - q[1]) :
        b[i] = [0, 0]
for i in b:
    if i == [0,0]:
        pass
    else:
        a.append(i)
for i in range(q[0] - 1, 0, -1):
    if [i, q[1]] in a:
        break
    count += 1
for i in range(q[0] + 1, n + 1, 1):
    if [i, q[1]] in a:
        break
    count += 1
for i in range(q[1] - 1, 0, -1):
    if [q[0], i] in a:
        break
    count += 1
for i in range(q[1] + 1, n + 1, 1):
    if [q[0], i] in a:
        break
    count += 1
j = q[1] - 1
for i in range(q[0] - 1, 0, -1):
    if j == 0:
        break
    if [i, j] in a:
        break
    j -= 1
    count += 1
j = q[1] - 1
for i in range(q[0] + 1, n + 1, 1):
    if j == 0:
        break
    if [i, j] in a:
        break
    j -= 1
    count += 1
j = q[1] + 1
for i in range(q[0] - 1, 0, -1):
    if j == n + 1:
        break
    if [i, j] in a:
        break
    j += 1
    count += 1
j = q[1] + 1
for i in range(q[0] + 1, n + 1, 1):
    if j == n + 1:
        break
    if [i, j] in a:
        break
    j += 1
    count += 1
print(count)