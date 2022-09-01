from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return render(request,"index.html")
    # return HttpResponse("<h1>this is home page</h1>")
def about(request):
    return HttpResponse("About page")
def service(request):
    return HttpResponse("service page")
def contact(request):
    return HttpResponse("contact page")
