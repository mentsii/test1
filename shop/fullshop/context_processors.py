def menu_processor(request):
    return {
        'menu': [
            {"title": "Каталог", "url_name": "categories", "class": "burger", "icon": None},
            {"title": "Mentsi", "url_name": "home", "class": "site-title", "icon": None},
            {"title": "Войти", "url_name": "login", "class": "login", "icon": None},
        ]
    }