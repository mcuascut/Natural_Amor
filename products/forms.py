from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')
        
    first_name = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={"style":"text-transform: capitalize;", "autocapitalize": "word"}))
    last_name = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={"style":"text-transform: capitalize;", "autocapitalize": "word"}))
    email = forms.EmailField(required=True)
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"style":"margin: 10px 0;padding: 10px 10px"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"style":"margin: 10px 0;padding: 10px 10px"}))
        
    def save(self, commit=True):
        
        user = super(SignUpForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

