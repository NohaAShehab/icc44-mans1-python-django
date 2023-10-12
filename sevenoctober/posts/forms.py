
from django import  forms
from posts.models import Post
class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
