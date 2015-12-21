# coding=utf-8

#for语句可以循环访问任何的序列
words = ['apple', 'banana', 'orange']
for w in words:
    print(w)

#如果要在循环内修改正在迭代的序列，采用副本作为循环体，采用切片
for w in words[:]:
    if len(w) < 6:
        words.insert(0,w)
print(words)

#打印索引和值的两种方法
# 1.采用range()和len()
for i in range(len(words)):
    print(i, words[i])
# 2.采用enumerate() 函数
for i, v in enumerate(words):
    print(i, v)

#采用zip()可以同时便利两个或更多序列
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))