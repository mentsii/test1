from django.urls import path, re_path, register_converter
from . import views
from . import converters

register_converter(converters.TwoConverorNumbers, 'numbers2')



urlpatterns = [
    path('', views.index, name='home'),
    path('categories/', views.categories, name="categories"),
    path('categories/<slug:cate_slug>/', views.show_category, name="category"), 
    path('about/', views.about, name="about"),
    path('product/<int:product_id>/', views.product, name="product"),
    path('special/<slug:tag_slug>/', views.show_special_tag, name="special_tag"),
    path('login/', views.login, name="login")
]