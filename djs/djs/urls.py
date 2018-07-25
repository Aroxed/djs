from django.contrib import admin
from django.urls import include, path

urlpatterns = [
  path('djapp1/', include('djapp1.urls')),
  path('djapp2/', include('djapp2.urls')),
  path('admin/', admin.site.urls),
]
