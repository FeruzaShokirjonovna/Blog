from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import (
    PostList,
    PostDetail,
    read_later,
    add_to_read_later,
    post_upvote,
    post_downvote,
)
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", PostList.as_view(), name="home"),  # Root URL pattern
    path(
        "<slug:slug>/", PostDetail.as_view(), name="post_detail"
    ),  # Post Detail
    path(
        "read_later/", read_later, name="read_later"
    ),  # Read Later URL pattern
    # Add to Read Later URL pattern
    path(
        "add_to_read_later/<int:post_id>/",
        add_to_read_later,
        name="add_to_read_later",
    ),
    path(
        "post/<int:post_id>/upvote/", post_upvote, name="post_upvote"
    ),  # Post upvote URL pattern
    path(
        "post/<int:post_id>/downvote/", post_downvote, name="post_downvote"
    ),  # Post downvote URL pattern
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)