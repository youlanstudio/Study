# coding = utf-8

# Generator 生成器
# 生成器是简单且功能强大的工具，用于创建迭代器。
# 它们写起来就像是正规的函数，需要返回数据的时候使用yield语句。
# 每次在它上面调用next()时，生成器恢复它脱离的位置（它记忆语句最后一次执行的位置和所有的数据值）。

# 创建Generator的方法一：把一个列表生成式的[]改成()，就创建了一个generator
l = [x ** 2 for x in range(10)] # 列表
print(l)
g = (y ** 2 for y in range(10)) # 生成器Generator
print(g)

# 创建Generator的方法二： 在函数中包含yield关键字
# 变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n += 1
    return 'done'

f1 = fib(9)  # f就是一个generator object
print(f1)
for i in f1:
    print(i)

# 用for循环调用generator时，发现拿不到generator的return语句的返回值。
# 如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中
f2 = fib(9)
while True:
    try:
        print('g:', next(f2))
    except StopIteration as e:
        print('Generator return value: ', e.value)
        break

# 杨辉三角
def yanghui():
    b = [1]
    while True:
        yield b
        b = [1] + [b[i] + b[i + 1] for i in range(len(b) - 1)] + [1]

x = 0
for y in yanghui():
    print(y)
    x += 1
    if x > 10:
        break




