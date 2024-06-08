
import sys
from typing import Optional
from src.logger import logging
def message_error(error,error_message:sys):
    _,_,exe_tb=error_message.exc_info()
    file_name=exe_tb.tb_frame.f_code.co_filename
    return f"Error is in {file_name} on {exe_tb.tb_lineno} and error is {str(error)}"


class CustomException(Exception):
    def __init__(self, error, error_message:sys):
        super().__init__(error)
        self.error=message_error(error=error,error_message=error_message)
    def __str__(self):
        return self.error








