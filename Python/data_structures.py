# coding=utf-8

# 列表解析(List Comprehensions)
# 创建列表的方法：
list_len = 10
# 1.普通方法：
squares1 = []
for x in range(list_len):
    squares1.append(x ** 2)
print(squares1)

# 2.匿名函数法：
squares2 = list(map(lambda y: y ** 2, range(list_len)))
print(squares2)

# 3.列表解析法：
squares3 = [z ** 2 for z in range(list_len)]
print(squares3)

# 列表解析：组合两个列表中不相等的元素(如果表达式是一个元组, 它必须带圆括号)
print([(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y])

# 上述列表解析等效于如下的语句
combs = []
for x in [1, 2, 3]:
    for y in [3, 1, 4]:
        if x != y:
            combs.append((x, y))
print(combs)

# 更多列表解析
vec = [-4, -2, 0, 2, 4]
print([x ** 2 for x in vec])
print([x for x in vec if x >= 0])
print([abs(x) for x in vec])
print([(x, x ** 2) for x in range(list_len)])
vec1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print([num for elem in vec1 for num in elem])  # 结果：[1, 2, 3, 4, 5, 6, 7, 8, 9]


# 列表解析可以包含复杂的表达式和嵌套的函数：
from math import pi
print([str(round(pi, i)) for i in range(1, 6)])

# 转置行和列
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
# 列表解析实现方式，结果 [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
print([[row[i] for row in matrix] for i in range(len(matrix[0]))])
# zip()实现方式,zip()接收多个序列并将它们组合成为元组
print(list(zip(*matrix)))

# 集合：集合中的元素不会重复且没有顺序。集合对象还支持并集、 交集、 差和对称差等数学运算。
# 花大括号或 set() 函数可以用于创建集合。注意： 若要创建一个空集必须使用set()，而不能用 {}；后者将创建一个空的字典
# 集合也支持集合解析
print({x for x in 'abracadabra' if x not in 'abc'})  # 结果{'r', 'd'}

# 字典：字典由 键 做索引，键可以是任意不可变类型。字符串和数字永远可以拿来做键。

# dict() 构造函数直接从键-值对序列创建字典：
print(dict([('alex', 4139), ('guido', 4127), ('jack', 4098)]))

# 字典解析可以用于从任意键和值表达式创建字典
print({x: x ** 2 for x in range(list_len)})

# 循环迭代字典的时候，键和对应的值通过使用items()方法可以同时得到。
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)
