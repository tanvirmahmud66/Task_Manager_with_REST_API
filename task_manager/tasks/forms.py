from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Tasks, Photos


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']


class TaskForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ['title','description','due_date','priority']
        widgets = {
           'due_date': forms.DateInput(attrs={'type': 'date'}),
        }


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photos
        fields = ['image']