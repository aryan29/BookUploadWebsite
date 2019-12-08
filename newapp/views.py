from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import BookForm
from .models import Books
def homepage(request):
    return render(request,"base.html")
def viewlist(request):
    books=Books.objects.all()
    return render(request,"viewlist.html",{"books":books})
def upload(request):
    if(request.method=="POST"):
        print("coming here")
        form=BookForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('viewlist')
    else:
        form =BookForm()
    return render(request,"upload.html",{
        "form":form
    })
# Create your views here
