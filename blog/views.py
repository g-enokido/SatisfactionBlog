from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.utils import timezone
from comment.models import Comment
from .models import Post, Category
from accounts.models import Blog, CustomUser
from .forms import PostForm, CategoryForm

# Create your views here.


def index(request):
    posts = Post.objects.filter(
        published_date__lte=timezone.now()).order_by('created_date').reverse().select_related(
        "blog")[:5]

    if 'blog' in request.session:
        del request.session['blog']

    if request.user.is_authenticated:
        request.session['own_blogs'] = Blog.objects.filter(
            author_id=request.user).count()
    return render(request, 'blog/index.html', {'articles': posts})


def paging_query(request, queryset, count):
    paginator = Paginator(queryset, count)
    page = request.GET.get('page')
    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    return page_obj


def post_list(request, pk):
    posts = Post.objects.filter(
        published_date__lte=timezone.now(), blog_id=pk).order_by('created_date').reverse()
    page_obj = paging_query(request, posts, 10)
    blog = get_object_or_404(Blog, pk=pk)
    user = get_object_or_404(CustomUser, pk=blog.author_id)
    request.session['user'] = user
    request.session['blog'] = blog
    category = Category.objects.filter(blog_id=blog.id)
    request.session['category'] = category
    category.group_by = ['category_id']

    return render(request, 'blog/post_list.html',
                  {'posts': posts, 'category': category, 'page_obj': page_obj, })


def post_detail(request, pk):

    blog = get_object_or_404(Post, pk=pk).blog
    if 'blog'not in request.session:
        request.session['blog'] = blog
    post = get_object_or_404(Post, pk=pk, blog_id=blog.id)
    if post.category_id == 0:
        category = '未分類'
    else:
        category = get_object_or_404(
            Category, pk=post.category_id, blog_id=blog.id)
    comment = Comment.objects.filter(article_id=pk)

    return render(request, 'blog/post_detail.html', {'post': post, 'comment': comment, 'category': category})


def Category_Scope(request, pk):
    blogId = request.session['blog'].id
    post = Post.objects.filter(category_id=pk, blog_id=blogId)
    return render(request, 'blog/post_list.html', {'posts': post})


@login_required
@csrf_protect
def post_new(request, pk):
    if request.method == "POST":

        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            blogs = get_object_or_404(
                Blog, pk=request.session['target_blog'].id)
            post = form.save(commit=False)
            post.author = request.user
            post.blog_id = blogs.id

            if request.POST['category_name'] != ''and Category.objects.filter(
                    category_name=request.POST['category_name'], blog_id=blogs.id).count() == 0:
                new_category = CategoryForm(request.POST)
                if new_category.is_valid():
                    create = new_category.save(commit=False)
                    create.holder = request.user
                    create.category_name = request.POST['category_name']
                    create.blog_id = request.session['target_blog'].id
                    create.updated_date = timezone.now()
                    create.save()
                post.category_id = get_object_or_404(
                    Category, category_name=request.POST['category_name'],
                    blog_id=request.session['target_blog'].id).id
            else:
                if request.POST['category_name'] != '':
                    post.category_id = get_object_or_404(
                        Category, category_name=request.POST['category_name'], blog_id=blogs.id).id
                else:
                    post.category_id = request.POST['category_set']

            if 'draft_flag'not in request.POST:
                post.published_date = timezone.now()

            post.save()
            blogs.published_date = timezone.now()
            blogs.save()
            return redirect('post_list', pk=post.blog_id)

    else:
        categories = Category.objects.filter(blog_id=pk)
        target_blog = get_object_or_404(Blog, pk=pk)
        request.session['target_blog'] = target_blog
        form = PostForm()
        return render(request, 'blog/post_edit.html', {'form': form, 'categories': categories})


@login_required
@csrf_protect
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()

            blogs = get_object_or_404(Blog, pk=request.POST['blog_set'])
            blogs.published_date = timezone.now()
            blogs.save()
            return redirect('post_detail', pk=post.pk)

    else:
        form = PostForm(instance=post)
        return render(request, 'blog/post_edit.html', {'form': form, 'detail_flag': True})


@login_required
def post_draft_list(request):
    posts = Post.objects.filter(
        published_date__isnull=True, author_id=request.user.id).order_by('created_date')

    return render(request, 'blog/post_draft_list.html', {'posts': posts})


@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)


@login_required
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list', pk=request.session['blog'].id)


def post_login(request):
    return render(request, 'blog/post_login.html')
