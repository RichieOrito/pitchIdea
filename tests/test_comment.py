import unittest
from app.models import Comment


class CommentModelTest(unittest.TestCase):
    """
    Test Class to test the behaviour of the Comment class
    """

    def setUp(self):
        """
        Set up method that will run before every Test
        """
        self.comment= Comment(comment_content = 'testing testing')


    def tearDown(self):
        Comment.query.delete()


    def test_instance(self):
        self.assertTrue(isinstance(self.comment, Comment))


    def test_check_instance_variables(self):
        self.assertEquals(self.comment.comment_content,'testing testing')
