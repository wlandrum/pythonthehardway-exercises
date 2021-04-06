# Decorators
from functools import wraps
def add_wrapping(item):
    @wraps(item)
    def wrapped_item():
        return 'a wrapped up box of {}'.format(str(item()))
    return wrapped_item


@add_wrapping
@add_wrapping
def new_gpu():
    return 'a new Tesla P100 GPU'

@add_wrapping
def new_bicycle():
    return 'a new bicycle'


print(new_gpu.__name__)
print(new_bicycle())

