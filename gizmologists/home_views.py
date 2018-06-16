from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from .forms import SignupForm, SigndownForm
from projects.models import Person

def home(request):
    return render(request, "index.html")
    
def about(request):
    return render(request, "about.html")

def contact(request):
    message = ''
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        signup_form = SignupForm(request.POST, prefix="signup")
        signdown_form = SigndownForm(request.POST, prefix="signdown")
        # check whether it's valid:
        if signup_form.is_valid():
            # process the data in form.cleaned_data as required
            first_name = signup_form.cleaned_data['first_name']
            last_name = signup_form.cleaned_data['last_name']
            comp_id = signup_form.cleaned_data['comp_id']
            email_domain = "@virginia.edu"
            email = comp_id + email_domain

            users_with_same_comp_id = Person.objects.filter(id=comp_id).count()
            if users_with_same_comp_id > 0:
                message = "There's already a person registered with that computing ID!"

            # else no one exists with that - that's all we need!
            else:
                person = Person(first_name=first_name, 
                        last_name=last_name,
                        id=comp_id,
                        email=email)
                person.save()
                message = "Cool!"

        elif signdown_form.is_valid():
            comp_id = signdown_form.cleaned_data['comp_id']
            person_to_delete = Person.objects.filter(id=comp_id)
            person_to_delete.delete()
            message = "Person with computing id " + comp_id + " successfully removed!"

    signup_form   = SignupForm(prefix="signup")
    signdown_form = SigndownForm(prefix="signdown")

    return render(request, 'contact.html', {
        'signup_form': signup_form,
        'signdown_form': signdown_form,
        'message': message,
        })
