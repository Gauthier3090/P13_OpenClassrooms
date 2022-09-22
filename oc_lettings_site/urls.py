from django.contrib import admin
from django.urls import path, include
from . import views

admin.site.site_header = 'Orange County Lettings'
admin.site.site_title = "Orange County Lettings"
admin.site.index_title = "Orange County Lettings Administration"

urlpatterns = [
    path('', views.index, name='index'),
    path('lettings/', include('lettings.urls')),
    path('profiles/', include('profiles.urls')),
    path('admin/', admin.site.urls),
]
