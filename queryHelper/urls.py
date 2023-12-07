from django.contrib import admin
from django.urls import path, include

from dashboard.views import update_data

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', include('dashboard.urls')),
    path('', include('aplicacao.urls')),
    path('update_data/', update_data, name='update_data'),
]
