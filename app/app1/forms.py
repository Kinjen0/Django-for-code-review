from django import forms
from .models import *

class CommentForm(forms.ModelForm):
    content = forms.TextInput()

    class Meta:
        model = Comment
        fields = ['content']
