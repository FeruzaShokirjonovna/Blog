from .models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    """
    Form class for users to comment on a post
    """
    class Meta:
        model = Comment
        fields = ("body",)
