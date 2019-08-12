import profile
import sys


def profiler(frame, event, arg):
    print('profiler: %r %r' % (event, arg))


sys.setprofile(profiler)


# 计算斐波那契数列的简单（也是非常低效的）示例
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def fib_seq(n):
    seq = []
    if n > 0:
        seq.extend(fib_seq(n - 1))
    seq.append(fib(n))
    return seq


print(fib_seq(2))
