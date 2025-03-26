from django import forms
from .models import FAQ
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class FAQGenerateForm(forms.Form):
    description = forms.CharField(
        label="Toote või teenuse kirjeldus",
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
        help_text="Sisesta toote või teenuse info, mille põhjal luuakse korduma kippuvad küsimused"
    )

class FAQForm(forms.ModelForm):
    class Meta:
        model = FAQ
        fields = ['question', 'answer', 'image']
