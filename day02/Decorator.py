import functools


def now():
    print('2018-01-15')


f = now
print(f())
print(now.__name__)
print(f.__name__)
print('++++++++++++++++++++++++++++')


def log(func):
    def wrapper(*args, **kwargs):
        print('call %s():' % func.__name__)
        return func(*args, **kwargs)

    return wrapper


@log
def now():
    print('2018-01-15')


print(now())
print('+++++++++++++++++++++++++++++++')


# 如果装饰器本身需要传入参数的情况
def log2(text):
    def decorator(func):
        # 使用Python内置的functools.wraps可以保证原始函数的__name__属性不会改变
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kwargs)

        return wrapper

    return decorator


@log2('excute')
def now():
    print('2018-01-15')


print(now())
print(now.__name__)
