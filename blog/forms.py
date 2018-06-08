from django import forms
from django.forms.extras.widgets import SelectDateWidget
from .models import HW_Comment, HW_Post

class PostForm(forms.ModelForm):
    class Meta:
        model = HW_Post
        fields = (
            'author',
            'psttitle',
            # 'pstdate',
            'psttext',
            'bphoto',
        )
        widgets = {


            'psttitle': forms.TextInput(
                attrs={
                    'class': 'psttitle',
                    'placeholder': '제목',
                }
            ),


            'psttext': forms.Textarea(
                attrs={
                    'class': 'psttext',
                    'placeholder': '내용 작성...',
                }
            ),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = HW_Comment
        fields = (
            'content',
        )
        widgets = {
            'content': forms.TextInput(
                attrs={
                    'class': 'content',
                    'placeholder': '댓글 달기...',
                }
            )
        }

    def clean_content(self):
        data = self.cleaned_data['content']
        errors = []
        if data == '':
            errors.append(forms.ValidationError('댓글 내용을 입력해주세요'))
        elif len(data) > 50:
            errors.append(forms.ValidationError('댓글 내용은 50자 이하로 입력해주세요'))
        if errors:
            raise forms.ValidationError(errors)
        return data
