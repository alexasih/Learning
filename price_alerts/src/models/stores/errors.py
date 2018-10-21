__author__ = 'alexasih'


class StoreException(Exception):
    def __init__(self):
        self.message


class StoreNotFoundException(StoreException):
    pass