from enum import Enum


class ResponseCodeEnum(Enum):
    """custom_errors codes"""
    SUCCESS = 202
    BAD_REQUEST = 404
    INVALID = 403


    @classmethod
    def value_of(cls, value):
        for k, v in cls.__members__.items():
            if k == value:
                return v
            else:
                raise ValueError(f"'{cls.__name__}' enum not found for '{value}'")
