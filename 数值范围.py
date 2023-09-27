import random  # 导入随机数模块

# 生成随机参数的函数，maxNum 参数用于指定生成的随机数范围
#生成随机参数
def random_parameter( maxNum ):

    #随机生成整数或者分数的标志
    tag = random.randint(0, 1)
    maxNum=int(maxNum)
    num = ''
    # tag == 0 时生成整数
    if tag == 0:
        num = str(random.randint( 0, maxNum ))

    # tag == 1 时生成分数
    elif tag == 1:
        num = random_fraction( maxNum )

    return num

# 随机生成分数的函数，maxNum 参数用于指定生成的随机数范围
def random_fraction(maxshuzi):

    # 随机生成分母
    maxshuzi = int(maxshuzi)  # 将输入的最大值转换为整数
    denominator = random.randint(1, maxshuzi)  # 生成一个随机分母

    # 随机生成分子
    molecule = random.randint(0, maxshuzi * denominator)  # 生成一个随机分子

    if molecule == 0:
        return 0  # 如果分子为 0，则返回 0

    if molecule > denominator:
        m = int(molecule / denominator)  # 计算整数部分
        molecule -= m * denominator  # 计算新的分子
        if molecule != 0:
            return str(m) + "'" + str(molecule) + '/' + str(denominator)  # 返回带整数部分的分数
        else:
            return str(m)  # 返回整数部分

    return str(molecule) + '/' + str(denominator)  # 返回普通分数表示形式
