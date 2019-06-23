from django.shortcuts import render
# from django.http import HttpResponse

posts = [
    {
        'title': 'A title',
        'author': 'Frank',
        'content': 'Here is some content',
        'date_posted': 'August 29, 2029'
    },
    {
        'title': 'A title2',
        'author': 'George',
        'content': 'Here is some content2',
        'date_posted': 'August 29, 3333'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'A Title'})

