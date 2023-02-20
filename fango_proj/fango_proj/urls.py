from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('concerto3000/', include('concerto3000.urls')),
    path('admin/', admin.site.urls),
] 