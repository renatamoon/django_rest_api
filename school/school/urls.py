# STANDARD IMPORTS
from django.contrib import admin
from django.urls import path, include

# PROJECT IMPORTS
from school.courses.urls import router


urlpatterns = [
    path('api/v1/', include('courses.urls')),  # also indicating the version of the project
    path('api/v2', include(router.urls)),  # just instantiating the router here
    path('admin/', admin.site.urls),
    path('auth/', include('rest_framework.urls'))
]
