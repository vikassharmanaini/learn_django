from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return render(request,"index.html")
def about(request):
    return render(request,"./pages/about.html")
def service(request):
    return HttpResponse("./")
def contact (request):
    return render(request,"./pages/contact.html")