from django.shortcuts import render, get_object_or_404
from . import models

def index(request):

    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('paste', id=post.id)
        else:
            form = PostForm()
        return render(request, 'pastebin/index.jinja2', {'form': form})


def paste(request, id):
    ctx = get_object_or_404(Post, pk=pk)
    return render(request, 'pastebin/paste-detail.jinja2', ctx)

def language_list(request, language):
    ctx = {'paste': models.Paste.objects.all()}
    return render(request, 'pastebin/paste-language.jinja2', ctx)
