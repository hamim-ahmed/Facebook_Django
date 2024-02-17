from django import forms

class ChangePasswordForm(forms.Form):
    current_password = forms.CharField(label="Current Password", widget=forms.PasswordInput)
    new_password = forms.CharField(label="New Password", widget=forms.PasswordInput)