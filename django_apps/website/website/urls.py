from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('forecast/', include('forecast.urls')),
    path('accounts/', include('django.contrib.auth.urls')), # Include Django's auth URLs
    path('', RedirectView.as_view(url='/forecast/')), # Redirects to the index view of your forecast app
]
