from typing import Any


class ExceptionBase(Exception):
    def __init__(self, status_code: int, msg: str):
        self.msg = msg
        self.status_code = status_code
        super().__init__(msg)

class UserAlreadyExist(ExceptionBase):
    pass

class UserNotFound(ExceptionBase):
    pass

class InvalidPassword(ExceptionBase):
    pass

class WeakPassword(ExceptionBase):
    pass

class FailedToSaveUser(ExceptionBase):
    pass

