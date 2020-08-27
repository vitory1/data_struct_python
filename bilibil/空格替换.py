class Solution:
    def replaceSpace(self, s: str) -> str:
        ch = list(s)
        for i in range(len(s)):
            if ch[i] == " ":
                ch[i] == "%20"
        ss = "".join(ch)
        return ss


if __name__ == "__main__":
    s = Solution()
    ss = "We are happy."
    s.replaceSpace(ss)
