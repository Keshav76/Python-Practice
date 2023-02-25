def sort(list):
    for i in range(len(list) - 1, 0, -1):           #to iterate through list for 'one number fixation'
        for j in range(i):                          #to swap consecutive values and make biggest value at the end
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
    return list


list = [int(i) for i in input("Enter a list : ").split()]
list = sort(list)
print("Sorted List : ", end ='')
print(list)