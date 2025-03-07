from django import template
from fullshop.models import Tags

register = template.Library()


@register.inclusion_tag('fullshop/list_tags.html')
def show_tags():
    tags = Tags.objects.all()
    return {"tags": tags}