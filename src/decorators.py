from functools import wraps
from typing import Callable, Any, Optional


def log(filename: Optional [str] = None) -> Callable[[Callable],Callable]:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)
                msg = f"{func.__name__} ok"
                if filename:
                    with open(filename, 'a', encoding='utf-8') as f:
                        f.write(msg + '\n')
                else:
                    print(msg)
                return result
            except Exception as e:
                msg = f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}"
                if filename:
                    with open(filename, 'a', encoding='utf-8') as f:
                        f.write(msg + '\n')
                else:
                    print(msg)
                raise
        return wrapper
    return decorator
