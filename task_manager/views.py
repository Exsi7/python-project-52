from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.urls import reverse


def index(request):
    return render(request, 'index.html', context={'who': 'World',})