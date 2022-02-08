import unittest
from app.models import Post

class PostModelTest(unittest.TestCase):
    """
    Test Class to test the behaviour of the class
    """
    
    def setUp(self):
        """
        Set up method that will run before every Test
        """
        self.post= Post(title = 'Ideas change the world', content = 'It is displayed here')


    def tearDown(self):
        Post.query.delete()



    def test_instance(self):
        self.assertTrue(isinstance(self.post, Post))



    def test_check_instance_variables(self):
        self.assertEquals(self.post.title,'Ideas change the world')
        self.assertEquals(self.post.content,'It is displayed here')