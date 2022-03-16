from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.views import TemplateView, LoginView

class UserLoginView(LoginView):
    template_name = 'LoginView_form.html'

class FormView(TemplateView):
    template_name = 'form.html'

class SignUpView(TemplateView):
    template_name = 'SignUp_form.html'

    def post(self, request, *args, **kwargs):
        data = self.request.POST
        user = User(username=data.get('username'), first_name=data.get('name'))

        user.set_password(data.get('password'))
        user.save()
        return redirect('form')
        