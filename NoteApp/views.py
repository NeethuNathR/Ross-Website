
from django.contrib import messages,auth
from django.http import HttpResponse
from django.shortcuts import render,redirect

from django.contrib.auth.models import User
from rest_framework import request

from .models import Profile
# Create your views here.




def demo(request):
   return render(request,'index.html')
def about(request):
   return render(request,'about.html')
def service(request):
   return render(request,'service.html')
def contact(request):
   return render(request,'contact.html')
def login(request):
   return render(request,'login.html')
def careers(request):
   return render(request,'careers.html')
def senior(request):
    return render(request,'senior.html')

#def register(request):
  #  if request.method=='POST':
        #username=request.POST['username']
       # first_name=request.POST.get('username')
        #last_name=request.POST['last_name']
        #email=request.POST.get('email')
        #password=request.POST.get('password')
        #cpassword=request.POST.get('re-pass')
        #if password==cpassword:
         #   if User.objects.filter(username=first_name).exists():
          #      messages.info(request,"username already exist")
           #     return redirect("register")
            #elif User.objects.filter(email=email).exists():
             #   messages.info(request,"this email id already exist")
              #  return redirect("register")
            #else:
             #   user=User.objects.create_user(first_name,email,password)
              #  user.save()
               # print("user created")

        #else:
         #   messages.info(request,"password not matching")
          #  return redirect("register")
        #return redirect("login")
    #return render(request,'register.html')
#def login(request):
 #   if request.method=='POST':
  #      username=request.POST["username"]
   #     password=request.POST["password"]
    #    user=auth.authenticate(username=username,password=password)
     #   if user is not None:
      #      auth.login(request,user)
       #     return redirect("/")
        #else:
         #   messages.info(request,"invalid credentials")
          #  return redirect("login")
    #return render(request,"login.html")


#
# from django.contrib import messages, auth
# from django.contrib.auth.models import User
# from django.shortcuts import render, redirect
#
#
# # Create your views here.
#
#
#
# # def login(request):
#     # if request.method=='POST':
#     #     email = request.POST['email']
#     #     password = request.POST['password']
#     #     user = auth.authenticate(email=email,password=password)
#     #     if user is not None:
#     #         auth.login(request,user)
#     #         return redirect('/')
#     #     else:
#     #         messages.info(request,"invalid credentials")
#     #         return redirect('login')
#     # return render(request,"login.html")
# def login(request):
#     if request.method=='POST':
#         email=request.POST["email"]
#         password=request.POST["password"]
#         user=auth.authenticate(email=email,password=password)
#         if user is not None:
#             auth.login(request,user)
#             return redirect("/")
#         else:
#             messages.info(request,"invalid credentials")
#             return redirect("login")
#     return render(request,"login.html")
#
#
#
# def register(request):
#     if request.method == 'POST':
#
#         firstname = request.POST['firstname']
#         lastname = request.POST['lastname']
#         username = request.POST['username']
#         email = request.POST['email']
#         password = request.POST['password1']
#         cpassword = request.POST['password2']
#         if password == cpassword:
#             if User.objects.filter(username=username).exists():
#                 messages.info(request, "username Taken")
#                 return redirect('register')
#             elif User.objects.filter(email=email).exists():
#                 messages.info(request, "email Taken")
#                 return redirect('register')
#             else:
#                 user = User.objects.create_user(first_name=firstname, last_name=lastname, username=username,email=email)
#                 user.save()
#                 return redirect('login')
#         else:
#             messages.info(request, "password not match")
#             return redirect('register')
#         return redirect('/')
#
#     return render(request, 'register.html')
#
# def logout(request):
#     auth.logout(request)
#     return redirect('/')
#
#
#
from django.shortcuts import render

# Create your views here.
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.

def register(request):

    if request.method=='POST':
        businessid= request.POST['businessid']

        username=request.POST['username']
        businessname=request.POST['businessname']
        email=request.POST['email']
        address=request.POST['address']
        contact=request.POST['contact']
        pincode=request.POST['pincode']
        district=request.POST['district']
        state=request.POST['state']
        password=request.POST['password1']
        cpassword=request.POST['password2']

        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username already exist")
                return redirect("register")
            elif User.objects.filter(email=email).exists():
                messages.info(request,"this email id already exist")
                return redirect("register")
            else:
                user=User.objects.create_user(username=username,email=email,password=password)
                user.save()
                profile=Profile(businessid=businessid,businessname=businessname,address=address,pincode=pincode,contact=contact,district=district,state=state)
                profile.save()

                print("user created")

        else:
            messages.info(request,"password not matching")
            return redirect("register")
        return redirect("login")

    return render(request,'register.html')

def login(request):
    if request.method=='POST':
        businessid=request.POST['businessid']
        username=request.POST["username"]
        password=request.POST["password"]
        user=auth.authenticate(username=username,password=password,businessid=businessid)


        if user is not None:

            auth.login(request,user)
            return redirect("senior")
        else:
            messages.info(request,"invalid Username or Password")
            return redirect("login")
    return render(request,"login.html")

def logout(request):
    auth.logout(request,)
    return redirect("/")
