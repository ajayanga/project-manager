from django.urls import path
from . import views

urlpatterns = [
    path('projects', views.projectList, name='projects'),
    path('projects/<int:pk>', views.projectDetail, name='project_detail'),
]

from django.conf import settings
from django.conf.urls.static import static
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)