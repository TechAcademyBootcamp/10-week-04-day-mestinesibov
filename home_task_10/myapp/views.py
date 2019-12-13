from django.shortcuts import render
# from newsapi import NewsApiClient
# import random

# Create your views here.
def owl_carousel(requests):
    return render(requests, 'owlcarousel.html')


# newsapi = NewsApiClient(api_key='92abc5bc54b942a2902d288433122a9b')
# newsapi = NewsApiClient(api_key='92abc5bc54b942a2902d288433122a9b')
# all_articles = newsapi.get_everything(q='bitcoin',
#                                     sources='bbc-news,the-verge',
#                                     domains='bbc.co.uk,techcrunch.com',
#                                     from_param='2019-12-12',
#                                     to='2019-12-13',
#                                     language='en',
#                                     sort_by='relevancy',
#                                     page=2)
# def news_function(requests):
    
#     random_article=random.choice(sources["sources"])
#     print(random_article)
#     return render(requests,"news.html",{"article":random_article})



