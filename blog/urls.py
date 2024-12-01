from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views
from .views import (
    PostList,
    PostDetail,
    read_later,
    add_to_read_later,
    remove_from_read_later,
    post_upvote,
    post_downvote,
)
from django.contrib.auth import views as auth_views

urlpatterns = [
    
    path("", views.PostList.as_view(), name='home'),
    # URL to view saved "Read Later" posts
    path('read_later/', views.read_later, name='read_later'),
    path('remove_from_read_later/<slug:post_slug>/', views.remove_from_read_later, name='remove_from_read_later'),
        # URL to add posts to "Read Later"
    path('add_to_read_later/<slug:post_slug>/', views.add_to_read_later, name='add_to_read_later'),
    path(
        "<slug:slug>/", views.PostDetail.as_view(), name="post_detail"
    ),  # Post Detail

    # Post upvote URL pattern
    path("post/<slug:post_slug>/upvote/", views.post_upvote, name="post_upvote"), 
    # Post downvote URL pattern
    path("post/<slug:post_slug>/downvote/", views.post_downvote, name="post_downvote"), 
    path('<slug:slug>/edit_comment/<int:comment_id>', views.comment_edit, name='comment_edit'),
    path('<slug:slug>/delete_comment/<int:comment_id>', views.comment_delete, name='comment_delete'),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path('accounts/', include('django.contrib.auth.urls')),  
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)