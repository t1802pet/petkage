from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect


from .forms import CommentForm, PostForm
from .models import HW_Post

# 꿀팁모음 작성
def blog_list(request):

    posts = HW_Post.objects.all()
    comment_form = CommentForm()
    context = {
        'posts': posts,
        'comment_form': comment_form,
    }

    return render(request, 'blog/blog_list.html', context)

# 꿀팁상세
def blog_detail(request, post_pk):
    post = get_object_or_404(HW_Post, pk=post_pk)
    comment_form = CommentForm()
    context = {
        'post': post,
        'comment_form': comment_form,
    }
    return render(request, 'blog/blog_detail.html', context)

# 꿀팁작성
@login_required
def blog_create(request):
    if request.method == 'POST':
        # PostForm은 파일을 처리하므로 request.FILES도 함께 바인딩
        post_form = PostForm(request.POST, request.FILES)
        if post_form.is_valid():
            # author필드를 채우기 위해 인스턴스만 생성
            post = post_form.save(commit=False)
            # author필드를 채운 후 DB에 저장
            post.author = request.user

            post.save()

            # 성공 알림을 messages에 추가 후 post_list뷰로 이동
            messages.success(request, '내용이 등록되었습니다')
            return redirect('blog:blog_list')
    else:
        post_form = PostForm()

    context = {
        'post_form': post_form,
    }
    return render(request, 'blog/blog_create.html', context)
