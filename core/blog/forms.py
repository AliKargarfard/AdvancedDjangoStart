from django import forms
from .models import Post


class DateInput(forms.DateInput):
    input_type = "date"


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "content", "category", "status", "published_date")
        widgets = {
            "published_date": DateInput(),
        }
