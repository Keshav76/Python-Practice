def sort(list):
    for i in range(0, len(list) - 1):
        min = i
        for j in range(i,len(list)):
            if list[min] > list[j]:
                min = j
        list[i], list[min] = list[min], list[i]

    return list


list = [int(i) for i in input("Enter a list: ").split()]
list = sort(list)
print("Sorted List: {}".format(list))