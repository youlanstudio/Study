# coding=utf-8

#默认参数
# 定义默认参数要牢记一点：默认参数必须指向不变对象
# 默认值是列表、字典或大部分类的实例等易变的对象的时候又有所不同。例如，下面的函数在后续调用过程中会累积传给它的参数：
def f1(a, L=[]):
    L.append(a)
    return L

print(f1(1))
print(f1(2))
print(f1(3))


# 如果你不想默认值在随后的调用中共享，可以像这样编写函数：
def f2(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

print(f2(1))
print(f2(2))
print(f2(3))


# 可变参数---可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。
# 在参数前加上星号 *
def calc_sum(*numbers):
    sum = 0
    for i in numbers:
        sum += i
    return sum

print(calc_sum(1, 2, 3))
# 如果参数本身就是一个list或者tuple，则在list或者tuple前加一个*号，变为可变参数传入
num_tuple = (1, 2, 3, 4, 5, 6)
print(calc_sum(*num_tuple))

# 关键字参数---关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict
#


# 如果可变参数和关键字参数同时出现时，可变参数必须出现在关键字参数前面
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

person('Michael', 30)
person('Bob', 35, city='Beijing')
person('Adam', 45, gender='M', job='Engineer')

# 参数列表的分拆
# 1. *-操作符将参数从列表或元组中分拆开来
# 2. **-操作符让字典传递关键字参数
args = [3, 6]
print(list(range(*args)))
extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, **extra)

# 文档字符串
def my_function():
    """Do nothing, but document it.

    No, really, it doesn't do anything.
    """
    pass
print(my_function.__doc__)
