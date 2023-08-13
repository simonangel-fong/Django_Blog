from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):
    ''' The form to submit a post '''
    class Meta:
        model = Post
        fields = ("title", "content")
        # set widgets for fields
        widgets = {
            "title": forms.TextInput(
                attrs={"class": "form-control"}
            ),
            "content": forms.Textarea(
                attrs={"class": "form-control editor", "rows": "3"}
            )
        }


class CommentForm(forms.ModelForm):
    ''' The form to submit a comment '''
    class Meta:
        model = Comment
        fields = ("author", "content")
        # set widgets for fields
        widgets = {
            "author": forms.TextInput(
                attrs={"class": "form-control"}
            ),
            "content": forms.Textarea(
                attrs={"class": "form-control editor"}
            )
        }
