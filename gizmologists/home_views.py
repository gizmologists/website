from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import send_mail
from .forms import SignupForm, SigndownForm
from projects.models import User

def home(request):
    return render(request, "index.html")
    
def about(request):
    return render(request, "about.html")

def contact(request):
    message = ''
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        signup_form = SignupForm(request.POST, prefix="signup")
        signdown_form = SigndownForm(request.POST, prefix="signdown")
        if signup_form.is_valid():
            # Get data from form
            first_name = signup_form.cleaned_data['first_name']
            last_name = signup_form.cleaned_data['last_name']
            comp_id = signup_form.cleaned_data['comp_id']
            major = signup_form.cleaned_data['major']
            degree_program = signup_form.cleaned_data['degree_program']
            graduation_year = signup_form.cleaned_data['graduation_year']

            email_domain = "@virginia.edu"
            email = comp_id + email_domain

            user_exists_with_comp_id = User.objects.filter(comp_id=comp_id).exists()
            if user_exists_with_comp_id:
                message = "There's already a person registered with that computing ID!"

            # else no one exists with that - that's all we need!
            else:
                person = User(first_name=first_name, 
                        last_name=last_name,
                        comp_id=comp_id,
                        email=email,
                        major=major,
                        degree_program=degree_program,
                        graduation_year=graduation_year,
                        need_added_to_email=True
                )
                person.save()
                message = """
                    You will be added to our mailing list as soon as possible.
                    If you suspect you have not been added after some time, try emailing us.
                    Thank you for your interest!
                    """

        # Signdown form currently unavailable - it's hard.
        #elif signdown_form.is_valid():
            #comp_id = signdown_form.cleaned_data['comp_id']
            #try:
                #person_to_delete = User.objects.get(comp_id=comp_id)
                # Need to send a confirmation email - but... tricky without users
                #person_to_delete.need_removed_from_email = True
                #message = "User with computing id " + comp_id + " will be removed shortly!"

            #except ObjectDoesNotExist:
                #message = """
                #User not in our database.  
                #If you are sure that you are on our mailing list, 
                #try emailing us and we will remove you.  
                #We apologize for the inconvenience.
                #"""

    signup_form   = SignupForm(prefix="signup")
    #signdown_form = SigndownForm(prefix="signdown")

    return render(request, 'contact.html', {
        'signup_form': signup_form,
        #'signdown_form': signdown_form,
        'message': message,
        })

def handler404(request):
    return render(request, '404.html', {}, status=404)

def handler500(request):
    return render(request, '500.html', {}, status=500)

