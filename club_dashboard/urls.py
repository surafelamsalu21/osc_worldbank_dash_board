

from django.contrib import admin
from django.urls import include, path
from dashboard.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('dashboard.urls')),
    path('', index, name='index'),
]
