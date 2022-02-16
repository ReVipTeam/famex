from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login
from .models import User, Initials


class UserView(TemplateView):
    def get(self, request, **kwargs):
        print(request.user)
        return render(request, "index.html")

    def post(self, request, *args, **kwargs):
        if feature := request.GET.get("feature", None):
            if feature == "sign_in":
                token, username, password, *r = request.POST.values()
                user = authenticate(username=username, password=password)

            if feature == "sign_up":
                token, first_name, last_name, username, birth, email, password, *r = request.POST.values()
                initials = Initials(first_name=first_name, last_name=last_name)
                user = User(initials=initials, birth=birth, username=username,
                            email=email, password=password)
                initials.save(); user.save()

        login(request, user)
        return redirect("user:index")
