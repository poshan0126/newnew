from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request=request, template_name="demo/index.html")

    
def about(request):
    return render(request, template_name="demo/index.html")
