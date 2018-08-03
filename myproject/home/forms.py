

from django import forms
from home.models import Post,Comment


class HomeForm(forms.ModelForm):



    class Meta:
        model = Post
        fields = ('post',)

class CommentForm(forms.ModelForm):
    author=forms.CharField(widget=forms.TextInput(          #gives bootstrap class

    attrs={
              'class': 'form-control',
              'placeholder':'Enter Title'

        }
        ))
    text=forms.CharField(widget=forms.Textarea(          #gives bootstrap class

    attrs={
          'class': 'form-control',
          'placeholder':'Write a post'

    }
    ))

    class Meta:
        model = Comment
        fields = ('author', 'text',)