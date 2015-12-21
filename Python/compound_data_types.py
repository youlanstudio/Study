#coding=utf-8

#复合数据类型(compound data types)
# 1.列表(list)/
# 2.元组

#列表
#列表可以包含不同类型的元素，但是通常一个列表中的所有元素都拥有相同的类型。
squares = [1, 4, 9, 16, 25]
#列表支持索引和切片
print(squares[0])
print(squares[1:2])

#列表也支持连接操作
print(squares + [36, 49, 64, 81, 100])

#在末尾添加新元素
squares.append(36)
print(squares)

#获取列表长度
print(len(squares))