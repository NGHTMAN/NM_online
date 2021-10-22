from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls, name='admin_panel'),
    path('polls/', include('polls.urls')),
    path('blog/', include('blog.urls')),
    path('', include('home.urls')),
]
