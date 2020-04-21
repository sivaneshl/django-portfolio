from django.shortcuts import render
from blog.models import Post, Category, Comment
from blog.forms import CommentForm

# Create the views for
# blog_index
#   - will display a list of all your posts.
# blog_detail
#   - will display the full post as well as comments and a form to allow users to create new comments.
# blog_category
#   - will be similar to blog_index, but the posts viewed will only be of a specific category chosen by the user.


def blog_index(request):
    posts = Post.objects.all().order_by('-created_on')  # The minus sign tells Django to start with the largest value
    context = {'posts': posts}
    return render(request, 'blog_index.html', context)


def blog_category(request, category):
    posts = Post.objects.filter(categories__name__contains=category).order_by('-created_on')
    # This is an usage of Django QuerySetFilter. The argument of the filter tells Django what conditions need to be met
    # for an object to be retrieved. In this case, we only want posts whose categories contain the category with the
    # name corresponding to that given in the argument of the view function.
    context = {
        'category': category,
        'posts': posts
    }
    return render(request, 'blog_category.html', context)


def blog_detail(request, pk):

    post = Post.objects.get(pk=pk)

    # get the comment form
    form = CommentForm()
    if request.method=='POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            # You can access the data from the form using form.cleaned_data, which is a dictionary. They keys of the
            # dictionary correspond to the form fields, so you can access the author using form.cleaned_data['author'].
            comment = Comment(
                author=form.cleaned_data['author'],
                body=form.cleaned_data['body'],
                post=post
            )
            comment.save()
            form = CommentForm()    # clear the form after submit

    comments = Comment.objects.filter(post=post)
    context = {
        'post': post,
        'comments': comments,
        'form':  form
    }
    return render(request, 'blog_detail.html', context)