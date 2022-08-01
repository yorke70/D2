from django import forms
from .models import Post
from django.core.exceptions import ValidationError

class NewsForm(forms.ModelForm):
    post_name = forms.CharField(min_length=10)
    class Meta:
        model = Post
        fields = [
            'author',
            'choice',
            'category',
            'post_name',
            'text'
        ]
    def clean(self):
        cleaned_data =super().clean()
        post_name = cleaned_data.get('post_name')
        text = cleaned_data.get('text')

        if post_name == text:
            raise ValidationError(
                "Заголовок и текст не должны совпадать"
            )
        return cleaned_data
