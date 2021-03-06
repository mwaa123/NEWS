class Config:
    '''
    General configuration parent class
    '''
    NEWS_API_BASE_URL ='https://newsapi.org/v2/top-headlines?country=us&category={}&apiKey=5b909bf0340d4286a32ffc2a1dd28dc7'
    EVERYTHING_API_BASE_URL ='https://newsapi.org/v2/everything?q=bitcoin&apiKey=5b909bf0340d4286a32ffc2a1dd28dc7'
    SOURCES_API_BASE_URL='https://newsapi.org/v2/sources?country=us&category={}&apiKey=5b909bf0340d4286a32ffc2a1dd28dc7'

class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True
