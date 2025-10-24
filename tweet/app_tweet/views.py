from django.shortcuts import render

def tweet(request):
    return render(request, 'index.html')
