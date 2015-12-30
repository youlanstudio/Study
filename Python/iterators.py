# coding = utf-8

# Iterators 迭代器

# 凡是可作用于for循环的对象都是Iterable类型；
# 凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；
# 集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。
# Python的for循环本质上就是通过不断调用next()函数实现的

# 迭代器的用法在 Python 中普遍而且统一。
# 在后台， for语句调用传入了容器对象的iter() 。
# 该函数返回一个定义了__next__()方法的迭代器对象，它在容器中逐一访问元素。没有后续的元素时，
# __next__()会引发StopIteration异常，告诉for循环终止。你可以是用内建的next()函数调用__next__()方法；

# 看过迭代器协议背后的机制后，将很容易将迭代器的行为添加到你的类中。
# 定义一个__iter__()方法，它使用__next__()方法返回一个对象。如果类定义了__next__()，__iter__()可以只返回self


class Reverse:
    """Iterator for looping over a sequence backwards."""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.data[self.index]

rev = Reverse('spam')
print(iter(rev))
for c in rev:
    print(c)
