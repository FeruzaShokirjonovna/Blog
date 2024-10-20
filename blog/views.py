from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.urls import reverse
from django.views import View, generic
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
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
            
            comment_form = CommentForm(data=request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.author = request.user
                comment.post = post
                comment.save()
                messages.add_message(request, messages.SUCCESS,'Comment submitted and awaiting approval')
            else:
                print(comment_form.errors)  # Log the validation errors
                return redirect('post_detail', slug=post.slug)

        comment_form = CommentForm
            
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
    post = get_object_or_404(Post, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author != request.user:
        messages.error(request, "You can only edit your own comments.")
        return redirect('post_detail', slug=post.slug)

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST, instance=comment)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.approved = False
            comment.save()
            messages.success(request, 'Comment updated successfully and awaiting approval.')
        else:
            messages.error(request, 'Error updating comment. Please check the form.')
    else:
        comment_form = CommentForm(instance=comment)

    return redirect('post_detail', slug=post.slug)

@login_required
def comment_delete(request, slug, comment_id):
    post = get_object_or_404(Post, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.user != request.user:
        messages.error(request, "You can only delete your own comments.")
    elif request.method == "POST":
        comment.delete()
        messages.success(request, 'Comment deleted successfully.')
    else:
        messages.error(request, 'Invalid request method for comment deletion.')

    return redirect('post_detail', slug=post.slug)


@login_required
def add_to_read_later(request, post_slug):
    post = get_object_or_404(Post, slug=post_slug)
    read_later_entry, created = ReadLater.objects.get_or_create(user=request.user, post=post)
    
    if created:
        # The post was added to read later
        message = "Post added to your 'Read Later' list!"
    else:
        # The post is already in the user's read later list
        message = "Post is already in your 'Read Later' list."
    
    # Redirect to post detail after adding
    return redirect(reverse("post_detail", args=[post.slug]))

@login_required
def read_later(request):
    if request.user.is_authenticated:
        read_later_posts = ReadLater.objects.filter(user=request.user)
        return render(request, "read_later.html", {"read_later_posts": read_later_posts})
    else:
        return render(request, "read_later.html", {"read_later_posts": []})
        
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
