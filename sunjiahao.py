import os
import re
from collections import Counter
import sys
from re import findall
def reads(path):   #读取文件
        f = open(path, encoding='utf-8')
        words = re.findall(r'\w+', f.read().lower())#转为小写字母
        return words

def txt_conts(words):  #统计文件数目并打印前10个出现最多词汇
        cnt = Counter(words)
        sum = 0
        for i in cnt:
             sum = sum + 1
        if sys.argv[1] == '-s':
             print('total ', sum)
        else:
             print('total  {} words'.format(sum))
        list1 = cnt.most_common(10)#使用Counter自带排序
        for i in range(10):
             word, count = list1[i]    #解包
             print("{0:<10}{1:>5}".format(word, count))

def num_conts(path):  #功能5统计不同字母的最大前n个
        words = reads(path)
        cnt = Counter(words)
        sum = 0
        for i in cnt:
                sum = sum + 1
        print('total     {} words'.format(sum))
        j = 0
        maxwords = cnt.most_common()
        for i in range(sum):
            word, count = maxwords[i]
            if len(word) == int(sys.argv[2]):
                    print("{0:<10}{1:>5}".format(word, count))
                    j = j + 1
            if j == int(sys.argv[3]):
                    break
def doCount(argvs):  # 对文件名进行更改
            str = '.txt'
            if str in argvs:
                    path = argvs
            else:
                    path = argvs + str
            txt_conts(reads(path))
def Dic_word(path):#读取文件夹
        #paths = 'D:\Project1\homework2\\' + path
        #for root, subdir, file_list in os.walk(paths):
                files = os.listdir(path)
                for file in files:
                        #file_path = os.path.join(root, file)
                        filename = os.path.splitext(file)[0]
                        print(filename)
                        file_path = path + '\\' +file
                        f = open(file_path, encoding='utf-8')  # 打开
                        # w = re.findall(r'[a-z0-9^-]+', f.read().lower())
                        # txt_conts(w)
                        # print('----')
                        words = re.findall(r'[a-z0-9^-]+', f.read().lower())
                        cnts = Counter(words)
                        sums = 0
                        for i in cnts:
                            sums = sums + 1
                        print('total {} words'.format(sums))
                        list1 = cnts.most_common(10)  # 使用Counter自带排序
                        for i in range(10):
                                word, count = list1[i]  # 解包
                                print("{0:<10}{1:>5}".format(word, count))
                        print('----')
                        f.close()
def  function_four():#重定向
         str = input()
         filename = "D://python//Scripts//dist//test.txt"
         with open(filename, "w") as f:
               f.write(str)
               file = 'test.txt'
               doCount(file)

def main(argv):#主函数
        if sys.argv[1] == '-s':#重定向或者功能一
               if len(sys.argv) == 3:
                    doCount(sys.argv[2])
               else:# 重定向1
                    function_four()
        elif os.path.isdir(sys.argv[1]):# 功能三
               Dic_word(sys.argv[1])
        elif  len(sys.argv) == 4 and( 1<=int(sys.argv[2]) or int(sys.argv[2])<=10 ):#功能五
               num_conts(argv[1])
        else:
               doCount(sys.argv[1])
# if __name__ == "__main__":#是否是自身调用，自身调用就执行如果是引入就不去执行
#     main(sys.argv[0:])
Dic_word('noval')