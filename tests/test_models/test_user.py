#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.user import User


class test_User(test_basemodel):
    """ Tests user.py module """

    def __init__(self, *args, **kwargs):
        """ inits the user module """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """ tests first name attribute of user module """
        new = self.value()
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """  tests last name attribute of user module """
        new = self.value()
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """  tests email name attribute of user module """
        new = self.value()
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """  tests password attribute of user module """
        new = self.value()
        self.assertEqual(type(new.password), str)
