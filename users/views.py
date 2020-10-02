from django.shortcuts import render, redirect, reverse
from django.views.generic import FormView
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth import authenticate, login, logout
from . import forms

# Create your views here.

class LoginView(View):

    
    def get(self, request):
        form = forms.LoginForm(initial={"email":"junhee1469@gmail.com"})
        print("wft",request.GET)
        return render(request, "users/login.html",{"form":form})
    
    def post(self, request):
        form = forms.LoginForm(request.POST)
        print("ttt", request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse("core:home"))
        return render(request, "users/login.html", {"form": form})


'''
class LoginView(FormView):

    template_name = "users/login.html"
    form_class = forms.LoginForm
    success_url = reverse_lazy("core:home")

    def form_valid(self, form):
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, username=email, password=password)
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)
        #return redirect(self.success_url)
'''



def log_out(request):
    logout(request)
    return redirect(reverse("core:home"))


class SignUpView(FormView):

    template_name = "users/signup.html"
    form_class = forms.SignUpForm
    success_url = reverse_lazy("core:home")
    initial = {"first_name":"Junhee", "last_name":"Kim", "email": "junhee1469@gmail.com"}

    def form_valid(self, form):
        form.save()
        
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, username=email, password=password)
        if user is not None:
            login(self.request, user)
        user.verify_email()
        return super().form_valid(form)
        