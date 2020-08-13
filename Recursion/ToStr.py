def tostr(n, base):
    convertString = "0123456789ABCDEF"
    if n < base:
        return convertString[n]
    else:
        return tostr(n//base, base) + convertString[n % base]


if __name__ == "__main__":
    print(tostr(1453, 16))
