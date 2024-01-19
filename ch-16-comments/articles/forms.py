from django import forms
from django.forms.models import ModelFormMetaclass
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta(ModelFormMetaclass):
        model=Comment
        fields= ("comment", )
