import unittest
from models import news
NEWS = news.news

class NewsTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Movie class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_news = News('cnn','CNN',"Faith Karimi, CNN","Georgia is reopening hair salons, gyms and bowling alleys despite a rise in coronavirus deaths statewide - CNN",
        "Undeterred by a barrage of criticism, Georgia is moving ahead with its plan to reopen some nonessential businesses despite an increase in coronavirus deaths statewide.",
        "https://www.cnn.com/2020/04/24/us/georgia-coronavirus-reopening-businesses-friday/index.html",
        "https://cdn.cnn.com/cnnnext/dam/assets/200423233851-georgia-businesses-reopen-0422-super-tease.jpg",
        "2020-04-24T10:35:51Z","(CNN)Undeterred by a barrage of criticism, Georgia is moving ahead with its plan to reopen some nonessential businesses despite an increase in coronavirus deaths statewide.\r\nGov. Brian Kemp was one of the last state leaders to issue a stay-at-home order effec… [+5500 chars]")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,news))


if __name__ == '__main__':
    unittest.main()
