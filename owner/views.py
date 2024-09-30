from django.shortcuts import render,redirect
from . import forms
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from cars.models import Car
from django.contrib.auth.views import LoginView
from django.views.generic import ListView
from django.urls import reverse_lazy

# --------------> Attention <-------------------
# I've used 3 class based views. Two are here and another is in cars app's views --> DetailCarView

def register(request):  
    if request.method == "POST":  
        register_form = forms.RegistrationForm(request.POST)  
        if register_form.is_valid(): 
            register_form.save()  
            return redirect('login') 
    else: 
        register_form = forms.RegistrationForm() 
    return render(request, 'register.html', {'form': register_form}) 

class UserLoginView(LoginView):
    template_name = 'register.html'
    def get_success_url(self):
        return reverse_lazy('profile')
    def form_valid(self, form):
        messages.success(self.request, "Logged in Successfully")
        return super().form_valid(form)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ProfileView(ListView):
    model = Car
    template_name = 'profile.html'
    context_object_name = 'data'

    def get_queryset(self):
        return Car.objects.filter(owner=self.request.user)



@login_required
def edit_profile(request):
    if request.method == "POST":
        edit_profile_form = forms.ChangeUserForm(request.POST, instance = request.user)
        if edit_profile_form.is_valid():
            messages.success(request, "Profile updated successfully!")
            edit_profile_form.save()
            return redirect('profile')
    else:
        edit_profile_form = forms.ChangeUserForm(instance = request.user)
    return render(request, 'edit_profile.html', {'form': edit_profile_form})

def user_logout(request):
    logout(request)
    return redirect('login')

def pass_change(request):
    if request.method=='POST':
        pass_change_form = PasswordChangeForm(request.user, data = request.POST)
        if pass_change_form.is_valid():
            pass_change_form.save()
            messages.warning(request, "Password has been updated successfully!")
            update_session_auth_hash(request, pass_change_form.user) 
            return redirect('profile')
    else:
        pass_change_form = PasswordChangeForm(user = request.user)
    return render(request, 'pass_change.html', {'form': pass_change_form})







