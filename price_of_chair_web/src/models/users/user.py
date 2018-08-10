import uuid

from src.common.database import Database
from src.common.utils import Utils
import src.models.users.errors as UserErrors

__author__ = 'alexasih'


class User(object):
    def __init__(self, email, password, _id=None):
        self.email = email
        self.password = password
        self._id = uuid.uuid4().hex if _id is None else _id

    def __repr__(self):
        return "<User {}>".format(self.email)

    @staticmethod
    def is_login_valid(email, password):
        """
        This method verifies that an e-mail/password combo (as sent by the site forms) is valid or not.
        Checks that the e-mail exists, and that the password associated to that e-mail is correct.
        :param email: The user's email
        :param password: A sha512 hashed password
        :return: True if valid, False otherwise
        """
        user_data = Database.find_one("users", {'email': email})  # Password in sha512 -> pbkdf2_sha512
        if user_data is None:
            # Tell the user that their e-mail doesn't exist
            raise UserErrors.UserNotExistsError("Your user does not exist.")
        if not Utils.check_hashed_password(password, user_data['password']):
            # Tell the user that their password is wrong
            raise UserErrors.IncorrectPasswordError("Your password was wrong.")

        return True
