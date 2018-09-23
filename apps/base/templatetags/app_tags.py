from django import template
from django.conf import settings

from apps.category.models import Category

register = template.Library()


@register.simple_tag
def shop_name():
    return settings.SHOP_NAME


@register.simple_tag
def page_title(category_slug):
    title = 'Страница товаров'
    if not category_slug:
        return title
    try:
        category = Category.objects.get(slug=category_slug)
        title = category.name
    except Category.DoesNotExist:
        pass
    return title
