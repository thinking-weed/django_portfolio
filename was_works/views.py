from django.shortcuts import render
from django.http import HttpResponse

#prefixのURLは「was_works/」

def show(request):
    return render(request, 'was_works/was_works.html')