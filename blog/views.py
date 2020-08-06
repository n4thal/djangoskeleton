from django.shortcuts import render, get_object_or_404
from blog.models import Post
from blog.forms import CommentForm
from django.views import generic
from core.models import Author, MetaInfo


# Create your views here.
class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-publication_date')
    template_name = 'blog_index.html'


def post_detail(request, slug):
    author = get_object_or_404(Author, pk=1)
    meta = get_object_or_404(MetaInfo, pk=1)

    template_name = 'post_detail.html'
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True).order_by("-publication_date")
    new_comment = None

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, template_name, {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form,
                                           'author': author,
                                           'meta': meta,
                                           })
