import unittest
from models import Articles
Articles = articles.Articles

class ArticlesTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the articles class
    '''

    def setUp(self):
      '''
        Set up method that will run before every Test
        '''
        self.new_articles = Articles('Roman','The pandemic strike','"https://www.cnn.com/2020/04/24/us/georgia-coronavirus-reopening-businesses-friday/index.html"',
       "https://cdn.cnn.com/cnnnext/dam/assets/200423233851-georgia-businesses-reopen-0422-super-tease.jpg",  )

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,articles))


if __name__ == '__main__':
    unittest.main()  