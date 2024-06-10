from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views import View
from .models import Post, ReadLater
from .forms import CommentForm

class PostList(View):
    def get(self, request, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        return render(request, 'index.html', {'posts': queryset})

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
                "commented": False,
                "upvoted": upvoted,
                "downvoted": downvoted,
                "number_of_upvotes": post.number_of_upvotes(),
                "number_of_downvotes": post.number_of_downvotes(),
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_on')
        upvoted = False
        downvoted = False

        if post.upvotes.filter(id=self.request.user.id).exists():
            upvoted = True
        if post.downvotes.filter(id=self.request.user.id).exists():
            downvoted = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            Comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "upvoted": upvoted,
                "downvoted": downvoted,
                "number_of_upvotes": post.number_of_upvotes(),
                "number_of_downvotes": post.number_of_downvotes(),
                "comment_form": CommentForm()
            },
        )


def read_later(request):
    if request.user.is_authenticated:
        read_later_posts = ReadLater.objects.filter(user=request.user)
        return render(request, 'read_later.html', {'read_later_posts': read_later_posts})
    else:
        return render(request, 'read_later.html', {'read_later_posts': []})

def add_to_read_later(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    ReadLater.objects.get_or_create(user=request.user, post=post)
    return redirect(reverse('post_detail', args=[post.slug]))

def post_upvote(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if post.upvotes.filter(id=request.user.id).exists():
        post.upvotes.remove(request.user)
    else:
        # Ensure user can only upvote or downvote, not both
        post.upvotes.add(request.user)
        post.downvotes.remove(request.user)  
    return redirect(reverse('post_detail', kwargs={'slug': post.slug}))

def post_downvote(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if post.downvotes.filter(id=request.user.id).exists():
        post.downvotes.remove(request.user)
    else:
        # Ensure user can only upvote or downvote, not both
        post.downvotes.add(request.user)
        post.upvotes.remove(request.user)  
    return redirect(reverse('post_detail', kwargs={'slug': post.slug}))
