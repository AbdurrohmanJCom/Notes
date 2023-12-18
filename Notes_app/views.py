from django.shortcuts import render

def main(request):
    return render(request, 'main.html')

def layout(request):
    return render(request, 'layout.html')