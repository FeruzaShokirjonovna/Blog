from django.shortcuts import render
from django.views import generic
from .models import Post, ReadLater


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 5
    
def read_later(request):
    if request.user.is_authenticated:
        read_later_posts = ReadLater.objects.filter(user=request.user)
        return render(request, 'read_later.html', {'read_later_posts': read_later_posts})
    else:
        return render(request, 'read_later.html', {'read_later_posts': []})