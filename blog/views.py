from datetime import date
from django.shortcuts import render

# Data muestra momentanea luego vendra de una Bases de Datos

all_posts = [
    {
        'slug': 'holbox-street-art',
        'image': 'https://images.unsplash.com/photo-1581610439579-626c987508de?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80',
        'autor': 'Falso personaje',
        'autorImage': 'https://images.unsplash.com/photo-1542326529804-0cd9d861ebaa?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=675&q=80',
        'date': date(2021, 6, 27),
        'title': 'Holbox Street Art ',
        'excerpt': 'Lorem ipsum, dolor sit amet consectetur adipisicing elit.',
        'content': 'Assumenda minus quae adipisci earum numquam. Quo nam, recusandae molestiae commodi consequuntur voluptates, excepturi molestias sint vero, nostrum quis corporis optio deserunt tenetur itaque voluptatum alias adipisci quae. Totam, voluptatem ad, quos obcaecati quod quae fugiat, incidunt optio eaque rem omnis nemo!',
    },
    {
        'slug': 'recordando-la-fecha',
        'image': 'https://source.unsplash.com/random/780x400',
        'autor': 'EL magnanimo AmbushinMid ',
        'autorImage': 'https://images.unsplash.com/photo-1617296539691-67feaadf389e?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=624&q=80',
        'date': date(2021, 7, 23),
        'title': 'Un día de dolor ',
        'excerpt': 'Quo nam, recusandae molestiae commodi consequuntur voluptates.',
        'content': 'Assumenda minus quae adipisci earum numquam. Quo nam, recusandae molestiae commodi consequuntur voluptates, excepturi molestias sint vero, nostrum quis corporis optio deserunt tenetur itaque voluptatum alias adipisci quae. Totam, voluptatem ad, quos obcaecati quod quae fugiat, incidunt optio eaque rem omnis nemo!',
    },
    {
        'slug': 'dia-de-muertos',
        'image': 'https://images.unsplash.com/photo-1620074506951-33a51f7f454a?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1050&q=80',
        'autor': 'Jr AmbushinMid de Mitgard ',
        'autorImage': 'https://images.unsplash.com/photo-1617296539691-67feaadf389e?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=624&q=80',
        'date': date(2021, 10, 2),
        'title': 'Dia de Muertos ',
        'excerpt': 'Una festividad Mexicana exportada para todo el mundo',
        'content': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Voluptas commodi quod cumque explicabo ducimus officia error a facilis voluptate. Nisi. hic inventore laudantium? Assumenda minus quae adipisci earum numquam. Quo nam, recusandae molestiae commodi consequuntur voluptates, excepturi molestias sint vero, nostrum quis corporis optio deserunt tenetur itaque voluptatum alias adipisci quae. Totam, voluptatem ad, quos obcaecati quod quae fugiat, incidunt optio eaque rem omnis nemo!',
    }

]

# Create your views here.

# helper


def get_date(post):
    return post['date']


def starting_page(request):

    sorted_post = sorted(all_posts, key=get_date)
    latest_post = sorted_post[-1:]
    print(latest_post)
    return render(request, 'blog/index.html', {
        'latest_posts': latest_post
    })


def posts(request):
    return render(request, 'blog/all_posts.html', {
        'todos_los_posts': all_posts
    })


def post_details(request, slug):
    identified_post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, 'blog/post-details.html', {
        'post': identified_post
    })
