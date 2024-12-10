from django import forms
from .models import studytable,Comment

class datatable(forms.ModelForm):
    class Meta:
        model = studytable
        fields = ['Name', 'Email', 'Username', 'Password']  # Exclude 'Amount'


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'text',]  # Exclude 'Amount'