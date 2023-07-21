from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class formulaire_inscription(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']