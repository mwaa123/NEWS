# from flask import render_template
# from app import app
# from .request import get_news, get_everything,get_sources


# # Views
# @app.route('/')
# def index():
#     '''
#     View root page function that returns the index page and its data
#     '''
#     general = get_sources('general')
#     sports = get_sources('sports')
#     technology = get_sources('technology')
#     entertainment = get_sources('entertainment')
#     health = get_sources('health')
#     science =get_sources('science')
#     business = get_sources('business')
#     # import pdb; pdb.set_trace()
#     title = 'NEWS UPDATE'
#     heading = 'CHECK MISSED UPDATES'
#     return render_template('index.html', title=title, heading=heading,general=general,technology=technology,sports=sports,entertainment=entertainment,health=health,business=business,science=science)


# @app.route('/headlines.html')
# def headlines():
#     '''
#     View root page function that returns the headlines page and its data
#     '''
#     general = get_news('general')
#     sports = get_news('sports')
#     technology = get_news('technology')
#     entertainment = get_news('entertainment')
#     health = get_news('health')
#     science =get_news('science')
#     business = get_news('business')

#     return render_template('headlines.html',general=general,technology=technology,sports=sports,entertainment=entertainment,health=health,business=business,science=science)



