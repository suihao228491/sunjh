import collections
import re #正则
import os
import sys
from collections import Counter
#计数
def count(words):  # 统计文件数目并打印前10个出现最多词汇
    cnt = Counter(words)
    sum = 0
    for i in cnt:
        sum = sum + 1
    if sys.argv[1] == '-s':
       print('total ', sum)
    else:
       print('total  {} words'.format(sum))
    list1 = cnt.most_common(10)  # 使用Counter自带排序
    for i in range(10):
        word, count = list1[i]  # 解包
        print("{0:<10}{1:>5}".format(word, count))


#打开.txt文件
def opentxt(filename):
    s = '.txt'
    if s in filename:#判断命令控制行.txt文件
        path = filename
    else:
        path = filename + '.txt'
    f=open(path, encoding='utf-8')
    w= re.findall(r'[a-z0-9^-]+', f.read().lower())#通过正则读进去
    count(w)
#通过命令行输入到txt文件
def inputText(Text):
    w = re.findall(r'[a-z0-9^-]+', Text.lower())
    count(w)
#功能三
def FCount(path):
    f = open(path, encoding='utf-8')#打开
    w = re.findall(r'[a-z0-9^-]+', f.read().lower())
    count(w)
    print('----')
def path(path1):
    files = os.listdir(path1)
    for file in files: #循环打开每个文件
        filename = os.path.splitext(file)[0]
        print(filename)
        FCount(path1 + '\\' +file)

#主函数
def main(argv):
    if sys.argv[1] == '-s':
        if (len(sys.argv) == 3):
            opentxt(sys.argv[2])
        else:
            Text = sys.stdin.read()#读出来是字符串形式
            inputText(Text)
    elif os.path.isdir(sys.argv[1]):
            path(sys.argv[1])
    else:
        opentxt(sys.argv[1])

#main(sys.argv[1:])

path('noval')


