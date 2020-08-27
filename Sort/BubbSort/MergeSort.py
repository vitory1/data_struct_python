def merge_sort(alist):
    if len(alist) <= 1:
        return alist

    mid = len(alist) // 2
    left = merge_sort(alist[:mid])
    right = merge_sort(alist[mid:])

    merged = []
    while left and right:
        if left[0] <= right[0]:
            merged.append(left.pop(0))
        else:
            merged.append(right.pop(0))
    merged.extend(right if right else left)
    return merged


if __name__ == "__main__":
    alist = [54, 26, 93, 17, 88, 31, 66, 55, 20]
    merge_sort(alist)
    print(alist)
