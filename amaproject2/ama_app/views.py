from django.shortcuts import render, get_object_or_404
from .models import *

cats = Category.objects.all()
auts = Author.objects.all()
regions = Region.objects.all()
# Create your views here.
def index(request):
    return render(request, 'ama_app/index.html', {'title': 'Главная', 'cats': cats, 'authors': auts, 'regions': regions})

def about(request):
    return render(request, 'ama_app/about.html', {'title': 'О сайте', 'cats': cats, 'authors': auts, 'regions': regions})


def contacts(request):
    return render(request, 'ama_app/contacts.html', {'title': 'Контакты', 'cats': cats, 'authors': auts, 'regions': regions})


def show_by_category(request, cat_id):
    catt = get_object_or_404(Category, pk=cat_id)

    arts = Text.objects.filter(cat=catt)

    auts = Author.objects.all()
    regions = Region.objects.all()

    param_list = {
        'cats': Category.objects.all(),
        'catt': catt,
        'title': catt.cat,
        'cat_selected': catt.pk,
        'articles': arts,
        'authors': auts,
        'regions': regions
    }

    return render(request, 'ama_app/categs.html', context=param_list)



def show_by_author(request, name_id):
    author = get_object_or_404(Author, pk=name_id)

    arts = Text.objects.filter(author=author)

    param_list = {
        'cats': Category.objects.all(),
        'aut': author,

        'author_selected': author.pk,
        'articles': arts,
        'authors': auts,
        'regions': regions
    }

    return render(request, 'ama_app/author.html', context=param_list)


def show_by_region(request, name_id):
    region = get_object_or_404(Region, pk=name_id)

    arts = Text.objects.filter(region=region)

    param_list = {
        'cats': Category.objects.all(),
        'reg': region,

        'region_selected': region.pk,
        'articles': arts,
        'authors': auts,
        'regions': regions
    }

    return render(request, 'ama_app/regions.html', context=param_list)


def text(request, text_id):

    text = get_object_or_404(Text, pk=text_id)
    cats = Category.objects.all()

    param_list = {
        'text': text,
        'title': text.title,
        'cats': cats,
        'authors': auts,
        'regions': regions

    }
    return render(request, 'ama_app/self_text.html', context=param_list)


def wrighting(request):
    texts = Text.objects.all()
    texts2 = Texts.object.filter(cat == 'Сказки')


    return render(request, 'ama_app/now_wrighting.html',
                  {'title': 'В процессе', 'cats': cats, 'authors': auts, 'regions': regions, 'texts2': texts2})