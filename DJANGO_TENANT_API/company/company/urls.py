# STANDARD IMPORTS
from django.contrib import admin
from django.urls import path

# PROJECT IMPORTS
from DJANGO_TENANT_API.company.tenant.views import our_team

urlpatterns = [
    path('our_team', our_team, name='our_team'),
    path('admin/', admin.site.urls),
]
