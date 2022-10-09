from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from . import views


def trigger_error(request):
    division_by_zero = 1 / 0
    return division_by_zero


admin.site.site_header = 'Orange County Lettings'
admin.site.site_title = "Orange County Lettings"
admin.site.index_title = "Orange County Lettings Administration"

urlpatterns = [
    path('', views.index, name='index'),
    path('lettings/', include('lettings.urls')),
    path('profiles/', include('profiles.urls')),
    path('admin/', admin.site.urls),
    path('sentry/', trigger_error),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
