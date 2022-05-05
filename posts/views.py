from datetime import datetime

from django.shortcuts import render
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

posts = [
    {
        'title': 'Sayayin1',
        'user': {
            'name': 'Goku fase 4',
            'picture': 'https://static.wikia.nocookie.net/dragonball/images/6/62/Goku_SS4_Artwork.png/revision/latest?cb=20170201223848&path-prefix=es'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://i.imgur.com/983bCDo.png'

    },
    {
        'title': 'Sayayin2',
        'user': {
            'name': 'Vegeta fase 4',
            'picture': 'https://static.wikia.nocookie.net/dragonball/images/e/ea/Vegeta_SS4_Artwork_2.png/revision/latest?cb=20170201224221&path-prefix=es'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://i.imgur.com/TEdPDL2.png'

    },
]

@login_required
def show_all_views(request):
    # content= []
    # for post in posts:
    #     content.append("""
    #     <p><strong>{name}</strong></p>
    #     <p><small>{user}- <i>{timestamp}</i></small></p>
    #     <figure><img src="{picture}"></figure>
    #     """.format(**post))
    # return HttpResponse('</br>'.join(content))
    return render(request, 'posts/feed.html', {'posts': posts})


@login_required
def log_out(request):
    logout(request)
    print("log out was done perfectly")
    return render(request, 'users/login.html')
