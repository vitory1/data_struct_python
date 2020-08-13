def BubbleSort(alist):
    for passnum in range(len(alist)-1, 0, -1):
        for pos in range(passnum):
            if alist[pos] > alist[pos+1]:
                alist[pos], alist[pos+1] = alist[pos+1], alist[pos]
                # temp = alist[pos+1]
                # alist[pos+1] = alist[pos]
                # alist[pos] = temp


if __name__ == "__main__":
    alist = [54, 26, 93, 17, 88, 31, 66, 55, 20]
    BubbleSort(alist)
    print(alist)
