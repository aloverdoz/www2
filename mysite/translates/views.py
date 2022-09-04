from django.shortcuts import render, get_object_or_404

from .models import Translates, Category

def index(request):
    translates = Translates.objects.all()
    categories = Category.objects.all()
    context = {
        'translates': translates,
        'title': 'Aloverdoz',
        'categories': categories,
    }
    return render(request, 'translates/index.html', context)


def get_category(request, category_id):
    translates = Translates.objects.filter(category_id=category_id)
    categories = Category.objects.all()
    category = Category.objects.get(pk=category_id)
    context = {
        'translates': translates,
        'categories': categories,
        'category': category,
    }
    return render(request, 'translates/category.html', context)


def view_translates(request, translates_id):
    #translates_item = Translates.objects.get(pk=translates_id)
    translates_item = get_object_or_404(Translates, pk=translates_id)
    context = {
        'translates_item': translates_item,
    }
    return render(request, 'translates/view_translates.html', context)