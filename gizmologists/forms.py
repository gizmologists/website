from django import forms

class SignupForm(forms.Form):
    first_name = forms.CharField(label="first name", max_length=50, 
            widget=forms.TextInput(attrs={'placeholder': 'First Name'}))

    last_name = forms.CharField(label="last name", max_length=50, 
            widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))

    comp_id = forms.CharField(label="UVA Computing ID", max_length=7, 
            widget=forms.TextInput(attrs={'placeholder': 'Computing ID'}))

class SigndownForm(forms.Form):
    comp_id = forms.CharField(label="UVA Computing ID", max_length=7, 
            widget=forms.TextInput(attrs={'placeholder': 'Computing ID'}))
