from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from apps.base import views

handler400 = 'core.views.bad_request'
handler404 = 'core.views.page_not_found'
handler500 = 'core.views.server_error'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('apps.category.urls', 'apps.category'), namespace='category')),
    path('cart/', include(('apps.cart.urls', 'apps.cart'), namespace='cart')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    urlpatterns += [
        path('400', views.bad_request, {'exception': 'test'}),
        path('404', views.page_not_found, {'exception': 'test'}),
        path('500', views.server_error),
    ]

    import debug_toolbar
    urlpatterns += [
        path(r'__debug__/', include(debug_toolbar.urls)),
    ]
