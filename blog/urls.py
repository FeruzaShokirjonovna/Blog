from . import views import home, read_later
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'), # Root URL pattern
    path('read_later/', read_later, name='read_later'),  # Read Later URL pattern
    path('add_to_read_later/<int:post_id>/', add_to_read_later, name='add_to_read_later'),  # Add to Read Later URL pattern
]