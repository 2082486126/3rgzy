import sys, getopt
import time
from 题目数量 import *
from 检查判断 import *


def main(argv):
    n_default = 10  # 默认题目数量
    r_default = 10  # 默认数值范围
    try:
        input_np= ''  # 题目文件
        input_rp = ''  # 答案文件
        opts, args = getopt.getopt(argv, "hgn:r:e:a:", ["ifile=", "ofile="])
    except getopt.GetoptError:
        print('输入错误:  \n 请按以下格式输入：-n num -r num / -e -a \n（可输入参数-h输出帮助信息）')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print(
                " 程序指令说明\n-n <数字>(大于0) ,指定生成题目的数量，默认为10"
                "\n-r <数字>(大于0) ,指定题目中数值范围，默认[0,10]"
                "\n-e <exercisefile>.txt -a <answerfile>.txt 对给定的题目文件和答案文件，判定答案中的对错并进行数量统计 ")
            sys.exit(2)
        elif opt in ("-n", "--num"):
            n_default = arg
        elif opt in ("-r", "--range"):
            r_default= arg
        elif opt in ("-e", "--question"):
            input_np= arg
        elif opt in ("-a", "--answer"):
            input_rp = arg

    if (input_np == '' and input_rp == ''):
        makeproblem(n_default, r_default)
    else:
        jianchadaan(input_np ,input_rp)


def jianchadaan(file1, file2):
    try:
        question_path = open(file1, 'r', encoding='utf-8')
        question_text = question_path.read()
    except IOError:
        print("读取失败".format(file1))
    else:
        try:
            answer_path = open(file2, 'r', encoding='utf-8')
            answer_text = answer_path.read()
        except IOError:
            print("读取失败".format(file2))
        else:

            q_spilt = re.split('\n', question_text)
            a_spilt = re.split('\n', answer_text)
            q_spilt = [i for i in q_spilt if i != '']
            a_spilt = [i for i in a_spilt if i != '']
            q_spilt = renameaq(q_spilt)
            a_spilt = renameaq(a_spilt)
            if (len(q_spilt) == len(a_spilt)):
                print("进入批改系统\n" + "\n题目来源来源:" + file1 +
                      "\n答案来源:" + file2 + "\n已批改" + str(len(q_spilt)) + "道题目\n\n")
                # print('检查题目： 已检查' + str(len(q_spilt)) + '道题目')
                aq_dict = dict(zip(q_spilt, a_spilt))
                checkanswers = checkAnswers(aq_dict)
                wrong_list = wrongAnswers(aq_dict)
                correct_str = "Correct: " + str(len(checkanswers)) + '(' + ",".join(
                    str(i) for i in checkanswers) + ')'
                wrong_str = "   Wrong: " + str(len(wrong_list)) + '(' + ",".join(str(i) for i in wrong_list) + ')'
                print(correct_str + wrong_str + "\n正确率：" + str(
                    round((len(q_spilt) - len(wrong_list)) / len(q_spilt),
                          2)))
                getdown = pigaijieguo(aq_dict)
                Grade_txt = open('Grade' + '.txt', "w", encoding='utf-8')
                Grade_txt.write(getdown)
                Grade_txt.close()
            else:
                print("题目总数和答案总数不相等：\n题目个数" + str(len(q_spilt)) + "\n答案个数：" + str(
                    len(a_spilt)) + "\n请检查上传的问题答案文件n\n")


def get_current_time():
    current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    return current_time


def renameaq(aq):
    last_aq = []
    for change in aq:
        # print(change)
        last_aq.append("".join(str(i) for i in pro_suanshi(change)))
    return last_aq


def makeproblem(n_num, r_num):
    Exercises_txt = open('Exercises' + '.txt', "w", encoding='utf-8')
    Answers_txt = open('Answers' + '.txt', "w", encoding='utf-8')

    getmain = Rmain(n_num, r_num)
    for i in range(len(getmain[0])):
        Exercises_txt.write(str(i + 1) + ". " + getmain[0][i] + '\n')
        Answers_txt.write(str(i + 1) + ". " + getmain[1][i] + '\n')
        print('正在生成算式...')
    Exercises_txt.close()
    Answers_txt.close()
    print("已生成" + str(n_num) + "个题目，其中题目中的数值（自然数、真分数和真分数分母）的范围在[0," + str(r_num) + "]")
    return getmain


if __name__ == '__main__':
    main(sys.argv[1:])
    # jianchadaan('1.txt','2.txt')
    import cProfile
    import re

    #
    # cProfile.run('re.compile("foo|bar")')
