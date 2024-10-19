from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
STATUS = ((0, "Draft"), (1, "Published"))


# Post Model
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    featured_image = CloudinaryField("image", default="placeholder")
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    excerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    upvotes = models.ManyToManyField(
        User, related_name="blogpost_upvote", blank=True
    )
    downvotes = models.ManyToManyField(
        User, related_name="blogpost_downvote", blank=True
    )
    read_later = models.ManyToManyField(
        User, related_name="blogpost_read_later", blank=True
    )

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title
        
    def number_of_upvotes(self):
        return self.upvotes.count()

    def number_of_downvotes(self):
        return self.downvotes.count()


# Comment Models


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments"
    )
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"


# Upvote/downvote


class Vote(models.Model):
    UPVOTE = 1
    DOWNVOTE = -1

    VOTE_CHOICES = [
        (UPVOTE, "Upvote"),
        (DOWNVOTE, "Downvote"),
    ]

    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="votes"
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vote = models.IntegerField(choices=VOTE_CHOICES)

    class Meta:
        unique_together = ("post", "user")


# Read Later Model


class ReadLater(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    added_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "post")

    def __str__(self):
        return f"{self.user.username} - {self.post.title}"
