from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.template.loader import render_to_string
from . import product_info
from .models import Product, Category

data_m = [
    {"title": "О сайте", "url_name": "about"},
    {"title": "Каталог", "url_name": "categories"},
    {"title": "Войти", "url_name": "login"},

]

def index(request): 

    data = {
        "title": "Главная страница", 
        "menu": data_m,
        "info": Product.active_products.all()
    }
    return render(request, "fullshop/index.html", context=data)

def product(request, product_id):
    
    product = get_object_or_404(Product, active=1, pk=product_id) 

    prod = { 
        "title": product.title, 
        "menu": data_m,
        "info": product
    }
    
    return render(request, "fullshop/product.html", prod)


def login(request):
    return HttpResponse(f"<h1>Страница входа</h1>")

def about(request):
    return render(request, "fullshop/about.html", {'title': "О сайте", "menu": data_m})

def show_categories(request, cate_slug): #HttpRequest
    category = get_object_or_404(Category, slug=cate_slug)
    product_from_catrgory = Product.objects.filter(cate_id=category.pk)

    category_info = { 
        "title": category.title, 
        "menu": data_m,
        "info": product_from_catrgory
    }
    
    return render(request, "fullshop/category.html", category_info)

def categories(request): #HttpRequest
    all_categories = Category.objects.all()
    

    category_info = { 
        "title": "Категории", 
        "menu": data_m,
        "info": all_categories
    }
    
    return render(request, "fullshop/index.html", category_info)

def page_not_found(request, exception): #HttpRequest
    return HttpResponseNotFound(f"<h1>УПС..</h1><p>Что то пошло не так, ошибочка :\</p>")


