from django import forms

from . models import Blog

class BlogForm(forms.ModelForm):

    class Meta:
        model = Blog
        fields = ('title','content','paragraph1','paragraph2','paragraph3','paragraph4','paragraph5','author',)
