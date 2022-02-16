from django.shortcuts import render
from django.views.generic import TemplateView


class SignInView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, "sign_in.html", context={"user": request.user})


class SignUpView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, "sign_up.html", context={"user": request.user})
