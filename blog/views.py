# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import Post


# this will list all of the posts/articles 
def blog_list(request):
    posts_from_db = Post.objects.all()  # fetching all posts from database
    return render(request, 'blog/blog_list_page.html', {"posts_from_db" : posts_from_db })


def blog_detail(request, post_id):
    # This will pull the object from the db with the id 
    single_post_from_db = get_object_or_404(Post, id=post_id)

    return render(request, 'blog/blog_detail_page.html', { "single_post_from_db" : single_post_from_db})