# 数列的和 = ”首个数“ + ”余下数列“
# listSum(numList) = first(numList) + listSum(rest(numList))
#     问题         分解                    相同问题，规模更小
# ----------------------------------------------------------------
# 递归的三定律
# 1）递归算法必须有一个基本结束条件（最小规模问题的直接解决）
# 2）递归算法必须能改变状态向基本结束条件演进（减小问题规模）
# 3）递归算法必须调用自身
def listsum(numlist):
    if len(numlist) == 1:
        return numlist[0]
    else:
        return numlist[0] + listsum(numlist[1:])


if __name__ == "__main__":
    print(listsum([1, 3, 5, 7, 9]))
