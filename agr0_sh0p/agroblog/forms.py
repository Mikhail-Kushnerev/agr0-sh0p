from django import forms

from .models import Comment, Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('text', 'image',)
        help_texts = {
            'text': 'Запиши свои мысли',
        }
        labels = {
            'text': 'Текст поста',
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
        help_texts = {
            'text': 'Запиши свои мысли',
        }
        labels = {
            'text': 'Текст комментарии',
        }