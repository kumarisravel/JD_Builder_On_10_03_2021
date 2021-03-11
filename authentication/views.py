from django.shortcuts import render, redirect
import json
from .models import Clients
from django.http import HttpResponse


# Create your views here.

class DataX:
    def __init__(self,email):
        self.email=email
        self.currentUser=None

c_data=DataX(None)


def isEmail(email):
    client = Clients.objects.filter(Email=email)

    if client:
        return True,client

    return False,None


def home(request):
    if 'current_user' in request.session:
        return redirect('/dashboard/')
    return render(request,"index.html")

def signIn(request):

    try:

        if request.method=="POST":
            user=Clients.objects.filter(Email=request.POST.__getitem__('email'),Password=request.POST.__getitem__('password'))
            if user:
                 print("line number 38")
                 request.session['current_user']="kumar"#user
                 print("line number 40")
                 return render(request,"ProfilePage.html")

            from django.contrib import messages
            messages.warning(request,"Username or Password is incorrect!.")

        return render(request,"signIn.html")

    except Exception as e:
        return HttpResponse(e)

def signUp(request):

    def isSendConfirmationEmail(email):

        from django.core.mail import send_mail

        message_str = """
            Hello,
    
                We received a request to reset the password for your account for this email address. To initiate the password reset process for your account, click the link below.
    
                http://localhost:8000/createPassword/.
    
                This link can only be used once. If you need to reset your password again, please visit http://127.0.0.1:8000 and request another reset.
    
                If you did not make this request, you can simply ignore this email.
    
                Sincerely,
                The Website Team
    
            """

        if send_mail('From JD Builder', message_str, 'kumarisravel724298@gmail.com', [email], fail_silently=False, ):
            return True
        return False

    if request.method=="POST":
        import random

        try:
            is_Email,client=isEmail(request.POST.__getitem__('email'))

            if not is_Email:

                if True:#isSendConfirmationEmail(request.POST.__getitem__('email')):

                    client = Clients(ClientId=str(random.randint(1000,9999)),ClientName=request.POST.__getitem__('name'), Email=request.POST.__getitem__('email'), Password=request.POST.__getitem__('passwordConfirmed'))
                    client.save()

                    return render(request,"afterSignUp.html")

            from django.contrib import messages
            messages.warning(request,"Entered e-mail is already taken!.  Try with another e-mail!.")

        except Exception as e:

            json_data=json.dumps({'value':str(e)})

            return HttpResponse(json_data)

    return render(request,'signUp.html')

def resetPassword(request):

    if request.method=="POST":

        c_data.email = request.POST.__getitem__('email')

        is_Email,c_data.currentUser=isEmail(c_data.email)

        if is_Email:

            from django.core.mail import send_mail

            message_str="""
                Hello,
                    
                    We received a request to reset the password for your account for this email address. To initiate the password reset process for your account, click the link below.
                    
                    http://localhost:8000/createPassword/.
                    
                    This link can only be used once. If you need to reset your password again, please visit http://127.0.0.1:8000 and request another reset.
                    
                    If you did not make this request, you can simply ignore this email.
                    
                    Sincerely,
                    The Website Team
                
                """

            if True:#send_mail('From JD Builder',message_str,'kumarisravel724298@gmail.com',[c_data.email],fail_silently=False,):

                return render(request,"seeEmail.html",{'email':c_data.email})

        from django.contrib import messages

        messages.warning(request,"Entered e-mail is not registered one!.")

    return render(request,"forgetPassword.html")

def createPassword(request):

    if request.method=="POST":

        client=Clients.objects.filter(Email=c_data.email)

        client.update(Password=request.POST.__getitem__('passwordConfirmed'))

        return render(request,"successPasswordUpdation.html",{'user':c_data.currentUser[0].ClientName})

    return render(request,"passwordCreation.html")

def dashboard(request):

    return render(request,'ProfilePage.html')


