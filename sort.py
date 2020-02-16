def BubbleSort(lst):
    length = len(lst)
    counter = 0
    lastExchangeIndex = 0
    sortBorder = length - 1
    for i in range(length):
        isSorted = True
        for j in range(sortBorder):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                isSorted = False
                lastExchangeIndex = j
        sortBorder = lastExchangeIndex
        if isSorted:
             break
        counter += 1

    return counter

def QuickSort(lst):
    if len(lst) <= 1:
        return lst
    pivot = lst[len(lst) // 2]
    print(pivot)
    left = [x for x in lst if x < pivot]
    print(left)
    middle = [x for x in lst if x == pivot]
    print(middle)
    right = [x for x in lst if x > pivot]
    print(right)

    return QuickSort(left) + middle + QuickSort(right)

if __name__ == '__main__':
    # lst = [64, 34, 25, 12, 22, 11, 90]
    # lst = [5,8,6,3,9,2,1,7]
    # lst = [3,4,2,1,5,6,7,8]
    lst = [2,3,4,5,6,7,1,8]


    print("Before sort: ")
    for i in lst:
        print(i, end = ' ')

    print("\nAfter sort: ")
    for i in QuickSort(lst):
        print(i, end = ' ')
