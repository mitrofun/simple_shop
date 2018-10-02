from django import template
from apps.category.models import Category

register = template.Library()


@register.inclusion_tag('category/sidebar/_categories.html')
def menu_categories(active_category_name):
    return {
        'categories': Category.objects.all().values('name', 'slug'),
        'active_category': active_category_name
    }
