from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Post
from .forms import NewPostForm


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        return render(
            request,
            "post_detail.html",
            {
                "post": post,
            },
        )

def new_post(request):
    if request.method == 'GET':
        return render(request, "new_post.html")

    if request.method == 'POST':
        form = NewPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index.html")
    form = NewPostForm()
    context = {
        'form': form
    }
    return render(request, "new_post.html", context)