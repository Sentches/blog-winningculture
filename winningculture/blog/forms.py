from msilib.schema import Class
from django import forms
from .models import Comment

class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')
        widgets = {
            "name": forms.TextInput(attrs={"class": "col-sm-12"}),
            "body": forms.Textarea(attrs={"class": "form-control"}),
        }