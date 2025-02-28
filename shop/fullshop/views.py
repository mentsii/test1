from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from django.urls import reverse
from django.template.loader import render_to_string
from . import product_info

dt = product_info.dt


data_m = [
    {"title": "О сайте", "url_name": "about"},
    {"title": "Каталог", "url_name": "categories"},
    {"title": "Войти", "url_name": "login"},

]

def index(request): 

    data = {
        "title": "Главная страница", 
        "menu": data_m,
        "info": dt
    }
    return render(request, "fullshop/index.html", context=data)

def product(request, product_id):

    product = {}
    for products in dt:
        if products["id"] == product_id:
            product["info"] = products
            product["menu"] = data_m
            break

    if not product:
        raise Http404()
    return render(request, "fullshop/product.html", product)

def login(request):
    return HttpResponse(f"<h1>Страница входа</h1>")

def about(request):
    return render(request, "fullshop/about.html", {'title': "О сайте", "menu": data_m})

def categories(request): #HttpRequest
    return HttpResponse(f"<h1>Страница приложения c категориями</h1>")


def page_not_found(request, exception): #HttpRequest
    return HttpResponseNotFound(f"<h1>УПС..</h1><p>Что то пошло не так, ошибочка :\</p>")


