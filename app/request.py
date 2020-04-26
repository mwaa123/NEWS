from app import app
import urllib.request,json
from .models import news
from .models import everything
from .models import sources
News = news.News

# Getting api key
api_key = app.config['NEWS_API_KEY']
# Getting the news base url
base_url = app.config["NEWS_API_BASE_URL"]

def get_news(category): #top-headlines
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)
        news_results = None

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

        news_object = News(source,title,author,description,url,urlToImage,publishedAt,content)

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
# source_url = app.config["SOURCES_API_BASE_URL"]

# def get_sources(category): #sources
#     '''
#     Function that gets the json response to our url request
#     '''
#     get_sources_url = source_url.format(category,api_key)

#     with urllib.request.urlopen(get_sources_url) as url:
#         get_sources_data = url.read()
#         get_sources_response = json.loads(get_sources_data)
#         # import pdb; pdb.set_trace()
#         sources_results = None

#         if get_sources_response['sources']:
#             sources_results_list = get_sources_response['sources']
#             sources_results = process_results(sources_results_list)


#     return sources_results

# def process_results(sources_list):
#     '''
#     Function  that processes the sources result and transform them to a list of Objects

#     Args:
#         sources_list: A list of dictionaries that contain sources details

#     Returns :
#         sources_results: A list of sources objects
#     '''

#     sources_results = []
#     for sources_item in sources_list:
#         id = sources_item.get('id')
#         name = sources_item.get('name')
#         url = sources_item.get('url')
#         category =sources_item.get('category')
#         language = sources_item.get('language')
#         country = sources_item.get('country')
#         description = sources_item.get('description')
#         sources_object = Sources(id,name,url,category,language,country,description)

#         sources_results.append(sources_object)

#     return sources_results




    