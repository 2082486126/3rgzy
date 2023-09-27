import re  # 导入正则表达式模块
from fractions import Fraction  # 导入分数模块


# 处理算式的函数
def pro_suanshi(suanshi):
    if '.' in suanshi:
        par = suanshi.partition('.')
        suanshi = par[2].partition('=')[0][:]
    suanshi = re.sub(' ', '', suanshi)  # 去掉空格
    l = list(filter(None, re.split('([\+\-\×\÷\(\)])', suanshi)))
    return l  # 返回拆分后的列表


# 判断是否为操作符的函数
def IS_operator(element):
    operators = ['+', '-', '×', '÷', '(', ')']  # 定义操作符列表
    if element in operators:
        return True  # 如果元素在操作符列表中则返回True，否则返回False
    else:
        return False


# 判断在栈中进行何种操作的函数，1 表示入栈，-1 表示出栈
def panduancaozuo(top, current):
    low = ['+', '-']
    mid = ['×', '÷']
    high = ['(']
    proxy = [')']

    if top in low:
        if current in mid or current in high:
            return 1  # 低优先级操作符入栈
        else:  # 当两个操作符相等时进行出栈操作
            return -1

    # 当 top 为乘除的时候都应出栈进行计算
    elif top in mid:
        return -1  # 中优先级操作符出栈

    elif top in high:
        if current == ')':
            return 0  # 栈顶是'('，且当前是')'，出栈
        else:
            return 1  # 其他情况入栈
    else:
        return 1  # 默认情况入栈


# 对两个数进行计算的函数
def calculate(n1, n2, op):
    result = 0
    n1 = chulishuzi(n1)
    n2 = chulishuzi(n2)

    if op == '+':
        result = n1 + n2
    elif op == '-':
        result = n1 - n2
        if result < 0:
            return 'False'
    elif op == '×':
        result = n1 * n2
    elif op == '÷':
        if n2 == 0 or n1 > n2:
            return 'False'
        result = n1 / n2

    return str(result)


# 将分数转换成真分数的函数
def transform_to_zhenfenshu(result):
    if '/' in result[0]:
        p = re.split('\/', result[0])
        if int(p[0]) > int(p[1]):
            m = int(int(p[0]) / int(p[1]))
            result = str(m) + "'" + str(int(p[0]) - m * int(p[1])) + '/' + p[1]
            return result

    return result[0]


# 对数字进行处理的函数，例如将真分数转为假分数
def chulishuzi(num):
    if '/' not in num:
        return Fraction(int(num))
    elif '\'' in num:
        p_1 = re.split('([\'\/])', num)
        molecule = int(p_1[0]) * int(p_1[4]) + int(p_1[2])
        return Fraction(molecule, int(p_1[4]))
    elif '/' in num:
        return Fraction(str(num))


# 主要函数，用于计算算式的函数
def operate(suanshi):
    processedsuanshi = pro_suanshi(suanshi)
    number_stack = []
    operator_stack = []

    for element in processedsuanshi:
        # 判断是数字还是运算符
        op_tag = IS_operator(element)

        if op_tag:
            # 如果是运算符
            while True:
                # 如果运算符栈为空或栈顶元素为'('，则入栈
                if len(operator_stack) == 0 or element == '(':
                    operator_stack.append(element)
                    break

                # 调用 panduancaozuo 函数进行决策
                tag = panduancaozuo(operator_stack[-1], element)
                if tag == 1:
                    # 如果是-1，压入运算符栈并进入下一次循环
                    operator_stack.append(element)
                    break
                elif tag == 0:
                    # 如果是0，弹出运算符栈内最后一个'('，丢掉当前元素，进入下一次循环
                    operator_stack.pop()
                    break
                elif tag == -1:
                    # 如果是1，弹出运算符栈内最后两个元素，弹出数字栈最后两位元素
                    op = operator_stack.pop()
                    p2 = number_stack.pop()
                    p1 = number_stack.pop()

                    # 执行计算
                    final_result = calculate(p1, p2, op)

                    # 判断算式中是否存在除数为零
                    if 'False' in final_result:
                        return [' ']
                    # 计算之后压入数字栈
                    number_stack.append(final_result)
        else:
            # 如果是数字则压入数字栈
            number_stack.append(element)

    # 处理大循环结束后数字栈和运算符栈中可能还有元素的情况
    while len(operator_stack) != 0:
        op = operator_stack.pop()
        num2 = number_stack.pop()
        num1 = number_stack.pop()

        # 执行计算
        final_result = calculate(num1, num2, op)

        # 判断算式中是否存在除数为零
        if 'False' in final_result:
            return [' ']

        number_stack.append(final_result)

    return transform_to_zhenfenshu(number_stack)
