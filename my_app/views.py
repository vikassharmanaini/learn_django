from multiprocessing import context
from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    context={
        'variable':"this is var"
    }
    return render(request,"index.html",context)
    # return HttpResponse("<h1>this is home page</h1>")
def about(request):
    return HttpResponse("About page")
def service(request):
    return HttpResponse("service page")
def contact(request):
    return HttpResponse("contact page")
