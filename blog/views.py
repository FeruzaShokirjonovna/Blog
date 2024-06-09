from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Post, ReadLater
from django.http import HttpResponseRedirect
from django.urls import reverse


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 5

 class PostDetail(View):
    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_on')
        upvoted = False
        downvoted = False
        if post.upvotes.filter(id=self.request.user.id).exists():
            upvoted = True
        if post.downvotes.filter(id=self.request.user.id).exists():
            downvoted = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "upvoted": upvoted,
                "downvoted": downvoted
            }
        )

def read_later(request):
    # Enables logged in users to bookmark the page
    if request.user.is_authenticated:
        read_later_posts = ReadLater.objects.filter(user=request.user)
        return render(request, 'read_later.html', {'read_later_posts': read_later_posts})
    else:
        return render(request, 'read_later.html', {'read_later_posts': []})

def add_to_read_later(request, post_id):
    # Adds functionality to bookmark Posts
    post = get_object_or_404(Post, id=post_id)
    ReadLater.objects.get_or_create(user=request.user, post=post)
    return HttpResponseRedirect(reverse('post_detail', args=[post.slug]))