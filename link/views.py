from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def home(request):
    return render(request,'index.html')

@csrf_exempt
def analyze(request):
    return render(request,'analyze.html')