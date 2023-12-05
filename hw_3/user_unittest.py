import unittest
from user import User
from user_repository import UserRepository


class UserTest(unittest.TestCase):
    def test_user_logout_test(self):
        repository = UserRepository()
        repository.add_user(User("name1", "password1", True))
        repository.add_user(User("name2", "password2", False))
        repository.add_user(User("name3", "password3", True))
        repository.add_user(User("name4", "password4", False))
        repository.add_user(User("name5", "password5", False))
        repository.all_users_logout()
        for user in repository.users:
            self.assertTrue(user.admin)
