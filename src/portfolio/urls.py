from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('projects/', include('projects.urls')),
    path('', include('projects.urls', namespace='projects')),
    path('admin/', admin.site.urls),
]
