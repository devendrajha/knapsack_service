from app.util.status_code_enum import ResponseCodeEnum


class BothListSizesNotMatch(Exception):

    def __init__(self, message):
        self._message = message
        self.code = ResponseCodeEnum.BAD_REQUEST.value
        super().__init__(self._message, self.code)


class InsufficientDataFound(Exception):

    def __init__(self, message):
        self._message = message
        self.code = ResponseCodeEnum.BAD_REQUEST.value
        super().__init__(self._message, self.code)
