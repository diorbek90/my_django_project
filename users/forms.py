from django import forms


class RegisterForm(forms.Form):
    avatar = forms.ImageField()
    age = forms.IntegerField()
    
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput)


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)
