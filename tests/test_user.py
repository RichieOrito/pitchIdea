import unittest
from app.models import User

class UserModelTest(unittest.TestCase):
    """
    Test class to test the behaviour of the user class
    """

    def setUp(self):
        """
        Set up method that will run before every Test
        """

        self.new_user=User(username='richie', password = 'xoxo')


    def test_password_setter(self):
        self.assertTrue(self.new_user.pass_secure is not None)

    def test_no_access_password(self):
        with self.assertRaises(AttributeError):
            self.new_user.password


    def test_password_verification(self):
        self.assertTrue(self.new_user.verify_password('xoxo'))


    def tearDown(self):
        user = User.query.filter_by(username="richie").first()
        if user:
            print("found")