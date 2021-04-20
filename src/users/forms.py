from django import forms
from .models import User


# The base of our survey form with field definitions
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'home_state',
            'work_state',
            'age',
            'essential',
            'vaccine_group',
        ]
