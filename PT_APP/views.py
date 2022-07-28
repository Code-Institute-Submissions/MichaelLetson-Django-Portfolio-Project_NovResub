from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Post


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 5


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        post = get_object_or_404(slug=slug)
        
        return render(
            request,
            "post_detail.html",
            {
                "post": post,
            },
        )