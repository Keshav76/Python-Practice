def BinarySearch(list,n):
    l = 0
    u = len(list) - 1
    while(l <= u):
        mid = (l + u) // 2
        if list[mid] == n:
            globals()['pos'] = mid
            return True
        elif list[mid] > n:
            u = mid - 1
        else:
            l = mid + 1
    else:
        return False


pos = -1
a = [12,34,54,65,72,83,96,102,106,784,987,1025,4510,7888,10154]
n = int(input("Enter a number: "))
if BinarySearch(a,n):
    print("Found at position : {}".format(pos + 1))
else:
    print("Not Found ")