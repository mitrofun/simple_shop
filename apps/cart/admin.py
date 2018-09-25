from django.contrib import admin
from django.contrib.sessions.models import Session
from django.utils.safestring import mark_safe

from apps.category.models import Product


@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):

    def show_data_admin(self, obj):
        data = obj.get_decoded()

        if 'cart' in data:
            result = ''
            for key, values in data['cart'].items():
                prodict = Product.objects.get(pk=key)
                result += f'<p><strong>{prodict.name}</strong> ' \
                          f'по цене {values["price"]} руб.' \
                          f'кол-во: {values["quantity"]} шт.</p>'
            return mark_safe(f'<div>{result}</div>')
        return ''

    show_data_admin.short_description = 'Корзина'
    show_data_admin.allow_tags = True

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False

    list_display = ['session_key', 'show_data_admin', 'expire_date', ]
