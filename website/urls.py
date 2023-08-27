from django.contrib import admin
from django.urls import include, path
from forecast import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('forecast/', include('forecast.urls')),
    path('', include('allauth.urls')),
    path('', include('user.urls')),
    path('', views.index)
]
