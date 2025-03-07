from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.template.loader import render_to_string
from .models import Product, Category, Tags



def index(request): 

    data = {
        "title": "Mentsi", 
        "info": Product.active_products.all()
    }
    return render(request, "fullshop/index.html", context=data)

def product(request, product_id):
    
    product = get_object_or_404(Product, active=1, pk=product_id) 

    prod = { 
        "title": product.title, 
        "info": product
    }
    
    return render(request, "fullshop/product.html", prod)


def login(request):
    return HttpResponse(f"<h1>Страница входа</h1>")

def about(request):
    return render(request, "fullshop/about.html", {'title': "О сайте"})

def show_category(request, cate_slug): #HttpRequest
    category = get_object_or_404(Category, slug=cate_slug)
    product_from_catrgory = Product.objects.filter(cate_id=category.pk)

    category_info = { 
        "title": category.title, 
        "info": product_from_catrgory
    }
    
    return render(request, "fullshop/index.html", category_info)

def categories(request): #HttpRequest
    all_categories = Category.objects.all()
    

    category_info = { 
        "title": "Категории", 
        "info": all_categories
    }
    
    return render(request, "fullshop/categories.html", category_info)

def show_special_tag(request, tag_slug):
    tag = get_object_or_404(Tags, slug=tag_slug)
    products = tag.tags.filter(active=Product.Status.Active)

    result_table = {
        "title":tag.tag, 
        "info": products
        }
    
    return render(request, "fullshop/index.html", result_table)

def page_not_found(request, exception): #HttpRequest
    return HttpResponseNotFound(f"<h1>УПС..</h1><p>Что то пошло не так, ошибочка :\</p>")


