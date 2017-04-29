from django import forms
from .models import Post
from .models import News
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# class NewsForm(forms.ModelForm):
#     class Meta:
#         model = News
#         fields = ('title', 'category', 'src', 'pic', 'weburl', 'date',)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text',)

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )