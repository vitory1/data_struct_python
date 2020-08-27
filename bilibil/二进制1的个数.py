class Solution:
    def hammingWeight(self, n: int) -> int:
        stack = []
        count = 0
        while n > 0:
            stack.append(n % 2)
            n = n // 2
        while stack:
            if stack.pop() == 1:
                count = count + 1
        return count


if __name__ == "__main__":
    s = Solution()
    print(s.hammingWeight(20))
