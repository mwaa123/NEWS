from app import app
import urllib.request,json
from .models import news
from .models import everything
from .models import sources
News = news.News
# Articles = articles.Articles
# Getting api key
api_key = app.config['NEWS_API_KEY']
# Getting the news base url
base_url = app.config["NEWS_API_BASE_URL"]

def get_news(category): #top-headlines
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = base_url.format(category,api_key) #'s://nhttpewsapi.org/v2/top-headlines?category={sports}&apiKey=5b909bf0340d4286a32ffc2a1dd28dc7'

    with urllib.request.urlopen(get_news_url) as url:  # sports, 5b909bf0340d4286a32ffc2a1dd28dc7
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data) # {"key": "value"}
        '''
           get_news_response = {

        "status": "ok",
        "totalResults": 10,
        -
        "articles": [
            -
            {
                -
                "source": {
                    "id": "bbc-news",
                    "name": "BBC News"
                },
                "author": "BBC News",
    '''


        news_results = None # Response will be {} | None

        if get_news_response['articles']:
            news_results_list = get_news_response['articles']
            news_results = process_results(news_results_list)


    return news_results

def process_results(news_list):
    '''
    Function  that processes the news result and transform them to a list of Objects

    Args:
        news_list: A list of dictionaries that contain news details

    Returns :
        news_results: A list of news objects
    '''

    news_results = []
    for news_item in news_list:
        source = news_item.get('source')
        author = news_item.get('author')
        title = news_item.get('title')
        description = news_item.get('description')
        url = news_item.get('url')
        urlToImage=news_item.get('urlToImage')
        publishedAt =news_item.get('publishedAt')
        content = news_item.get('content')

        news_object = News(source,author,title,description,url,urlToImage,publishedAt,content)

        news_results.append(news_object)

    return news_results


Everything = everything.Everything

# Getting api key
api_key = app.config['NEWS_API_KEY']
# Getting the news base url
evn_url = app.config["EVERYTHING_API_BASE_URL"]

def get_everything(): #everything
    '''
    Function that gets the json response to our url request
    '''
    get_everything_url = evn_url

    with urllib.request.urlopen(get_everything_url) as url:
        get_everything_data = url.read()
        get_everything_response = json.loads(get_everything_data)

        everything_results = None

        if get_everything_response['articles']:
            everything_results_list = get_everything_response['articles']
            everything_results = process_results(everything_results_list)


    return everything_results

def process_results(everything_list):
    '''
    Function  that processes the news result and transform them to a list of Objects

    Args:
        news_list: A list of dictionaries that contain news details

    Returns :
        news_results: A list of news objects
    '''

    everything_results = []
    for everything_item in everything_list:
        id = everything_item['source'].get('id')
        name = everything_item["source"].get('name')
        # author = news_item.get('author')
        title = everything_item.get('title')
        description = everything_item.get('description')
        url = everything_item.get('url')
        urlToImage=everything_item.get('urlToImage')
        publishedAt =everything_item.get('publishedAt')
        content = everything_item.get('content')
        # import pdb; pdb.set_trace()
        everything_object = Everything(id,name,title,description,url,urlToImage,publishedAt,content)

        everything_results.append(everything_object)

    return everything_results





    

Sources = sources.Sources

# Getting api key
api_key = app.config['NEWS_API_KEY']
# Getting the news base url
source_url = app.config["SOURCES_API_BASE_URL"]

def get_sources(category): #sources
    '''
    Function that gets the json response to our url request
    '''
    get_sources_url = source_url.format(category,api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)
        # import pdb; pdb.set_trace()
        sources_results = None

        if get_sources_response['sources']:
            sources_results_list = get_sources_response['sources']
            sources_results = process_results(sources_results_list)


    return sources_results

def process_results(sources_list):
    '''
    Function  that processes the sources result and transform them to a list of Objects

    Args:
        sources_list: A list of dictionaries that contain sources details

    Returns :
        sources_results: A list of sources objects
    '''

    sources_results = []
    for sources_item in sources_list:
        id = sources_item.get('id')
        name = sources_item.get('name')
        description = sources_item.get('description')
        url = sources_item.get('url')
        category =sources_item.get('category')
        language = sources_item.get('language')
        country = sources_item.get('country')
        sources_object = Sources(id,name,description,url,category,language,country)

        sources_results.append(sources_object)

    return sources_results




# the search form request

def search_sources(sources_name):
    search_sources_url = 'https://newsapi.org/v2/sources?country=us&category={}&apiKey={}&query={}'.format(api_key,sources_name)
    with urllib.request.urlopen(search_sources_url) as url:
        search_sources_data = url.read()
        search_sources_response = json.loads(search_sources_data)

        search_sources_results = None

        if search_sources_response['articles']:
            search_sources_list = search_sources_response['articles']
            search_sources_results = process_results(search_sources_list)


    return search_sources_results
# Getting api key
api_key = app.config['NEWS_API_KEY']
# Getting the news base url
evn_url = app.config["EVERYTHING_API_BASE_URL"]
def get_articles(): #articles
    '''
    Function that gets the json response to our url request
    '''
    get_articles_url = evn_url.format(api_key)

    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        articles_results = None

        if get_articles_response['articles']:
            articles_results_list = get_articles_response['articles']
            articles_results = process_results(articles_results_list)


    return articles_results

def process_articles(articles_list):

    articles_results = []
    for articles_item in articles_list:
        title = articles_item.get('title')
        description = articles_item.get('description')
        url = articles_item.get('url')
        urlToImage = articles_item.get('urlToImage')
        publishedAt =articles_item.get('publishedAt')
        content = articles_item.get('content')
        articles_object = Articles(title,description,url,urlToImage,publishedAt,content)

        articles_results.append(articles_object)

    return articles_results