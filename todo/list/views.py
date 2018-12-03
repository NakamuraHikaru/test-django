from django.shortcuts import render

# indexアクションを定義
def index(request):
    return render(request, 'list/index.html')

def item1(request):
    return render(request, 'list/item1.html')
# Create your views here.
