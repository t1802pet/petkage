from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, TemplateView, CreateView, DeleteView
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from .forms import CommentForm, PostForm
from .models import Post
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q
from django.shortcuts import render


from django.contrib.auth.decorators import login_required


##




def post_list(request):
    posts = Post.objects.all()
    comment_form = CommentForm()
    context = {
        'posts': posts,
        'comment_form': comment_form,
    }
    return render(request, 'post/post_list.html', context)





def post_detail(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    comment_form = CommentForm()
    context = {
        'post': post,
        'comment_form': comment_form,
    }
    return render(request, 'post/post_detail.html', context)


@login_required
def post_create(request):
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
            messages.success(request, '사진이 등록되었습니다')
            return redirect('post:post_list')
    else:
        post_form = PostForm()

    context = {
        'post_form': post_form,
    }
    return render(request, 'post/post_create.html', context)



@login_required
def comment_create(request, post_pk):
    # GET파라미터로 전달된 작업 완료 후 이동할 URL값
    next_path = request.GET.get('next')

    # 요청 메서드가 POST방식 일 때만 처리
    if request.method == 'POST':
        # Post인스턴스를 가져오거나 404 Response를 돌려줌
        post = get_object_or_404(Post, pk=post_pk)
        # request.POST데이터를 이용한 Bounded Form생성
        comment_form = CommentForm(request.POST)
        # 올바른 데이터가 Form인스턴스에 바인딩 되어있는지 유효성 검사
        if comment_form.is_valid():
            # 유효성 검사에 통과하면 ModelForm의 save()호출로 인스턴스 생성
            # DB에 저장하지 않고 인스턴스만 생성하기 위해 commit=False옵션 지정
            comment = comment_form.save(commit=False)
            # CommentForm에 지정되지 않았으나 필수요소인 author와 post속성을 지정
            comment.post = post
            comment.author = request.user
            # DB에 저장
            comment.save()

            # 성공 메시지를 다음 request의 결과로 전달하도록 지정
            messages.success(request, '댓글이 등록되었습니다')
        else:
            # 유효성 검사에 실패한 경우
            # 에러 목록을 순회하며 에러메시지를 작성, messages의 error레벨로 추가
            error_msg = '댓글 등록에 실패했습니다\n{}'.format(
                '\n'.join(
                    [f'- {error}'
                     for key, value in comment_form.errors.items()
                     for error in value]))
            messages.error(request, error_msg)
        # next parameter에 값이 담겨 온 경우, 해당 경로로 이동

        if next_path:
            return redirect(next_path)
        # next parameter가 빈 경우 post_list뷰로 이동
        return redirect('post:post_list')

# POST요청에 대해 커스터마이징한 login_required를 사용한다
@login_required
def post_like_toggle(request, post_pk):
    # GET파라미터로 전달된 이동할 URL
    next_path = request.GET.get('next')
    # post_pk에 해당하는 Post객체
    post = get_object_or_404(Post, pk=post_pk)
    # 요청한 사용자
    user = request.user

    # 사용자의 like_posts목록에서 like_toggle할 Post가 있는지 확인
    filtered_like_posts = user.like_posts.filter(pk=post.pk)
    # 존재할경우, like_posts목록에서 해당 Post를 삭제
    if filtered_like_posts.exists():
        user.like_posts.remove(post)
    # 없을 경우, like_posts목록에 해당 Post를 추가
    else:
        user.like_posts.add(post)

    # 이동할 path가 존재할 경우 해당 위치로, 없을 경우 Post상세페이지로 이동
    if next_path:
        return redirect(next_path)
    return redirect('post:post_detail', post_pk=post_pk)

# #--- @login_required
# class LoginRequiredMixin(object):
#     @classmethod
#     def as_view(cls, **initkwargs):
#         view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
#         return login_required(view)


# class PostDeleteView(DeleteView) :
#     model = Post
#     success_url = reverse_lazy('post:list')

@login_required
# 삭제 처음 도전
def post_delete(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    if post.author != request.user or request.method == 'GET':
        messages.warning(request, '잘못된 접근입니다.')
        return redirect('post:post_list')

    if request.method == 'POST':
        post.delete()
        messages.success(request, '삭제완료')
    return redirect('post:post_list')

# 삭제 두번째 도전
# def post_delete(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     post.delete()
#     return redirect('post:post_list')