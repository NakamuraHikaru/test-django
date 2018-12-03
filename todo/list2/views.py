from django.shortcuts import render

def index(request):
    return render(request, 'list2/index.html')
# Create your views here.
