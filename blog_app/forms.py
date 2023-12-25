from django import forms

from .models import BlogPost


class PostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ["title", "content", "category"]
        labels = {"title": "", "content": "", "category": ""}
        widgets = {"content": forms.Textarea(attrs={"cols": 80})}

    # so that the category field is not required - from StackOverflow
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields["category"].required = False
