from django import forms
from projects.models import User
import datetime

def year_choices():
    this_year = datetime.date.today().year
    return [(r,r) for r in range(this_year-1, this_year+6)]

class SignupForm(forms.Form):
    first_name = forms.CharField(label="First name", max_length=50, 
            widget=forms.TextInput(attrs={
                'placeholder': 'John',
            }))

    last_name = forms.CharField(label="Last name", max_length=50, 
            widget=forms.TextInput(attrs={
                'placeholder': 'Doe',
            }))

    comp_id = forms.CharField(label="UVA computing ID", max_length=7, 
            widget=forms.TextInput(attrs={
                'placeholder': 'jd5xd',
            }))

    major = forms.CharField(label="Major", max_length=50, 
            widget=forms.TextInput(attrs={
                'placeholder': 'Undecided',
            }))

    degree_program = forms.ChoiceField(label="Degree program", 
            choices=User.DEGREES, initial='Degree program')

    graduation_year  = forms.TypedChoiceField(label="Expected graduation year", coerce=int,
            choices=year_choices, initial=datetime.date.today().year+4)

# Currently unused but kept just in case
class SigndownForm(forms.Form):
    comp_id = forms.CharField(label="UVA Computing ID", max_length=7, 
            widget=forms.TextInput(attrs={'placeholder': 'Computing ID'}))
