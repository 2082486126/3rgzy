import json  # 导入 JSON 模块
import re  # 导入正则表达式模块
from fractions import Fraction  # 导入分数模块中的 Fraction 类
from 四则运算实现 import operate, pro_suanshi  # 导入 calculate 中的


# 去除无用括号
def qukuohao(suanshi):
    l = list(suanshi)  # 将算式字符串转换为字符列表
    left_bracket = [key for key, value in enumerate(l) if value == '(']  # 获取左括号的索引列表
    right_bracket = [key for key, value in enumerate(l) if value == ')']  # 获取右括号的索引列表

    suanshi = re.sub(' ', '', suanshi)  # 去除空格

    # 如果存在两个括号对，且相邻，将其删除
    if len(left_bracket) == 2:
        if left_bracket[1] - left_bracket[0] == 1 and right_bracket[1] - right_bracket[0] == 1:
            del l[right_bracket[0]]
            del l[left_bracket[1]]
            del left_bracket[1]
            del right_bracket[0]

    # 如果算式以左括号开头且以右括号结尾，将其删除
    if l.index('(') == 0 and l.index(')') == len(l) - 1:
        del l[l.index('(')]
        del l[l.index(')')]

    print(left_bracket, right_bracket)
    print(l)
    return


# 检测算式的答案是否符合要求，符合则返回具体答案，否则返回空字符串 ''
def checksuanshi(suanshi, maxNum):
    answer = operate(suanshi)  # 使用 operate 函数计算算式的答案
    # 去除答案为负数和算式中除数为零时的算式
    if '-' in answer[0] or ' ' in answer[0]:
        return 'Null'
    return str(answer)


# 检查答案对错（用于文件输入）
def checkAnswers(text):
    correct_list = []  # 存储正确答案的列表
    wrong_list = []  # 存储错误答案的列表
    count = 0

    for i in text:
        if i == '':
            break
        count += 1
        result = operate(i)  # 使用 operate 函数计算算式的答案
        if text[i] == result:
            correct_list.append(str(count))  # 答案正确，将题号添加到正确答案列表中
        else:
            wrong_list.append(str(count))  # 答案错误，将题号添加到错误答案列表中
    wrong_count = len(wrong_list)
    correct_count = len(correct_list)
    wrong_str = "Wrong: " + str(wrong_count) + '(' + ",".join(str(i) for i in wrong_list) + ')'
    correct_str = "Correct: " + str(correct_count) + '(' + ",".join(str(i) for i in correct_list) + ')'

    print(correct_str, wrong_str)  # 输入批改结果
    return correct_list


# 获取错误答案的题号列表
def wrongAnswers(text):
    correct_list = []  # 存储正确答案的列表
    wrong_list = []  # 存储错误答案的列表
    count = 0

    for i in text:
        if i == '':
            break
        count += 1
        result = operate(i)  # 使用 operate 函数计算算式的答案

        if text[i] == result:
            correct_list.append(str(count))  # 答案正确，将题号添加到正确答案列表中
        else:
            wrong_list.append(str(count))  # 答案错误，将题号添加到错误答案列表中

    return wrong_list


# 获取批改结果的字符串
def pigaijieguo(text):
    correct_list = []  # 存储正确答案的列表
    wrong_list = []  # 存储错误答案的列表
    count = 0

    for i in text:
        if i == '':
            break
        count += 1
        result = operate(i)  # 使用 operate 函数计算算式的答案

        if text[i] == result:
            correct_list.append(str(count))  # 答案正确，将题号添加到正确答案列表中
        else:
            wrong_list.append(str(count))  # 答案错误，将题号添加到错误答案列表中

    correct_count = len(correct_list)
    wrong_count = len(wrong_list)

    correct_str = "Correct: " + str(correct_count) + '(' + ",".join(str(i) for i in correct_list) + ')'
    wrong_str = "Wrong: " + str(wrong_count) + '(' + ",".join(str(i) for i in wrong_list) + ')'
    last_str = correct_str + "\n" + wrong_str

    return last_str  # 返回批改结果的字符串
