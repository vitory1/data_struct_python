def SequentialSearch(alist, item):
    pos = 0
    found = False

    while pos < len(alist) and not found:
        if alist[pos] == item:
            found = True
        else:
            pos = pos + 1
    return found


if __name__ == "__main__":

    testlist = [1, 2, 32, 8, 17, 19, 42, 13, 0]
    print(SequentialSearch(testlist, 3))
    print(SequentialSearch(testlist, 13))
