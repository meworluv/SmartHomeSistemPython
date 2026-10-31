import time
from functools import wraps

def measure_time(func):
    """Декоратор отображающий скорость выполнения функции (и немного замедляющий)"""

    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        print(f"[ЗАПУСК]: Выполняется {func.__name__}...")
        result = func(*args, **kwargs)
        finish_time = time.perf_counter()
        result_time = finish_time - start_time
        print(f"[ЗАВЕРШЕНО]: {func.__name__} выполнена за {result_time:.2f} сек.")
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