from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    # Rota principal (Catálogo / Dashboard)
    path('admin/', admin.site.urls),
    path('', include('catalogacao.urls')),
]