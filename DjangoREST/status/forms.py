from .models import Status
from django import forms

class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = [
            'id',
            'user',
            'content',
            'image'
        ]

    def clean_content(self, *args, **kwargs):
        content = self.cleaned_data.get('content', None)
        if len(content) > 20:
            raise forms.ValidationError('Content is too long!')
        return content


    def clean(self, *args, **kwargs):
        data = self.cleaned_data
        content = data.get('content', None)
        image = data.get('image', None)
        if not content and not image:
            raise forms.ValidationError('Content or image is required!')
        return super().clean(*args, **kwargs)