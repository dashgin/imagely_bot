from functools import wraps
from typing import Callable

from imagely.domain.exceptions import WrongFileExtensionModelException


def is_jpeg(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(code, src_path):
        if src_path.endswith(".jpeg") or src_path.endswith(".jpg"):
            return func(code=code, src_path=src_path)
        raise WrongFileExtensionModelException(
            "Wrong file extensions: expected .jpeg or .jpg"
        )
    return wrapper
