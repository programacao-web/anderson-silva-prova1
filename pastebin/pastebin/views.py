from django.shortcuts import render, get_object_or_404


def index(request):

    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            # post.author = request.user
            post.save()
            return redirect('paste', id=post.id)
        else:
            form = PostForm()

        # return render(request, 'blog/post_edit.html', {'form': form})
        # return render(request, 'pastebin/index.jinja2', ctx)
        return render(request, 'pastebin/index.jinja2', {'form': form})

# def post_list(request):
#     posts = Post.objects.filter(publish_date__lte=timezone.now()).order_by('publish_date')
#     return render(request, 'blog/post_list.html', {'posts': posts})


# def post_detail(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     return render(request, 'blog/post_detail.html', {'post': post})

def paste(request, id):
    ctx = get_object_or_404(Post, pk=pk)
    return render(request, 'pastebin/paste-detail.jinja2', ctx)

def language_list(request, language):
    ctx = {'pastes': models.Paste.objects.all()}
    return render(request, 'pastebin/paste-language.jinja2', ctx)
