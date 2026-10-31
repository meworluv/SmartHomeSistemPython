import time
from random import randint
from functools import wraps

def measure_time(func):
    """Декоратор отображающий скорость выполнения функции (и немного замедляющий)"""

    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        print(f"[ЗАПУСК]: Выполняется {func.__name__}...")
        time.sleep(randint(1, 3))
        result = func(*args, **kwargs)
        finish_time = time.time() - start_time
        print(f"[ЗАВЕРШЕНО]: {func.__name__} выполнена за {int(finish_time)} сек.")
        return result
    return wrapper

# def require_permission(level: str):
#     """Декоратор проверяющий уровень доступа для выполнения функции"""
#     def decorator(func):
#         @wraps(func)
#         def wrapper(req_level: str, *args, **kwargs):
#             if level == "admin" or req_level == "user":
#                 return func(*args, **kwargs)
#             else:
#                 print()
#         return wrapper
#     return decorator