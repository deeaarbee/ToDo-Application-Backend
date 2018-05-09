from django.test import TestCase

from .models import User
from todo.functions import core as core

class TestUserUpdates(TestCase):
    def setUp(self):
        pass

    def test_create_user(self):
        user = User()
        user = core.createUser("deeaarbee","spiderman","drbalaji97@gmail.com",2015103506)
        self.assertEqual(user.username,"deeaarbee")
        # self.assertEqual(user.password,"spiderman")
        self.assertEqual(user.email,"drbalaji97@gmail.com")
        self.assertEqual(user.rollnumber, 2015103506)

