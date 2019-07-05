

from django import forms

from comments.models import Comment


class CommentForm(forms.ModelForm):
    '''
    评论表单
    '''
    class Meta:
        model = Comment
        fields = ['name','email','url','text']