from .models import Comment
from django import crispy_forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)