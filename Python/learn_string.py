# -*- coding: utf-8 -*-


#'\'用于转义引号
print('doesn\'t')


#如果字符串中只有单引号而没有双引号，就用双引号引用，否则用单引号引用。
print("doesn't")              #结果 doesn't
print('"Yes," he said.')      #结果 "Yes," he said.
print("\"Yes,\" he said.")    #结果 "Yes," he said.
print('"Isn\'t," she said.')  #结果 "Isn't," she said.

#如果你前面带有\的字符被当作特殊字符，你可以使用原始字符串，方法是在第一个引号前面加上一个r
print('C:\some\name')
print(r'C:\some\name')

#多行字符串采用三引号
print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")

#字符串连接采用加号(+)，乘号(*)操作符用于重复多次
print('Good ' + 'luck ' + '!'*3)

#字符串可以索引。Python 没有单独的字符类型；字符就是长度为 1 的字符串。
word = 'Python'
for i in range(len(word)):
    print('word[%d] : %s' % (i, word[i]))

#索引可以为负数，从右边开始计数
word = 'Python'
for i in range(len(word)):
    print('word[%d] : %s' % (-i-1, word[-i-1]))

#切片(slicing)
# +---+---+---+---+---+---+
# | P | y | t | h | o | n |
# +---+---+---+---+---+---+
#   0   1   2   3   4   5
#  -6  -5  -4  -3  -2  -1
print(word[0:2])
print(word[2:5])
print(word[:2])
print(word[2:])
print(word[4:])
print(word[-2:])

#Python 字符串不可以改变—它们是不可变的。因此，赋值给字符串索引的位置会导致错误
#word[1] = 'a'  #TypeError: 'str' object does not support item assignment

