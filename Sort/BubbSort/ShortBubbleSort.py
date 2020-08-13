# BubbleSort 性能改进： 设置一个交换项，当某一次不发生就换的时候，代表数列已经排序成功了，直接返回
def BubbleSort(alist):
    exchanges = True
    passnum = len(alist)-1
    while passnum > 1 and exchanges:
        exchanges = False
        for pos in range(passnum):
            if alist[pos] > alist[pos+1]:
                exchanges = True
                alist[pos], alist[pos+1] = alist[pos+1], alist[pos]
        passnum = passnum - 1


if __name__ == "__main__":
    alist = [54, 26, 93, 17, 88, 31, 66, 55, 20]
    BubbleSort(alist)
    print(alist)
