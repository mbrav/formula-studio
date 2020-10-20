from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def list(request):
    return HttpResponse('Books List')

def reviews(request):
    return HttpResponse('Books Reviews')
