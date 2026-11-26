import functools

def log(filename=None):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
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