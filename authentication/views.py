from django.shortcuts import render, redirect
import json
from .models import Clients
from django.http import HttpResponse


# Create your views here.

def home(request):
    return render(request,"index.html")

def signIn(request):
    try:
        if request.method=="POST":
            user=Clients.objects.filter(Email=request.POST.__getitem__('email'),Password=request.POST.__getitem__('password'))
            if user:
                 return HttpResponse("Page is in progress!")
            return HttpResponse("you are not authorized person.")
        return render(request,"signIn.html")
    except Exception as e:
        print(e)
        return HttpResponse(e)
        #return HttpResponse(str(e))

def signUp(request):
    import random
    if request.method=="POST":
        try:
            client = Clients(ClientId=str(random.randint(1000,9999)),ClientName=request.POST.__getitem__('name'), Email=request.POST.__getitem__('email'), Password=request.POST.__getitem__('passwordConfirmed'))
            client.save()
            json_data=json.dumps({'value':'signed up successfully!'})
            return HttpResponse(json_data)

        except Exception as e:
            print(e)
            json_data=json.dumps({'value':'E-mail is Already taken please sign up other email!'})
            return HttpResponse(json_data)

    return render(request,'signUp.html')

def resetPassword(request):

    if request.method=="POST":
        return render(request, "passwordCreation.html")
        '''from django.core.mail import send_mail

        message_str="""
            Hello,
                
                We received a request to reset the password for your account for this email address. To initiate the password reset process for your account, click the link below.
                
                <a href="http://localhost:8000/createPassword/">http://localhost:8000/createPassword/</a>
                
                This link can only be used once. If you need to reset your password again, please visit http://127.0.0.1:8000 and request another reset.
                
                If you did not make this request, you can simply ignore this email.
                
                Sincerely,
                The Website Team
            
            """
        if send_mail('From JD Builder',message_str,'kumarisravel724298@gmail.com',['kumarisravel724298@gmail.com'],fail_silently=False,):
            return HttpResponse("message got sent")
        return HttpResponse("Couldn't able to send messages")'''
    return render(request,"forgetPassword.html")

def createPassword(request):
    return render(request,"passwordCreation.html")




