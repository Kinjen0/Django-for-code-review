from django import forms
from .models import *

# Comment form that is used to create the comment
class CommentForm(forms.ModelForm):
    content = forms.TextInput()

    class Meta:
        model = Comment
        fields = ['content']
