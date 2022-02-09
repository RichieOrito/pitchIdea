import unittest
from app.models import Pitch

class PostModelTest(unittest.TestCase):
    """
    Test Class to test the behaviour of the class
    """
    
    def setUp(self):
        """
        Set up method that will run before every Test
        """
        self.new_pitch= Pitch(id=1234,content='technology',category_id=123,user_id=456)


    def test_instance(self):
        self.assertTrue(isinstance(self.new_pitch, Pitch))


    def test_check_instance_variables(self):
        self.assertEquals(self.new_pitch.id,1234)
        self.assertEquals(self.new_pitch.content,'technology')
        self.assertEquals(self.new_pitch.category_id,123)
        self.assertEquals(self.new_pitch.user_id,456)



