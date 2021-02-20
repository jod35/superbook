from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


class HomeView(View):
    template_name='blog/index.html'
    title='Home'
    
    def get(self,request):
        context={
            'title':self.title
        }
        return render(request,self.template_name,context)


class SignUpView(View):
    template_name='blog/signup.html'
    title='Create Your Account'
    form_class=UserCreationForm

    def get(self,request):

        context={
            'title':self.title,
            'form':self.form_class()
        }

        return render(request,self.template_name,context)


    def post(self,request):
        form =self.form_class(request.POST)

        if form.is_valid():
            form.save()

            messages.success(request,"Account Created Successfully! Login")

            return redirect("blog:login")

        return render(request,self.template_name)


class LoginView(View):
    template_name='blog/login.html'
    title='Sign In'

    def get(self,request):
        context={
            'title':self.title
        }

        return render(request,self.template_name,context)