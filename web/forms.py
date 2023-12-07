from django.forms import ModelForm
from django.contrib.auth.models import User
class UserForm(ModelForm):
    class Meta:
        model = User
        exclude = ('created_by',"groups","user_permissions","is_staff","last_login","date_joined","is_active","is_superuser")


class LoginForm(ModelForm):
    class Meta:
        model = User
        fields=("email","password")