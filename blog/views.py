from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.urls import reverse
from django.views import View, generic
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Post, ReadLater, Comment
from .forms import CommentForm


class PostList(generic.ListView):
    '''
    Returns all published posts in :model:`blog.Post`
    and displays them in a page of six posts.

    **Template:**

    :template:`templates/index.html`
    '''
    queryset = Post.objects.filter(author=1)
    template_name = "index.html"
    paginate_by = 6


class PostDetail(View):
    """
    Display an individual post.

    **Template:**

    :template:`templates/post_detail.html`
    """

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.all().order_by("-created_on")
        comment_count = post.comments.filter(approved=True).count()
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
                "comment_count": comment_count,
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
                messages.add_message(
                    request,
                    messages.SUCCESS,
                    'Comment submitted and awaiting approval')
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
     Display an individual comment for edit.


    **Context**

    ``post``
        An instance of :model:`blog.Post`.
    ``comment``
        A single comment related to the post.
    ``comment_form``
        An instance of :form:`blog.CommentForm`
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
            # comment.approved = False
            comment.save()
            messages.success(
                request, 'Comment updated successfully and awaiting approval.')
        else:
            messages.error(
                request, 'Error updating comment. Please check the form.')
    else:
        comment_form = CommentForm(instance=comment)

    return redirect('post_detail', slug=post.slug)


@login_required
def comment_delete(request, slug, comment_id):
    """
    Delete an individual comment.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.
    ``comment``
        A single comment related to the post.
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR,
                             'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))


@login_required
def add_to_read_later(request, post_slug):
    """
    Save to read later a favourite post.
    """
    post = Post.objects.get(slug=post_slug)

    # Check if the post is already in the user's "Read Later" list
    existing_post = ReadLater.objects.filter(user=request.user, post=post)

    if existing_post.exists():
        # If the post is already in "Read Later", remove it
        existing_post
        messages.info(request, "This post is already in your Read Later list.")
    else:
        # If the post is not in "Read Later", add it
        ReadLater.objects.create(user=request.user, post=post)
        messages.success(
            request,
            "This post is successfully added to your Read Later list.")
    # Redirect to the post detail page to refresh the state
    return redirect('post_detail', slug=post.slug)


@login_required
def read_later(request):
    """
    Display list of posts saved for read later.
    """
    if request.user.is_authenticated:
        read_later_posts = ReadLater.objects.filter(user=request.user)
        return render(
            request, "read_later.html", {
                "read_later_posts": read_later_posts})
    else:
        return render(request, "read_later.html", {"read_later_posts": []})


@login_required
def remove_from_read_later(request, post_slug):
    """
    Remove a post from the list in read later page.
    """
    # Fetch the post based on the slug
    post = Post.objects.get(slug=post_slug)

    # Remove the post from the ReadLater list for the user
    ReadLater.objects.filter(user=request.user, post=post).delete()

    # Display a success message
    messages.success(
        request,
        "This post has been removed from your Read Later list.")

    # Redirect back to the Read Later page
    return redirect('read_later')


def post_upvote(request, post_slug):
    """
    Enable the logged-in user to vote for the post.
    """
    post = get_object_or_404(Post, slug=post_slug)
    if request.user.is_authenticated:
        if post.upvotes.filter(id=request.user.id).exists():
            post.upvotes.remove(request.user)  # Remove the upvote if it exists
        else:
            post.upvotes.add(request.user)  # Add the upvote
            post.downvotes.remove(request.user)  # Remove downvote if it exists
    return redirect(reverse("post_detail", kwargs={"slug": post.slug}))


def post_downvote(request, post_slug):
    """
    Enable the logged-in user to vote for the post.
    """
    post = get_object_or_404(Post, slug=post_slug)
    if request.user.is_authenticated:
        if post.downvotes.filter(id=request.user.id).exists():
            # Remove the downvote if it exists
            post.downvotes.remove(request.user)
        else:
            post.downvotes.add(request.user)  # Add the downvote
            post.upvotes.remove(request.user)  # Remove upvote if it exists
    return redirect(reverse("post_detail", kwargs={"slug": post.slug}))
