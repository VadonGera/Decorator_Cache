import asyncio
from functools import wraps


class Cache:
    def __init__(self):
        self.data_cache = {}

    def __call__(self, func):
        self.invalidate(func)

        if asyncio.iscoroutinefunction(func):
            @wraps(func)
            async def wrapper(*args, **kwargs):
                if args in self.data_cache:
                    return self.data_cache[args]
                result = self.data_cache[args] = await func(*args, **kwargs)
                return result
        else:
            @wraps(func)
            def wrapper(*args, **kwargs):
                if args in self.data_cache:
                    return self.data_cache[args]
                result = self.data_cache[args] = func(*args, **kwargs)
                return result

        return wrapper

    def invalidate(self, func):
        self.data_cache.clear()
        print("Invalidate for", func.__name__)
