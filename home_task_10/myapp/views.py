from django.shortcuts import render
import requests
import random



# Create your views here.



def owl_carousel(requests):
    return render(requests, 'owlcarousel.html')





def news_function(request):
    news_url = 'https://newsapi.org/v2/top-headlines?sources=le-monde&apiKey=92abc5bc54b942a2902d288433122a9b'

    r = requests.get(news_url)

    total_news = r.json()['totalResults']

    news_number = random.randrange(0,total_news)

    title = r.json()['articles'][news_number]['title']
    author = r.json()['articles'][news_number]['author']
    content = r.json()['articles'][news_number]['content']
    image = r.json()['articles'][news_number]['urlToImage']
    published = r.json()['articles'][news_number]['publishedAt']

    context = {
        'title': title,
        'author': author,
        'content': content,
        'image': image,
        'published': published,
    }

    return render(request, 'news.html', context)


























