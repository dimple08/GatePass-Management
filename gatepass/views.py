from django.shortcuts import render


def login(request):
    return render(request, "admin1/login.html")

