def Search_by_while(lst, n):
    i = 0
    while i < len(lst):
        if lst[i] == n:
            globals()['pos'] = i
            return True
        i += 1
    else :
        return False

def Search_by_for(lst,n):
    for i in range(len(lst)):
        if lst[i] == n:
            globals()['pos'] = i
            return True
    else:
        return False

pos = -1
lis = [1,2,3,8,4,7,5]
num = 4
if Search_by_for(lis, num):
    print(" Found at : ", pos + 1)
else:
    print(" Not Found ")