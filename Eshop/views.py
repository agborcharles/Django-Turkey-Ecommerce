from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):

    context = {}
    template_name = 'Eshop/index.html'

    return render(request, template_name, context)
