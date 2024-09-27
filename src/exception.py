
import sys
from typing import Optional
from src.logger import logging
def message_error(error,error_message:sys):
    """
    Constructs an error message string with detailed information about the error.

    Args:
    - error: The exception instance.
    - error_message: The sys module to extract exception information.

    Returns:
    - A formatted error message string.
    """
    _,_,exe_tb=error_message.exc_info()
    file_name=exe_tb.tb_frame.f_code.co_filename
    return f"Error is in {file_name} on {exe_tb.tb_lineno} and error is {str(error)}"


class CustomException(Exception):
    def __init__(self, error, error_message:sys):
        """
        Initializes the custom exception with a detailed error message.
        Args:
        - error: The exception instance.
        - error_message: The sys module to extract exception information.
        """
        super().__init__(error)
        self.error=message_error(error=error,error_message=error_message)
    def __str__(self):
        """
        Returns the error message string.
        Returns:
        - The error message string.
        """
        return self.error
#code by Abdul-Basit 






