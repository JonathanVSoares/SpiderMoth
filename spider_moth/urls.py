from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('cobweb/', include('cobweb.urls')),
    path('admin/', admin.site.urls),
]