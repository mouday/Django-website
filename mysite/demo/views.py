from django.shortcuts import render, HttpResponse
from demo import forms

# Create your views here.

def add(request):
    if request.method == "GET":
        addform = forms.AddForm()
        return render(request, "demo/add.html", {"addform": addform})

    if request.method == "POST":
        addform = forms.AddForm(request.POST)
        if addform.is_valid():
            a = addform.cleaned_data["a"]
            b = addform.cleaned_data["b"]
        return HttpResponse(str(a+b))

def sendemail(request):
    from django.core.mail import send_mail
    subject = ""
    send_mail('Subject here', 'Here is the message.', 'pengshiyuyx@163.com',
        ['pengsy@byzxt.com.cn'], fail_silently=False)
    return HttpResponse("ok")