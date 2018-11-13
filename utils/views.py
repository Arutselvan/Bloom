from django.views import View
from django.db import IntegrityError
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import UploadForm
from .models import MyUploads
from django.forms.models import model_to_dict

class LoginPageView(View):
    template_name = 'login.html'

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('/qa')
        return render(request, self.template_name)

    def post(self, request):
        user_name = request.POST.get('username')
        user_pass = request.POST.get('password')

        user = authenticate(request, username=user_name, password=user_pass)

        if user is None:
            return render(request, self.template_name, {'error_msg': 'Invalid credentials'})
        
        login(request, user)
        return redirect('/qa')

class SignupPageView(View):
    template_name = 'signup.html'

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('/qa')
        return render(request, self.template_name)

    def post(self, request):
        user_name = request.POST.get('username')
        user_pass = request.POST.get('password')
        user_pass = make_password(user_pass)

        user = User(username=user_name, password=user_pass)
        try:
            user.save()
        except IntegrityError:
            return render(request, self.template_name, {'error_msg': 'Username already exists'})

        return redirect('/accounts/login')

@login_required
def portal_logout(request):
    logout(request)
    return redirect('login_view')

class FileUploadsView(View):
    template_name = 'file_uploads.html'

    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('/accounts/login')
        my_files = MyUploads.objects.filter(user=request.user)
        files = []
        for my_file in my_files:
            temp = model_to_dict(my_file)
            temp['filename'] = my_file.file_path.name.split('_')[-1]
            temp['timestamp'] = my_file.file_path.name.split('/')[-1].rstrip(temp['filename'])
            files += [temp]
        return render(request, self.template_name, {'my_files': files})
    
    def post(self, request):
        upload_form = UploadForm(request.POST, request.FILES)
        upload_form.instance.user = request.user
        if upload_form.is_valid():
            upload_form.save()
            return redirect('/my_uploads')
