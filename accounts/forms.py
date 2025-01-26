from django import forms

class CheckedUserForm(forms.Form):
    id = forms.IntegerField(label='ID')