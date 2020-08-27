class Solution:
    def isMatch(self, s, p):
        def remove(ss, index, lindex):
            ch = list[ss]
            for i in range(index, lindex, -1):
                ch[i] = ""
            ss = "".join(ch)
            return ss
        Flag = True
        count1index = []
        count2index = []
        for i in range(len(p)):
            if p[i] == ".":
                count1index.append(i)
                p.replace(".", "")
            if p[i] == "*":
                count2index.append(i)
        for index1 in count1index:
            s.replace(s[index1], "")
        for index2 in count2index:
            cur = index2
            for i in range(index2, -1, -1):
                if i == 0:
                    s = remove(s, cur, 0)
                if s[index2] != s[index2 - 1]:
                    if (cur - index2) == 0:
                        Flag = False
                    s = remove(s, cur, index2)
            p.replace("*", "")
        if s == p:
            return Flag
        else:
            Flag = False
            return Flag


if __name__ == "__main__":
    s = "aa"
    p = "a*"
    a = Solution()
    print(a.isMatch(s, p))
