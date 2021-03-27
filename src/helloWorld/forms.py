from django import forms

STATE_CHOICES = (
    ("Kentucky", "Kentucky"),
    ("Indiana", "Indiana"),
)


# creating a form
class StateForm(forms.Form):
    state_name = forms.ChoiceField(choices=STATE_CHOICES)
