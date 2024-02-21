from .models import User
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = {'name','email','password1','password2'}