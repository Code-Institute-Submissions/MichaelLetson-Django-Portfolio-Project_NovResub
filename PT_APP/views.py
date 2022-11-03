from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views import generic, View
from django.contrib import messages
from .models import Post
from .forms import NewPostForm


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6


@login_required
def delete_post(request, post_id=None):
    if not request.user.is_superuser:
        messages.error(
            request,
            'Sorry, only store owners can do that. Contact us for help!'
            )
        return redirect(('home'))

    Model = Post
    post_to_delete = Model.objects.get(id=post_id)
    post_to_delete.delete()
    messages.success(request, ('Item successfully deleted!'))
    return redirect('home')


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


@login_required
def new_post(request):
    if request.method == "POST":
        form = NewPostForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                ('Successfully added! Return to home page to view it.')
                )
            return render(request, "new_post.html", {"form": form, },)
    else:
        form = NewPostForm
    return render(request, "new_post.html", {"form": form, },)


@login_required
def edit_post(request, post_slug):
    post = Post.objects.get(slug=post_slug)
    form = NewPostForm(instance=post)

    if not request.user.is_superuser:
        messages.error(
            request,
            'Sorry, only store owners can do that. Contact us for help!'
            )
        return redirect(('home'))

    if request.method == "POST":
        form = NewPostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                ('Successfully updated! Return to home page to view it.')
                )
            return render(request, "new_post.html", {"form": form, },)

    context = {'form': form}
    return render(request, 'new_post.html', context)
