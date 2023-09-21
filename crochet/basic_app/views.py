from django.shortcuts import render, redirect
from basic_app.forms import NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.views.generic import TemplateView

# Create your views here.
def signup_request(request):

    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Sign Up Successful")
            return redirect("basic_app:home")
        messages.error(request, "Registration Failed. Invalid Information.")
    
    form = NewUserForm()
    return render(request=request, template_name='bootstrap4/uni_form.html', context={"uni_form":form})

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password= password)

            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect('basic_app:home')
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid username or password')

    form = AuthenticationForm()
    return render(request, template_name='bootstrap4/login.html', context={'login_form':form})


def logout_request(request):
    logout(request)
    messages.info(request, 'You have successfully logged out')
    return redirect('basic_app:home')

class HomePage(TemplateView):
    template_name = 'index.html'

class DailyPage(TemplateView):
    template_name = 'daily.html'

class EbookPage(TemplateView):
    template_name = 'ebook.html'

class BeginnersPage(TemplateView):
    template_name = 'courses/beginners.html'

class AdvancedPage(TemplateView):
    template_name = 'courses/advanced.html'

class ProfessionalPage(TemplateView):
    template_name = 'courses/professional.html'

class GlossaryPage(TemplateView):
    template_name = 'courses/glossary.html'

class FaqPage(TemplateView):
    template_name = 'courses/faq.html'

class CollectionsPage(TemplateView):
    template_name = 'collections.html'

class ConditionsPage(TemplateView):
    template_name = 'terms_conditions.html'

class PrivacyPolicyPage(TemplateView):
    template_name = 'privacy.html'

class AboutPage(TemplateView):
    template_name = 'about.html'

