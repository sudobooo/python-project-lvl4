from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='main'),
    path('users/', include('task_manager.users.urls'), name='list_of_users'),
    path('admin/', admin.site.urls),
]