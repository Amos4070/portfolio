from django import forms

from django.forms import ModelForm



from .models import Post

# this read from the data base
class PostForm(ModelForm):
    class Meta:
        model =    Post
        fields = '__all__'

        widgets = {'tags': forms.CheckboxSelectMultiple(),}

