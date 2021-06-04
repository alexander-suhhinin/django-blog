from datetime import date
from django.shortcuts import render

all_posts = [
    {
        'slug': 'hike-in-the-mountains',
        'image': 'racoon.jpg',
        'author': 'Aleksandr',
        'date': date(2021, 6, 4),
        'title': 'Mountain Hiking',
        'excerpt': 'There is nothing like the views in the mountains! And I wasn\'t even prepared for what happened whilst I was enjoying the view!',
        'content': """Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
 tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
 quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
 consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
 cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non
 proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
"""
    },
    {
        'slug': 'sm1420',
        'image': 'sm1420.jpg',
        'author': 'Aleksandr',
        'date': date(2021, 5, 3),
        'title': 'SM 1420 - my first computer',
        'excerpt': 'There is nothing like the views in the mountains! And I wasn\'t even prepared for what happened whilst I was enjoying the view!',
        'content': """Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
 tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
 quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
 consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
 cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non
 proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
"""
    },
 {
        'slug': 'microsoft-surface',
        'image': 'surface.jpg',
        'author': 'Aleksandr',
        'date': date(2021, 6, 1),
        'title': 'Modern surface',
        'excerpt': 'I would like to try this device. Is it better than ',
        'content': """Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
 tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
 quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
 consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
 cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non
 proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
"""
    }
]

def get_date(post):
    return post['date']

# Create your views here.

def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, 'blog/index.html', {
        'posts': latest_posts
    })

def posts(request):
    return render(request, 'blog/all-posts.html', {
        'all_posts': all_posts
    })

def post_detail(request, slug):
    post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, 'blog/post-detail.html', {
        'post': post
    })
