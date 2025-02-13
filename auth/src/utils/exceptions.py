from typing import Any

class ExceptionBase(Exception):
    pass

class UserAlreadyExist(Exception):
    def __init__(self, status_code:int, msg:str):
        self.msg = msg
        self.status_code = status_code

