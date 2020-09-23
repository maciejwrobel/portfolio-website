from django.shortcuts import render





# Create your views here.

def index(request):
        return render(request, 'portfolio/index.html')

def p1(request):
    return render(request, 'portfolio/1.html')

def p2(request):
    return render(request, 'portfolio/2.html')

def p3(request):
    return render(request, 'portfolio/3.html')

def eng(request):
    return render(request, 'portfolio/eng.html')

def e1(request):
    return render(request, 'portfolio/1en.html')

def e2(request):
    return render(request, 'portfolio/2en.html')

def e3(request):
    return render(request, 'portfolio/3en.html')