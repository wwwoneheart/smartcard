"""
Enclosure base error
"""


class ApiError(Exception):
    """Base class for custom exceptions"""
    des = ''
    message = 'Internal server error'
    code = 500

    def __init__(self, message=None, code: int = None, des=None, *args):
        # If the key `msg` is provided, provide the msg string
        # to Exception class in order to display
        # the msg while raising the exception
        if code:
            self.code = code
        if message:
            self.message = message
        if des:
            self.des = des

        super(Exception, self).__init__(self.code, self.message, self.des, *args)

    def __str__(self):
        return '[{code}] {message} {des}'.format(code=self.code,
                                                 message=self.message,
                                                 des=self.des)

    def make_error_message(self):
        message_dict = {
            "message": self.message
        }
        return message_dict, self.code


