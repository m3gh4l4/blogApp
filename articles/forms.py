from django import forms
from django.db.models import fields
from . import models

class CreateArticleForm(forms.ModelForm):
    class Meta:
        model = models.Articles
        fields = ['title','slug','body','thumb']