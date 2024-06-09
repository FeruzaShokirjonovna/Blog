from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'), # Root URL pattern
    path('read_later/', read_later, name='read_later'),  # Read Later URL pattern
]