from flask import render_template,request,redirect,url_for
from app import app
from .request import get_news, get_everything,get_sources,search_sources,get_articles


# Views
@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    general = get_sources('general')
    sports = get_sources('sports')
    technology = get_sources('technology')
    entertainment = get_sources('entertainment')
    health = get_sources('health')
    science =get_sources('science')
    business = get_sources('business')
    search_sources = request.args.get('sources_query')

    if search_sources:
        return redirect(url_for('search',sources_name=search_sources))
    title = 'NEWS UPDATE'
    heading = 'CHECK MISSED UPDATES'
    return render_template('index.html', title=title, heading=heading,general=general,technology=technology,sports=sports,entertainment=entertainment,health=health,business=business,science=science)


@app.route('/headlines.html')
def headlines():
    '''
    View root page function that returns the headlines page and its data
    '''
    general = get_news('general')
    sports = get_news('sports')
    technology = get_news('technology')
    entertainment = get_news('entertainment')
    health = get_news('health')
    science =get_news('science')
    business = get_news('business')

    return render_template('headlines.html',general=general,technology=technology,sports=sports,entertainment=entertainment,health=health,business=business,science=science)



# @app.route('/search/<sources_name>')
# def search(sources_name):
#     '''
#     View function to display the search results
#     '''
#     sources_name_list = sources_name.split(" ")
#     sources_name_format = "+".join(sources_name_list)
#     searched_sources = search_sources(sources_name_format)
#     title = f'search results for '{sources_name}
#     return render_template('search.html',sources = searched_sources)



@app.route('/article.html')
def articles():

    top_articles = get_articles()
    print(top_articles)
    return render_template('article.html',get_articles =top_articles)


