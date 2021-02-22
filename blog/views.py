from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Post, Profile
from .forms import ProfileCreationForm, PostCreateForm


class HomeView(View):
    template_name = 'blog/index.html'
    title = 'Home'

    def get(self, request):
        context = {
            'title': self.title,
            'posts':Post.objects.all()
        }
        return render(request, self.template_name, context)


class SignUpView(View):
    template_name = 'blog/signup.html'
    title = 'Create Your Account'
    form_class = UserCreationForm
    initial = {'key': 'value'}

    def get(self, request):

        context = {
            'title': self.title,
            'form': self.form_class(initial=self.initial)
        }

        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()

            messages.success(request, "Account Created Successfully! Login")

            return redirect("blog:login")

        return render(request, self.template_name)


class LoginView(View):
    template_name = 'blog/login.html'
    title = 'Sign In'

    def get(self, request):
        context = {
            'title': self.title
        }

        return render(request, self.template_name, context)


class ProfileCreationView(View):
    template_name = 'blog/createprofile.html'
    form_class = ProfileCreationForm
    initial = {'key': 'value'}

    def get(self, request):
        context = {
            'form': self.form_class(initial=self.initial)
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            obj = form.save(commit=False)

            obj.user = request.user

            obj.save()

            messages.success(request, "Profile Created Successfully")

            return redirect('blog:user_profile')


class UserProfileView(View):
    template_name = 'blog/profile.html'

    def get(self, request):
        profile = Profile.objects.filter(user=request.user).first()
        posts=Post.objects.filter(author=request.user)
        context = {
            'profile': profile,
            'posts':posts
        }
        return render(request, self.template_name, context)


class PostCreateView(View):
    template_name='blog/createpost.html'
    form_class=PostCreateForm
    initial={'key':'value'}

    def get(self,request):
        context={
            'form':self.form_class(initial=self.initial)
        }
        return render(request,self.template_name,context)


    def post(self,request):
        form=PostCreateForm(request.POST)

        if form.is_valid():
            form_obj=form.save(commit=False)
            form_obj.author=request.user
            form_obj.save()

            return redirect('blog:home')

        return render(request,self.template_name)



class PostDetailView(View):
    template_name='blog/postdetails.html'


    def get(self,request,title):
        post=Post.objects.get(title=title)

        context={
            'post':post
        }
        return render(request,self.template_name,context)

        
