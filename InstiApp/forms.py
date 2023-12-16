from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import RegisterClasses

class RegisterClassCreationForm(UserCreationForm):
    class Meta:
        model = RegisterClasses
        fields = '__all__'

class RegisterChangeForm(UserChangeForm):
    class Meta:
        model = RegisterClasses
        fields = '__all__'
        
class PostForm(forms.ModelForm):
     class Meta:
        model = RegisterClasses
        fields = '__all__'