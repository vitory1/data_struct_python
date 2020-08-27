def shellSort(alist):
    sublistcount = len(alist) // 2
    while sublistcount > 0:
        for startposition in range(sublistcount):
            gapInsertionSort(alist, startposition, sublistcount)
        print("After increments of size", sublistcount, "The list is", alist)
        sublistcount = sublistcount // 2


def gapInsertionSort(alist, start, gap):
    for fillsolt in range(start+gap, len(alist), gap):
        currentValue = alist[fillsolt]
        position = fillsolt
        while position > 0 and alist[position-gap] > currentValue:
            alist[position] = alist[position-gap]
            position = position - gap
        alist[position] = currentValue


if __name__ == "__main__":
    alist = [54, 26, 93, 17, 88, 31, 66, 55, 20]
    shellSort(alist)
    print(alist)
