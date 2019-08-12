import datetime

tstart = None
tend = None
def start_time():
    global tstart
    tstart=datetime.datetime.now()

def get_delta():
    global tend
    global tstart
    tend=datetime.datetime.now()
    return tend-tstart

# 计算斐波那契数列的简单（也是非常低效的）示例
def fib(n):
    return n if n==0 or n==1 else fib(n-1)+fib(n-2)


def fib_seq(n):
    seq = []
    if n > 0:
        seq.extend(fib_seq(n - 1))
    seq.append(fib(n))
    return seq

start_time()
delta1=get_delta()


start_time()
seq=fib_seq(30)
delta2=get_delta()

start_time()
for n in seq:
    print(n)

delta3=get_delta()

print(delta1)
print(delta2)
print(delta3)

