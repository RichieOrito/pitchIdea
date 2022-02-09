import unittest
from app.models import Comments

class CommentModelTest(unittest.TestCase):
    """
    Test Class to test the behaviour of the Comment class
    """

    def setUp(self):
        """
        Set up method that will run before every Test
        """
        self.new_comments= Comments(id = 12345,opinion='awesome',user_id=254,pitches_id=1234)

    def tearDown(self):
        Comments.query.delete()


    def test_instance(self):
        self.assertTrue(isinstance(self.new_comments, Comments))


    def test_check_instance_variables(self):
        self.assertEquals(self.new_comments.opinion,'awesome')
        self.assertEquals(self.new_comments.user_id,254)
        self.assertEquals(self.new_comments.pitches_id,1234)

