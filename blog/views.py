from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.urls import reverse
from django.views import View, generic
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import Post, ReadLater, Comment
from .forms import CommentForm

#def home(request):
#    return render(request, 'blog/home.html')  # Render the home template in the blog app

#class PostList(View):
#    def get(self, request, *args, **kwargs):
#       queryset = Post.objects.filter(status=1)
#      return render(request, "index.html", {"posts": queryset})
class PostList(generic.ListView):
    queryset = Post.objects.filter(author=1)
    template_name = "index.html"
    paginate_by = 6


class PostDetail(View):
    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("created_on")
        comment_form = CommentForm()
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
                "comment_form": comment_form,
                
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("created_on")
        upvoted = False
        downvoted = False

        if post.upvotes.filter(id=self.request.user.id).exists():
            upvoted = True
        if post.downvotes.filter(id=self.request.user.id).exists():
            downvoted = True

        if request.method == "POST":
            print("Received a POST request")
            comment_form = CommentForm(data=request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.author = request.user
                comment.post = post
                comment.save()
                messages.add_message(
                    request, messages.SUCCESS,
                    'Comment submitted and awaiting approval'
                )
            comment_form = CommentForm(data=request.POST)
            print("About to render template")
                #return redirect('post_detail', slug=post.slug)
            #else:
                #messages.error(request, 'There was an error submitting your comment.')

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
                "comment_form": comment_form,
            },
        )

def comment_edit(request, slug, comment_id):
    """
    view to edit comments
    """
    if request.method == "POST":

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating comment!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))

def comment_delete(request, slug, comment_id):
    """
    view to delete comment
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))

def read_later(request):
    if request.user.is_authenticated:
        read_later_posts = ReadLater.objects.filter(user=request.user)
        return render(
            request, "read_later.html", {"read_later_posts": read_later_posts}
        )
    else:
        return render(request, "read_later.html", {"read_later_posts": []})


def add_to_read_later(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    ReadLater.objects.get_or_create(user=request.user, post=post)
    return redirect(reverse("post_detail", args=[post.slug]))


def post_upvote(request, post_slug):
    post = get_object_or_404(Post, id=post_id)
    if post.upvotes.filter(id=request.user.id).exists():
        post.upvotes.remove(request.user)
    else:
        # Ensure user can only upvote or downvote, not both
        post.upvotes.add(request.user)
        post.downvotes.remove(request.user)
    return redirect(reverse("post_detail", kwargs={"slug": post.slug}))


def post_downvote(request, post_slug):
    post = get_object_or_404(Post, slug=post_slug)
    if post.downvotes.filter(id=request.user.id).exists():
        post.downvotes.remove(request.user)
    else:
        # Ensure user can only upvote or downvote, not both
        post.downvotes.add(request.user)
        post.upvotes.remove(request.user)
    return redirect(reverse("post_detail", kwargs={"slug": post.slug}))
