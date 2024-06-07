from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
 
# Create your models here.
STATUS = ((0, "Draft"), (1, "Published"))

class Post(models.Model):
    title = models.CharField(max_lenth=200, unique=True)
    slug = models.SlugField(max_lenth=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    upvotes = models.ManyToManyField(User, related_name='blogpost_upvote', blank=True)
    downvotes = models.ManyToManyField(User, related_name='blogpost_downvote', blank=True)
    favorites = models.ManyToManyField(User, related_name='blogpost_favorite', blank=True)
    read_later = models.ManyToManyField(User, related_name='blogpost_read_later', blank=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

    def number_of_upvotes(self):
        return self.upvotes.count()

    def number_of_downvotes(self):
        return self.downvotes.count()

    def number_of_favorites(self):
        return self.favorites.count()

    def number_of_read_later(self):
        return self.read_later.count()

# Comment Models

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"
