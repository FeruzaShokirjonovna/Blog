from django.shortcuts import render
from django.views import generic
from .models import Post


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 5
    
def favourites(request):
    # Logic to get the favourite posts for the user
    return render(request, 'favourites.html')

def read_later(request):
    # Logic to get the posts bookmarked for later read
    return render(request, 'read_later.html')