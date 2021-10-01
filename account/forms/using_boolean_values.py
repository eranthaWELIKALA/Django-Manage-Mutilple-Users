from django.contrib.auth.forms import UserCreationForm
from account.models.using_boolean_values import User

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'is_spy', 'is_driver', 'password1', 'password2']