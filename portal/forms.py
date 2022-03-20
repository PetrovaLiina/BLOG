from django import forms
from .models import Portal
import re
from django.core.exceptions import ValidationError


class PostForm(forms.ModelForm):
    class Meta:
        model = Portal
        # fields = '__all__'
        fields = ['title', 'post', 'is_published', 'category']
        widgets = {
            'title': forms.TextInput(attrs={"class": "form-control"}),
            'post': forms.Textarea(attrs={"class": "form-control", "rows": 5}),
            'category': forms.Select(attrs={"class": "form-control"}),
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if re.match(r'\d', title):
            raise ValidationError('Название не должно начинаться с цифры')
        return title
