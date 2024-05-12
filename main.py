from cache import Cache
import asyncio

cache = Cache()


@cache
async def async_func(arg):
    return arg


asyncio.run(async_func('первый'))
asyncio.run(async_func('второй'))
f = asyncio.run(async_func('первый'))
f2 = asyncio.run(async_func('четверка'))
f5 = asyncio.run(async_func('первый'))
print("cache:", [value for value in cache.data_cache.values()])
print("=" * 32)


@cache
def slow_function(arg):
    return arg


res1 = slow_function(1111)
res2 = slow_function(2222)
res3 = slow_function(1111)
res4 = slow_function(3333)
res5 = slow_function(1111)
print("cache:", [value for value in cache.data_cache.values()])
print("=" * 32)


class MyClass:
    @cache
    def method(self, arg):
        return arg


c = MyClass()
res25 = c.method("100_999")
c.method("100_000")
res10 = c.method("100_000")
res20 = c.method("100_999")
res30 = c.method("170_000")

print("cache:", [value for value in cache.data_cache.values()])
print("=" * 32)
