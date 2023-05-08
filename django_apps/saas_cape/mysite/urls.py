from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('forecast/', include('forecast.urls')),
    path('accounts/', include('pegasus.urls'))
]
