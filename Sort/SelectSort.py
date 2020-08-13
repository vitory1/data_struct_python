def selectSort(alist):
    for fillslot in range(len(alist)-1, 0, -1):
        positionOfMax = 0
        for location in range(1, fillslot+1):
            if alist[location] > alist[positionOfMax]:
                positionOfMax = location

        alist[positionOfMax], alist[fillslot] = alist[fillslot], alist[positionOfMax]


if __name__ == "__main__":
    alist = [54, 26, 93, 17, 88, 31, 66, 55, 20]
    selectSort(alist)
    print(alist)
