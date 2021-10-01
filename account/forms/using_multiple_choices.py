from django.contrib.auth.forms import UserCreationForm
from account.models.using_multiple_choices import User

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'type', 'password1', 'password2']