from django.shortcuts import render

posts = [
    {
        'author': 'David Bwalya',
        'title': 'My first post',
        'content': 'This is the first post on Whats on Zambia',
        'date_posted': '15 August, 2022'
    },
    {
        'author': 'Teddy Mulubwa',
        'title': 'My second post',
        'content': 'This is the second post on Whats on Zambia',
        'date_posted': '16 August, 2022'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'whatsonzambia/home.html', context)

def about(request):
    return render(request, 'whatsonzambia/about.html', {'title': 'About'})
